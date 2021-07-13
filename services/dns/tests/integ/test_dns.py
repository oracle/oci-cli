# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci
import oci_cli
import pytest
import random

from tests import util
from tests import test_config_container
CASSETTE_LIBRARY_DIR = 'services/dns/tests/cassettes'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    my_vcr = test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)
    # This will help us match the random zone name from the cassette.
    # For test_update_zone, we are only expecting POST for the fixture and PUT.
    print(request.function.__name__)
    if request.function.__name__ == "test_update_zone":
        my_vcr.match_on = ['method']
    with my_vcr.use_cassette('dns_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def zone(dns_client, runner, config_file, config_profile):
    # Since zone names are global, if the name is used in another tenancy or even another instance
    # of this test, it would make this test fail.  So by varying the zone name, we have less
    # chances of name collision.
    zone_name = 'clitest-dnszone-' + str(random.randint(0, 1000000)) + '.test'
    params = [
        'zone', 'create',
        '--name', zone_name,
        '--compartment-id', util.COMPARTMENT_ID,
        '--zone-type', 'PRIMARY'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    oci.wait_until(dns_client, dns_client.get_zone(zone_name), evaluate_response=lambda r: r.data.lifecycle_state == 'ACTIVE', max_wait_seconds=360)
    # The zone name from a cassette response will not match the zone name randomly generated.
    zone_name = json.loads(result.output)['data']['name']
    zone_id = dns_client.get_zone(zone_name).data.id

    print("created zone_id=" + str(zone_id) + ", zone_name=" + str(zone_name))
    yield zone_id, zone_name

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('dns_test_cleanup.yml'):
        params = [
            'zone', 'delete',
            '--zone-name-or-id', zone_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        print("deleted zone_id=" + str(zone_id) + ", zone_name=" + str(zone_name))


@pytest.mark.skip('DEXREQ-2415')
def test_update_zone(zone, runner, config_file, config_profile):
    zone_name = zone[1]
    params = [
        'zone', 'update',
        '--zone-name-or-id', zone_name,
        '--external-masters', '[]',
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@pytest.mark.skip('DEXREQ-2415')
def test_get_dns_zone(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    zone_name = zone[1]
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@pytest.mark.skip('DEXREQ-2415')
def test_list_dns_zones(runner, config_file, config_profile):
    params = [
        'zone', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@pytest.mark.skip('DEXREQ-2415')
def test_get_zone_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    zone_name = zone[1]
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_name,
        '--all'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) > 0
    assert int(parsed_result['opc-total-items']) == len(parsed_result['data']['items'])
    assert_all_records_in_list_have_not_none_fields(parsed_result['data']['items'])

    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_name,
        '--limit', '2',
        '--page-size', '1'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) == 2
    assert_all_records_in_list_have_not_none_fields(parsed_result['data']['items'])


@pytest.mark.skip('DEXREQ-2415')
def test_patch_zone_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]

    failing_record_operations = [
        {
            "operation": "REQUIRE",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "some fake data",
            "recordHash": "abc123",
            "rrsetVersion": "1",
            "rtype": "TXT",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'zone', 'patch',
        '--zone-name-or-id', zone_name,
        '--items', json.dumps(failing_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_service_error(result)

    successful_record_operations = [
        {
            "operation": "ADD",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "some fake data",
            "recordHash": "abc123",
            "rrsetVersion": "1",
            "rtype": "TXT",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'zone', 'patch',
        '--zone-name-or-id', zone_id,
        '--items', json.dumps(successful_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    records = json.loads(result.output)['data']['items']
    txt_record = [record for record in records if record['rtype'] == 'TXT'][0]

    # remove added TXT record
    remove_record_operation = [
        {
            "operation": "REMOVE",
            "domain": zone_name,
            "rdata": txt_record['rdata'],
            "recordHash": txt_record['record-hash'],
            "rtype": txt_record['rtype']
        }
    ]

    params = [
        'record', 'zone', 'patch',
        '--zone-name-or-id', zone_id,
        '--items', json.dumps(remove_record_operation)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch zone records list for current version
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id,
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert that TXT record was removed
    remaining_txt_records = [record for record in json.loads(result.output)['data']['items'] if record['rtype'] == 'TXT']
    assert len(remaining_txt_records) == 0


@pytest.mark.skip('DEXREQ-2415')
def test_update_zone_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    original_records = json.loads(result.output)['data']['items']

    remaining_txt_records = [record for record in original_records if record['rtype'] == 'TXT']
    assert len(remaining_txt_records) == 0

    new_record = {
        "domain": zone_name,
        "isProtected": True,
        "rdata": "some fake data",
        "recordHash": "abc123",
        "rrsetVersion": "1",
        "rtype": "TXT",
        "ttl": 86400
    }

    new_records = original_records[:]
    new_records.append(new_record)

    params = [
        'record', 'zone', 'update',
        '--zone-name-or-id', zone_name,
        '--items', json.dumps(new_records),
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch zone records list for current version
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id,
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    updated_records = json.loads(result.output)['data']['items']

    # assert that TXT record is now in the list
    remaining_txt_records = [record for record in updated_records if record['rtype'] == 'TXT']
    assert len(remaining_txt_records) == 1

    updated_records = [record for record in updated_records if 'some' not in record['rdata']]

    params = [
        'record', 'zone', 'update',
        '--zone-name-or-id', zone_name,
        '--items', json.dumps(updated_records),
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@pytest.mark.skip('DEXREQ-2415')
def test_get_domain_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]
    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--all'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) > 0
    assert int(parsed_result['opc-total-items']) == len(parsed_result['data']['items'])
    assert_all_records_in_list_have_not_none_fields(parsed_result['data']['items'])

    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--limit', '2',
        '--page-size', '1'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) == 2
    assert_all_records_in_list_have_not_none_fields(parsed_result['data']['items'])


@pytest.mark.skip('DEXREQ-2415')
def test_patch_domain_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]

    failing_record_operations = [
        {
            "operation": "REQUIRE",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "some fake data",
            "recordHash": "abc123",
            "rrsetVersion": "1",
            "rtype": "TXT",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'domain', 'patch',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--items', json.dumps(failing_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_service_error(result)

    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    successful_record_operations = [
        {
            "operation": "ADD",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "test data",
            "recordHash": "abc123",
            "rtype": "TXT",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'domain', 'patch',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--items', json.dumps(successful_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    records = json.loads(result.output)['data']['items']
    txt_record = [record for record in records if record['rtype'] == 'TXT'][0]

    # remove added TXT record
    remove_record_operation = [
        {
            "operation": "REMOVE",
            "domain": zone_name,
            "rdata": txt_record['rdata'],
            "recordHash": txt_record['record-hash'],
            "rtype": txt_record['rtype']
        }
    ]

    params = [
        'record', 'domain', 'patch',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--items', json.dumps(remove_record_operation)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch domain records list for current version
    params = [
        'record', 'domain', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert that TXT record was removed
    remaining_txt_records = [record for record in json.loads(result.output)['data']['items'] if record['rtype'] == 'TXT']
    assert len(remaining_txt_records) == 0


@pytest.mark.skip('DEXREQ-2415')
def test_update_domain_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]

    domain_name = 'foo.{}'.format(zone_name)

    new_records = [{
        "domain": domain_name,
        "isProtected": True,
        "rdata": "some fake data",
        "recordHash": "abc123",
        "rrsetVersion": "1",
        "rtype": "TXT",
        "ttl": 86400
    }]

    params = [
        'record', 'domain', 'update',
        '--zone-name-or-id', zone_name,
        '--domain', domain_name,
        '--items', json.dumps(new_records),
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch domain records list for current version
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', domain_name,
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert that TXT record is now in the list
    remaining_txt_records = [record for record in json.loads(result.output)['data']['items'] if record['rtype'] == 'TXT']
    assert len(remaining_txt_records) == 1

    # delete domain records
    params = [
        'record', 'domain', 'delete',
        '--zone-name-or-id', zone_id,
        '--domain', domain_name,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


@pytest.mark.skip('DEXREQ-2415')
def test_get_rrset_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]
    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--rtype', 'NS'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--rtype', 'NS'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--rtype', 'NS',
        '--all'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) > 0
    assert int(parsed_result['opc-total-items']) == len(parsed_result['data']['items'])
    for item in parsed_result['data']['items']:
        assert_record_fields_not_none(item)
        assert item['rtype'] == 'NS'

    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--rtype', 'NS',
        '--limit', '2',
        '--page-size', '1'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    assert len(parsed_result['data']['items']) == 2
    for item in parsed_result['data']['items']:
        assert_record_fields_not_none(item)
        assert item['rtype'] == 'NS'


@pytest.mark.skip('DEXREQ-2415')
def test_patch_rrset_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]

    failing_record_operations = [
        {
            "operation": "REQUIRE",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "127.0.0.1",
            "recordHash": "abc123",
            "rrsetVersion": "1",
            "rtype": "A",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'rrset', 'patch',
        '--zone-name-or-id', zone_name,
        '--domain', zone_name,
        '--rtype', 'A',
        '--items', json.dumps(failing_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_service_error(result)

    successful_record_operations = [
        {
            "operation": "ADD",
            "domain": zone_name,
            "isProtected": True,
            "rdata": "127.0.0.1",
            "recordHash": "abc123",
            "rrsetVersion": "1",
            "rtype": "A",
            "ttl": 86400
        }
    ]

    params = [
        'record', 'rrset', 'patch',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--rtype', 'A',
        '--items', json.dumps(successful_record_operations)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--rtype', 'A'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    records = json.loads(result.output)['data']['items']
    a_record = [record for record in records if record['rtype'] == 'A'][0]

    # remove added TXT record
    remove_record_operation = [
        {
            "operation": "REMOVE",
            "domain": zone_name,
            "rdata": a_record['rdata'],
            "recordHash": a_record['record-hash'],
            "rtype": a_record['rtype']
        }
    ]

    params = [
        'record', 'rrset', 'patch',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--rtype', 'A',
        '--items', json.dumps(remove_record_operation)
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch zone records list for current version
    params = [
        'record', 'rrset', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', zone_name,
        '--rtype', 'A',
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert that TXT record was removed
    remaining_a_records = [record for record in json.loads(result.output)['data']['items'] if record['rtype'] == 'A']
    assert len(remaining_a_records) == 0


@pytest.mark.skip('DEXREQ-2415')
def test_update_rrset_records(zone, runner, config_file, config_profile):
    zone_id = zone[0]
    zone_name = zone[1]

    domain_name = 'test-rrset.{}'.format(zone_name)

    new_records = [{
        "domain": domain_name,
        "isProtected": True,
        "rdata": "127.0.0.2",
        "recordHash": "abc123",
        "rrsetVersion": "1",
        "rtype": "A",
        "ttl": 86400
    }]

    params = [
        'record', 'rrset', 'update',
        '--zone-name-or-id', zone_name,
        '--domain', domain_name,
        '--rtype', 'A',
        '--items', json.dumps(new_records),
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # retrieve zone to determine current version
    params = [
        'zone', 'get',
        '--zone-name-or-id', zone_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    current_zone_version = json.loads(result.output)['data']['version']

    # fetch rrset records list for current version
    params = [
        'record', 'zone', 'get',
        '--zone-name-or-id', zone_id,
        '--domain', domain_name,
        '--rtype', 'A',
        '--zone-version', current_zone_version
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # assert that A record is now in the list
    remaining_a_records = [record for record in json.loads(result.output)['data']['items'] if record['rtype'] == 'A']
    assert len(remaining_a_records) == 1

    # delete rrset
    params = [
        'record', 'rrset', 'delete',
        '--zone-name-or-id', zone_id,
        '--domain', domain_name,
        '--rtype', 'A',
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'dns'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'dns'] + params, ** args)

    return result


def assert_all_records_in_list_have_not_none_fields(record_list):
    for record in record_list:
        assert_record_fields_not_none(record)


def assert_record_fields_not_none(record):
    assert record['domain'] is not None
    assert record['record-hash'] is not None
    assert record['is-protected'] is not None
    assert record['rdata'] is not None
    assert record['rrset-version'] is not None
    assert record['rtype'] is not None
    assert record['ttl'] is not None
