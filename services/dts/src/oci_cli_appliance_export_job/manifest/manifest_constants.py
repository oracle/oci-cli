# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# Constants for manifest operation

OBJECT_NAME_MAX_PATH_LENGTH = 255  # Max length allowed for a file name on linux systems
OBJECT_PATH_SEPARATOR = '/'
MANIFEST_OBJECT_NAME_PREFIX = 'oci_data_export_manifest_{}'  # oci_data_export_<job-id>
MAX_PART_SIZE_MB = 1024 * 1024 * 100  # 100MB
MAX_EXPORT_SIZE = 1024 * 1024 * 1024 * 1024 * 150  # 150 TB
ENCODING_FORMAT_UTF = 'utf-8'
