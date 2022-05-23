# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.oda.src.oci_cli_oda.generated import oda_service_cli


@click.command(cli_util.override('management.management_root_group.command_name', 'management'), cls=CommandGroupWithAlias, help=cli_util.override('management.management_root_group.help', """API to create and maintain Oracle Digital Assistant service instances."""), short_help=cli_util.override('management.management_root_group.short_help', """Digital Assistant Service Instance API"""))
@cli_util.help_option_group
def management_root_group():
    pass


@click.command(cli_util.override('management.digital_assistant_parameter_group.command_name', 'digital-assistant-parameter'), cls=CommandGroupWithAlias, help="""Metadata for a Digital Assistant Parameter.""")
@cli_util.help_option_group
def digital_assistant_parameter_group():
    pass


@click.command(cli_util.override('management.authentication_provider_group.command_name', 'authentication-provider'), cls=CommandGroupWithAlias, help="""Settings for the Authentication Provider.""")
@cli_util.help_option_group
def authentication_provider_group():
    pass


@click.command(cli_util.override('management.digital_assistant_group.command_name', 'digital-assistant'), cls=CommandGroupWithAlias, help="""Digital Assistant metadata.""")
@cli_util.help_option_group
def digital_assistant_group():
    pass


@click.command(cli_util.override('management.skill_parameter_group.command_name', 'skill-parameter'), cls=CommandGroupWithAlias, help="""Metadata for a Skill Parameter.""")
@cli_util.help_option_group
def skill_parameter_group():
    pass


@click.command(cli_util.override('management.bot_group.command_name', 'bot'), cls=CommandGroupWithAlias, help="""Metadata for a Bot resource.""")
@cli_util.help_option_group
def bot_group():
    pass


@click.command(cli_util.override('management.skill_group.command_name', 'skill'), cls=CommandGroupWithAlias, help="""Skill metadata.""")
@cli_util.help_option_group
def skill_group():
    pass


@click.command(cli_util.override('management.translator_group.command_name', 'translator'), cls=CommandGroupWithAlias, help="""The properties for a Translator.""")
@cli_util.help_option_group
def translator_group():
    pass


@click.command(cli_util.override('management.channel_group.command_name', 'channel'), cls=CommandGroupWithAlias, help="""Properties of a Channel.""")
@cli_util.help_option_group
def channel_group():
    pass


oda_service_cli.oda_service_group.add_command(management_root_group)
management_root_group.add_command(digital_assistant_parameter_group)
management_root_group.add_command(authentication_provider_group)
management_root_group.add_command(digital_assistant_group)
management_root_group.add_command(skill_parameter_group)
management_root_group.add_command(bot_group)
management_root_group.add_command(skill_group)
management_root_group.add_command(translator_group)
management_root_group.add_command(channel_group)


@digital_assistant_parameter_group.command(name=cli_util.override('management.configure_digital_assistant_parameters.command_name', 'configure'), help=u"""This will store the provided parameters in the Digital Assistant instance and update any Digital Assistants with matching parameters. \n[Command Reference](configureDigitalAssistantParameters)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--parameters', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The values to use to configure the Digital Assistant Parameters.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parameters': {'module': 'oda', 'class': 'list[DigitalAssistantParameterValue]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameters': {'module': 'oda', 'class': 'list[DigitalAssistantParameterValue]'}})
@cli_util.wrap_exceptions
def configure_digital_assistant_parameters(ctx, from_json, oda_instance_id, parameters):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.configure_digital_assistant_parameters(
        oda_instance_id=oda_instance_id,
        configure_digital_assistant_parameters_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@authentication_provider_group.command(name=cli_util.override('management.create_authentication_provider.command_name', 'create'), help=u"""Creates a new Authentication Provider \n[Command Reference](createAuthenticationProvider)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--grant-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"]), help=u"""The grant type for the Authentication Provider.""")
@cli_util.option('--identity-provider', required=True, type=custom_types.CliCaseInsensitiveChoice(["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]), help=u"""Which type of Identity Provider (IDP) you are using.""")
@cli_util.option('--name', required=True, help=u"""A name to identify the Authentication Provider.""")
@cli_util.option('--token-endpoint-url', required=True, help=u"""The IDPs URL for requesting access tokens.""")
@cli_util.option('--authorization-endpoint-url', required=True, help=u"""The IDPs URL for the page that users authenticate with by entering the user name and password.""")
@cli_util.option('--client-id', required=True, help=u"""The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application ID.""")
@cli_util.option('--client-secret', required=True, help=u"""The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application secret.""")
@cli_util.option('--scopes', required=True, help=u"""A space-separated list of the scopes that must be included when Digital Assistant requests an access token from the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled, include the scope that\u2019s necessary to get the refresh token (typically offline_access).""")
@cli_util.option('--subject-claim', required=True, help=u"""The access-token profile claim to use to identify the user.""")
@cli_util.option('--short-authorization-code-request-url', help=u"""A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows you to send query parameters).  You might need this because the generated authorization-code-request URL could be too long for SMS and older smart phones.""")
@cli_util.option('--revoke-token-endpoint-url', help=u"""If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens component to revoke the user's tokens for this service.""")
@cli_util.option('--refresh-token-retention-period-in-days', type=click.INT, help=u"""The number of days to keep the refresh token in the Digital Assistant cache.""")
@cli_util.option('--redirect-url', help=u"""The OAuth Redirect URL.""")
@cli_util.option('--is-visible', type=click.BOOL, help=u"""Whether this Authentication Provider is visible in the ODA UI.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'AuthenticationProvider'})
@cli_util.wrap_exceptions
def create_authentication_provider(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, grant_type, identity_provider, name, token_endpoint_url, authorization_endpoint_url, client_id, client_secret, scopes, subject_claim, short_authorization_code_request_url, revoke_token_endpoint_url, refresh_token_retention_period_in_days, redirect_url, is_visible, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['grantType'] = grant_type
    _details['identityProvider'] = identity_provider
    _details['name'] = name
    _details['tokenEndpointUrl'] = token_endpoint_url
    _details['authorizationEndpointUrl'] = authorization_endpoint_url
    _details['clientId'] = client_id
    _details['clientSecret'] = client_secret
    _details['scopes'] = scopes
    _details['subjectClaim'] = subject_claim

    if short_authorization_code_request_url is not None:
        _details['shortAuthorizationCodeRequestUrl'] = short_authorization_code_request_url

    if revoke_token_endpoint_url is not None:
        _details['revokeTokenEndpointUrl'] = revoke_token_endpoint_url

    if refresh_token_retention_period_in_days is not None:
        _details['refreshTokenRetentionPeriodInDays'] = refresh_token_retention_period_in_days

    if redirect_url is not None:
        _details['redirectUrl'] = redirect_url

    if is_visible is not None:
        _details['isVisible'] = is_visible

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_authentication_provider(
        oda_instance_id=oda_instance_id,
        create_authentication_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_authentication_provider') and callable(getattr(client, 'get_authentication_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_authentication_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.create_channel.command_name', 'create'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"]), help=u"""The Channel type.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel(ctx, from_json, oda_instance_id, name, type, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['type'] = type

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_ms_teams_channel_details.command_name', 'create-channel-create-ms-teams-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--msa-app-id', required=True, help=u"""The Microsoft App ID that you obtained when you created your bot registration in Azure.""")
@cli_util.option('--msa-app-password', required=True, help=u"""The client secret that you obtained from your bot registration.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_ms_teams_channel_details(ctx, from_json, oda_instance_id, name, msa_app_id, msa_app_password, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['msaAppId'] = msa_app_id
    _details['msaAppPassword'] = msa_app_password

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'MSTEAMS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_web_channel_details.command_name', 'create-channel-create-web-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--is-client-authentication-enabled', required=True, type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--allowed-domains', help=u"""A comma-delimited whitelist of allowed domains.

The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain.

Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_web_channel_details(ctx, from_json, oda_instance_id, name, is_client_authentication_enabled, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, allowed_domains, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if allowed_domains is not None:
        _details['allowedDomains'] = allowed_domains

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'WEB'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_facebook_channel_details.command_name', 'create-channel-create-facebook-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--app-secret', required=True, help=u"""The app secret for your Facebook app.""")
@cli_util.option('--page-access-token', required=True, help=u"""The page access token that you generated for your Facebook page.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_facebook_channel_details(ctx, from_json, oda_instance_id, name, app_secret, page_access_token, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['appSecret'] = app_secret
    _details['pageAccessToken'] = page_access_token

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'FACEBOOK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_application_channel_details.command_name', 'create-channel-create-application-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--is-authenticated-user-id', required=True, type=click.BOOL, help=u"""True if the user id in the AIC message should be treated as an authenticated user id.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--outbound-url', help=u"""The URL to send response and error messages to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_application_channel_details(ctx, from_json, oda_instance_id, name, is_authenticated_user_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, outbound_url):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isAuthenticatedUserId'] = is_authenticated_user_id

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if outbound_url is not None:
        _details['outboundUrl'] = outbound_url

    _details['type'] = 'APPLICATION'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_service_cloud_channel_details.command_name', 'create-channel-create-service-cloud-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--domain-name', required=True, help=u"""The domain name.

If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.

If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.""")
@cli_util.option('--host-name-prefix', required=True, help=u"""The host prefix.

If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.

If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.""")
@cli_util.option('--user-name', required=True, help=u"""The user name for an Oracle B2C Service staff member who has the necessary profile permissions.""")
@cli_util.option('--password', required=True, help=u"""The password for the Oracle B2C Service staff member who has the necessary profile permissions.""")
@cli_util.option('--client-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["WSDL", "REST"]), help=u"""The type of Service Cloud client.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_service_cloud_channel_details(ctx, from_json, oda_instance_id, name, domain_name, host_name_prefix, user_name, password, client_type, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['domainName'] = domain_name
    _details['hostNamePrefix'] = host_name_prefix
    _details['userName'] = user_name
    _details['password'] = password
    _details['clientType'] = client_type

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['type'] = 'SERVICECLOUD'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_slack_channel_details.command_name', 'create-channel-create-slack-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--client-id', required=True, help=u"""The Slack Client Id for the Slack app.""")
@cli_util.option('--signing-secret', required=True, help=u"""The Signing Secret for the Slack App.""")
@cli_util.option('--client-secret', required=True, help=u"""The Client Secret for the Slack App.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--auth-success-url', help=u"""The URL to redirect to when authentication is successful.""")
@cli_util.option('--auth-error-url', help=u"""The URL to redirect to when authentication is unsuccessful.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_slack_channel_details(ctx, from_json, oda_instance_id, name, client_id, signing_secret, client_secret, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, auth_success_url, auth_error_url, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['clientId'] = client_id
    _details['signingSecret'] = signing_secret
    _details['clientSecret'] = client_secret

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if auth_success_url is not None:
        _details['authSuccessUrl'] = auth_success_url

    if auth_error_url is not None:
        _details['authErrorUrl'] = auth_error_url

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'SLACK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_osvc_channel_details.command_name', 'create-channel-create-osvc-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--host', required=True, help=u"""The host.

For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com.

For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.""")
@cli_util.option('--port', required=True, help=u"""The port.""")
@cli_util.option('--user-name', required=True, help=u"""The user name for the digital-assistant agent.""")
@cli_util.option('--password', required=True, help=u"""The password for the digital-assistant agent.""")
@cli_util.option('--total-session-count', required=True, type=click.INT, help=u"""The total session count.""")
@cli_util.option('--authentication-provider-name', required=True, help=u"""The name of the Authentication Provider to use to authenticate the user.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--channel-service', type=custom_types.CliCaseInsensitiveChoice(["OSVC", "FUSION"]), help=u"""The type of OSVC service.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_osvc_channel_details(ctx, from_json, oda_instance_id, name, host, port, user_name, password, total_session_count, authentication_provider_name, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, channel_service, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['host'] = host
    _details['port'] = port
    _details['userName'] = user_name
    _details['password'] = password
    _details['totalSessionCount'] = total_session_count
    _details['authenticationProviderName'] = authentication_provider_name

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if channel_service is not None:
        _details['channelService'] = channel_service

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'OSVC'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_app_event_channel_details.command_name', 'create-channel-create-app-event-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--outbound-url', help=u"""The URL for sending errors and responses to.""")
@cli_util.option('--event-sink-bot-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The IDs of the Skills and Digital Assistants that the Channel is routed to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_app_event_channel_details(ctx, from_json, oda_instance_id, name, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, outbound_url, event_sink_bot_ids):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if outbound_url is not None:
        _details['outboundUrl'] = outbound_url

    if event_sink_bot_ids is not None:
        _details['eventSinkBotIds'] = cli_util.parse_json_parameter("event_sink_bot_ids", event_sink_bot_ids)

    _details['type'] = 'APPEVENT'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_oss_channel_details.command_name', 'create-channel-create-oss-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--inbound-message-topic', required=True, help=u"""The topic inbound messages are received on.""")
@cli_util.option('--outbound-message-topic', required=True, help=u"""The topic outbound messages are sent on.""")
@cli_util.option('--bootstrap-servers', required=True, help=u"""The Oracle Streaming Service bootstrap servers.""")
@cli_util.option('--security-protocol', required=True, help=u"""The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.""")
@cli_util.option('--sasl-mechanism', required=True, help=u"""The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.""")
@cli_util.option('--tenancy-name', required=True, help=u"""The tenancy to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--user-name', required=True, help=u"""The user name to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--stream-pool-id', required=True, help=u"""The stream pool OCI to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--auth-token', required=True, help=u"""The authentication token to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--event-sink-bot-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The IDs of the Skills and Digital Assistants that the Channel is routed to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_oss_channel_details(ctx, from_json, oda_instance_id, name, inbound_message_topic, outbound_message_topic, bootstrap_servers, security_protocol, sasl_mechanism, tenancy_name, user_name, stream_pool_id, auth_token, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, event_sink_bot_ids):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['inboundMessageTopic'] = inbound_message_topic
    _details['outboundMessageTopic'] = outbound_message_topic
    _details['bootstrapServers'] = bootstrap_servers
    _details['securityProtocol'] = security_protocol
    _details['saslMechanism'] = sasl_mechanism
    _details['tenancyName'] = tenancy_name
    _details['userName'] = user_name
    _details['streamPoolId'] = stream_pool_id
    _details['authToken'] = auth_token

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if event_sink_bot_ids is not None:
        _details['eventSinkBotIds'] = cli_util.parse_json_parameter("event_sink_bot_ids", event_sink_bot_ids)

    _details['type'] = 'OSS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_cortana_channel_details.command_name', 'create-channel-create-cortana-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--msa-app-id', required=True, help=u"""The Microsoft App ID that you obtained when you created your bot registration in Azure.""")
@cli_util.option('--msa-app-password', required=True, help=u"""The client secret that you obtained from your bot registration.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_cortana_channel_details(ctx, from_json, oda_instance_id, name, msa_app_id, msa_app_password, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['msaAppId'] = msa_app_id
    _details['msaAppPassword'] = msa_app_password

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'CORTANA'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_android_channel_details.command_name', 'create-channel-create-android-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--is-client-authentication-enabled', required=True, type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_android_channel_details(ctx, from_json, oda_instance_id, name, is_client_authentication_enabled, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'ANDROID'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_twilio_channel_details.command_name', 'create-channel-create-twilio-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--account-sid', required=True, help=u"""The Account SID for the Twilio number.""")
@cli_util.option('--phone-number', required=True, help=u"""The Twilio phone number.""")
@cli_util.option('--auth-token', required=True, help=u"""The Auth Token for the Twilio number.""")
@cli_util.option('--is-mms-enabled', required=True, type=click.BOOL, help=u"""Whether MMS is enabled for this channel or not.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--original-connectors-url', help=u"""The original connectors URL (used for backward compatibility).""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_twilio_channel_details(ctx, from_json, oda_instance_id, name, account_sid, phone_number, auth_token, is_mms_enabled, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, original_connectors_url, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['accountSID'] = account_sid
    _details['phoneNumber'] = phone_number
    _details['authToken'] = auth_token
    _details['isMmsEnabled'] = is_mms_enabled

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if original_connectors_url is not None:
        _details['originalConnectorsUrl'] = original_connectors_url

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'TWILIO'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_webhook_channel_details.command_name', 'create-channel-create-webhook-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--outbound-url', required=True, help=u"""The URL to send responses to.""")
@cli_util.option('--payload-version', required=True, type=custom_types.CliCaseInsensitiveChoice(["1.0", "1.1"]), help=u"""The version for payloads.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_webhook_channel_details(ctx, from_json, oda_instance_id, name, outbound_url, payload_version, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['outboundUrl'] = outbound_url
    _details['payloadVersion'] = payload_version

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'WEBHOOK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.create_channel_create_ios_channel_details.command_name', 'create-channel-create-ios-channel-details'), help=u"""Creates a new Channel. \n[Command Reference](createChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The Channel's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--is-client-authentication-enabled', required=True, type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def create_channel_create_ios_channel_details(ctx, from_json, oda_instance_id, name, is_client_authentication_enabled, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, bot_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'IOS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_channel(
        oda_instance_id=oda_instance_id,
        create_channel_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@digital_assistant_group.command(name=cli_util.override('management.create_digital_assistant.command_name', 'create'), help=u"""Creates a new Digital Assistant. \n[Command Reference](createDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--kind', required=True, type=custom_types.CliCaseInsensitiveChoice(["NEW", "CLONE", "VERSION", "EXTEND"]), help=u"""How to create the Digital Assistant.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_digital_assistant(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, kind, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['kind'] = kind

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_digital_assistant(
        oda_instance_id=oda_instance_id,
        create_digital_assistant_details=_details,
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


@digital_assistant_group.command(name=cli_util.override('management.create_digital_assistant_create_digital_assistant_version_details.command_name', 'create-digital-assistant-create-digital-assistant-version-details'), help=u"""Creates a new Digital Assistant. \n[Command Reference](createDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Digital Assistant to create a new version of.""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_digital_assistant_create_digital_assistant_version_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, version_parameterconflict, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['version'] = version_parameterconflict

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['kind'] = 'VERSION'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_digital_assistant(
        oda_instance_id=oda_instance_id,
        create_digital_assistant_details=_details,
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


@digital_assistant_group.command(name=cli_util.override('management.create_digital_assistant_clone_digital_assistant_details.command_name', 'create-digital-assistant-clone-digital-assistant-details'), help=u"""Creates a new Digital Assistant. \n[Command Reference](createDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Digital Assistant to clone.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-parameterconflict', help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_digital_assistant_clone_digital_assistant_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, name, display_name, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, version_parameterconflict):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['name'] = name
    _details['displayName'] = display_name

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    _details['kind'] = 'CLONE'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_digital_assistant(
        oda_instance_id=oda_instance_id,
        create_digital_assistant_details=_details,
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


@digital_assistant_group.command(name=cli_util.override('management.create_digital_assistant_create_new_digital_assistant_details.command_name', 'create-digital-assistant-create-new-digital-assistant-details'), help=u"""Creates a new Digital Assistant. \n[Command Reference](createDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-parameterconflict', help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--native-language-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of native languages supported by this resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'native-language-tags': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'native-language-tags': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_digital_assistant_create_new_digital_assistant_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, name, display_name, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, version_parameterconflict, native_language_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['displayName'] = display_name

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    if native_language_tags is not None:
        _details['nativeLanguageTags'] = cli_util.parse_json_parameter("native_language_tags", native_language_tags)

    _details['kind'] = 'NEW'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_digital_assistant(
        oda_instance_id=oda_instance_id,
        create_digital_assistant_details=_details,
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


@digital_assistant_group.command(name=cli_util.override('management.create_digital_assistant_extend_digital_assistant_details.command_name', 'create-digital-assistant-extend-digital-assistant-details'), help=u"""Creates a new Digital Assistant. \n[Command Reference](createDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Digital Assistant to extend.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-parameterconflict', help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_digital_assistant_extend_digital_assistant_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, name, display_name, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, version_parameterconflict):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['name'] = name
    _details['displayName'] = display_name

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    _details['kind'] = 'EXTEND'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_digital_assistant(
        oda_instance_id=oda_instance_id,
        create_digital_assistant_details=_details,
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


@skill_group.command(name=cli_util.override('management.create_skill.command_name', 'create'), help=u"""Creates a new Skill from scratch. \n[Command Reference](createSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--kind', required=True, type=custom_types.CliCaseInsensitiveChoice(["NEW", "CLONE", "VERSION", "EXTEND"]), help=u"""How to create the Skill.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_skill(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, kind, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['kind'] = kind

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill(
        oda_instance_id=oda_instance_id,
        create_skill_details=_details,
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


@skill_group.command(name=cli_util.override('management.create_skill_clone_skill_details.command_name', 'create-skill-clone-skill-details'), help=u"""Creates a new Skill from scratch. \n[Command Reference](createSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Skill to clone.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-parameterconflict', help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_skill_clone_skill_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, name, display_name, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, version_parameterconflict):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['name'] = name
    _details['displayName'] = display_name

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    _details['kind'] = 'CLONE'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill(
        oda_instance_id=oda_instance_id,
        create_skill_details=_details,
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


@skill_group.command(name=cli_util.override('management.create_skill_create_new_skill_details.command_name', 'create-skill-create-new-skill-details'), help=u"""Creates a new Skill from scratch. \n[Command Reference](createSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--native-language-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of native languages supported by this resource.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'native-language-tags': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'native-language-tags': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_skill_create_new_skill_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, name, display_name, version_parameterconflict, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, native_language_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['displayName'] = display_name
    _details['version'] = version_parameterconflict

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if native_language_tags is not None:
        _details['nativeLanguageTags'] = cli_util.parse_json_parameter("native_language_tags", native_language_tags)

    _details['kind'] = 'NEW'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill(
        oda_instance_id=oda_instance_id,
        create_skill_details=_details,
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


@skill_group.command(name=cli_util.override('management.create_skill_create_skill_version_details.command_name', 'create-skill-create-skill-version-details'), help=u"""Creates a new Skill from scratch. \n[Command Reference](createSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Skill to create a new version of.""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_skill_create_skill_version_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, version_parameterconflict, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['version'] = version_parameterconflict

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['kind'] = 'VERSION'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill(
        oda_instance_id=oda_instance_id,
        create_skill_details=_details,
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


@skill_group.command(name=cli_util.override('management.create_skill_extend_skill_details.command_name', 'create-skill-extend-skill-details'), help=u"""Creates a new Skill from scratch. \n[Command Reference](createSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', required=True, help=u"""The unique identifier of the Skill to extend.""")
@cli_util.option('--name', required=True, help=u"""The reource's name. The name can contain only letters, numbers, periods, and underscores. The name must begin with a letter.""")
@cli_util.option('--display-name', required=True, help=u"""The resource's display name.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--platform-version', help=u"""The ODA Platform Version for this resource.""")
@cli_util.option('--multilingual-mode', type=custom_types.CliCaseInsensitiveChoice(["NATIVE", "TRANSLATION"]), help=u"""The multilingual mode for the resource.""")
@cli_util.option('--primary-language-tag', help=u"""The primary language for the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-parameterconflict', help=u"""The resource's version. The version can only contain numbers, letters, periods, underscores, dashes or spaces.  The version must begin with a letter or a number.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_skill_extend_skill_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, id, name, display_name, category, description, platform_version, multilingual_mode, primary_language_tag, freeform_tags, defined_tags, version_parameterconflict):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['id'] = id
    _details['name'] = name
    _details['displayName'] = display_name

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if platform_version is not None:
        _details['platformVersion'] = platform_version

    if multilingual_mode is not None:
        _details['multilingualMode'] = multilingual_mode

    if primary_language_tag is not None:
        _details['primaryLanguageTag'] = primary_language_tag

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if version_parameterconflict is not None:
        _details['version'] = version_parameterconflict

    _details['kind'] = 'EXTEND'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill(
        oda_instance_id=oda_instance_id,
        create_skill_details=_details,
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


@skill_parameter_group.command(name=cli_util.override('management.create_skill_parameter.command_name', 'create'), help=u"""Creates a new Skill Parameter. \n[Command Reference](createSkillParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--name', required=True, help=u"""The Parameter name.  This must be unique within the parent resource.""")
@cli_util.option('--display-name', required=True, help=u"""The display name for the Parameter.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE"]), help=u"""The value type.""")
@cli_util.option('--value', required=True, help=u"""The current value.  The value will be interpreted based on the `type`.""")
@cli_util.option('--description', help=u"""A description of the Parameter.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'SkillParameter'})
@cli_util.wrap_exceptions
def create_skill_parameter(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, skill_id, name, display_name, type, value, description):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['displayName'] = display_name
    _details['type'] = type
    _details['value'] = value

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_skill_parameter(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        create_skill_parameter_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_skill_parameter') and callable(getattr(client, 'get_skill_parameter')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_skill_parameter(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@translator_group.command(name=cli_util.override('management.create_translator.command_name', 'create'), help=u"""Creates a new Translator \n[Command Reference](createTranslator)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["GOOGLE", "MICROSOFT"]), help=u"""The Translation Service to use for this Translator.""")
@cli_util.option('--base-url', required=True, help=u"""The base URL for invoking the Translation Service.""")
@cli_util.option('--auth-token', required=True, help=u"""The authentication token to use when invoking the Translation Service""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Properties used when invoking the translation service. Each property is a simple key-value pair.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Translator'})
@cli_util.wrap_exceptions
def create_translator(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, type, base_url, auth_token, properties, freeform_tags, defined_tags):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type
    _details['baseUrl'] = base_url
    _details['authToken'] = auth_token

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.create_translator(
        oda_instance_id=oda_instance_id,
        create_translator_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_translator') and callable(getattr(client, 'get_translator')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_translator(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@authentication_provider_group.command(name=cli_util.override('management.delete_authentication_provider.command_name', 'delete'), help=u"""Delete the specified Authentication Provider. \n[Command Reference](deleteAuthenticationProvider)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--authentication-provider-id', required=True, help=u"""Unique Authentication Provider identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_authentication_provider(ctx, from_json, oda_instance_id, authentication_provider_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(authentication_provider_id, six.string_types) and len(authentication_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --authentication-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_authentication_provider(
        oda_instance_id=oda_instance_id,
        authentication_provider_id=authentication_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.delete_channel.command_name', 'delete'), help=u"""Delete the specified Channel. \n[Command Reference](deleteChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_channel(ctx, from_json, oda_instance_id, channel_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@digital_assistant_group.command(name=cli_util.override('management.delete_digital_assistant.command_name', 'delete'), help=u"""Delete the specified Digital Assistant. \n[Command Reference](deleteDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_digital_assistant(ctx, from_json, oda_instance_id, digital_assistant_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_digital_assistant(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@skill_group.command(name=cli_util.override('management.delete_skill.command_name', 'delete'), help=u"""Delete the specified Skill. \n[Command Reference](deleteSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_skill(ctx, from_json, oda_instance_id, skill_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_skill(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@skill_parameter_group.command(name=cli_util.override('management.delete_skill_parameter.command_name', 'delete'), help=u"""Delete the specified Skill Parameter. \n[Command Reference](deleteSkillParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--parameter-name', required=True, help=u"""The name of a Skill Parameter.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_skill_parameter(ctx, from_json, oda_instance_id, skill_id, parameter_name, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    if isinstance(parameter_name, six.string_types) and len(parameter_name.strip()) == 0:
        raise click.UsageError('Parameter --parameter-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_skill_parameter(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        parameter_name=parameter_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@translator_group.command(name=cli_util.override('management.delete_translator.command_name', 'delete'), help=u"""Delete the specified Translator. \n[Command Reference](deleteTranslator)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--translator-id', required=True, help=u"""Unique Translator identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_translator(ctx, from_json, oda_instance_id, translator_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(translator_id, six.string_types) and len(translator_id.strip()) == 0:
        raise click.UsageError('Parameter --translator-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.delete_translator(
        oda_instance_id=oda_instance_id,
        translator_id=translator_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@skill_group.command(name=cli_util.override('management.export_digital_assistant.command_name', 'export-digital-assistant'), help=u"""Exports the specified Digital Assistant as an archive to Object Storage. \n[Command Reference](exportDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.wrap_exceptions
def export_digital_assistant(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, digital_assistant_id, target):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = cli_util.parse_json_parameter("target", target)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.export_digital_assistant(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        export_digital_assistant_details=_details,
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


@skill_group.command(name=cli_util.override('management.export_skill.command_name', 'export'), help=u"""Exports the specified Skill as an archive to Object Storage. \n[Command Reference](exportSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--target', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.wrap_exceptions
def export_skill(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, skill_id, target):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['target'] = cli_util.parse_json_parameter("target", target)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.export_skill(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        export_skill_details=_details,
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


@authentication_provider_group.command(name=cli_util.override('management.get_authentication_provider.command_name', 'get'), help=u"""Gets the specified Authentication Provider. \n[Command Reference](getAuthenticationProvider)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--authentication-provider-id', required=True, help=u"""Unique Authentication Provider identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'AuthenticationProvider'})
@cli_util.wrap_exceptions
def get_authentication_provider(ctx, from_json, oda_instance_id, authentication_provider_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(authentication_provider_id, six.string_types) and len(authentication_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --authentication-provider-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_authentication_provider(
        oda_instance_id=oda_instance_id,
        authentication_provider_id=authentication_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.get_channel.command_name', 'get'), help=u"""Gets the specified Channel. \n[Command Reference](getChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def get_channel(ctx, from_json, oda_instance_id, channel_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@digital_assistant_group.command(name=cli_util.override('management.get_digital_assistant.command_name', 'get'), help=u"""Gets the specified Digital Assistant. \n[Command Reference](getDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistant'})
@cli_util.wrap_exceptions
def get_digital_assistant(ctx, from_json, oda_instance_id, digital_assistant_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_digital_assistant(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@digital_assistant_parameter_group.command(name=cli_util.override('management.get_digital_assistant_parameter.command_name', 'get'), help=u"""Gets the specified Digital Assistant Parameter. \n[Command Reference](getDigitalAssistantParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--parameter-name', required=True, help=u"""The name of a Digital Assistant Parameter.  This is unique with the Digital Assistant.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistantParameter'})
@cli_util.wrap_exceptions
def get_digital_assistant_parameter(ctx, from_json, oda_instance_id, digital_assistant_id, parameter_name):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    if isinstance(parameter_name, six.string_types) and len(parameter_name.strip()) == 0:
        raise click.UsageError('Parameter --parameter-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_digital_assistant_parameter(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        parameter_name=parameter_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@skill_group.command(name=cli_util.override('management.get_skill.command_name', 'get'), help=u"""Gets the specified Skill. \n[Command Reference](getSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Skill'})
@cli_util.wrap_exceptions
def get_skill(ctx, from_json, oda_instance_id, skill_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_skill(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@skill_parameter_group.command(name=cli_util.override('management.get_skill_parameter.command_name', 'get'), help=u"""Gets the specified Skill Parameter. \n[Command Reference](getSkillParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--parameter-name', required=True, help=u"""The name of a Skill Parameter.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'SkillParameter'})
@cli_util.wrap_exceptions
def get_skill_parameter(ctx, from_json, oda_instance_id, skill_id, parameter_name):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    if isinstance(parameter_name, six.string_types) and len(parameter_name.strip()) == 0:
        raise click.UsageError('Parameter --parameter-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_skill_parameter(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        parameter_name=parameter_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@translator_group.command(name=cli_util.override('management.get_translator.command_name', 'get'), help=u"""Gets the specified Translator. \n[Command Reference](getTranslator)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--translator-id', required=True, help=u"""Unique Translator identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Translator'})
@cli_util.wrap_exceptions
def get_translator(ctx, from_json, oda_instance_id, translator_id):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(translator_id, six.string_types) and len(translator_id.strip()) == 0:
        raise click.UsageError('Parameter --translator-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.get_translator(
        oda_instance_id=oda_instance_id,
        translator_id=translator_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bot_group.command(name=cli_util.override('management.import_bot.command_name', 'import'), help=u"""Import a Bot archive from Object Storage. \n[Command Reference](importBot)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--source', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source': {'module': 'oda', 'class': 'StorageLocation'}})
@cli_util.wrap_exceptions
def import_bot(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, source):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = cli_util.parse_json_parameter("source", source)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.import_bot(
        oda_instance_id=oda_instance_id,
        import_bot_details=_details,
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


@authentication_provider_group.command(name=cli_util.override('management.list_authentication_providers.command_name', 'list'), help=u"""Returns a page of Authentication Providers that belong to the specified Digital Assistant instance.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listAuthenticationProviders)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', help=u"""Unique Authentication Provider identifier.""")
@cli_util.option('--identity-provider', type=custom_types.CliCaseInsensitiveChoice(["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]), help=u"""List only Authentication Providers for this Identity Provider.""")
@cli_util.option('--name', help=u"""List only the information for Authentication Providers with this name. Authentication Provider names are unique and may not change.

Example: `MyProvider`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name", "identityProvider"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'AuthenticationProviderCollection'})
@cli_util.wrap_exceptions
def list_authentication_providers(ctx, from_json, all_pages, page_size, oda_instance_id, id, identity_provider, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if identity_provider is not None:
        kwargs['identity_provider'] = identity_provider
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_authentication_providers,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_authentication_providers,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_authentication_providers(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.list_channels.command_name', 'list'), help=u"""Returns a page of Channels that belong to the specified Digital Assistant instance.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listChannels)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', help=u"""Unique Channel identifier.""")
@cli_util.option('--name', help=u"""List only the information for Channels with this name. Channels names are unique and may not change.

Example: `MyChannel`""")
@cli_util.option('--category', type=custom_types.CliCaseInsensitiveChoice(["AGENT", "APPLICATION", "BOT", "BOT_AS_AGENT", "SYSTEM", "EVENT"]), help=u"""List only Channels with this category.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"]), help=u"""List only Channels of this type.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

The default sort order for `timeCreated` and `timeUpdated` is descending, and the default sort order for `name` is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'ChannelCollection'})
@cli_util.wrap_exceptions
def list_channels(ctx, from_json, all_pages, page_size, oda_instance_id, id, name, category, type, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if category is not None:
        kwargs['category'] = category
    if type is not None:
        kwargs['type'] = type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_channels,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_channels,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_channels(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@digital_assistant_parameter_group.command(name=cli_util.override('management.list_digital_assistant_parameters.command_name', 'list'), help=u"""Returns a page of Parameters that belong to the specified Digital Assistant.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listDigitalAssistantParameters)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--name', help=u"""List only Parameters with this name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "displayName", "type"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `name`.

The default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistantParameterCollection'})
@cli_util.wrap_exceptions
def list_digital_assistant_parameters(ctx, from_json, all_pages, page_size, oda_instance_id, digital_assistant_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_digital_assistant_parameters,
            oda_instance_id=oda_instance_id,
            digital_assistant_id=digital_assistant_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_digital_assistant_parameters,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            digital_assistant_id=digital_assistant_id,
            **kwargs
        )
    else:
        result = client.list_digital_assistant_parameters(
            oda_instance_id=oda_instance_id,
            digital_assistant_id=digital_assistant_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@digital_assistant_group.command(name=cli_util.override('management.list_digital_assistants.command_name', 'list'), help=u"""Returns a page of Digital Assistants that belong to the specified Digital Assistant instance.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listDigitalAssistants)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--category', help=u"""List only Bot resources with this category.""")
@cli_util.option('--name', help=u"""List only Bot resources with this name. Names are unique and may not change.

Example: `MySkill`""")
@cli_util.option('--version-parameterconflict', help=u"""List only Bot resources with this version. Versions are unique and may not change.

Example: `1.0`""")
@cli_util.option('--namespace', help=u"""List only Bot resources with this namespace. Namespaces may not change.

Example: `MyNamespace`""")
@cli_util.option('--platform-version', help=u"""List only Bot resources with this platform version.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--lifecycle-details', help=u"""List only Bot resources with this lifecycle details.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistantCollection'})
@cli_util.wrap_exceptions
def list_digital_assistants(ctx, from_json, all_pages, page_size, oda_instance_id, digital_assistant_id, category, name, version_parameterconflict, namespace, platform_version, lifecycle_state, lifecycle_details, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if digital_assistant_id is not None:
        kwargs['digital_assistant_id'] = digital_assistant_id
    if category is not None:
        kwargs['category'] = category
    if name is not None:
        kwargs['name'] = name
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    if namespace is not None:
        kwargs['namespace'] = namespace
    if platform_version is not None:
        kwargs['platform_version'] = platform_version
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lifecycle_details is not None:
        kwargs['lifecycle_details'] = lifecycle_details
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_digital_assistants,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_digital_assistants,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_digital_assistants(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@skill_parameter_group.command(name=cli_util.override('management.list_skill_parameters.command_name', 'list'), help=u"""Returns a page of Skill Parameters that belong to the specified Skill.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listSkillParameters)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--name', help=u"""List only Parameters with this name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "displayName", "type"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `name`.

The default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'SkillParameterCollection'})
@cli_util.wrap_exceptions
def list_skill_parameters(ctx, from_json, all_pages, page_size, oda_instance_id, skill_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_skill_parameters,
            oda_instance_id=oda_instance_id,
            skill_id=skill_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_skill_parameters,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            skill_id=skill_id,
            **kwargs
        )
    else:
        result = client.list_skill_parameters(
            oda_instance_id=oda_instance_id,
            skill_id=skill_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@skill_group.command(name=cli_util.override('management.list_skills.command_name', 'list'), help=u"""Returns a page of Skills that belong to the specified Digital Assistant instance.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listSkills)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', help=u"""Unique Skill identifier.""")
@cli_util.option('--category', help=u"""List only Bot resources with this category.""")
@cli_util.option('--name', help=u"""List only Bot resources with this name. Names are unique and may not change.

Example: `MySkill`""")
@cli_util.option('--version-parameterconflict', help=u"""List only Bot resources with this version. Versions are unique and may not change.

Example: `1.0`""")
@cli_util.option('--namespace', help=u"""List only Bot resources with this namespace. Namespaces may not change.

Example: `MyNamespace`""")
@cli_util.option('--platform-version', help=u"""List only Bot resources with this platform version.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--lifecycle-details', help=u"""List only Bot resources with this lifecycle details.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'SkillCollection'})
@cli_util.wrap_exceptions
def list_skills(ctx, from_json, all_pages, page_size, oda_instance_id, skill_id, category, name, version_parameterconflict, namespace, platform_version, lifecycle_state, lifecycle_details, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if skill_id is not None:
        kwargs['skill_id'] = skill_id
    if category is not None:
        kwargs['category'] = category
    if name is not None:
        kwargs['name'] = name
    if version_parameterconflict is not None:
        kwargs['version'] = version_parameterconflict
    if namespace is not None:
        kwargs['namespace'] = namespace
    if platform_version is not None:
        kwargs['platform_version'] = platform_version
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if lifecycle_details is not None:
        kwargs['lifecycle_details'] = lifecycle_details
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_skills,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_skills,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_skills(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@translator_group.command(name=cli_util.override('management.list_translators.command_name', 'list'), help=u"""Returns a page of Translators that belong to the specified Digital Assistant instance.

If the `opc-next-page` header appears in the response, then there are more items to retrieve. To get the next page in the subsequent GET request, include the header's value as the `page` query parameter. \n[Command Reference](listTranslators)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--id', help=u"""Unique Translator identifier.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["GOOGLE", "MICROSOFT"]), help=u"""List only Translators of this type.""")
@cli_util.option('--name', help=u"""List only Translators with this name. Translator names are unique and may not change.

Example: `MyTranslator`""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""List only the resources that are in this lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return per page.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.

You get this value from the `opc-next-page` header in a previous list request. To retireve the first page, omit this query parameter.

Example: `MToxMA==`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "name", "type"]), help=u"""Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.

The default sort order for `timeCreated` and `timeUpdated` is descending. For all other sort fields the default sort order is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'TranslatorCollection'})
@cli_util.wrap_exceptions
def list_translators(ctx, from_json, all_pages, page_size, oda_instance_id, id, type, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if type is not None:
        kwargs['type'] = type
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_translators,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_translators,
            limit,
            page_size,
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    else:
        result = client.list_translators(
            oda_instance_id=oda_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@digital_assistant_group.command(name=cli_util.override('management.publish_digital_assistant.command_name', 'publish'), help=u"""Publish a draft Digital Assistant. Once published the Digital Assistant cannot be modified. \n[Command Reference](publishDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistant'})
@cli_util.wrap_exceptions
def publish_digital_assistant(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, digital_assistant_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.publish_digital_assistant(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_digital_assistant') and callable(getattr(client, 'get_digital_assistant')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_digital_assistant(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@skill_group.command(name=cli_util.override('management.publish_skill.command_name', 'publish'), help=u"""Publish a draft Skill. Once published it cannot be modified. \n[Command Reference](publishSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Skill'})
@cli_util.wrap_exceptions
def publish_skill(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, skill_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.publish_skill(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_skill') and callable(getattr(client, 'get_skill')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_skill(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.rotate_channel_keys.command_name', 'rotate-channel-keys'), help=u"""This will generate new keys for any generated keys in the Channel (eg. secretKey, verifyToken). If a Channel has no generated keys then no changes will be made. Ensure that you take note of the newly generated keys in the response as they will not be returned again. \n[Command Reference](rotateChannelKeys)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'CreateChannelResult'})
@cli_util.wrap_exceptions
def rotate_channel_keys(ctx, from_json, oda_instance_id, channel_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.rotate_channel_keys(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@channel_group.command(name=cli_util.override('management.start_channel.command_name', 'start'), help=u"""Starts a Channel so that it will begin accepting messages. \n[Command Reference](startChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def start_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.start_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.stop_channel.command_name', 'stop'), help=u"""Stops a Channel so that it will no longer accept messages. \n[Command Reference](stopChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def stop_channel(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('oda', 'management', ctx)
    result = client.stop_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@authentication_provider_group.command(name=cli_util.override('management.update_authentication_provider.command_name', 'update'), help=u"""Updates the specified Authentication Provider with the information in the request body. \n[Command Reference](updateAuthenticationProvider)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--authentication-provider-id', required=True, help=u"""Unique Authentication Provider identifier.""")
@cli_util.option('--token-endpoint-url', help=u"""The IDPs URL for requesting access tokens.""")
@cli_util.option('--authorization-endpoint-url', help=u"""The IDPs URL for the page that users authenticate with by entering the user name and password.""")
@cli_util.option('--short-authorization-code-request-url', help=u"""A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows you to send query parameters).  You might need this because the generated authorization-code-request URL could be too long for SMS and older smart phones.""")
@cli_util.option('--revoke-token-endpoint-url', help=u"""If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens component to revoke the user's tokens for this service.""")
@cli_util.option('--client-id', help=u"""The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application ID.""")
@cli_util.option('--client-secret', help=u"""The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration. With Microsoft identity platform, use the application secret.""")
@cli_util.option('--scopes', help=u"""A space-separated list of the scopes that must be included when Digital Assistant requests an access token from the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled, include the scope that\u2019s necessary to get the refresh token (typically offline_access).""")
@cli_util.option('--subject-claim', help=u"""The access-token profile claim to use to identify the user.""")
@cli_util.option('--refresh-token-retention-period-in-days', type=click.INT, help=u"""The number of days to keep the refresh token in the Digital Assistant cache.""")
@cli_util.option('--redirect-url', help=u"""The OAuth Redirect URL.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'AuthenticationProvider'})
@cli_util.wrap_exceptions
def update_authentication_provider(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, authentication_provider_id, token_endpoint_url, authorization_endpoint_url, short_authorization_code_request_url, revoke_token_endpoint_url, client_id, client_secret, scopes, subject_claim, refresh_token_retention_period_in_days, redirect_url, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(authentication_provider_id, six.string_types) and len(authentication_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --authentication-provider-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if token_endpoint_url is not None:
        _details['tokenEndpointUrl'] = token_endpoint_url

    if authorization_endpoint_url is not None:
        _details['authorizationEndpointUrl'] = authorization_endpoint_url

    if short_authorization_code_request_url is not None:
        _details['shortAuthorizationCodeRequestUrl'] = short_authorization_code_request_url

    if revoke_token_endpoint_url is not None:
        _details['revokeTokenEndpointUrl'] = revoke_token_endpoint_url

    if client_id is not None:
        _details['clientId'] = client_id

    if client_secret is not None:
        _details['clientSecret'] = client_secret

    if scopes is not None:
        _details['scopes'] = scopes

    if subject_claim is not None:
        _details['subjectClaim'] = subject_claim

    if refresh_token_retention_period_in_days is not None:
        _details['refreshTokenRetentionPeriodInDays'] = refresh_token_retention_period_in_days

    if redirect_url is not None:
        _details['redirectUrl'] = redirect_url

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_authentication_provider(
        oda_instance_id=oda_instance_id,
        authentication_provider_id=authentication_provider_id,
        update_authentication_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_authentication_provider') and callable(getattr(client, 'get_authentication_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_authentication_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel.command_name', 'update'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"]), help=u"""The Channel type.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, type, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_osvc_channel_details.command_name', 'update-channel-update-osvc-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--host', help=u"""The host.

For OSVC, you can derive these values from the URL that you use to launch the Agent Browser User Interface or the chat launch page. For example, if the URL is https://sitename.exampledomain.com/app/chat/chat_launch, then the host is sitename.exampledomain.com.

For FUSION, this is the host portion of your Oracle Applications Cloud (Fusion) instance's URL. For example: sitename.exampledomain.com.""")
@cli_util.option('--port', help=u"""The port.""")
@cli_util.option('--user-name', help=u"""The user name for the digital-assistant agent.""")
@cli_util.option('--password', help=u"""The password for the digital-assistant agent.""")
@cli_util.option('--total-session-count', type=click.INT, help=u"""The total session count.""")
@cli_util.option('--channel-service', type=custom_types.CliCaseInsensitiveChoice(["OSVC", "FUSION"]), help=u"""The type of OSVC service.""")
@cli_util.option('--authentication-provider-name', help=u"""The name of the Authentication Provider to use to authenticate the user.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_osvc_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, host, port, user_name, password, total_session_count, channel_service, authentication_provider_name, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if user_name is not None:
        _details['userName'] = user_name

    if password is not None:
        _details['password'] = password

    if total_session_count is not None:
        _details['totalSessionCount'] = total_session_count

    if channel_service is not None:
        _details['channelService'] = channel_service

    if authentication_provider_name is not None:
        _details['authenticationProviderName'] = authentication_provider_name

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'OSVC'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_oss_channel_details.command_name', 'update-channel-update-oss-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--event-sink-bot-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The IDs of the Skills and Digital Assistants that the Channel is routed to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--inbound-message-topic', help=u"""The topic inbound messages are received on.""")
@cli_util.option('--outbound-message-topic', help=u"""The topic outbound messages are sent on.""")
@cli_util.option('--bootstrap-servers', help=u"""The Oracle Streaming Service bootstrap servers.""")
@cli_util.option('--security-protocol', help=u"""The security protocol to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.""")
@cli_util.option('--sasl-mechanism', help=u"""The SASL mechanmism to use when conecting to the Oracle Streaming Service. See Oracle Streaming Service documentation for a list of valid values.""")
@cli_util.option('--tenancy-name', help=u"""The tenancy to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--user-name', help=u"""The user name to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--stream-pool-id', help=u"""The stream pool OCI to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--auth-token', help=u"""The authentication token to use when connecting to the Oracle Streaming Service.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_oss_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, event_sink_bot_ids, inbound_message_topic, outbound_message_topic, bootstrap_servers, security_protocol, sasl_mechanism, tenancy_name, user_name, stream_pool_id, auth_token, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or event_sink_bot_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and event-sink-bot-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if event_sink_bot_ids is not None:
        _details['eventSinkBotIds'] = cli_util.parse_json_parameter("event_sink_bot_ids", event_sink_bot_ids)

    if inbound_message_topic is not None:
        _details['inboundMessageTopic'] = inbound_message_topic

    if outbound_message_topic is not None:
        _details['outboundMessageTopic'] = outbound_message_topic

    if bootstrap_servers is not None:
        _details['bootstrapServers'] = bootstrap_servers

    if security_protocol is not None:
        _details['securityProtocol'] = security_protocol

    if sasl_mechanism is not None:
        _details['saslMechanism'] = sasl_mechanism

    if tenancy_name is not None:
        _details['tenancyName'] = tenancy_name

    if user_name is not None:
        _details['userName'] = user_name

    if stream_pool_id is not None:
        _details['streamPoolId'] = stream_pool_id

    if auth_token is not None:
        _details['authToken'] = auth_token

    _details['type'] = 'OSS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_android_channel_details.command_name', 'update-channel-update-android-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--is-client-authentication-enabled', type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_android_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, is_client_authentication_enabled, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if is_client_authentication_enabled is not None:
        _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'ANDROID'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_ms_teams_channel_details.command_name', 'update-channel-update-ms-teams-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--msa-app-id', help=u"""The Microsoft App ID that you obtained when you created your bot registration in Azure.""")
@cli_util.option('--msa-app-password', help=u"""The client secret that you obtained from your bot registration.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_ms_teams_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, msa_app_id, msa_app_password, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if msa_app_id is not None:
        _details['msaAppId'] = msa_app_id

    if msa_app_password is not None:
        _details['msaAppPassword'] = msa_app_password

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'MSTEAMS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_app_event_channel_details.command_name', 'update-channel-update-app-event-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--outbound-url', help=u"""The URL for sending errors and responses to.""")
@cli_util.option('--event-sink-bot-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The IDs of the Skills and Digital Assistants that the Channel is routed to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}, 'event-sink-bot-ids': {'module': 'oda', 'class': 'list[string]'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_app_event_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, outbound_url, event_sink_bot_ids, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or event_sink_bot_ids:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and event-sink-bot-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if outbound_url is not None:
        _details['outboundUrl'] = outbound_url

    if event_sink_bot_ids is not None:
        _details['eventSinkBotIds'] = cli_util.parse_json_parameter("event_sink_bot_ids", event_sink_bot_ids)

    _details['type'] = 'APPEVENT'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_web_channel_details.command_name', 'update-channel-update-web-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--is-client-authentication-enabled', type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--allowed-domains', help=u"""A comma-delimited whitelist of allowed domains.

The channel will only communicate with the sites from the domains that you add to this list. For example, *.corp.example.com, *.hdr.example.com. Entering a single asterisk (*) allows unrestricted access to the channel from any domain.

Typically, you'd only enter a single asterisk during development. For production, you would add an allowlist of domains.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_web_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, is_client_authentication_enabled, allowed_domains, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if is_client_authentication_enabled is not None:
        _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if allowed_domains is not None:
        _details['allowedDomains'] = allowed_domains

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'WEB'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_ios_channel_details.command_name', 'update-channel-update-ios-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-token-expiration-time-in-minutes', type=click.INT, help=u"""The maximum time until the token expires (in minutes).""")
@cli_util.option('--is-client-authentication-enabled', type=click.BOOL, help=u"""Whether client authentication is enabled or not.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_ios_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, max_token_expiration_time_in_minutes, is_client_authentication_enabled, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if max_token_expiration_time_in_minutes is not None:
        _details['maxTokenExpirationTimeInMinutes'] = max_token_expiration_time_in_minutes

    if is_client_authentication_enabled is not None:
        _details['isClientAuthenticationEnabled'] = is_client_authentication_enabled

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'IOS'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_slack_channel_details.command_name', 'update-channel-update-slack-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--client-id', help=u"""The Slack Client Id for the Slack app.""")
@cli_util.option('--auth-success-url', help=u"""The URL to redirect to when authentication is successful.""")
@cli_util.option('--auth-error-url', help=u"""The URL to redirect to when authentication is unsuccessful.""")
@cli_util.option('--signing-secret', help=u"""The Signing Secret for the Slack App.""")
@cli_util.option('--client-secret', help=u"""The Client Secret for the Slack App.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_slack_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, client_id, auth_success_url, auth_error_url, signing_secret, client_secret, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if client_id is not None:
        _details['clientId'] = client_id

    if auth_success_url is not None:
        _details['authSuccessUrl'] = auth_success_url

    if auth_error_url is not None:
        _details['authErrorUrl'] = auth_error_url

    if signing_secret is not None:
        _details['signingSecret'] = signing_secret

    if client_secret is not None:
        _details['clientSecret'] = client_secret

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'SLACK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_service_cloud_channel_details.command_name', 'update-channel-update-service-cloud-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--domain-name', help=u"""The domain name.

If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.

If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.""")
@cli_util.option('--host-name-prefix', help=u"""The host prefix.

If you have access to Oracle B2C Service, you can derive this value from the URL that you use to launch the Agent Browser User Interface. For example, if the URL is sitename.exampledomain.com, then the host name prefix is sitename and the domain name is exampledomain.com.

If the channel is connecting to Oracle B2C Service version 19A or later, and you have multiple interfaces, then you must include the interface ID in the host (site) name . For example, for the interface that has an ID of 2, you would use something like sitename-2.exampledomain.com.""")
@cli_util.option('--user-name', help=u"""The user name for an Oracle B2C Service staff member who has the necessary profile permissions.""")
@cli_util.option('--password', help=u"""The password for the Oracle B2C Service staff member who has the necessary profile permissions.""")
@cli_util.option('--client-type', type=custom_types.CliCaseInsensitiveChoice(["WSDL", "REST"]), help=u"""The type of Service Cloud client.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_service_cloud_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, domain_name, host_name_prefix, user_name, password, client_type, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if domain_name is not None:
        _details['domainName'] = domain_name

    if host_name_prefix is not None:
        _details['hostNamePrefix'] = host_name_prefix

    if user_name is not None:
        _details['userName'] = user_name

    if password is not None:
        _details['password'] = password

    if client_type is not None:
        _details['clientType'] = client_type

    _details['type'] = 'SERVICECLOUD'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_twilio_channel_details.command_name', 'update-channel-update-twilio-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--account-sid', help=u"""The Account SID for the Twilio number.""")
@cli_util.option('--phone-number', help=u"""The Twilio phone number.""")
@cli_util.option('--auth-token', help=u"""The Auth Token for the Twilio number.""")
@cli_util.option('--is-mms-enabled', type=click.BOOL, help=u"""Whether MMS is enabled for this channel or not.""")
@cli_util.option('--original-connectors-url', help=u"""The original connectors URL (used for backward compatibility).""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_twilio_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, account_sid, phone_number, auth_token, is_mms_enabled, original_connectors_url, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if account_sid is not None:
        _details['accountSID'] = account_sid

    if phone_number is not None:
        _details['phoneNumber'] = phone_number

    if auth_token is not None:
        _details['authToken'] = auth_token

    if is_mms_enabled is not None:
        _details['isMmsEnabled'] = is_mms_enabled

    if original_connectors_url is not None:
        _details['originalConnectorsUrl'] = original_connectors_url

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'TWILIO'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_webhook_channel_details.command_name', 'update-channel-update-webhook-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--outbound-url', help=u"""The URL to send responses to.""")
@cli_util.option('--payload-version', type=custom_types.CliCaseInsensitiveChoice(["1.0", "1.1"]), help=u"""The version for payloads.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_webhook_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, outbound_url, payload_version, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if outbound_url is not None:
        _details['outboundUrl'] = outbound_url

    if payload_version is not None:
        _details['payloadVersion'] = payload_version

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'WEBHOOK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_application_channel_details.command_name', 'update-channel-update-application-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--outbound-url', help=u"""The URL to send response and error messages to.""")
@cli_util.option('--is-authenticated-user-id', type=click.BOOL, help=u"""True if the user id in the AIC message should be treated as an authenticated user id.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_application_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, outbound_url, is_authenticated_user_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if outbound_url is not None:
        _details['outboundUrl'] = outbound_url

    if is_authenticated_user_id is not None:
        _details['isAuthenticatedUserId'] = is_authenticated_user_id

    _details['type'] = 'APPLICATION'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_facebook_channel_details.command_name', 'update-channel-update-facebook-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--app-secret', help=u"""The app secret for your Facebook app.""")
@cli_util.option('--page-access-token', help=u"""The page access token that you generated for your Facebook page.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_facebook_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, app_secret, page_access_token, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if app_secret is not None:
        _details['appSecret'] = app_secret

    if page_access_token is not None:
        _details['pageAccessToken'] = page_access_token

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'FACEBOOK'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@channel_group.command(name=cli_util.override('management.update_channel_update_cortana_channel_details.command_name', 'update-channel-update-cortana-channel-details'), help=u"""Updates the specified Channel with the information in the request body. \n[Command Reference](updateChannel)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--channel-id', required=True, help=u"""Unique Channel identifier.""")
@cli_util.option('--description', help=u"""A short description of the Channel.""")
@cli_util.option('--session-expiry-duration-in-milliseconds', type=click.INT, help=u"""The number of milliseconds before a session expires.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--msa-app-id', help=u"""The Microsoft App ID that you obtained when you created your bot registration in Azure.""")
@cli_util.option('--msa-app-password', help=u"""The client secret that you obtained from your bot registration.""")
@cli_util.option('--bot-id', help=u"""The ID of the Skill or Digital Assistant that the Channel is routed to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Channel'})
@cli_util.wrap_exceptions
def update_channel_update_cortana_channel_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, channel_id, description, session_expiry_duration_in_milliseconds, freeform_tags, defined_tags, msa_app_id, msa_app_password, bot_id, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(channel_id, six.string_types) and len(channel_id.strip()) == 0:
        raise click.UsageError('Parameter --channel-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if session_expiry_duration_in_milliseconds is not None:
        _details['sessionExpiryDurationInMilliseconds'] = session_expiry_duration_in_milliseconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if msa_app_id is not None:
        _details['msaAppId'] = msa_app_id

    if msa_app_password is not None:
        _details['msaAppPassword'] = msa_app_password

    if bot_id is not None:
        _details['botId'] = bot_id

    _details['type'] = 'CORTANA'

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_channel(
        oda_instance_id=oda_instance_id,
        channel_id=channel_id,
        update_channel_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_channel') and callable(getattr(client, 'get_channel')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_channel(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@digital_assistant_group.command(name=cli_util.override('management.update_digital_assistant.command_name', 'update'), help=u"""Updates the specified Digital Assistant with the information in the request body. \n[Command Reference](updateDigitalAssistant)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'DigitalAssistant'})
@cli_util.wrap_exceptions
def update_digital_assistant(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, digital_assistant_id, category, description, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_digital_assistant(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        update_digital_assistant_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_digital_assistant') and callable(getattr(client, 'get_digital_assistant')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_digital_assistant(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@digital_assistant_parameter_group.command(name=cli_util.override('management.update_digital_assistant_parameter.command_name', 'update'), help=u"""Updates the specified Digital Assistant Parameter with the information in the request body. \n[Command Reference](updateDigitalAssistantParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--digital-assistant-id', required=True, help=u"""Unique Digital Assistant identifier.""")
@cli_util.option('--parameter-name', required=True, help=u"""The name of a Digital Assistant Parameter.  This is unique with the Digital Assistant.""")
@cli_util.option('--value', required=True, help=u"""The current value.  The value will be interpreted based on the `type`.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'DigitalAssistantParameter'})
@cli_util.wrap_exceptions
def update_digital_assistant_parameter(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, digital_assistant_id, parameter_name, value, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(digital_assistant_id, six.string_types) and len(digital_assistant_id.strip()) == 0:
        raise click.UsageError('Parameter --digital-assistant-id cannot be whitespace or empty string')

    if isinstance(parameter_name, six.string_types) and len(parameter_name.strip()) == 0:
        raise click.UsageError('Parameter --parameter-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['value'] = value

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_digital_assistant_parameter(
        oda_instance_id=oda_instance_id,
        digital_assistant_id=digital_assistant_id,
        parameter_name=parameter_name,
        update_digital_assistant_parameter_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_digital_assistant_parameter') and callable(getattr(client, 'get_digital_assistant_parameter')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_digital_assistant_parameter(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@skill_group.command(name=cli_util.override('management.update_skill.command_name', 'update'), help=u"""Updates the specified Skill with the information in the request body. \n[Command Reference](updateSkill)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--category', help=u"""The resource's category.  This is used to group resource's together.""")
@cli_util.option('--description', help=u"""A short description of the resource.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Skill'})
@cli_util.wrap_exceptions
def update_skill(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, skill_id, category, description, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if category is not None:
        _details['category'] = category

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_skill(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        update_skill_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_skill') and callable(getattr(client, 'get_skill')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_skill(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@skill_parameter_group.command(name=cli_util.override('management.update_skill_parameter.command_name', 'update'), help=u"""Updates the specified Skill Parameter with the information in the request body. \n[Command Reference](updateSkillParameter)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--skill-id', required=True, help=u"""Unique Skill identifier.""")
@cli_util.option('--parameter-name', required=True, help=u"""The name of a Skill Parameter.""")
@cli_util.option('--display-name', help=u"""The display name for the Parameter.""")
@cli_util.option('--description', help=u"""A description of the Parameter.""")
@cli_util.option('--value', help=u"""The current value.  The value will be interpreted based on the `type`.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oda', 'class': 'SkillParameter'})
@cli_util.wrap_exceptions
def update_skill_parameter(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, skill_id, parameter_name, display_name, description, value, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(skill_id, six.string_types) and len(skill_id.strip()) == 0:
        raise click.UsageError('Parameter --skill-id cannot be whitespace or empty string')

    if isinstance(parameter_name, six.string_types) and len(parameter_name.strip()) == 0:
        raise click.UsageError('Parameter --parameter-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if value is not None:
        _details['value'] = value

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_skill_parameter(
        oda_instance_id=oda_instance_id,
        skill_id=skill_id,
        parameter_name=parameter_name,
        update_skill_parameter_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_skill_parameter') and callable(getattr(client, 'get_skill_parameter')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_skill_parameter(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@translator_group.command(name=cli_util.override('management.update_translator.command_name', 'update'), help=u"""Updates the specified Translator with the information in the request body. \n[Command Reference](updateTranslator)""")
@cli_util.option('--oda-instance-id', required=True, help=u"""Unique Digital Assistant instance identifier.""")
@cli_util.option('--translator-id', required=True, help=u"""Unique Translator identifier.""")
@cli_util.option('--base-url', help=u"""The base URL for invoking the Translation Service.""")
@cli_util.option('--auth-token', help=u"""The authentication token to use when invoking the Translation Service""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Properties used when invoking the translation service. Each property is a simple key-value pair.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control in a PUT or DELETE call for a Digital Assistant instance, set the `if-match` query parameter to the value of the `ETAG` header from a previous GET or POST response for that instance. The service updates or deletes the instance only if the etag that you provide matches the instance's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'oda', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'oda', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'oda', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'oda', 'class': 'Translator'})
@cli_util.wrap_exceptions
def update_translator(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, oda_instance_id, translator_id, base_url, auth_token, properties, freeform_tags, defined_tags, if_match):

    if isinstance(oda_instance_id, six.string_types) and len(oda_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --oda-instance-id cannot be whitespace or empty string')

    if isinstance(translator_id, six.string_types) and len(translator_id.strip()) == 0:
        raise click.UsageError('Parameter --translator-id cannot be whitespace or empty string')
    if not force:
        if properties or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to properties and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if base_url is not None:
        _details['baseUrl'] = base_url

    if auth_token is not None:
        _details['authToken'] = auth_token

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('oda', 'management', ctx)
    result = client.update_translator(
        oda_instance_id=oda_instance_id,
        translator_id=translator_id,
        update_translator_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_translator') and callable(getattr(client, 'get_translator')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_translator(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
