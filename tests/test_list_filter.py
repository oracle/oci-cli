# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from . import test_config_container

import json
import pytest


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_images_by_state_no_results():
    retrieve_list_by_field_and_check(['compute', 'image', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'DISABLED'], 'lifecycle-state', 'DISABLED', 0)


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_images_by_state_with_results():
    retrieve_list_by_field_and_check(['compute', 'image', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'AVAILABLE'], 'lifecycle-state', 'AVAILABLE', match_at_least_one=True)


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_images_by_display_name_without_results():
    display_name = 'this-is-a-fake-name-{}'.format(util.random_number_string())
    retrieve_list_by_field_and_check(['compute', 'image', 'list', '-c', util.COMPARTMENT_ID, '--display-name', display_name], 'display-name', display_name, 0)


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_images_by_display_name_with_results():
    result = invoke(['compute', 'image', 'list', '-c', util.COMPARTMENT_ID, '--all'])
    images = json.loads(result.output)

    windows_image_display_name = next(image['display-name'] for image in images['data'] if 'Windows' in image['display-name'])
    print(str(windows_image_display_name))

    retrieve_list_by_field_and_check(
        ['compute', 'image', 'list', '-c', util.COMPARTMENT_ID, '--display-name', windows_image_display_name],
        'display-name',
        windows_image_display_name,
        1
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_by_state():
    retrieve_list_by_field_and_check(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'TERMINATED', '--all'], 'lifecycle-state', 'TERMINATED')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_by_display_name_without_results():
    # Yes, this test will break if someone calls their instance "purple monkey dishwasher"
    retrieve_list_by_field_and_check(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--display-name', 'purple monkey dishwasher', '--all'], 'display-name', 'purple monkey dishwasher')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_by_display_name_with_results():
    all_instances = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--all'])
    util.validate_response(all_instances)

    if all_instances.output != '':
        parsed_all_instances = json.loads(all_instances.output)
        display_name = parsed_all_instances['data'][0]['display-name']
        retrieve_list_by_field_and_check(
            ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--display-name', display_name, '--all'], 'display-name', display_name, match_at_least_one=True)
    else:
        pytest.skip('Skipped test as there are no instances in any state')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_with_ad_sorted_by_display_name():
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
        'display-name',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
        'display-name',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_all_by_display_name_is_sorted():
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc', '--all'],
        'display-name',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc', '--all'],
        'display-name',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_all_by_time_created_is_sorted():
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_instances_with_ad_sorted_by_time_created():
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'asc'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'desc'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_console_histories_by_state():
    # The enums are case insensitive so "requested" == "REQUESTED"
    retrieve_list_by_field_and_check(['compute', 'console-history', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'requested'], 'lifecycle-state', 'REQUESTED')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_console_histories_with_ad_sorted_by_time_created():
    retrieve_list_and_ensure_sorted(
        ['compute', 'console-history', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'asc'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['compute', 'console-history', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'desc'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_volumes_by_state_no_results():
    # Hopefully there are never any faulty volumes
    retrieve_list_by_field_and_check(['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'FAULTY'], 'lifecycle-state', 'FAULTY', 0)


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_volumes_by_state():
    retrieve_list_by_field_and_check(['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'TERMINATED'], 'lifecycle-state', 'TERMINATED')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_volumes_sorted_by_display_name():
    retrieve_list_and_ensure_sorted(
        ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
        'display-name',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
        'display-name',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_volumes_sorted_by_time_created():
    retrieve_list_and_ensure_sorted(
        ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['bv', 'volume', 'list', '-c', util.COMPARTMENT_ID, '--availability-domain', util.availability_domain(), '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_volume_backups_by_state_no_results():
    # Hopefully there are never any faulty backups
    retrieve_list_by_field_and_check(['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'FAULTY'], 'lifecycle-state', 'FAULTY', 0)


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_list_volume_backups_by_state():
    retrieve_list_by_field_and_check(['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'TERMINATED'], 'lifecycle-state', 'TERMINATED')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_volume_backups_sorted_by_display_name():
    retrieve_list_and_ensure_sorted(
        ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
        'display-name',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
        'display-name',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_volume_backups_sorted_by_time_created():
    retrieve_list_and_ensure_sorted(
        ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['bv', 'backup', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_vcns_by_state():
    retrieve_list_by_field_and_check(['network', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--lifecycle-state', 'AVAILABLE', '--all'], 'lifecycle-state', 'AVAILABLE')


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_vcns_sorted_by_display_name():
    retrieve_list_and_ensure_sorted(
        ['network', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc'],
        'display-name',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['network', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc'],
        'display-name',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_vcns_sorted_by_time_created():
    retrieve_list_and_ensure_sorted(
        ['network', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
        'time-created',
        'asc'
    )
    retrieve_list_and_ensure_sorted(
        ['network', 'vcn', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
        'time-created',
        'desc'
    )


@test_config_container.RecordReplayWithNoClickContext('list_filter')
def test_must_provide_ad_when_sorting():
    result = invoke(['compute', 'instance', 'list', '-c', util.COMPARTMENT_ID, '--sort-by', 'DISPLAYNAME'])
    assert 'You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter' in result.output


def retrieve_list_by_field_and_check(commands, check_field, check_value, expected_count=None, match_at_least_one=False):
    result = invoke(commands)
    util.validate_response(result)

    if expected_count == 0:
        assert result.output == ''
        return

    if match_at_least_one or (expected_count is not None and expected_count != 0):
        parsed_result = json.loads(result.output)
        if expected_count:
            assert len(parsed_result['data']) == expected_count

        if 'data' in parsed_result:
            for d in parsed_result['data']:
                assert d[check_field] == check_value


def retrieve_list_and_ensure_sorted(commands, sort_field, sort_direction):
    result = invoke(commands)
    util.validate_response(result)

    if result.output == '':  # There are no results, so technically it's sorted
        return

    parsed_result = json.loads(result.output)
    if sort_direction == 'asc':
        sorted_list = sorted(parsed_result['data'], key=lambda d: d[sort_field])
    else:
        sorted_list = sorted(parsed_result['data'], key=lambda d: d[sort_field], reverse=True)

    assert sorted_list == parsed_result['data']


def invoke(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, ** args)
