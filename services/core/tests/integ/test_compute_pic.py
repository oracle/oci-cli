# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest
import unittest
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('compute_pic.yml'):
        yield


class TestComputePic(unittest.TestCase):

    def test_010_compute_pic_listing_list(self):
        # A policy is required so we don't have to run as ADMIN:
        # Allow group PythonCLITestGroup to manage app-catalog-listing in tenancy
        result = self.invoke(['compute', 'pic', 'listing', 'list'])
        util.validate_response(result)
        json_result = json.loads(result.output)
        TestComputePic.listing_id = json_result['data'][0]['listing-id']

    def test_020_compute_pic_listing_get(self):
        result = self.invoke(
            ['compute', 'pic', 'listing', 'get'])
        self.assertTrue("Error: Missing option" in result.output)

        # TODO: Check for correct return status.
        # As of 9/21/18, this returns 500 instead of 40x.
        # result = self.invoke(
        #    ['compute', 'pic', 'listing', 'get',
        #        '--listing-id', "bogus_listing_id",
        #        '--profile', 'ADMIN'])

        result = self.invoke(
            ['compute', 'pic', 'listing', 'get',
                '--listing-id', TestComputePic.listing_id])
        util.validate_response(result)

    def test_030_compute_pic_version_list(self):
        result = self.invoke(
            ['compute', 'pic', 'version', 'list'])
        self.assertTrue("Error: Missing option" in result.output)

        result = self.invoke(
            ['compute', 'pic', 'version', 'list',
                '--listing-id', TestComputePic.listing_id])
        util.validate_response(result)
        json_result = json.loads(result.output)
        TestComputePic.version = json_result['data'][0]['listing-resource-version']

    def test_040_compute_pic_version_get(self):
        result = self.invoke(
            ['compute', 'pic', 'version', 'get'])
        self.assertTrue("Error: Missing option" in result.output)
        self.assertTrue("listing-id" in result.output)
        self.assertTrue("resource-version" in result.output)

        result = self.invoke(
            ['compute', 'pic', 'version', 'get',
                '--listing-id', TestComputePic.listing_id,
                '--resource-version', TestComputePic.version])
        util.validate_response(result)

    def test_050_compute_pic_agreements_get(self):
        result = self.invoke(
            ['compute', 'pic', 'agreements', 'get'])
        self.assertTrue("Error: Missing option" in result.output)
        self.assertTrue("listing-id" in result.output)
        self.assertTrue("resource-version" in result.output)

        result = self.invoke(
            ['compute', 'pic', 'agreements', 'get',
                '--listing-id', TestComputePic.listing_id,
                '--resource-version', TestComputePic.version])
        util.validate_response(result)
        json_result = json.loads(result.output)
        time_retrieved = json_result['data']['time-retrieved']
        TestComputePic.time_retrieved = time_retrieved.replace("000+00:00", "Z")
        TestComputePic.signature = json_result['data']['signature']
        TestComputePic.oracle_tou_link = json_result['data']['oracle-terms-of-use-link']
        TestComputePic.eula_link = json_result['data']['eula-link']

    # This is async so it is very hard to verify.
    # May take 15 minutes or more.
    def test_060_compute_pic_subscription_create(self):
        # without eula-link
        result = self.invoke(
            ['compute', 'pic', 'subscription', 'create',
                '--compartment-id', util.COMPARTMENT_ID,
                '--listing-id', TestComputePic.listing_id,
                '--resource-version', TestComputePic.version,
                '--signature', TestComputePic.signature,
                '--oracle-tou-link', TestComputePic.oracle_tou_link,
                '--time-retrieved', TestComputePic.time_retrieved])
        util.validate_response(result)

        # with eula-link
        result = self.invoke(
            ['compute', 'pic', 'subscription', 'create',
                '--compartment-id', util.COMPARTMENT_ID,
                '--listing-id', TestComputePic.listing_id,
                '--resource-version', TestComputePic.version,
                '--signature', TestComputePic.signature,
                '--oracle-tou-link', TestComputePic.oracle_tou_link,
                '--eula-link', TestComputePic.eula_link,
                '--time-retrieved', TestComputePic.time_retrieved])
        util.validate_response(result)

    def test_070_compute_pic_subscription_list(self):
        result = self.invoke(
            ['compute', 'pic', 'subscription', 'list',
                '--profile', 'ADMIN'])
        self.assertTrue("Error: Missing option" in result.output)
        self.assertTrue("compartment-id" in result.output)

        result = self.invoke(
            ['compute', 'pic', 'subscription', 'list',
                '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)
        # Since subscription create is async, we can't count on this returning anything.
        # json_result = json.loads(result.output)

    # This is async so it is very hard to verify.
    # May take 15 minutes or more.
    def test_080_compute_pic_subscription_delete(self):
        result = self.invoke(
            ['compute', 'pic', 'subscription', 'delete',
                '--force'])
        self.assertTrue("Error: Missing option" in result.output)
        self.assertTrue("listing-id" in result.output)
        self.assertTrue("resource-version" in result.output)
        self.assertTrue("compartment-id" in result.output)

        result = self.invoke(
            ['compute', 'pic', 'subscription', 'delete',
                '--compartment-id', util.COMPARTMENT_ID,
                '--listing-id', TestComputePic.listing_id,
                '--resource-version', TestComputePic.version,
                '--force'])
        util.validate_response(result)

    def invoke(self, commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands
        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
