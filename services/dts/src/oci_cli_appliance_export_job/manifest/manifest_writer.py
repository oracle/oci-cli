# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .manifest_constants import ENCODING_FORMAT_UTF, MAX_EXPORT_SIZE, OBJECT_NAME_MAX_PATH_LENGTH, MAX_PART_SIZE_MB
from .manifest_stats import ManifestStats
import logging


class ManifestWriter:
    """
    Utility class to create a manifest file from the iterator of objects
    :param iterator of type ManifestIterator to iterate over the items to be written to manifest
    :param object_uploader of type ObjectUploader that manages all uploads to object storage
    :param stats_consumer of type ManifestStatsConsumer that takes manifest stats object to report progress
    :param size_of_part: The maximum size of a part. Usually 100MB
    """
    def __init__(self, iterator, object_uploader, stats_consumer, size_of_part=MAX_PART_SIZE_MB):
        self._iterator = iterator
        self._uploader = object_uploader
        self._consumer = stats_consumer
        self._buffer = None
        self._stats = ManifestStats()
        self._part_counter = 0
        self._max_part_size = size_of_part
        self.log = logging.getLogger(self.__module__ + "." + self.__class__.__name__)

    def write(self):
        """
        This method iterates over the iterator to read objects and write them to a local buffer. This buffer is then passed
        in to the ObjectUploader which eventually uploads it as either a multipart or a regular object to objectStorage
        :return: String name of the object that was uploaded to object storage
        """
        self.log.debug("Starting manifest writer ... ")

        while self._iterator.has_next():
            line_item = self._iterator.get_next()

            if not self._do_xa_capacity_check(line_item.size):
                _msg_ = "MAXIMUM CAPACITY REACHED FOR THIS EXPORT, TOTAL SIZE = {}.\nPLEASE CREATE A NEW EXPORT REQUEST "
                "WITH SPECIFYING THE FILTER '--start={}' WHICH IS THE NEXT OBJECT TO BE PROCESSED FOR THIS BUCKET.\n"
                "STOPPING THE CURRENT MANIFEST GENERATION HERE. TOTAL NUMBER OF OBJECTS IN THIS MANIFEST = {}".format(self._stats.get_total_size(), line_item.path, self._stats.get_total_count())  # noqa: F523

                print(_msg_)
                self.log.info(_msg_)
                self._stats.set_next_start_with(line_item.path)
                break

            if not ManifestWriter._is_object_valid(line_item.path):
                raise Exception("Object validation failed for object {}".format(str(line_item)))

            if not self._do_buffer_capacity_check(len(str(line_item))):
                self.log.debug("Reached max buffer size, flushing buffer for next items ... ")
                self._do_mp_upload()

            self._write_and_record(line_item)

        if self._part_counter > 1:
            self._do_mp_upload()
            _result = self._uploader.commit_mp_object()
        else:
            self._consumer.consume(self._stats)
            _result = self._uploader.upload_regular_object(self._buffer)

        self._stats.set_manifest_md5(_result['md5'])
        self._stats.set_manifest_obj_name(_result['name'])
        return self._stats

    def _write_and_record(self, line_item):
        """
        Write line_item to buffer and update the stats info with this line_item
        :param line_item: Object of type ManifestLineItem with __str__() defined
        """
        # Todo: check memory leak?
        if self._buffer is None or len(self._buffer) == 0:
            self._buffer = bytearray(str(line_item), ENCODING_FORMAT_UTF)
        else:
            self._buffer.extend(bytearray(str(line_item), ENCODING_FORMAT_UTF))

        if self._stats.get_first_object() is None:
            self._stats.set_first_object(line_item.path)

        self._stats.increment_total_count()
        self._stats.increment_total_size(int(line_item.size))
        self._stats.set_last_object(line_item.path)

    def _clear_buffer(self):
        self.log.debug("Reached max part size limit, clearing buffer for next write")
        self._buffer.clear()

    def _do_mp_upload(self):
        self._part_counter += 1
        self._uploader.upload_part(self._buffer, self._part_counter)
        self._clear_buffer()
        self._consumer.consume(self._stats)

    def _do_xa_capacity_check(self, requested_size):
        return self._stats.get_total_size() + requested_size <= MAX_EXPORT_SIZE

    def _do_buffer_capacity_check(self, requested_size):
        return self._buffer is None or len(self._buffer) + requested_size <= self._max_part_size

    @staticmethod
    def _is_object_valid(o):
        o1 = o
        if o1:
            path_arr = o1.split('/')
            for path in path_arr:
                if len(path) > OBJECT_NAME_MAX_PATH_LENGTH:
                    return False

            return True
