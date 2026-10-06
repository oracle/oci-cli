# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.

import json
import os

import oci.base_client
import pytest

from tests import test_config_container
from tests import util
from tests.util import target_config  # noqa: F401


CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'
CASSETTE_FILENAME = 'compute_nvme_volume_attachment.yml'

INSTANCE_ID_ENV = 'OCI_CLI_NVME_TEST_INSTANCE_ID'
VOLUME_ID_ENV = 'OCI_CLI_NVME_TEST_VOLUME_ID'
DEVICE_ENV = 'OCI_CLI_NVME_TEST_DEVICE'

REPLAY_INSTANCE_ID = 'ocid1.instance.oc1.phx.exampleuniqueID'
REPLAY_VOLUME_ID = 'ocid1.volume.oc1.phx.exampleuniqueID'
REPLAY_DEVICE = '/dev/oracleoci/oraclevde'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture():
    expect_header_was_enabled = oci.base_client.enable_expect_header
    oci.base_client.enable_expect_header = False
    recorder = test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)
    recorder.filter_headers = ['authorization']
    try:
        with recorder.use_cassette(CASSETTE_FILENAME):
            yield
    finally:
        oci.base_client.enable_expect_header = expect_header_was_enabled


@pytest.mark.usefixtures('target_config')
class TestComputeNvmeVolumeAttachment:

    def test_attach_nvme_volume_commands(self):
        instance_id = self._recording_value(INSTANCE_ID_ENV, REPLAY_INSTANCE_ID)
        volume_id = self._recording_value(VOLUME_ID_ENV, REPLAY_VOLUME_ID)
        device = self._recording_value(DEVICE_ENV, REPLAY_DEVICE)

        self._attach_and_detach(
            ['compute', 'volume-attachment', 'attach-nvme-volume'],
            instance_id,
            volume_id,
            device
        )
        self._attach_and_detach(
            ['compute', 'volume-attachment', 'attach', '--type', 'nvme'],
            instance_id,
            volume_id,
            device
        )

    @staticmethod
    def _recording_value(environment_variable, replay_value):
        if test_config_container.vcr_mode != 'all':
            return replay_value

        value = os.environ.get(environment_variable)
        if not value:
            pytest.fail(
                '{} must be set when recording the NVMe volume attachment cassette'.format(
                    environment_variable
                )
            )
        return value

    def _attach_and_detach(self, attach_command, instance_id, volume_id, device):
        attachment_id = None
        try:
            result = util.invoke_command(
                attach_command + [
                    '--instance-id', instance_id,
                    '--volume-id', volume_id,
                    '--device', device
                ]
            )
            util.validate_response(result, expect_etag=True)
            attachment_id = util.find_id_in_response(result.output)

            result = util.wait_until(
                [
                    'compute', 'volume-attachment', 'get',
                    '--volume-attachment-id', attachment_id
                ],
                'ATTACHED',
                max_wait_seconds=900,
                max_interval_seconds=30
            )
            attachment = json.loads(result.output)['data']
            assert attachment['attachment-type'] == 'nvme'
            assert attachment['device'] == device
            assert attachment['lifecycle-state'] == 'ATTACHED'
        finally:
            if attachment_id:
                self._detach(attachment_id)

    @staticmethod
    def _detach(attachment_id):
        result = util.invoke_command(
            [
                'compute', 'volume-attachment', 'detach',
                '--volume-attachment-id', attachment_id,
                '--force'
            ]
        )
        util.validate_response(result, json_response_expected=False)
        util.wait_until(
            [
                'compute', 'volume-attachment', 'get',
                '--volume-attachment-id', attachment_id
            ],
            'DETACHED',
            max_wait_seconds=900,
            max_interval_seconds=30
        )
