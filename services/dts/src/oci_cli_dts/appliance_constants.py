# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os

APPLIANCE_ACCESS_TOKEN_KEY = "appliance_access_token"
APPLIANCE_AUTH_USER = "admin"
APPLIANCE_CONFIG_FILE_NAME = "config_appliance"
APPLIANCE_CERT_FILE_NAME = "appliance_cert_file.pem"
APPLIANCE_ENDPOINT_KEY = "appliance_endpoint"
APPLIANCE_SERIAL_ID_KEY = "appliance_serial_id"
KEY_FILE_KEY = "key_file"

APPLIANCE_STATE_NOT_LOCKED = "NOT_LOCKED"
APPLIANCE_STATE_LOCKED = "LOCKED"
APPLIANCE_STATUS_NA = "NA"

NFS_DATASET_STATE_ACTIVE = "ACTIVE"

CONFIG_DIR = os.path.expanduser('~') + '/.oci'
APPLIANCE_CONFIGS_BASE_DIR = CONFIG_DIR + '/appliance_configs'
APPLIANCE_KEYSTORE_PATH = APPLIANCE_CONFIGS_BASE_DIR + '/appliance_keystore'
APPLIANCE_UPLOAD_USER_CONFIG_PATH = CONFIG_DIR + '/config_upload_user'

DEFAULT_PROFILE = 'DEFAULT'

ENDPOINT = 'endpoint'
APPLIANCE_PROFILE = 'appliance_profile'

TEST_OBJECT = "BulkDataTransferTestObject"

XA_AUTH = "xa-auth"
XA_SERIAL_ID = "xa-serial-id"
