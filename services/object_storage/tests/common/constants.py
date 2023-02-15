# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

import os

default_recording_path = 'services/object_storage/tests/cassettes'
objectstorage_recording_path = 'services/object_storage/tests/objectstorage_cassettes'

is_objectstorage_env = os.environ['OCI_CLI_NAMESPACE'] == 'axzbp3kgiaim'

CASSETTE_LIBRARY_DIR = objectstorage_recording_path if is_objectstorage_env else default_recording_path
DEST_REGION = 'us-ashburn-1' if is_objectstorage_env else 'us-phoenix-1'
