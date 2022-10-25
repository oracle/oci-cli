# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import logging
import os
import os.path
import pytest
import oci_cli
from tests import util
from tests import test_config_container
import json

CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'

created_buckets = 'created_buckets'


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'object_storage_retention_rule_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(params=[False])
def debug(request):
    return request.param


def setup_module():
    if os.getenv('RECORD_ONLY', '') == '1':
        return


@pytest.fixture(scope='function')
def delete_pending_buckets():
    data = {created_buckets: []}
    yield data
    logging.debug("--------Deleting Created Buckets-----------")
    for bucket_name in data[created_buckets]:
        delete_bucket(bucket_name)


def delete_bucket(bucket_name):
    invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def invoke_new(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands
    return util.invoke_command(commands, ** args)


def test_run_all_operations(vcr_fixture, runner, config_file, config_profile, debug, test_id_recorded, delete_pending_buckets):
    """Successfully calls every operation with required arguments only."""
    bucket_name = 'cli_retentionrule_temp_bucket_' + test_id_recorded + ('_debug' if debug else '_no_debug')

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)
    delete_pending_buckets[created_buckets].append(bucket_name)

    # create a retention rule with a duration of 1 day
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'create', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--time-amount', '1', '--time-unit', 'DAYS'], debug=debug)
    result_json = json.loads(result.output)
    retentionruleid_1 = result_json['data']['id']

    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'get', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_1], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # create a retention rule with an infinite duration
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'create', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name], debug=debug)
    result_json = json.loads(result.output)
    retentionruleid_2 = result_json['data']['id']

    # list the retention rules for the bucket
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'list', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name], debug=debug)
    result_json = json.loads(result.output)
    rules = result_json['data']['items']

    # verify that there are 2 retention rules at this point and the order of listing is in descending order
    assert (len(rules) == 2)
    assert (rules[0]['id'] == retentionruleid_2)
    assert (rules[1]['id'] == retentionruleid_1)

    # update retention rule of retentionruleid_1 to a duration of 2 days
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_1, '--time-amount', '2', '--time-unit', 'DAYS'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # verify the update by retrieving the retention rule of retentionruleid_1
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'get', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_1], debug=debug)
    result_json = json.loads(result.output)
    time_amount = int(result_json['data']['duration']['time-amount'])
    assert (time_amount == 2)

    # update retention rule of retentionruleid_1 and unset the duration effectively making it an infinite duration
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_1, '--time-amount', ''], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # verify the update by retrieving the retention rule of retentionruleid_1
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'get', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_1], debug=debug)
    result_json = json.loads(result.output)
    duration = result_json['data']['duration']
    assert (duration is None)

    # update retention rule of retentionruleid_2 to a time-rule-locked duration of 1234
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2, '--time-rule-locked', '1234'], debug=debug)
    # This should fail because we can't set time-rule-locked when the rule duration is infinite
    assert "InvalidRetentionRuleDetails" in result.output
    assert '"status": 400' in result.output

    # update retention rule of retentionruleid_2 to a time-rule-locked duration of 1234 and set the rule duration to 1 day
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2, '--time-rule-locked', '5882-03-11T00:30:00+00:00', '--time-amount', '2', '--time-unit', 'DAYS'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # verify the update by retrieving the retention rule of retentionruleid_2
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'get', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2], debug=debug)
    result_json = json.loads(result.output)
    time_rule_locked = result_json['data']['time-rule-locked']
    assert (time_rule_locked == '5882-03-11T00:30:00+00:00')

    # update retention rule of retentionruleid_2 to an infinite rule duration. This should not succeed.
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2, '--time-amount', ''], debug=debug)
    # This should fail because we can't set the rule duration to infinite when a time-rule-locked is  set
    assert "InvalidRetentionRuleDetails" in result.output
    assert '"status": 400' in result.output

    # update retention rule of retentionruleid_2 to unset time-rule-locked
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'update', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2, '--time-rule-locked', '', '--time-amount', '1', '--time-unit', 'DAYS'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # verify the update by retrieving the retention rule of retentionruleid_2
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'get', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2], debug=debug)
    result_json = json.loads(result.output)
    time_rule_locked = result_json['data']['time-rule-locked']
    assert (time_rule_locked is None)

    # delete retention rule with retentionruleid_2
    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'delete', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name,
                     '--retention-rule-id', retentionruleid_2, '--force'], debug=debug)
    validate_response(result, includes_debug_data=debug)

    result = invoke(runner, config_file, config_profile,
                    ['retention-rule', 'list', '--namespace-name', util.NAMESPACE, '--bucket-name', bucket_name], debug=debug)
    result_json = json.loads(result.output)
    rules = result_json['data']['items']

    assert (len(rules) == 1)
    assert (retentionruleid_1 == rules[0]['id'])

    # bucket delete
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    delete_pending_buckets[created_buckets].remove(bucket_name)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, **args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--debug', '--config-file', config_file, '--profile', config_profile,
                                              'os'] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile, 'os'] + params,
                               **args)
    return result


def extra_response_validation(result):
    assert 'opc-client-request-id' in result.output


def validate_response(result, includes_debug_data=False, json_response_expected=True):
    extra_validation = None
    if includes_debug_data:
        extra_validation = extra_response_validation
    util.validate_response(result, extra_validation=extra_validation, includes_debug_data=includes_debug_data,
                           json_response_expected=json_response_expected)


# TODO: clean up and remove all of these which are drop in replacements for unittest validations
def assertEqual(a, b):
    assert a == b


def assertEquals(a, b):
    assertEqual(a, b)


def assertListEqual(a, b):
    if len(a) != len(b):
        return False

    equal = True
    for i in range(0, len(a)):
        equal = equal and a[i] == b[i]

    return equal


def assertNotEquals(a, b):
    assert not a == b
