# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import logging
from .manifest_line_item import ManifestLineItem


class CasperListIterator:
    """
    Iterator for iterating over the list of objects returned from the list_objects api
    :param os_client Http client to communicate with object storage
    :param namespace The name of the objecstorage namespace under which the bucket resides
    :param bucket The name of the bucket for which needs to be exported
    :param prefix The subset of objects that needs to be exported whose name starts with the supplied prefix
    :param start The subset of objects that needs to be exported starting with this object name (inclusive)
    :param end The subset of objects that needs to be exported upto this object name (inclusive)
    """
    def __init__(self, os_client, namespace, bucket, prefix, start, end):
        self._client = os_client
        self._namespace = namespace
        self._bucket = bucket
        self._next_obj = None
        self._obj_list_size = 0
        self._has_next_page = False
        self._next_start_with = None
        self._prefix = prefix
        self._range_start = start
        self._range_end = end
        self.log = logging.getLogger(self.__module__ + "." + self.__class__.__name__)
        self._initialize()

    def _initialize(self):
        self.log.debug("Initializing casper iterator ... ")
        self.obj_list = None
        self.curr_index = 0

        _fields = 'name,md5,size'
        self.log.debug("Doing LIST objects on the bucket ... ")

        if self._next_start_with is not None:
            response = self._client.list_objects(self._namespace, self._bucket, prefix=self._prefix, start=self._next_start_with, end=self._range_end, fields=_fields)
        else:
            response = self._client.list_objects(self._namespace, self._bucket, prefix=self._prefix, start=self._range_start, end=self._range_end, fields=_fields)
        if response.status == 200:
            self.obj_list = response.data.objects
            if self.obj_list is not None:
                self._obj_list_size = len(self.obj_list)
            self._next_start_with = response.data.next_start_with
            self._has_next_page = self._next_start_with is not None

            if self._obj_list_size > 0:
                self._next_obj = self.obj_list[self.curr_index]
            else:
                self.log.error("No objects found in the LIST bucket response")
                raise Exception("No objects found in the LIST bucket response")
        else:
            _msg = "Received error response from LIST objects, status: {}".format(response.status)
            self.log.error(_msg)
            raise Exception(_msg)

    def has_next(self):
        return self._next_obj is not None or self._has_next_page

    def get_next(self):
        if not self.has_next():
            self.log.error("There are no more objects to process")
            raise Exception("There are no more objects to process")

        if self._next_obj is None:
            if self._next_start_with is not None:
                self._initialize()
            else:
                self.log.error("Attempt to fetch next page but 'next_start_with' is empty")
                raise Exception("Attempt to fetch next page but 'next_start_with' is empty")

        curr_obj = self._next_obj
        curr_item = ManifestLineItem(curr_obj.name, curr_obj.md5, curr_obj.size)

        self.curr_index += 1
        if self.curr_index <= self._obj_list_size - 1:
            self._next_obj = self.obj_list[self.curr_index]
        else:
            self._next_obj = None

        return curr_item
