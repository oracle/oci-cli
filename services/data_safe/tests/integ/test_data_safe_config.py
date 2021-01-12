# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import pytest
import data_safe_util

from tests import util
from tests import test_config_container


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=data_safe_util.CASSETTE_LIBRARY_DIR).use_cassette('configuration_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.mark.skip("DEXREQ-1731")
def test_get(runner, config_file, config_profile):
    params = [
        'data-safe', 'configuration', 'get',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    expected_data = {
        "lifecycle-state": "ACTIVE",
        "is-enabled": True
    }
    data_safe_util.run_test(runner, config_file, config_profile, params, expected_data=expected_data)


@pytest.mark.skip(reason="Data Safe is Enabled by Default in Test Environment")
def test_enable(runner, config_file, config_profile):
    params = [
        'data-safe', 'service', 'enable',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    expected_data = {
    }
    data_safe_util.run_test(runner, config_file, config_profile, params, expected_data=expected_data)
