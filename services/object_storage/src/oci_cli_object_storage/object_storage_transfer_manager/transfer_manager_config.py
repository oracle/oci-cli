# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.object_storage.transfer import constants


# Configuration for the TransferManager. Recognized items are:
#
#   - max_object_storage_requests: The total number of requests to get, put (non-multipart), head and delete objects which can be in flight at any one time
#   - max_multipart_files_to_process: The total number of multipart files to process at any one time. "Process" means preparing a new multipart upload, figuring out
#     how the files will be split and into how many, kicking off the upload and committing it once done
#   - max_object_storage_multipart_requests: The total number of put requests we can issue at any one time, where the put request relates to part of a multipart upload
#   - multipart_part_size: Threshold (in MiB) after which we'll upload a file in multiple parts
#   - use_multipart_uploads: Whether to use multipart uploads or not
class TransferManagerConfig():
    DEFAULT_MAX_REQUESTS = 10
    DEFAULT_MAX_MULTIPART_TO_PROCESS = 10
    DEFAULT_MAX_MULTIPART_REQUESTS = 10
    DEFAULT_MULTIPART_MAX_RETRIES = 60

    def __init__(self,
                 max_object_storage_requests=DEFAULT_MAX_REQUESTS,
                 max_object_storage_multipart_requests=DEFAULT_MAX_MULTIPART_REQUESTS,
                 max_multipart_files_to_process=DEFAULT_MAX_MULTIPART_TO_PROCESS,
                 multipart_part_size=constants.DEFAULT_PART_SIZE,
                 use_multipart_uploads=True,
                 multipart_max_retries=DEFAULT_MULTIPART_MAX_RETRIES
                 ):
        self.max_object_storage_requests = max_object_storage_requests
        self.max_object_storage_multipart_requests = max_object_storage_multipart_requests
        self.max_multipart_files_to_process = max_multipart_files_to_process
        self.multipart_part_size = multipart_part_size
        self.use_multipart_uploads = use_multipart_uploads
        self.multipart_max_retries = multipart_max_retries
