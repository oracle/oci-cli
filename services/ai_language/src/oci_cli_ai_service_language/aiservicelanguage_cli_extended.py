# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from services.ai_language.src.oci_cli_ai_service_language.generated import aiservicelanguage_cli
from oci_cli import cli_util
from oci_cli.aliasing import CommandGroupWithAlias

# Batch APIs

# oci ai-language batch-detect-dominant-language batch-detect-dominant-language -> oci ai language batch-detect-language
# oci ai-language batch-detect-language-entities batch-detect-language-entities -> oci ai language batch-detect-entities
# oci ai-language batch-detect-language-key-phrases batch-detect-language-key-phrases -> oci ai language batch-detect-key-phrases
# oci ai-language batch-detect-language-sentiments batch-detect-language-sentiments -> oci ai language batch-detect-sentiments
# oci ai-language batch-detect-language-text-classification batch-detect-language-text-classification -> oci ai language batch-detect-text-classification

# Single document APIs

# oci ai-language detect-dominant-language detect-dominant-language -> oci ai language detect-language
# oci ai-language detect-language-entities detect-language-entities -> oci ai language detect-entities
# oci ai-language detect-language-key-phrases detect-language-key-phrases -> oci ai language detect-key-phrases
# oci ai-language detect-language-sentiments detect-language-sentiments -> oci ai language detect-sentiments
# oci ai-language detect-language-text-classification detect-language-text-classification -> oci ai language detect-text-classification


@click.command('language', cls=CommandGroupWithAlias, help="""Language group""")
@cli_util.help_option_group
def language_group():
    pass


# Batch APIs
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_dominant_language_group, aiservicelanguage_cli.batch_detect_dominant_language, "batch-detect-language")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_language_entities_group, aiservicelanguage_cli.batch_detect_language_entities, "batch-detect-entities")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_language_key_phrases_group, aiservicelanguage_cli.batch_detect_language_key_phrases, "batch-detect-key-phrases")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_language_sentiments_group, aiservicelanguage_cli.batch_detect_language_sentiments, "batch-detect-sentiments")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_language_text_classification_group, aiservicelanguage_cli.batch_detect_language_text_classification, "batch-detect-text-classification")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.batch_detect_language_pii_entities_group, aiservicelanguage_cli.batch_detect_language_pii_entities, "batch-detect-pii-entities")

# Single Documents APIs
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_dominant_language_group, aiservicelanguage_cli.detect_dominant_language, "detect-language")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_entities_group, aiservicelanguage_cli.detect_language_entities, "detect-entities")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_key_phrases_group, aiservicelanguage_cli.detect_language_key_phrases, "detect-key-phrases")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_sentiments_group, aiservicelanguage_cli.detect_language_sentiments, "detect-sentiments")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.detect_language_text_classification_group, aiservicelanguage_cli.detect_language_text_classification, "detect-text-classification")

# Batch APIs
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_dominant_language_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_language_entities_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_language_key_phrases_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_language_sentiments_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_language_text_classification_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_detect_language_pii_entities_group.name)

# Single Documents APIs
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_dominant_language_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_entities_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_key_phrases_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_sentiments_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.detect_language_text_classification_group.name)

# Batch APIs
aiservicelanguage_cli.ai_root_group.add_command(language_group)
language_group.add_command(aiservicelanguage_cli.batch_detect_dominant_language)
language_group.add_command(aiservicelanguage_cli.batch_detect_language_entities)
language_group.add_command(aiservicelanguage_cli.batch_detect_language_key_phrases)
language_group.add_command(aiservicelanguage_cli.batch_detect_language_sentiments)
language_group.add_command(aiservicelanguage_cli.batch_detect_language_text_classification)
language_group.add_command(aiservicelanguage_cli.batch_detect_language_pii_entities)

# Single Documents APIs
aiservicelanguage_cli.ai_root_group.add_command(language_group)
language_group.add_command(aiservicelanguage_cli.detect_dominant_language)
language_group.add_command(aiservicelanguage_cli.detect_language_entities)
language_group.add_command(aiservicelanguage_cli.detect_language_key_phrases)
language_group.add_command(aiservicelanguage_cli.detect_language_sentiments)
language_group.add_command(aiservicelanguage_cli.detect_language_text_classification)

# Remove polymorphic model commands
aiservicelanguage_cli.model_group.commands.pop(aiservicelanguage_cli.create_model_data_science_labeling_dataset.name)
aiservicelanguage_cli.model_group.commands.pop(aiservicelanguage_cli.create_model_object_storage_dataset.name)
aiservicelanguage_cli.model_group.commands.pop(aiservicelanguage_cli.create_model_named_entity_recognition_model_details.name)
aiservicelanguage_cli.model_group.commands.pop(aiservicelanguage_cli.create_model_text_classification_model_details.name)
aiservicelanguage_cli.model_group.commands.pop(aiservicelanguage_cli.create_model_test_and_validation_dataset_strategy.name)

# Rename evaluation result command
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.evaluation_result_collection_group, aiservicelanguage_cli.list_evaluation_results, "list")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.ai_root_group, aiservicelanguage_cli.evaluation_result_collection_group, "evaluation-result")

# Rename work-requst error and log
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.ai_root_group, aiservicelanguage_cli.work_request_error_group, "error")
cli_util.rename_command(aiservicelanguage_cli, aiservicelanguage_cli.ai_root_group, aiservicelanguage_cli.work_request_log_group, "log")

# Remove project, model, endpoint, language_translation, work_request_long and work_request_error from root
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.project_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.model_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.endpoint_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.work_request_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.batch_language_translation_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.work_request_error_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.work_request_log_group.name)
aiservicelanguage_cli.ai_root_group.commands.pop(aiservicelanguage_cli.evaluation_result_collection_group.name)

# Add project, model, endpoint, language_translation group to language_group
language_group.add_command(aiservicelanguage_cli.project_group)
language_group.add_command(aiservicelanguage_cli.model_group)
language_group.add_command(aiservicelanguage_cli.endpoint_group)
language_group.add_command(aiservicelanguage_cli.work_request_group)
language_group.add_command(aiservicelanguage_cli.batch_language_translation)
language_group.add_command(aiservicelanguage_cli.evaluation_result_collection_group)

# Add work-request error and logs messages to work-request group
aiservicelanguage_cli.work_request_group.add_command(aiservicelanguage_cli.work_request_error_group)
aiservicelanguage_cli.work_request_group.add_command(aiservicelanguage_cli.work_request_log_group)
