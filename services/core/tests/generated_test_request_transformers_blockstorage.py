# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.
import oci

from tests.generated_test_request_transformers import transformer


# mirroring manual changes from blockstorage_cli_extended.py for the create_boot_volume operation
@transformer('core', 'CreateBootVolume')
def _transform_create_boot_volume_request(request):
    if 'sourceDetails' in request:
        source_details = request.pop('sourceDetails')

        if source_details['type'] == oci.core.models.BootVolumeSourceFromBootVolumeDetails().type:
            request['sourceBootVolumeId'] = source_details['id']
        elif source_details['type'] == oci.core.models.BootVolumeSourceFromBootVolumeBackupDetails().type:
            request['bootVolumeBackupId'] = source_details['id']

    return request
