# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from services.ai_language.src.oci_cli_ai_service_language.generated import aiservicelanguage_cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias


# oci ai-language detect-dominant-language-result detect-dominant-language -> oci ai-language language detect-language
# oci ai-language detect-language-entities-result detect-language-entities -> oci ai-language language detect-entities
# oci ai-language detect-language-key-phrases-result detect-language-key-phrases -> oci ai-language language detect-key-phrases
# oci ai-language detect-language-sentiments-result detect-language-sentiments -> oci ai-language language detect-sentiments
# oci ai-language detect-language-text-classification-result detect-language-text-classification -> oci ocas language detect-text-classification
@click.command('language', cls=CommandGroupWithAlias, help="""Language group""")
@cli_util.help_option_group
def language_group():
    pass


cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_dominant_language_result_group, aiservicelanguage_cli.detect_dominant_language, "detect-language")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_entities_result_group, aiservicelanguage_cli.detect_language_entities, "detect-entities")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_key_phrases_result_group, aiservicelanguage_cli.detect_language_key_phrases, "detect-key-phrases")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_sentiments_result_group, aiservicelanguage_cli.detect_language_sentiments, "detect-sentiments")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_text_classification_result_group, aiservicelanguage_cli.detect_language_text_classification, "detect-text-classification")

aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_dominant_language_result_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_entities_result_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_key_phrases_result_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_sentiments_result_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_text_classification_result_group.name)


aiservicelanguage_cli.ai_root_group.add_command(language_group)
language_group.add_command(aiservicelanguage_cli.detect_dominant_language)
language_group.add_command(aiservicelanguage_cli.detect_language_entities)
language_group.add_command(aiservicelanguage_cli.detect_language_key_phrases)
language_group.add_command(aiservicelanguage_cli.detect_language_sentiments)
language_group.add_command(aiservicelanguage_cli.detect_language_text_classification)
