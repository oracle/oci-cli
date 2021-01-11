# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .manifest_constants import MANIFEST_OBJECT_NAME_PREFIX
from oci.object_storage.models import CreateMultipartUploadDetails
import logging


class ObjectUploader:
    """
    Utility class to manage regular and multipart uploads to object storage
    :param client to communicate with the object storage service
    :param namespace The object storage namespace where the bucket resides
    :param bucket The bucket on which export service has been requested
    :param obj_name_suffix job id of the export job that will be used as the suffix for the manifest file name
    """
    def __init__(self, client, namespace, bucket, obj_name_suffix):
        self._client = client
        self._namespace = namespace
        self._bucket = bucket
        self._parts_info = []
        self._object_key = MANIFEST_OBJECT_NAME_PREFIX.format(obj_name_suffix)
        self._multipart_request_details = None
        self.log = logging.getLogger(self.__module__ + "." + self.__class__.__name__)

    def _create_mp_upload_request(self):
        self.log.debug('Initiating a multipart upload request to object storage')
        details = CreateMultipartUploadDetails()
        details.object = self._object_key

        response = self._client.create_multipart_upload(self._namespace, self._bucket, details)
        if response is not None and response.status == 200:
            self._multipart_request_details = response.data
            self.log.debug("Successfully created request for multipart upload, upload id {}".format(self._multipart_request_details.upload_id))
        else:
            raise Exception("Failed to request multipart upload for bucket {}. Response status {}".format(self.manifest_writer.bucket, response.status))

    def upload_part(self, buffer, part_number):
        """
        Upload a part object of a multipart upload to object storage
        :param buffer: Array of bytes that needs to be uploaded in a single part
        :param part_number: part number of the current part to be uploaded
        :return: True or False depending on the status of upload
        """
        if self._multipart_request_details is None:
            self.log.debug("No upload request found, requesting a multipart upload ")
            self._create_mp_upload_request()

        # Upload part from buffer
        if buffer is not None and len(buffer) > 0:
            # TODO: Verify the encoding/decoding with non ascii chars if happening as expected
            # TODO: Check if this re-conversion from byte array to bytes object can be avoided
            # convert bytearray to bytes object / byte string
            _data = bytes(buffer)
            response = self._client.upload_part(self._namespace, self._bucket, self._object_key, self._multipart_request_details.upload_id, part_number, _data)
            if response is not None and response.status == 200:
                self._add_part_info_(part_number, response.headers['etag'])
                self.log.debug("Part number {} uploaded successfully".format(part_number))
            else:
                _msg = "Failed to upload part number {}. Response status {}".format(part_number, response.status)
                self.log.error(_msg)
                raise Exception(_msg)
        else:
            self.log.error("Upload part buffer is either missing or empty")
            raise Exception("Upload part buffer is either missing or empty")

    def commit_mp_object(self):
        """
        Commit the pending multipart upload to object storage
        :return: String name of the object that is committed and available in object storage
        """
        if self._multipart_request_details is not None:
            # commit
            commit_parts_map = {
                "partsToCommit": self._parts_info
            }

            response = self._client.commit_multipart_upload(self._namespace, self._bucket, self._multipart_request_details.object, self._multipart_request_details.upload_id, commit_parts_map)
            if response is not None and response.status == 200:
                self.log.debug("Successfully committed object {}, with Etag {}".format(self._multipart_request_details.object, response.headers['etag']))
                return {
                    "name": self._multipart_request_details.object,
                    "md5": response.headers['opc-multipart-md5']
                }
            else:
                raise Exception("Failed to commit multipart object. Response status {}, message {}".format(response.status, response.message))
        else:
            raise Exception("No pending multipart request found for committing")

    def upload_regular_object(self, buffer):
        """
        Upload a part object of a multipart upload to object storage
        :param buffer: Array of bytes that needs to be uploaded in a single object
        :return: String name of the object that is uploaded to object storage
        """
        if buffer is not None:
            self.log.info("Starting upload for regular object of size {}".format(len(buffer)))
            # TODO: Verify the encoding/decoding with non ascii chars if happening as expected
            # TODO: Check if this re-conversion from byte array to bytes object can be avoided
            # convert bytearray to bytes object / byte string
            _data = bytes(buffer)
            response = self._client.put_object(self._namespace, self._bucket, self._object_key, _data, content_length=len(buffer))
            if response is not None and response.status == 200:
                self.log.info("Successfully completed PUT Object operation on object storage. Response status {}, "
                              "object name {}, object etag {}".format(response.status, self._object_key, response.headers['etag']))
                return {
                    "name": self._object_key,
                    "md5": response.headers['opc-content-md5']
                }
            else:
                raise Exception("Failed to make PUT request to object storage. Response status {}, message {}".format(response.status, response.message))

    def _add_part_info_(self, part_number, part_etag):
        """
        Collect information about uploaded parts needed for doing commit()
        :param part_number: part number of the uploded part
        :param part_etag: etag of the uploaded part returned by upload_part()
        """
        # parts_info is a array of dictionaries
        self._parts_info.append({
            "partNum": part_number,
            "etag": part_etag
        })
