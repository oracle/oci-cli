# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.generative_ai.src.oci_cli_generative_ai.generated import generativeai_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci generative-ai imported-model create-imported-model-hugging-face-model -> oci generative-ai imported-model create-from-huggingface
cli_util.rename_command(generativeai_cli, generativeai_cli.imported_model_group, generativeai_cli.create_imported_model_hugging_face_model, "create-from-huggingface")


# oci generative-ai imported-model create-imported-model-object-storage-object -> oci generative-ai imported-model create-from-objectstorage
cli_util.rename_command(generativeai_cli, generativeai_cli.imported_model_group, generativeai_cli.create_imported_model_object_storage_object, "create-from-objectstorage")


# Remove create from oci generative-ai imported-model
generativeai_cli.imported_model_group.commands.pop(generativeai_cli.create_imported_model.name)


@cli_util.copy_params_from_generated_command(generativeai_cli.create_imported_model_hugging_face_model, params_to_exclude=['data_source_model_id', 'data_source_access_token', 'data_source_branch', 'data_source_commit', 'version_parameterconflict'])
@generativeai_cli.imported_model_group.command(name=generativeai_cli.create_imported_model_hugging_face_model.name, help=generativeai_cli.create_imported_model_hugging_face_model.help)
@cli_util.option('--model-id', required=True, help=u"""The full model OCID from Hugging Face, typically in the format "org/model-name" (e.g., "meta-llama/Llama-2-7b"). [required]""")
@cli_util.option('--access-token', help=u"""Hugging Face access token to authenticate requests for restricted models. This token will be securely stored in OCI Vault.""")
@cli_util.option('--branch', help=u"""The name of the branch in the Hugging Face repository to import the model from. If not specified, "main" will be used by default. If you provide both a branch and a commit hash, the model will be imported from the specified commit.""")
@cli_util.option('--commit', help=u"""The commit hash in the Hugging Face repository to import the model from. If both a branch and a commit are provided, the commit hash will be used.""")
@cli_util.option('--version', help=u"""The version of the imported model.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'generative_ai', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai', 'class': 'ImportedModel'})
@cli_util.wrap_exceptions
def create_imported_model_hugging_face_model_extended(ctx, **kwargs):

    if 'model_id' in kwargs:
        kwargs['data_source_model_id'] = kwargs['model_id']
        kwargs.pop('model_id')

    if 'access_token' in kwargs:
        kwargs['data_source_access_token'] = kwargs['access_token']
        kwargs.pop('access_token')

    if 'branch' in kwargs:
        kwargs['data_source_branch'] = kwargs['branch']
        kwargs.pop('branch')

    if 'commit' in kwargs:
        kwargs['data_source_commit'] = kwargs['commit']
        kwargs.pop('commit')

    if 'version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['version']
        kwargs.pop('version')

    ctx.invoke(generativeai_cli.create_imported_model_hugging_face_model, **kwargs)


@cli_util.copy_params_from_generated_command(generativeai_cli.create_imported_model_object_storage_object, params_to_exclude=['data_source_bucket_name', 'data_source_namespace_name', 'data_source_prefix_name', 'data_source_region', 'version_parameterconflict'])
@generativeai_cli.imported_model_group.command(name=generativeai_cli.create_imported_model_object_storage_object.name, help=generativeai_cli.create_imported_model_object_storage_object.help)
@cli_util.option('--bucket-name', required=True, help=u"""The name of the Object Storage bucket. [required]""")
@cli_util.option('--namespace', required=True, help=u"""The namespace of the Object Storage where the files are stored. [required]""")
@cli_util.option('--prefix-name', required=True, help=u"""The prefix path (or folder) within the bucket where files are located. [required]""")
@cli_util.option('--region', help=u"""The full canonical Oracle Cloud region identifier (e.g., "us-ashburn-1") where the object storage bucket containing the files resides.""")
@cli_util.option('--version', help=u"""The version of the imported model.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'generative_ai', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai', 'class': 'ImportedModel'})
@cli_util.wrap_exceptions
def create_imported_model_object_storage_object_extended(ctx, **kwargs):

    if 'bucket_name' in kwargs:
        kwargs['data_source_bucket_name'] = kwargs['bucket_name']
        kwargs.pop('bucket_name')

    if 'namespace' in kwargs:
        kwargs['data_source_namespace_name'] = kwargs['namespace']
        kwargs.pop('namespace')

    if 'prefix_name' in kwargs:
        kwargs['data_source_prefix_name'] = kwargs['prefix_name']
        kwargs.pop('prefix_name')

    if 'region' in kwargs:
        kwargs['data_source_region'] = kwargs['region']
        kwargs.pop('region')

    if 'version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['version']
        kwargs.pop('version')

    ctx.invoke(generativeai_cli.create_imported_model_object_storage_object, **kwargs)


@cli_util.copy_params_from_generated_command(generativeai_cli.update_imported_model, params_to_exclude=['version_parameterconflict'])
@generativeai_cli.imported_model_group.command(name=generativeai_cli.update_imported_model.name, help=generativeai_cli.update_imported_model.help)
@cli_util.option('--version', help=u"""The version of the imported model.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'generative_ai', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'generative_ai', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'generative_ai', 'class': 'ImportedModel'})
@cli_util.wrap_exceptions
def update_imported_model_extended(ctx, **kwargs):

    if 'version' in kwargs:
        kwargs['version_parameterconflict'] = kwargs['version']
        kwargs.pop('version')

    ctx.invoke(generativeai_cli.update_imported_model, **kwargs)
