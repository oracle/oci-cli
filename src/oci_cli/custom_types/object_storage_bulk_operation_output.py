# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .. import cli_util

import six


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
        self._uploaded[uploaded_object] = cli_util.filter_object_headers(kwargs.get('work_pool_task_result').headers, self.OBJECT_PUT_DISPLAY_HEADERS)

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

            for uploaded_object, result in six.iteritems(self._uploaded):
                output_result = {'action': 'Uploaded', 'file': uploaded_object}
                output_result.update(result)
                consolidated_result.append(output_result)

            for uploaded_object, failure in six.iteritems(self._failures):
                consolidated_result.append({
                    'action': 'Failed',
                    'file': uploaded_object,
                    'error-message': failure
                })

            for skip in self._skipped:
                consolidated_result.append({'action': 'Skipped', 'file': skip})

            return consolidated_result


class BulkGetOperationOutput(BulkObjectStorageOperationOutput):
    def __init__(self):
        super(BulkGetOperationOutput, self).__init__()
        self._skipped = []

    def add_skipped(self, skipped):
        self._skipped.append(skipped)

    def get_output(self, output_format):
        self.validate_output_format(output_format)

        if output_format == 'json':
            return {
                'download-failures': self._failures,
                'skipped-objects': self._skipped
            }
        elif output_format == 'table':
            consolidated_result = []

            for downloaded_obj, failure in six.iteritems(self._failures):
                consolidated_result.append({
                    'action': 'Failed',
                    'object': downloaded_obj,
                    'error-message': failure
                })

            for skip in self._skipped:
                consolidated_result.append({'action': 'Skipped', 'object': skip})

            return consolidated_result


class BulkDeleteOperationOutput(BulkObjectStorageOperationOutput):
    def __init__(self):
        super(BulkDeleteOperationOutput, self).__init__()
        self._deleted = []

    def add_deleted(self, deleted):
        self._deleted.append(deleted)

    def get_output(self, output_format, dry_run=False):
        self.validate_output_format(output_format)

        if output_format == 'json':
            return {
                'delete-failures': self._failures,
                'deleted-objects': self._deleted
            }
        elif output_format == 'table':
            consolidated_result = []

            for deleted_obj, failure in six.iteritems(self._failures):
                consolidated_result.append({
                    'action': 'Failed',
                    'object': deleted_obj,
                    'error-message': failure
                })

            for deleted in self._deleted:
                if dry_run:
                    consolidated_result.append({'action': 'Dry Run', 'object': deleted})
                else:
                    consolidated_result.append({'action': 'Deleted', 'object': deleted})

            return consolidated_result
