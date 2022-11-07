# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestAnalyticsCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    def test_analytics_instance_create(self):

        inst_name = 'testinstance1'
        description = 'Test Analytics Instance 1'
        capacity_type = 'OLPU_COUNT'
        capacity_value = '1'
        compartment_id = 'ocid1.tenancy.oc1..aaaaaaaaavy5ubqrzwcupgsapwvzeri4u6pzq4fqecryumqoqvvi2i7xaj7a'
        feature_set = 'ENTERPRISE_ANALYTICS'
        license_type = 'LICENSE_INCLUDED'
        email = 'olivier.louchart-fletcher@oracle.com'
        token_file = 'services/analytics/tests/cassettes/idcs_access_token.txt'

        # Check that --capacity-value is defined and required.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-type', capacity_type,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Missing option(s) --capacity-value.' in result.output

        # Check that --capacity-type is defined and required.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Missing option(s) --capacity-type.' in result.output

        # Check that --capacity is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity', '{"capacityType": "OLPU_COUNT", "capacityValue": 1}',
            '--capacity-type', capacity_type,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Error: no such option: --capacity ' in result.output

        # Check that --idcs-access-token is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-type', capacity_type,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token', 'eyJraWQiOiJhc3dfb2'
            '--idcs-access-token-file', token_file
        ])
        assert 'Error: no such option: --idcs-access-token ' in result.output

    def test_private_endpoint_feature(self):

        # Check that command "create-analytics-instance-public-endpoint-details" was removed from the API.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create-analytics-instance-public-endpoint-details'
        ])
        assert "Error: No such command 'create-analytics-instance-public-endpoint-details'." in result.output

        # Check that command "create-analytics-instance-private-endpoint-details" was removed from the API.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create-analytics-instance-private-endpoint-details'
        ])
        assert "Error: No such command 'create-analytics-instance-private-endpoint-details'." in result.output

        # Check that command "change-analytics-instance-network-endpoint-public-endpoint-details" was removed from the API.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'change-analytics-instance-network-endpoint-public-endpoint-details'
        ])
        assert "Error: No such command 'change-analytics-instance-network-endpoint-public-endpoint-details'." in result.output

        # Check that command "change-analytics-instance-network-endpoint-private-endpoint-details" was removed from the API.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'change-analytics-instance-network-endpoint-private-endpoint-details'
        ])
        assert "Error: No such command 'change-analytics-instance-network-endpoint-private-endpoint-details'." in result.output

        # Check that command "change-analytics-instance-network-endpoint" was removed from the API.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'change-analytics-instance-network-endpoint'
        ])
        assert "Error: No such command 'change-analytics-instance-network-endpoint'." in result.output

        # Check that command "change-network-endpoint" exists.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'change-network-endpoint',
            '--network-endpoint-details', '{}'
        ])
        assert 'Error: Missing option(s) --analytics-instance-id.' in result.output

    def test_vanity_url_feature(self):

        inst_ocid = 'ocid1.analyticsinstance.oc1.us-ashburn-1.test.aaaaaaaas2la4dx7kym6sibwhqav2ikgc2q3hnqbre4jxzx6lqfa2qxdku2r'
        key_file = 'services/analytics/tests/cassettes/key.pem'
        cert_file = 'services/analytics/tests/cassettes/cert.pem'
        intermediates_file = 'services/analytics/tests/cassettes/intermediates.pem'

        # Check that create-vanity-url --private-key is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--hosts', '["1"]',
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--private-key', 'abcdefg'
        ])
        assert 'Error: no such option: --private-key ' in result.output

        # Check that create-vanity-url --public-certificate is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--hosts', '["1"]',
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--public-certificate', 'abcdefg'
        ])
        assert 'Error: no such option: --public-certificate ' in result.output

        # Check that create-vanity-url --ca-certificate is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--hosts', '["1"]',
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--ca-certificate', 'abcdefg'
        ])
        assert 'Error: no such option: --ca-certificate ' in result.output

        # Check that update-vanity-url --private-key is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'update-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--private-key', 'abcdefg'
        ])
        assert 'Error: no such option: --private-key ' in result.output

        # Check that update-vanity-url --public-certificate is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'update-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--public-certificate', 'abcdefg'
        ])
        assert 'Error: no such option: --public-certificate ' in result.output

        # Check that update-vanity-url --ca-certificate is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'update-vanity-url',
            '--analytics-instance-id', inst_ocid,
            '--private-key-file', key_file,
            '--public-certificate-file', cert_file,
            '--ca-certificate-file', intermediates_file,
            '--ca-certificate', 'abcdefg'
        ])
        assert 'Error: no such option: --ca-certificate ' in result.output
