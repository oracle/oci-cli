# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('generic_artifacts_content.generic_artifacts_content_root_group.command_name', 'generic-artifacts-content'), cls=CommandGroupWithAlias, help=cli_util.override('generic_artifacts_content.generic_artifacts_content_root_group.help', """API covering the Generic Artifacts Service content
Use this API to put and get generic artifact content."""), short_help=cli_util.override('generic_artifacts_content.generic_artifacts_content_root_group.short_help', """Generic Artifacts Content API"""))
@cli_util.help_option_group
def generic_artifacts_content_root_group():
    pass


@click.command(cli_util.override('generic_artifacts_content.generic_artifact_group.command_name', 'generic-artifact'), cls=CommandGroupWithAlias, help="""The metadata of the artifact.""")
@cli_util.help_option_group
def generic_artifact_group():
    pass


generic_artifacts_content_root_group.add_command(generic_artifact_group)


@generic_artifact_group.command(name=cli_util.override('generic_artifacts_content.get_generic_artifact_content.command_name', 'get-generic-artifact-content'), help=u"""Gets the specified artifact's content. \n[Command Reference](getGenericArtifactContent)""")
@cli_util.option('--artifact-id', required=True, help=u"""The [OCID] of the artifact.

Example: `ocid1.genericartifact.oc1..exampleuniqueID`""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_generic_artifact_content(ctx, from_json, file, artifact_id):

    if isinstance(artifact_id, six.string_types) and len(artifact_id.strip()) == 0:
        raise click.UsageError('Parameter --artifact-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('generic_artifacts_content', 'generic_artifacts_content', ctx)
    result = client.get_generic_artifact_content(
        artifact_id=artifact_id,
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


@generic_artifact_group.command(name=cli_util.override('generic_artifacts_content.get_generic_artifact_content_by_path.command_name', 'get-generic-artifact-content-by-path'), help=u"""Gets the content of an artifact with a specified `artifactPath` and `version`. \n[Command Reference](getGenericArtifactContentByPath)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.repository.oc1..exampleuniqueID`""")
@cli_util.option('--artifact-path', required=True, help=u"""A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

Example: `project01/my-web-app/artifact-abc`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""A user-defined string to describe the artifact version.

Example: `1.1.2` or `1.2-beta-2`""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_generic_artifact_content_by_path(ctx, from_json, file, repository_id, artifact_path, version_parameterconflict):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(artifact_path, six.string_types) and len(artifact_path.strip()) == 0:
        raise click.UsageError('Parameter --artifact-path cannot be whitespace or empty string')

    if isinstance(version_parameterconflict, six.string_types) and len(version_parameterconflict.strip()) == 0:
        raise click.UsageError('Parameter --version-parameterconflict cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('generic_artifacts_content', 'generic_artifacts_content', ctx)
    result = client.get_generic_artifact_content_by_path(
        repository_id=repository_id,
        artifact_path=artifact_path,
        version=version_parameterconflict,
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


@generic_artifact_group.command(name=cli_util.override('generic_artifacts_content.put_generic_artifact_content_by_path.command_name', 'put-generic-artifact-content-by-path'), help=u"""Uploads an artifact. Provide `artifactPath`, `version` and content. Avoid entering confidential information when you define the path and version. \n[Command Reference](putGenericArtifactContentByPath)""")
@cli_util.option('--repository-id', required=True, help=u"""The [OCID] of the repository.

Example: `ocid1.repository.oc1..exampleuniqueID`""")
@cli_util.option('--artifact-path', required=True, help=u"""A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

Example: `project01/my-web-app/artifact-abc`""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""A user-defined string to describe the artifact version.

Example: `1.1.2` or `1.2-beta-2`""")
@cli_util.option('--generic-artifact-content-body', required=True, help=u"""Uploads an artifact. Provide artifact path, version and content. Avoid entering confidential information when you define the path and version.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the `etag` from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the `etag` you provide matches the resource's current `etag` value. When 'if-match' is provided and its value does not exactly match the 'etag' of the resource on the server, the request fails with the 412 response code.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'generic_artifacts_content', 'class': 'GenericArtifact'})
@cli_util.wrap_exceptions
def put_generic_artifact_content_by_path(ctx, from_json, repository_id, artifact_path, version_parameterconflict, generic_artifact_content_body, if_match):

    if isinstance(repository_id, six.string_types) and len(repository_id.strip()) == 0:
        raise click.UsageError('Parameter --repository-id cannot be whitespace or empty string')

    if isinstance(artifact_path, six.string_types) and len(artifact_path.strip()) == 0:
        raise click.UsageError('Parameter --artifact-path cannot be whitespace or empty string')

    if isinstance(version_parameterconflict, six.string_types) and len(version_parameterconflict.strip()) == 0:
        raise click.UsageError('Parameter --version-parameterconflict cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    # do not automatically retry operations with binary inputs
    kwargs['retry_strategy'] = oci.retry.NoneRetryStrategy()

    client = cli_util.build_client('generic_artifacts_content', 'generic_artifacts_content', ctx)
    result = client.put_generic_artifact_content_by_path(
        repository_id=repository_id,
        artifact_path=artifact_path,
        version=version_parameterconflict,
        generic_artifact_content_body=generic_artifact_content_body,
        **kwargs
    )
    cli_util.render_response(result, ctx)
