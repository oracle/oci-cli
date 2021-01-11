# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
import time
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.work_pool import WorkPool, WorkPoolFuture, WorkPoolFutureCollection
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.work_pool_task import WorkPoolTask


def sleep_function():
    time.sleep(1)


class Future():
    def __init__(self):
        self.is_ready = False

    def get(self):
        return "future get"

    def ready(self):
        return self.is_ready

    def successful(self):
        return True


class TestWorkPool(unittest.TestCase):
    def setUp(self):
        if not hasattr(self, 'wpt'):
            self.wpt = WorkPoolTask(None)
            self.wp = WorkPool(10, 3)
            self.future = Future()
            self.wpf = WorkPoolFuture(self.future)
            self.wpfc = WorkPoolFutureCollection(None)

    def test_submit(self):
        self.wp.submit(self.wpt)

    def test_map(self):
        iterable = []
        self.wp.map(sleep_function, iterable)

    def test_wait_for_completion(self):
        self.wp.wait_for_completion()

    def test_wpf_result(self):
        self.wpf.result()

    def test_wpf_done(self):
        is_done = self.wpf.done()
        self.assertFalse(is_done)
        self.future.is_ready = True
        is_done = self.wpf.done()
        self.assertTrue(is_done)

    def test_wpf_successful(self):
        self.wpf.successful()

    def test_wpfc_add(self):
        self.wpfc.add(self.wpf)

    def test_wpfc_any_futures_not_done(self):
        self.future.is_ready = False
        future = Future()
        wpf = WorkPoolFuture(future)
        self.wpfc.add(wpf)
        not_done = self.wpfc.any_futures_not_done()
        self.assertTrue(not_done)
        future.is_ready = True
        not_done = self.wpfc.any_futures_not_done()
        self.assertFalse(not_done)

    def test_wpfc_join(self):
        self.wpfc.join(1000)

    def test_wpfc_evict_done_futures(self):
        self.wpfc.evict_done_futures()

    def test_wpfc_clear(self):
        self.wpfc.clear()
