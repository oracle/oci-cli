# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import pytest
from oci_cli.cli_root import cli
from . import utils
from prompt_toolkit.document import Document
from interactive.oci_resources_completions import get_oci_resources
from tests import test_config_container

# COMMAND_LIST_TO_TEST takes {command:(parameter_to_test, regular_expression_to_test).
# We want to test if resource completion returns an OCID which has "compartment" word when we run --compartment-id.
# In case of --availability-domain, we test if completion returns a text which has "Iocq" in name


COMMAND_LIST_TO_TEST = {'oci iam compartment get': ('--compartment-id', 'compartment'),
                        'oci compute instance get': ('--instance-id', 'instance'),
                        'oci network vcn get': ('--vcn-id', 'vcn'),
                        'oci network subnet get': ('--subnet-id', 'subnet'),
                        'oci os object get': ('-bn', 'cli_temp'),
                        'oci compute instance launch': ('--availability-domain', 'Iocq'),
                        }


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir='tests/interactive/cassettes').use_cassette(
            'interactive_cli_{name}.yml'.format(name=request.function.__name__)):
        yield


def test_resource_completion(vcr_fixture):
    ctx = utils.set_up_context(cli)
    _test_resource_completion(ctx)


def _test_resource_completion(ctx):
    for cmd, param in COMMAND_LIST_TO_TEST.items():
        document = Document(cmd + ' ', len(cmd) + 1)
        parameter = param[0]
        expected_key_word = param[1]
        completions = get_oci_resources(
            ctx,
            parameter,
            word_before_cursor="",
            bottom_toolbar="",
            sub_string="",
        )

        resource_list = [completion.text for completion in completions]
        found = False
        for resource in resource_list:
            if expected_key_word in resource:
                found = True
        assert found is True
