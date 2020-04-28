# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import time

from multiprocessing.dummy import Pool

from .wrapped_semaphore import WrappedSemaphore
from .work_pool_task import WorkPoolTaskCallback


# Represents a generic pool to which work (tasks) can be submitted and executed.
class WorkPool():
    def __init__(self, pool_size, max_workers):
        self._sempahore = WrappedSemaphore(pool_size)
        self._inner_pool = Pool(processes=pool_size)

    def submit(self, work_pool_task, blocking=True):
        self._sempahore.acquire(blocking)

        # We always want to release the semaphore at the end so that subsequent
        # tasks can start work
        release_semaphore_callback = WorkPoolTaskCallback(self._sempahore.release)
        work_pool_task.add_completion_callback(release_semaphore_callback)

        return WorkPoolFuture(self._inner_pool.apply_async(work_pool_task.do_work))

    def map(self, function, iterable):
        self._inner_pool.map(function, iterable)

    # Closes off the pool for additional work, and then waits until all current work is completed
    def wait_for_completion(self):
        self._inner_pool.close()
        self._inner_pool.join()


# A wrapper around a collection of WorkPoolFuture objects. This provides a convenience for
# waiting until all futures in the collection have been executed.
class WorkPoolFutureCollection():
    def __init__(self, futures):
        if not futures:
            self.futures = []
        else:
            self.futures = futures

    def add(self, future):
        self.futures.append(future)

    def evict_done_futures(self):
        done_futures = []
        not_done_futures = []

        for f in self.futures:
            if f.done():
                done_futures.append(f)
            else:
                not_done_futures.append(f)

        self.futures = not_done_futures
        return done_futures

    def clear(self):
        previous_list = self.futures
        self.futures = []

        return previous_list

    def join(self, check_interval_millis=None):
        if not self.futures:
            return

        while self.any_futures_not_done():
            if check_interval_millis:
                time.sleep(check_interval_millis / 1000)
            pass

    def any_futures_not_done(self):
        for f in self.futures:
            if not f.done():
                return True

        return False


# A future returned from the work pool on which a caller can wait for a task to be done
class WorkPoolFuture():
    def __init__(self, future):
        # For multiprocessing, this will be a multiprocessing.pool.AsyncResult
        self._future = future

    def result(self):
        # This will block until the result is available. If the result is an exception, it'll throw it
        return self._future.get()

    def done(self):
        return self._future.ready()

    def successful(self):
        return self._future.successful()
