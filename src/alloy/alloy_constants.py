# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

DEFAULT_ALLOY_CONFIG_NAME = 'alloy-config.json'
ALLOY_CONFIG_DEFAULT_LOCATION = f'~/.oci/{DEFAULT_ALLOY_CONFIG_NAME}'

DEFAULT_SUBSCRIBED_SERVICE_MAPPING = './src/alloy/service_mapping.json'
DEFAULT_SUBSCRIBED_SERVICE_MAPPING = 'service_mapping.json'
DEFAULT_SUBSCRIBED_SERVICE_MAPPING_LOCATION = f'~/.oci/{DEFAULT_SUBSCRIBED_SERVICE_MAPPING}'


# Error Types
INVALID_INPUT = 'invalid_input'
NO_SERVICE_CONFIG = 'no_service_config'
NO_CLI_FOUND = 'no_cli_found'
ALLOY_NAME_TAKEN = 'alloy_name_taken'
PROVIDER_NAME_MISSING = 'provider_name_missing'
SUBSCRIBED_SERVICES_MISSING = 'subscribed_services_missing'
