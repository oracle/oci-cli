# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import threading


# A wrapper around threading's Semaphore class so we can inject our own behaviour if/when needed
class WrappedSemaphore():
    def __init__(self, limit):
        self._semaphore = threading.Semaphore(limit)

    def acquire(self, blocking=True):
        self._semaphore.acquire(blocking)

    def release(self):
        self._semaphore.release()
