# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .dataset_seal_status import DatasetSealStatus
from .details import Details
from .nfs_dataset_info import NfsDatasetInfo
from .nfs_dataset_spec import NfsDatasetSpec
from .nfs_export_config import NfsExportConfig
from .nfs_export_details import NfsExportDetails
from .object_storage_upload_config import ObjectStorageUploadConfig
from .passphrase_details import PassphraseDetails
from .physical_transfer_appliance import PhysicalTransferAppliance

# Maps type names to classes for client services.
client_type_mapping = {
    "DatasetSealStatus": DatasetSealStatus,
    "Details": Details,
    "NfsDatasetInfo": NfsDatasetInfo,
    "NfsDatasetSpec": NfsDatasetSpec,
    "NfsExportConfig": NfsExportConfig,
    "NfsExportDetails": NfsExportDetails,
    "ObjectStorageUploadConfig": ObjectStorageUploadConfig,
    "PassphraseDetails": PassphraseDetails,
    "PhysicalTransferAppliance": PhysicalTransferAppliance
}
