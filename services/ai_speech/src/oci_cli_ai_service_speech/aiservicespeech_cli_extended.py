# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from services.ai_speech.src.oci_cli_ai_service_speech.generated import aiservicespeech_cli

aiservicespeech_cli.transcription_job_group.commands.pop(aiservicespeech_cli.create_transcription_job_object_list_file_input_location.name)
aiservicespeech_cli.transcription_job_group.commands.pop(aiservicespeech_cli.create_transcription_job_object_list_inline_input_location.name)
