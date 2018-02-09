# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import threading


# A wrapper around threading's Semaphore class so we can inject our own behaviour if/when needed
class WrappedSemaphore():
    def __init__(self, limit):
        self._semaphore = threading.Semaphore(limit)

    def acquire(self, blocking=True):
        self._semaphore.acquire(blocking)

    def release(self):
        self._semaphore.release()
