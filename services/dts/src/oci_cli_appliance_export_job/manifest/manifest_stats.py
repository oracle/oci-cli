# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class ManifestStats:
    """
    This class is responsible to store information about the ongoing manifest process
    """
    def __init__(self):
        self._total_count = 0
        self._total_size = 0
        self._first_object = None
        self._last_object = None
        self._next_start_with = None
        self._manifest_obj_name = None
        self._manifest_md5 = None

    def increment_total_count(self):
        self._total_count += 1

    def increment_total_size(self, size):
        self._total_size += size

    def get_total_count(self):
        return self._total_count

    def get_total_size(self):
        return self._total_size

    def set_first_object(self, object):
        self._first_object = object

    def get_first_object(self):
        return self._first_object

    def set_last_object(self, object):
        self._last_object = object

    def get_last_object(self):
        return self._last_object

    def set_next_start_with(self, object):
        self._next_start_with = object

    def get_next_start_with(self):
        return self._next_start_with

    def set_manifest_obj_name(self, name):
        self._manifest_obj_name = name

    def get_manifest_object_name(self):
        return self._manifest_obj_name

    def set_manifest_md5(self, md5):
        self._manifest_md5 = md5

    def get_manifest_md5(self):
        return self._manifest_md5

    def __str__(self):
        return "************************* Manifest Progress ************************ \n" \
               "** Total Objects: \t{}\n" \
               "** Total Size: \t\t{}\n" \
               "** First Object: \t{}\n" \
               "** Last Object: \t{}\n" \
               "** Next Start With: \t{}\n" \
               "******************************************************************** \n"\
            .format(self._total_count, self._format_size(), self._first_object, self._last_object, self._next_start_with)

    def _format_size(self):
        """
        Print size in human readable format for ex: 200 MB, 20 GB, 2 TB etc.
        :return: Formatted string in human readable format
        """

        MiB = 1024 * 1024
        GiB = MiB * 1024
        TiB = GiB * 1024

        _format_str = '{number:.{digits}f}'

        if self._total_size < MiB:
            return '{} Bytes'.format(self._total_size)

        elif MiB <= self._total_size < GiB:
            return (_format_str + ' MB').format(number=self._total_size / MiB, digits=2)

        elif GiB <= self._total_size < TiB:
            return (_format_str + ' GB').format(number=self._total_size / GiB, digits=2)

        else:
            return (_format_str + ' TB').format(number=self._total_size / TiB, digits=2)
