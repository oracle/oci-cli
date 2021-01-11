# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('secrets.secrets_root_group.command_name', 'secrets'), cls=CommandGroupWithAlias, help=cli_util.override('secrets.secrets_root_group.help', """API for retrieving secrets from vaults."""), short_help=cli_util.override('secrets.secrets_root_group.short_help', """Secrets"""))
@cli_util.help_option_group
def secrets_root_group():
    pass


@click.command(cli_util.override('secrets.secret_bundle_version_summary_group.command_name', 'secret-bundle-version-summary'), cls=CommandGroupWithAlias, help="""The properties of the secret bundle. (Secret bundle version summary objects do not include the actual contents of the secret.)""")
@cli_util.help_option_group
def secret_bundle_version_summary_group():
    pass


@click.command(cli_util.override('secrets.secret_bundle_group.command_name', 'secret-bundle'), cls=CommandGroupWithAlias, help="""The contents of the secret, properties of the secret (and secret version), and user-provided contextual metadata for the secret.""")
@cli_util.help_option_group
def secret_bundle_group():
    pass


secrets_root_group.add_command(secret_bundle_version_summary_group)
secrets_root_group.add_command(secret_bundle_group)


@secret_bundle_group.command(name=cli_util.override('secrets.get_secret_bundle.command_name', 'get'), help=u"""Gets a secret bundle that matches either the specified `stage`, `label`, or `versionNumber` parameter. If none of these parameters are provided, the bundle for the secret version marked as `CURRENT` will be returned. \n[Command Reference](getSecretBundle)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--version-number', type=click.INT, help=u"""The version number of the secret.""")
@cli_util.option('--secret-version-name', help=u"""The name of the secret. (This might be referred to as the name of the secret version. Names are unique across the different versions of a secret.)""")
@cli_util.option('--stage', type=custom_types.CliCaseInsensitiveChoice(["CURRENT", "PENDING", "LATEST", "PREVIOUS", "DEPRECATED"]), help=u"""The rotation state of the secret version.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'secrets', 'class': 'SecretBundle'})
@cli_util.wrap_exceptions
def get_secret_bundle(ctx, from_json, secret_id, version_number, secret_version_name, stage):

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if version_number is not None:
        kwargs['version_number'] = version_number
    if secret_version_name is not None:
        kwargs['secret_version_name'] = secret_version_name
    if stage is not None:
        kwargs['stage'] = stage
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('secrets', 'secrets', ctx)
    result = client.get_secret_bundle(
        secret_id=secret_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@secret_bundle_version_summary_group.command(name=cli_util.override('secrets.list_secret_bundle_versions.command_name', 'list-secret-bundle-versions'), help=u"""Lists all secret bundle versions for the specified secret. \n[Command Reference](listSecretBundleVersions)""")
@cli_util.option('--secret-id', required=True, help=u"""The OCID of the secret.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["VERSION_NUMBER"]), help=u"""The field to sort by. You can specify only one sort order. The default order for `VERSION_NUMBER` is ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'secrets', 'class': 'list[SecretBundleVersionSummary]'})
@cli_util.wrap_exceptions
def list_secret_bundle_versions(ctx, from_json, all_pages, page_size, secret_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(secret_id, six.string_types) and len(secret_id.strip()) == 0:
        raise click.UsageError('Parameter --secret-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('secrets', 'secrets', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_secret_bundle_versions,
            secret_id=secret_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_secret_bundle_versions,
            limit,
            page_size,
            secret_id=secret_id,
            **kwargs
        )
    else:
        result = client.list_secret_bundle_versions(
            secret_id=secret_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
