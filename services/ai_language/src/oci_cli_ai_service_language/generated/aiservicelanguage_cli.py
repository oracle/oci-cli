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


@cli.command(cli_util.override('ai.ai_root_group.command_name', 'ai'), cls=CommandGroupWithAlias, help=cli_util.override('ai.ai_root_group.help', """OCI AI Service solutions can help Enterprise customers integrate AI into their products immediately using our proven,
    pre-trained and custom models or containers, without a need to set up an house team of AI and ML experts.
    This allows enterprises to focus on business drivers and development work rather than AI and ML operations, which shortens the time to market."""), short_help=cli_util.override('ai.ai_root_group.short_help', """Oracle Cloud Infrastructure Artificial Intelligence Services API"""))
@cli_util.help_option_group
def ai_root_group():
    pass


@click.command(cli_util.override('ai.detect_language_key_phrases_result_group.command_name', 'detect-language-key-phrases-result'), cls=CommandGroupWithAlias, help="""Result of a language keyPhrases detect call.""")
@cli_util.help_option_group
def detect_language_key_phrases_result_group():
    pass


@click.command(cli_util.override('ai.detect_language_text_classification_result_group.command_name', 'detect-language-text-classification-result'), cls=CommandGroupWithAlias, help="""Result of text labels detect call.""")
@cli_util.help_option_group
def detect_language_text_classification_result_group():
    pass


@click.command(cli_util.override('ai.detect_language_entities_result_group.command_name', 'detect-language-entities-result'), cls=CommandGroupWithAlias, help="""Result of entities detect call.""")
@cli_util.help_option_group
def detect_language_entities_result_group():
    pass


@click.command(cli_util.override('ai.detect_language_sentiments_result_group.command_name', 'detect-language-sentiments-result'), cls=CommandGroupWithAlias, help="""Result of sentiments detect call.""")
@cli_util.help_option_group
def detect_language_sentiments_result_group():
    pass


@click.command(cli_util.override('ai.detect_dominant_language_result_group.command_name', 'detect-dominant-language-result'), cls=CommandGroupWithAlias, help="""Result of language detect call.""")
@cli_util.help_option_group
def detect_dominant_language_result_group():
    pass


ai_root_group.add_command(detect_language_key_phrases_result_group)
ai_root_group.add_command(detect_language_text_classification_result_group)
ai_root_group.add_command(detect_language_entities_result_group)
ai_root_group.add_command(detect_language_sentiments_result_group)
ai_root_group.add_command(detect_dominant_language_result_group)


@detect_dominant_language_result_group.command(name=cli_util.override('ai.detect_dominant_language.command_name', 'detect-dominant-language'), help=u"""Make a detect call to language detection pre-deployed model. \n[Command Reference](detectDominantLanguage)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect language.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectDominantLanguageResult'})
@cli_util.wrap_exceptions
def detect_dominant_language(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_dominant_language(
        detect_dominant_language_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_entities_result_group.command(name=cli_util.override('ai.detect_language_entities.command_name', 'detect-language-entities'), help=u"""Make a detect call to enitiy pre-deployed model \n[Command Reference](detectLanguageEntities)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect entities.""")
@cli_util.option('--model-version', type=custom_types.CliCaseInsensitiveChoice(["V2.1", "V1.1"]), help=u"""Named Entity Recognition model versions. By default user will get output from V2.1 implementation.""")
@cli_util.option('--is-pii', type=click.BOOL, help=u"""If this parameter is set to true, you only get PII (Personally identifiable information) entities like PhoneNumber, Email, Person, and so on. Default value is false.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageEntitiesResult'})
@cli_util.wrap_exceptions
def detect_language_entities(ctx, from_json, text, model_version, is_pii):

    kwargs = {}
    if model_version is not None:
        kwargs['model_version'] = model_version
    if is_pii is not None:
        kwargs['is_pii'] = is_pii
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_entities(
        detect_language_entities_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_key_phrases_result_group.command(name=cli_util.override('ai.detect_language_key_phrases.command_name', 'detect-language-key-phrases'), help=u"""Make a detect call to the keyPhrase pre-deployed model. \n[Command Reference](detectLanguageKeyPhrases)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect keyPhrases.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageKeyPhrasesResult'})
@cli_util.wrap_exceptions
def detect_language_key_phrases(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_key_phrases(
        detect_language_key_phrases_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_sentiments_result_group.command(name=cli_util.override('ai.detect_language_sentiments.command_name', 'detect-language-sentiments'), help=u"""Make a detect call to sentiment pre-deployed model. \n[Command Reference](detectLanguageSentiments)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect sentiments.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageSentimentsResult'})
@cli_util.wrap_exceptions
def detect_language_sentiments(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_sentiments(
        detect_language_sentiments_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@detect_language_text_classification_result_group.command(name=cli_util.override('ai.detect_language_text_classification.command_name', 'detect-language-text-classification'), help=u"""Make a detect call to text classification from the pre-deployed model. \n[Command Reference](detectLanguageTextClassification)""")
@cli_util.option('--text', required=True, help=u"""Document text for detect text labels.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ai_language', 'class': 'DetectLanguageTextClassificationResult'})
@cli_util.wrap_exceptions
def detect_language_text_classification(ctx, from_json, text):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    client = cli_util.build_client('ai_language', 'ai_service_language', ctx)
    result = client.detect_language_text_classification(
        detect_language_text_classification_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
