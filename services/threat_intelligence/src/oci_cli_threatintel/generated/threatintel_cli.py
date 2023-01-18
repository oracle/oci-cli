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


@cli.command(cli_util.override('threat_intelligence.threat_intelligence_root_group.command_name', 'threat-intelligence'), cls=CommandGroupWithAlias, help=cli_util.override('threat_intelligence.threat_intelligence_root_group.help', """Use the Threat Intelligence API to search for information about known threat indicators, including suspicious IP addresses, domain names, and other digital fingerprints. Threat Intelligence is a managed database of curated threat intelligence that comes from first party Oracle security insights, open source feeds, and vendor-procured data. For more information, see the [Threat Intelligence documentation]."""), short_help=cli_util.override('threat_intelligence.threat_intelligence_root_group.short_help', """Threat Intelligence API"""))
@cli_util.help_option_group
def threat_intelligence_root_group():
    pass


@click.command(cli_util.override('threat_intelligence.indicator_group.command_name', 'indicator'), cls=CommandGroupWithAlias, help="""A data signature observed on a network or host that indicates a potential security threat. Indicators can be plain text or computed (hashed) values.""")
@cli_util.help_option_group
def indicator_group():
    pass


@click.command(cli_util.override('threat_intelligence.indicator_summary_collection_group.command_name', 'indicator-summary-collection'), cls=CommandGroupWithAlias, help="""List of indicator summary objects.""")
@cli_util.help_option_group
def indicator_summary_collection_group():
    pass


@click.command(cli_util.override('threat_intelligence.threat_types_collection_group.command_name', 'threat-types-collection'), cls=CommandGroupWithAlias, help="""List of threat types that can be associated with threat indicators.""")
@cli_util.help_option_group
def threat_types_collection_group():
    pass


@click.command(cli_util.override('threat_intelligence.indicator_count_collection_group.command_name', 'indicator-count-collection'), cls=CommandGroupWithAlias, help="""A list of indicator counts by indicator type.""")
@cli_util.help_option_group
def indicator_count_collection_group():
    pass


threat_intelligence_root_group.add_command(indicator_group)
threat_intelligence_root_group.add_command(indicator_summary_collection_group)
threat_intelligence_root_group.add_command(threat_types_collection_group)
threat_intelligence_root_group.add_command(indicator_count_collection_group)


@indicator_group.command(name=cli_util.override('threat_intelligence.get_indicator.command_name', 'get'), help=u"""Get detailed information about a threat indicator with a given identifier. \n[Command Reference](getIndicator)""")
@cli_util.option('--indicator-id', required=True, help=u"""The unique identifier (OCID) of the threat indicator.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) that is used to filter results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'threat_intelligence', 'class': 'Indicator'})
@cli_util.wrap_exceptions
def get_indicator(ctx, from_json, indicator_id, compartment_id):

    if isinstance(indicator_id, six.string_types) and len(indicator_id.strip()) == 0:
        raise click.UsageError('Parameter --indicator-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('threat_intelligence', 'threatintel', ctx)
    result = client.get_indicator(
        indicator_id=indicator_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@indicator_count_collection_group.command(name=cli_util.override('threat_intelligence.list_indicator_counts.command_name', 'list-indicator-counts'), help=u"""Get the current count of each threat indicator type. Indicator counts can be sorted in ascending or descending order. \n[Command Reference](listIndicatorCounts)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) that is used to filter results.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'threat_intelligence', 'class': 'IndicatorCountCollection'})
@cli_util.wrap_exceptions
def list_indicator_counts(ctx, from_json, all_pages, compartment_id, sort_order):

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('threat_intelligence', 'threatintel', ctx)
    result = client.list_indicator_counts(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@indicator_summary_collection_group.command(name=cli_util.override('threat_intelligence.list_indicators.command_name', 'list-indicators'), help=u"""Get a list of threat indicator summaries based on the search criteria. \n[Command Reference](listIndicators)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) that is used to filter results.""")
@cli_util.option('--threat-type-name', multiple=True, help=u"""The threat type of entites to be returned. To filter for multiple threat types, repeat this parameter.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL"]), help=u"""The indicator type of entities to be returned.""")
@cli_util.option('--value', help=u"""The indicator value of entities to be returned.""")
@cli_util.option('--confidence-greater-than-or-equal-to', type=click.INT, help=u"""The minimum confidence score of entities to be returned.""")
@cli_util.option('--time-updated-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest update time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-less-than', type=custom_types.CLI_DATETIME, help=u"""Return indicators updated before the provided time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-last-seen-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest last seen time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-last-seen-less-than', type=custom_types.CLI_DATETIME, help=u"""Return indicators last seen before the provided time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest created/first seen time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""Return indicators created/first seen before the provided time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["confidence", "timeCreated", "timeUpdated", "timeLastSeen"]), help=u"""The field to sort by. Only one field to sort by may be provided.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'threat-type-name': {'module': 'threat_intelligence', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'threat-type-name': {'module': 'threat_intelligence', 'class': 'list[string]'}}, output_type={'module': 'threat_intelligence', 'class': 'IndicatorSummaryCollection'})
@cli_util.wrap_exceptions
def list_indicators(ctx, from_json, all_pages, page_size, compartment_id, threat_type_name, type, value, confidence_greater_than_or_equal_to, time_updated_greater_than_or_equal_to, time_updated_less_than, time_last_seen_greater_than_or_equal_to, time_last_seen_less_than, time_created_greater_than_or_equal_to, time_created_less_than, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if threat_type_name is not None and len(threat_type_name) > 0:
        kwargs['threat_type_name'] = threat_type_name
    if type is not None:
        kwargs['type'] = type
    if value is not None:
        kwargs['value'] = value
    if confidence_greater_than_or_equal_to is not None:
        kwargs['confidence_greater_than_or_equal_to'] = confidence_greater_than_or_equal_to
    if time_updated_greater_than_or_equal_to is not None:
        kwargs['time_updated_greater_than_or_equal_to'] = time_updated_greater_than_or_equal_to
    if time_updated_less_than is not None:
        kwargs['time_updated_less_than'] = time_updated_less_than
    if time_last_seen_greater_than_or_equal_to is not None:
        kwargs['time_last_seen_greater_than_or_equal_to'] = time_last_seen_greater_than_or_equal_to
    if time_last_seen_less_than is not None:
        kwargs['time_last_seen_less_than'] = time_last_seen_less_than
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('threat_intelligence', 'threatintel', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_indicators,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_indicators,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_indicators(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@threat_types_collection_group.command(name=cli_util.override('threat_intelligence.list_threat_types.command_name', 'list-threat-types'), help=u"""Gets a list of threat types that are available to use as parameters when querying indicators. The list is sorted by threat type name according to the sort order query param. \n[Command Reference](listThreatTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) that is used to filter results.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'threat_intelligence', 'class': 'ThreatTypesCollection'})
@cli_util.wrap_exceptions
def list_threat_types(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('threat_intelligence', 'threatintel', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_threat_types,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_threat_types,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_threat_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@indicator_group.command(name=cli_util.override('threat_intelligence.summarize_indicators.command_name', 'summarize'), help=u"""Get indicator summaries based on advanced search criteria. \n[Command Reference](summarizeIndicators)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) that is used to filter results.""")
@cli_util.option('--indicator-type', type=custom_types.CliCaseInsensitiveChoice(["DOMAIN_NAME", "FILE_NAME", "MD5_HASH", "SHA1_HASH", "SHA256_HASH", "IP_ADDRESS", "URL"]), help=u"""The type of indicator this is""")
@cli_util.option('--indicator-value', help=u"""The value for the type of indicator this is""")
@cli_util.option('--threat-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The threat type of entites to be returned.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--confidence-greater-than-or-equal-to', type=click.INT, help=u"""The minimum level of confidence to return""")
@cli_util.option('--time-updated-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest update time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated-less-than', type=custom_types.CLI_DATETIME, help=u"""The newest update time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-last-seen-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest last seen time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-last-seen-less-than', type=custom_types.CLI_DATETIME, help=u"""The newest last seen time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""The oldest creation time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""The newest creation time of entities to be returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--indicator-seen-by', help=u"""Filter to include indicators that have been seen by the provided source.""")
@cli_util.option('--malware', help=u"""Filter to include indicators associated with the provided malware.""")
@cli_util.option('--threat-actor', help=u"""Filter to included indicators associated with the provided threat actor.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["CONFIDENCE", "TIMECREATED", "TIMEUPDATED", "TIMELASTSEEN"]), help=u"""The field to sort by. Only one field to sort by may be provided""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@json_skeleton_utils.get_cli_json_input_option({'threat-types': {'module': 'threat_intelligence', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'threat-types': {'module': 'threat_intelligence', 'class': 'list[string]'}}, output_type={'module': 'threat_intelligence', 'class': 'IndicatorSummaryCollection'})
@cli_util.wrap_exceptions
def summarize_indicators(ctx, from_json, compartment_id, indicator_type, indicator_value, threat_types, confidence_greater_than_or_equal_to, time_updated_greater_than_or_equal_to, time_updated_less_than, time_last_seen_greater_than_or_equal_to, time_last_seen_less_than, time_created_greater_than_or_equal_to, time_created_less_than, indicator_seen_by, malware, threat_actor, sort_order, sort_by, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if indicator_type is not None:
        _details['indicatorType'] = indicator_type

    if indicator_value is not None:
        _details['indicatorValue'] = indicator_value

    if threat_types is not None:
        _details['threatTypes'] = cli_util.parse_json_parameter("threat_types", threat_types)

    if confidence_greater_than_or_equal_to is not None:
        _details['confidenceGreaterThanOrEqualTo'] = confidence_greater_than_or_equal_to

    if time_updated_greater_than_or_equal_to is not None:
        _details['timeUpdatedGreaterThanOrEqualTo'] = time_updated_greater_than_or_equal_to

    if time_updated_less_than is not None:
        _details['timeUpdatedLessThan'] = time_updated_less_than

    if time_last_seen_greater_than_or_equal_to is not None:
        _details['timeLastSeenGreaterThanOrEqualTo'] = time_last_seen_greater_than_or_equal_to

    if time_last_seen_less_than is not None:
        _details['timeLastSeenLessThan'] = time_last_seen_less_than

    if time_created_greater_than_or_equal_to is not None:
        _details['timeCreatedGreaterThanOrEqualTo'] = time_created_greater_than_or_equal_to

    if time_created_less_than is not None:
        _details['timeCreatedLessThan'] = time_created_less_than

    if indicator_seen_by is not None:
        _details['indicatorSeenBy'] = indicator_seen_by

    if malware is not None:
        _details['malware'] = malware

    if threat_actor is not None:
        _details['threatActor'] = threat_actor

    if sort_order is not None:
        _details['sortOrder'] = sort_order

    if sort_by is not None:
        _details['sortBy'] = sort_by

    client = cli_util.build_client('threat_intelligence', 'threatintel', ctx)
    result = client.summarize_indicators(
        compartment_id=compartment_id,
        summarize_indicators_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
