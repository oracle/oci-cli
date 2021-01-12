# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util

# pytest -s --vcr-record-mode=none services/data_safe/tests/unit/test_datasafe_cli_extended.py


class TestDataSafeCliChanges(unittest.TestCase):
    def setUp(self):
        pass

    # Test 1 :
    # From: oci data-safe data-safe-configuration get --compartment-id | -c, -? | -h | --help
    # To: oci data-safe configuration get --compartment-id | -c, -? | -h | --help

    def test_data_safe_configuration_removed(self):
        result = util.invoke_command(['data-safe', 'data-safe-configuration'])
        assert 'Error: No such command ' in result.output

    # Test 2 :
    # From: oci data-safe data-safe-private-endpoint change-compartment --data-safe-private-endpoint-id, --compartment-id | -c, -? | -h | --help
    # To: oci data-safe private-endpoint change-compartment --private-endpoint-id, --compartment-id | -c, -? | -h | --help

    # Test 2.1:

    def test_data_safe_private_endpoint_removed(self):
        result = util.invoke_command(['data-safe', 'data-safe-private-endpoint'])
        assert 'Error: No such command ' in result.output

    # Test 2.2:

    def test_data_safe_private_endpoint_id_change_compartment_removed(self):
        result = util.invoke_command(['data-safe', 'private-endpoint', 'change-compartment'])
        assert 'Error: Missing option(s) --private-endpoint-id' in result.output

    # Test 3:
    # From: oci data-safe data-safe-private-endpoint delete --data-safe-private-endpoint-id, --force, -? | -h | --help
    # To: oci data-safe private-endpoint delete --private-endpoint-id, --force, -? | -h | --help

    def test_data_safe_private_endpoint_id_delete_removed(self):
        result = util.invoke_command(['data-safe', 'data-safe-private-endpoint'])
        assert 'Error: No such command ' in result.output
        result = util.invoke_command(['data-safe', 'private-endpoint', 'delete'])
        assert 'Error: Missing option(s) --private-endpoint-id' in result.output

    # Test 4:
    # From: oci data-safe data-safe-private-endpoint get --data-safe-private-endpoint-id, -? | -h | --help
    # To: oci data-safe private-endpoint get --private-endpoint-id, -? | -h | --help

    def test_data_safe_private_endpoint_id_get_removed(self):
        result = util.invoke_command(['data-safe', 'data-safe-private-endpoint'])
        assert 'Error: No such command ' in result.output
        result = util.invoke_command(['data-safe', 'private-endpoint', 'get'])
        assert 'Error: Missing option(s) --private-endpoint-id' in result.output

    # Test 5:
    # From: oci data-safe data-safe-private-endpoint update --data-safe-private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
    # To: oci data-safe private-endpoint update --private-endpoint-id, --display-name, --defined-tags, --description, --force, --freeform-tags, -? | -h | --help, --nsg-ids
    def test_data_safe_private_endpoint_id_update_removed(self):
        result = util.invoke_command(['data-safe', 'data-safe-private-endpoint'])
        assert 'Error: No such command ' in result.output
        result = util.invoke_command(['data-safe', 'private-endpoint', 'update'])
        assert 'Missing option(s) --display-name, --private-endpoint-id.' in result.output

    # Test 6 :
    # From: oci data-safe enable-data-safe-configuration-details enable-data-safe-configuration --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled
    # To: oci data-safe service enable --compartment-id | -c, --defined-tags, --force, --freeform-tags, -? | -h | --help, --is-enabled

    # Test 6.1:
    def test_enable_data_safe_configuration_details_removed(self):
        result = util.invoke_command(['data-safe', 'enable-data-safe-configuration-details'])
        assert 'Error: No such command ' in result.output

    # Test 7:
    # From:  oci data-safe work-request-log-entry list-work-request-logs --work-request-id, --all, -? | -h | --help
    # To: oci data-safe work-request-log-entry list --work-request-id, --all, -? | -h | --help
    def test_list_work_request_logs_removed(self):
        result = util.invoke_command(['data-safe', 'work-request-log-entry', 'list-work-request-logs'])
        assert 'list' in result.output
        assert 'Error: No such command ' in result.output
