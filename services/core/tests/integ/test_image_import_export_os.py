# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import unittest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


class TestImageImportExportOs(unittest.TestCase):

    # To re-record this test, you must first create a bucket and then export a image
    # into that bucket before running this test.
    # The variables must also be updated to the image you are recording for.
    @util.slow
    def test_import_from_object(self):
        with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_image_import_export_os.yml'):
            bucket_name = 'CliImageImportExport_vcr'
            image_name = 'exported-image-20200715-1133'
            operating_system = 'Windows'
            operating_system_version = 'Server 2019 Standard'
            result = util.invoke_command(['compute', 'image', 'import', 'from-object',
                                          '-c', util.COMPARTMENT_ID,
                                          '-bn', bucket_name,
                                          '--name', image_name,
                                          '-ns', util.NAMESPACE,
                                          '--operating-system', operating_system,
                                          '--operating-system-version', operating_system_version])
            image_from_object = json.loads(result.output)
            assert operating_system in image_from_object['data']['operating-system']
            assert operating_system_version in image_from_object['data']['operating-system-version']

            result = util.invoke_command(['compute', 'image', 'import', 'from-object-uri',
                                          '-c', util.COMPARTMENT_ID,
                                          '--uri',
                                          'https://objectstorage.us-phoenix-1.oraclecloud.com/n/dex-us-phx-cli-1/b/CliImageImportExport_vcr/o/exported-image-20200715-1133',
                                          '--operating-system', operating_system,
                                          '--operating-system-version', operating_system_version])
            image_from_object_uri = json.loads(result.output)
            assert operating_system in image_from_object_uri['data']['operating-system']
            assert operating_system_version in image_from_object_uri['data']['operating-system-version']
