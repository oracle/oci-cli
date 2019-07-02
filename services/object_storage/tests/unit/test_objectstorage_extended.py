# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import time_delta


class TestObjectStorage(unittest.TestCase):
    def setUp(self):
        pass

    def test_time_delta(self):
        assert time_delta(0, 34) == 'less than 1 minute'
        assert time_delta(0, 60 * 60) == '0 days 1 hour 0 mins'
        assert time_delta(1, 0) == '1 day 0 hours 0 mins'
        assert time_delta(2, 12840) == '2 days 3 hours 34 mins'
