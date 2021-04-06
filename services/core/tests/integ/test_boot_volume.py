# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from tests import util
from tests import test_config_container
import json
import pytest

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


@pytest.fixture(scope='module')
def network_resources():
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('boot_volume_network_resources_fixture.yml'):
        vcn_name = util.random_name('cli_test_boot_vol')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = invoke([
            'network', 'vcn', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', vcn_name,
            '--cidr-block', cidr_block,
            '--dns-label', vcn_dns_label,
            '--wait-for-state', 'AVAILABLE',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        util.validate_response(result, json_response_expected=False)
        vcn_ocid = util.get_json_from_mixed_string(result.output)['data']['id']

        subnet_name = util.random_name('cli_test_boot_vol')
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        result = invoke([
            'network', 'subnet', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--availability-domain', util.availability_domain(),
            '--display-name', subnet_name,
            '--vcn-id', vcn_ocid,
            '--cidr-block', cidr_block,
            '--dns-label', subnet_dns_label,
            '--wait-for-state', 'AVAILABLE',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        util.validate_response(result, expect_etag=True, json_response_expected=False)
        subnet_ocid = util.get_json_from_mixed_string(result.output)['data']['id']

        yield (vcn_ocid, subnet_ocid)

        result = invoke(
            ['network', 'subnet', 'delete', '--subnet-id', subnet_ocid, '--force', '--wait-for-state', 'TERMINATED',
             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        util.validate_response(result, json_response_expected=False)

        result = util.invoke_command(
            ['network', 'vcn', 'delete', '--vcn-id', vcn_ocid, '--force', '--wait-for-state', 'TERMINATED',
             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
        util.validate_response(result, json_response_expected=False)


@util.slow
def test_boot_volume_clone_backup(network_resources):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('boot_volume_test_boot_volume_clone_backup.yml'):
        boot_volume_id = None
        instance_ocid = None
        backup_boot_volume_id = None
        cloned_boot_volume_id = None
        backup_id = None
        try:
            instance_name = util.random_name('boot_vol_instance')
            image_id = util.oracle_linux_image()
            shape = 'VM.Standard1.1'
            hostname_label = util.random_name('bootvolinst', insert_underscore=False)
            boot_volume_size_in_gbs = '51'

            result = invoke([
                'compute', 'instance', 'launch',
                '--compartment-id', util.COMPARTMENT_ID,
                '--availability-domain', util.availability_domain(),
                '--display-name', instance_name,
                '--subnet-id', network_resources[1],
                '--image-id', image_id,
                '--shape', shape,
                '--hostname-label', hostname_label,
                '--boot-volume-size-in-gbs', boot_volume_size_in_gbs,
                '--wait-for-state', 'RUNNING',
                '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
            ])
            util.validate_response(result, json_response_expected=False)
            instance_data = util.get_json_from_mixed_string(result.output)['data']
            instance_ocid = instance_data['id']
            assert 'image' == instance_data['source-details']['source-type']
            assert image_id == instance_data['source-details']['image-id']

            result = invoke([
                'compute', 'boot-volume-attachment', 'list',
                '-c', util.COMPARTMENT_ID,
                '--availability-domain', util.availability_domain(),
                '--instance-id', instance_data['id']
            ])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert len(parsed_result['data']) == 1
            boot_volume_id = parsed_result['data'][0]['boot-volume-id']

            result = invoke([
                'bv', 'boot-volume', 'get',
                '--boot-volume-id', boot_volume_id
            ])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            boot_volume_size_in_gbs = parsed_result['data']['size-in-gbs']
            assert boot_volume_size_in_gbs == int(boot_volume_size_in_gbs)

            result = invoke([
                'compute', 'instance', 'terminate',
                '--instance-id', instance_ocid,
                '--wait-for-state', 'TERMINATED',
                '--preserve-boot-volume', 'true',
                '--force'
            ])
            util.validate_response(result, json_response_expected=False)
            instance_ocid = None

            # Since we preserved the volume it should still be available
            result = invoke(['bv', 'boot-volume', 'get', '--boot-volume-id', boot_volume_id])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert util.availability_domain() == parsed_result['data']['availability-domain']
            assert 'AVAILABLE' == parsed_result['data']['lifecycle-state']
            assert image_id == parsed_result['data']['image-id']
            size_in_gbs = int(parsed_result['data']['size-in-gbs'])

            new_size_in_gbs = size_in_gbs + 10

            # Resize boot volume to new_size_in_gbs
            result = invoke(['bv', 'boot-volume', 'update', '--boot-volume-id', boot_volume_id,
                             '--size-in-gbs', str(new_size_in_gbs),
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_response(result, json_response_expected=False)

            # Since we preserved the volume it should still be available
            result = invoke(['bv', 'boot-volume', 'get', '--boot-volume-id', boot_volume_id])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            assert 'AVAILABLE' == parsed_result['data']['lifecycle-state']
            assert new_size_in_gbs == int(parsed_result['data']['size-in-gbs'])

            # Take a backup
            result = invoke(['bv', 'boot-volume-backup', 'create', '--boot-volume-id', boot_volume_id,
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_response(result, json_response_expected=False)
            parsed_result = util.get_json_from_mixed_string(result.output)
            assert boot_volume_id == parsed_result['data']['boot-volume-id']
            assert image_id == parsed_result['data']['image-id']
            assert 'AVAILABLE' == parsed_result['data']['lifecycle-state']
            backup_id = parsed_result['data']['id']

            # Boot Volume Create Error cases

            # Error 1: No option specified
            result = invoke(['bv', 'boot-volume', 'create',
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            assert "An empty boot volume cannot be created. Please specify either --boot-volume-backup-id, --source-boot-volume-id or --source-volume-replica-id" in result.output

            # Error 2: Both options specified
            result = invoke(['bv', 'boot-volume', 'create',
                             '--source-boot-volume-id', boot_volume_id[0],
                             '--boot-volume-backup-id', boot_volume_id[0],
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            assert "You can only specify one of either --source-boot-volume-id, --boot-volume-backup-id or --source-volume-replica-id option" in result.output

            # Clone the boot volume (Error 1: Invalid Boot Volume ID)
            result = invoke(['bv', 'boot-volume', 'create',
                             '--source-boot-volume-id', boot_volume_id[0],
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_service_error(result, error_message="InvalidParameter")

            backup_policy_ids = get_backup_policy_ids()
            create_new_size_in_gbs = new_size_in_gbs + 10

            # Clone the boot volume with bronze backup policy and larger size
            result = invoke(['bv', 'boot-volume', 'create',
                             '--source-boot-volume-id', boot_volume_id,
                             '--backup-policy-id', backup_policy_ids["bronze"],
                             '--wait-for-state', 'AVAILABLE',
                             '--size-in-gbs', str(create_new_size_in_gbs),
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_response(result, json_response_expected=False)
            parsed_result = util.get_json_from_mixed_string(result.output)
            assert util.availability_domain() == parsed_result['data']['availability-domain']
            assert 'AVAILABLE' == parsed_result['data']['lifecycle-state']
            assert image_id == parsed_result['data']['image-id']
            assert create_new_size_in_gbs == int(parsed_result['data']['size-in-gbs'])
            cloned_boot_volume_id = parsed_result['data']['id']

            # Verify the backup policy
            result = invoke(['bv', 'volume-backup-policy-assignment',
                             'get-volume-backup-policy-asset-assignment',
                             '--asset-id', cloned_boot_volume_id])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            backup_policy_assignment_id = parsed_result["data"][0]["id"]
            assert parsed_result["data"][0]["policy-id"] == backup_policy_ids["bronze"]

            # Remove backup policy
            result = invoke(['bv', 'volume-backup-policy-assignment',
                             'delete', '--policy-assignment-id', backup_policy_assignment_id, '--force'])
            util.validate_response(result)

            # Change backup policy to silver
            result = invoke(['bv', 'volume-backup-policy-assignment', 'create',
                             '--asset-id', cloned_boot_volume_id,
                             '--policy-id', backup_policy_ids['silver']])
            util.validate_response(result)
            parsed_result = json.loads(result.output)
            backup_policy_assignment_id = parsed_result["data"]["id"]
            assert parsed_result["data"]["policy-id"] == backup_policy_ids["silver"]

            # Remove the backup policy
            result = invoke(['bv', 'volume-backup-policy-assignment',
                             'delete', '--policy-assignment-id', backup_policy_assignment_id, '--force'])
            util.validate_response(result)

            # We can now launch an instance using that boot volume
            result = invoke([
                'compute', 'instance', 'launch',
                '--compartment-id', util.COMPARTMENT_ID,
                '--availability-domain', util.availability_domain(),
                '--display-name', instance_name,
                '--subnet-id', network_resources[1],
                '--shape', shape,
                '--hostname-label', hostname_label,
                '--source-boot-volume-id', cloned_boot_volume_id,
                '--wait-for-state', 'RUNNING',
                '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
            ])
            util.validate_response(result, json_response_expected=False)
            instance_data = util.get_json_from_mixed_string(result.output)['data']
            instance_ocid = instance_data['id']
            assert 'bootVolume' == instance_data['source-details']['source-type']
            assert cloned_boot_volume_id == instance_data['source-details']['boot-volume-id']

            clean_up_instances(instance_ocid)
            cloned_boot_volume_id = None
            instance_ocid = None

            # Delete existing boot volume
            clean_up_boot_volume(boot_volume_id)
            boot_volume_id = None

            # Create boot volume from backup (Error 1: Invalid Backup Volume ID)
            result = invoke(['bv', 'boot-volume', 'create',
                             '--boot-volume-backup-id', backup_id[0],
                             '--availability-domain', util.availability_domain(),
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_service_error(result, error_message="InvalidParameter")

            # Create boot volume from backup (Error 2: Availability domain not specified)
            result = invoke(['bv', 'boot-volume', 'create',
                             '--boot-volume-backup-id', backup_id,
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            assert "An availability domain must be specified when restoring a boot volume from backup" in result.output

            # Create boot volume from backup
            result = invoke(['bv', 'boot-volume', 'create',
                             '--boot-volume-backup-id', backup_id,
                             '--availability-domain', util.availability_domain(),
                             '--wait-for-state', 'AVAILABLE',
                             '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS])
            util.validate_response(result, json_response_expected=False)
            parsed_result = util.get_json_from_mixed_string(result.output)
            assert util.availability_domain() == parsed_result['data']['availability-domain']
            assert 'AVAILABLE' == parsed_result['data']['lifecycle-state']
            assert image_id == parsed_result['data']['image-id']
            backup_boot_volume_id = parsed_result['data']['id']

            # We can now launch an instance using that boot volume
            result = invoke([
                'compute', 'instance', 'launch',
                '--compartment-id', util.COMPARTMENT_ID,
                '--availability-domain', util.availability_domain(),
                '--display-name', instance_name,
                '--subnet-id', network_resources[1],
                '--shape', shape,
                '--hostname-label', hostname_label,
                '--source-boot-volume-id', backup_boot_volume_id,
                '--wait-for-state', 'RUNNING',
                '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
            ])
            util.validate_response(result, json_response_expected=False)
            instance_data = util.get_json_from_mixed_string(result.output)['data']
            instance_ocid = instance_data['id']
            assert 'bootVolume' == instance_data['source-details']['source-type']
            assert backup_boot_volume_id == instance_data['source-details']['boot-volume-id']

            clean_up_instances(instance_ocid)
            backup_boot_volume_id = None
            instance_ocid = None

        finally:
            clean_up_instances(instance_ocid)
            clean_up_boot_volume(boot_volume_id)
            clean_up_boot_volume(cloned_boot_volume_id)
            clean_up_boot_volume(backup_boot_volume_id)
            clean_up_boot_volume_backup(backup_id)


def get_backup_policy_ids():
    result = invoke('bv volume-backup-policy list --profile ADMIN'.split())
    util.validate_response(result)
    parsed_result = json.loads(result.output)
    backup_policy_ids = {}
    for policy in parsed_result["data"]:
        backup_policy_ids[policy["display-name"]] = policy["id"]
    return backup_policy_ids


def clean_up_instances(instance_ocid):
    if instance_ocid:
        result = invoke(['compute', 'instance', 'terminate', '--instance-id', instance_ocid, '--wait-for-state',
                        'TERMINATED', '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS, '--force'])
        util.validate_response(result, json_response_expected=False)


def clean_up_boot_volume(boot_volume_id):
    if boot_volume_id:
        result = invoke([
            'bv', 'boot-volume', 'delete',
            '--boot-volume-id', boot_volume_id,
            '--force',
            '--wait-for-state', 'TERMINATED',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        util.validate_response(result, json_response_expected=False)


def clean_up_boot_volume_backup(backup_boot_volume_id):
    if backup_boot_volume_id:
        result = invoke([
            'bv', 'boot-volume-backup', 'delete',
            '--boot-volume-backup-id', backup_boot_volume_id,
            '--force',
            '--wait-for-state', 'TERMINATED',
            '--wait-interval-seconds', util.WAIT_INTERVAL_SECONDS
        ])
        util.validate_response(result, json_response_expected=False)


def invoke(commands, debug=False, **args):
    if debug is True:
        commands = ['--debug'] + commands

    return util.invoke_command(commands, **args)
