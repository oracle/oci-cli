# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .. import cli_util


class BulkObjectStorageOperationOutput(object):
    def __init__(self):
        self._failures = {}

    def add_failure(self, failed_item, **kwargs):
        self._failures[failed_item] = str(kwargs.get('callback_exception'))

    def has_failures(self):
        return len(self._failures) > 0

    def validate_output_format(self, output_format):
        if output_format != 'json' and output_format != 'table':
            raise RuntimeError('Unrecognised output format: {}. Supported formats are json and table'.format(output_format))


class BulkPutOperationOutput(BulkObjectStorageOperationOutput):
    OBJECT_PUT_DISPLAY_HEADERS = {
        "etag",
        "opc-content-md5",
        "last-modified",
        "opc-multipart-md5"
    }

    def __init__(self):
        super(BulkPutOperationOutput, self).__init__()
        self._uploaded = {}
        self._skipped = []

    def add_uploaded(self, uploaded_object, **kwargs):
        result, checksum = kwargs.get('work_pool_task_result')
        filtered_headers = cli_util.filter_object_headers(result.headers, self.OBJECT_PUT_DISPLAY_HEADERS)
        if checksum:
            message, match = cli_util.get_checksum_message(result.headers, checksum)
            if match:
                self._uploaded[uploaded_object] = filtered_headers
                self._uploaded[uploaded_object]['verify-md5-checksum'] = message
            else:
                self._failures[uploaded_object] = filtered_headers
                self._failures[uploaded_object]['verify-md5-checksum'] = message
        else:
            self._uploaded[uploaded_object] = filtered_headers

    def add_skipped(self, skipped):
        self._skipped.append(skipped)

    def get_output(self, output_format):
        self.validate_output_format(output_format)

        if output_format == 'json':
            return {
                'uploaded-objects': self._uploaded,
                'upload-failures': self._failures,
                'skipped-objects': self._skipped
            }
        elif output_format == 'table':
            consolidated_result = []

            for uploaded_object, result in self._uploaded.items():
                output_result = {'action': 'Uploaded', 'name': uploaded_object, 'type': 'file'}
                output_result.update(result)
                consolidated_result.append(output_result)

            for uploaded_object, failure in self._failures.items():
                consolidated_result.append({
                    'action': 'Failed',
                    'name': uploaded_object,
                    'type': 'file',
                    'error-message': failure
                })

            for skip in self._skipped:
                consolidated_result.append({'action': 'Skipped', 'name': skip, 'type': 'file'})

            return consolidated_result


class BulkGetOperationOutput(BulkObjectStorageOperationOutput):
    def __init__(self):
        super(BulkGetOperationOutput, self).__init__()
        self._downloaded = []
        self._skipped = []

    def add_downloaded(self, downloaded_object, **kwargs):
        self._downloaded.append(downloaded_object)

    def add_skipped(self, skipped):
        self._skipped.append(skipped)

    def get_output(self, output_format):
        self.validate_output_format(output_format)

        if output_format == 'json':
            return {
                'downloaded-objects': self._downloaded,
                'download-failures': self._failures,
                'skipped-objects': self._skipped
            }
        elif output_format == 'table':
            consolidated_result = []

            for downloaded_obj in self._downloaded:
                consolidated_result.append({
                    'action': 'Downloaded',
                    'name': downloaded_obj,
                    'type': 'object'
                })

            for downloaded_obj, failure in self._failures.items():
                consolidated_result.append({
                    'action': 'Failed',
                    'name': downloaded_obj,
                    'type': 'object',
                    'error-message': failure
                })

            for skip in self._skipped:
                consolidated_result.append({'action': 'Skipped', 'name': skip, 'type': 'object'})

            return consolidated_result


class BulkDeleteOperationOutput(BulkObjectStorageOperationOutput):
    def __init__(self, object_type='object'):
        super(BulkDeleteOperationOutput, self).__init__()
        self._deleted = []
        self._type = object_type

    def add_deleted(self, deleted):
        self._deleted.append(deleted)

    def get_type(self):
        return self._type

    def get_output(self, output_format, dry_run=False):
        self.validate_output_format(output_format)

        if output_format == 'json':
            return {
                'delete-failures': self._failures,
                'deleted-objects': self._deleted
            }
        elif output_format == 'table':
            consolidated_result = []

            for deleted_obj, failure in self._failures.items():
                consolidated_result.append({
                    'action': 'Failed',
                    self._type: deleted_obj,
                    'error-message': failure
                })

            for deleted in self._deleted:
                if dry_run:
                    consolidated_result.append({'action': 'Dry Run', 'type': self._type, 'name': deleted})
                else:
                    consolidated_result.append({'action': 'Deleted', 'type': self._type, 'name': deleted})

            return consolidated_result
