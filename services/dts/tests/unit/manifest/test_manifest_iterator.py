# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
import datetime

import unittest.mock as mock

from oci.object_storage.models.list_objects import ListObjects
from oci.object_storage.models.object_summary import ObjectSummary
from oci.response import Response
from services.dts.src.oci_cli_appliance_export_job.manifest.manifest_iterator import CasperListIterator


class ManifestIteratorTest(unittest.TestCase):

    def setUp(self):
        self.os_client = mock.Mock()

    def tearDown(self):
        # TODO: Implement me
        pass

    def test_iterator_next(self):
        self.os_client.list_objects.side_effect = list_objects_side_effect
        iterator = CasperListIterator(self.os_client, "namespace", "bucket", None, "start_object", "end_object")
        current_item = iterator.get_next()
        self.assertDictEqual({"size": 10, "md5": "abc123", "path": "first_object"}, current_item.__dict__)

    def test_iterator_has_next(self):
        self.os_client.list_objects.side_effect = list_objects_side_effect
        iterator = CasperListIterator(self.os_client, "namespace", "bucket", None, "start_object", "end_object")
        has_next = iterator.has_next()
        self.assertEqual(True, has_next)

    def test_iterator_next_pagination(self):
        self.os_client.list_objects.side_effect = list_objects_side_effect
        iterator = CasperListIterator(self.os_client, "namespace", "bucket", None, "start_object", "end_object")
        item1 = iterator.get_next()
        item2 = iterator.get_next()
        self.assertDictEqual({"size": 10, "md5": "abc123", "path": "first_object"}, item1.__dict__)
        self.assertDictEqual({"size": 20, "md5": "def456", "path": "second_object"}, item2.__dict__)

    def test_iterator_next_empty_list(self):
        self.os_client.list_objects.side_effect = list_objects_side_effect
        iterator = CasperListIterator(self.os_client, "namespace", "bucket", None, "start_empty_object", "end_object")
        item1 = iterator.get_next()
        self.assertDictEqual({"size": 10, "md5": "abc123", "path": "first_object"}, item1.__dict__)
        self.assertRaises(Exception, iterator.get_next)


def list_objects_side_effect(namespace, bucket, prefix, start, end, fields):
    response = Response(200, {}, ListObjects(), {})
    if start == "start_object":
        objects = [ObjectSummary(name="first_object", size=10, md5="abc123", time_created=datetime.datetime.now(), etag="tag1")]
        response.data.next_start_with = "second_object"
    elif start == "start_empty_object":
        objects = [ObjectSummary(name="first_object", size=10, md5="abc123", time_created=datetime.datetime.now(), etag="tag1")]
        response.data.next_start_with = "second_empty_object"
    elif start == "second_empty_object":
        objects = []
    else:
        objects = [ObjectSummary(name="second_object", size=20, md5="def456", time_created=datetime.datetime.now(), etag="tag2")]
    response.data.objects = objects
    return response
