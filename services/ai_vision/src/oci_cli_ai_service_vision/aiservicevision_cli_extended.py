# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ai_vision.src.oci_cli_ai_service_vision.generated import aiservicevision_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# Remove analyze-document from oci ai-vision analyze-document-result
aiservicevision_cli.analyze_document_result_group.commands.pop(aiservicevision_cli.analyze_document.name)

# Remove analyze-image from oci ai-vision analyze-image-result
aiservicevision_cli.analyze_image_result_group.commands.pop(aiservicevision_cli.analyze_image.name)

# Move commands under 'oci ai-vision analyze-document-result' -> 'oci ai-vision'
aiservicevision_cli.ai_vision_root_group.commands.pop(aiservicevision_cli.analyze_document_result_group.name)
aiservicevision_cli.ai_vision_root_group.add_command(aiservicevision_cli.analyze_document)
aiservicevision_cli.ai_vision_root_group.add_command(
    aiservicevision_cli.analyze_document_object_storage_document_details)
aiservicevision_cli.ai_vision_root_group.add_command(aiservicevision_cli.analyze_document_inline_document_details)

# Move commands under 'oci ai-vision analyze-image-result' -> 'oci ai-vision'
aiservicevision_cli.ai_vision_root_group.commands.pop(aiservicevision_cli.analyze_image_result_group.name)
aiservicevision_cli.ai_vision_root_group.add_command(aiservicevision_cli.analyze_image)
aiservicevision_cli.ai_vision_root_group.add_command(aiservicevision_cli.analyze_image_object_storage_image_details)
aiservicevision_cli.ai_vision_root_group.add_command(aiservicevision_cli.analyze_image_inline_image_details)
