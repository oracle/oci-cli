# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import traceback
from oci.exceptions import RequestException, ConnectTimeout


# An abstract task which can be submitted to the work pool and contains everything needed to execute the task. Implementors
# should create a subclass that contains their specific logic in do_work_hook()
class WorkPoolTask(object):
    def __init__(self, callbacks_container):
        if callbacks_container:
            self._completion_callbacks = callbacks_container.get_completion_callbacks()
            self._success_callbacks = callbacks_container.get_success_callbacks()
            self._error_callbacks = callbacks_container.get_error_callbacks()
        else:
            self._completion_callbacks = []
            self._success_callbacks = []
            self._error_callbacks = []

    def add_completion_callback(self, callback):
        self._completion_callbacks.append(callback)

    def add_success_callback(self, callback):
        self._success_callbacks.append(callback)

    def add_error_callback(self, callback):
        self._error_callbacks.append(callback)

    def get_completion_callbacks(self):
        return list(self._completion_callbacks)

    def get_success_callbacks(self):
        return list(self._success_callbacks)

    def get_error_callbacks(self):
        return list(self._error_callbacks)

    def do_work(self):
        result = None
        try:
            result = self.do_work_hook()
            self._run_success_callbacks(result, self._success_callbacks)
        except Exception as e:
            self._run_error_callbacks(e, self._error_callbacks)
            raise e
        finally:
            self._run_callbacks(self._completion_callbacks)

        return result

    def do_work_hook(self):
        raise NotImplementedError('do_work_hook() is not implemented')

    def _run_error_callbacks(self, exception, callbacks):
        if callbacks:
            for c in callbacks:
                c.execute(exception=exception)

    def _run_success_callbacks(self, result, callbacks):
        if callbacks:
            for c in callbacks:
                c.execute(result=result)

    def _run_callbacks(self, callbacks):
        if callbacks:
            for c in callbacks:
                c.execute()


# A container object which knows about completion, success and error callbacks
class WorkPoolTaskCallbacksContainer():
    def __init__(self, completion_callbacks=[], success_callbacks=[], error_callbacks=[]):
        self._completion_callbacks = self._get_list(completion_callbacks)
        self._success_callbacks = self._get_list(success_callbacks)
        self._error_callbacks = self._get_list(error_callbacks)

    def get_completion_callbacks(self):
        return list(self._completion_callbacks)

    def get_success_callbacks(self):
        return list(self._success_callbacks)

    def get_error_callbacks(self):
        return list(self._error_callbacks)

    def _get_list(self, callbacks):
        if callbacks is None:
            return []
        else:
            return list(callbacks)


# A container object which encapsulates a function which can be called as a callback on WorkPoolTask
class WorkPoolTaskCallback(object):
    def __init__(self, func_ref, *args, **kwargs):
        self._func_ref = func_ref
        self._args = args
        self._kwargs = kwargs

    def execute(self, **exec_kwargs):
        return self._func_ref(*self._args, **self._kwargs)


# A WorkPoolTaskCallback which is intended to be used as a callback in success scenarios as it can forward the
# result of the operation to the callback function
class WorkPoolTaskSuccessCallback(WorkPoolTaskCallback):
    def __init__(self, func_ref, *args, **kwargs):
        super(WorkPoolTaskSuccessCallback, self).__init__(func_ref, *args, **kwargs)

    def execute(self, **exec_kwargs):
        if 'result' in exec_kwargs:
            self._kwargs['work_pool_task_result'] = exec_kwargs['result']
        return self._func_ref(*self._args, **self._kwargs)


# A WorkPoolTaskCallback which is intended to be used as a callback in error scenarios as it can forward the
# exception which caused the failure to the callback function
class WorkPoolTaskErrorCallback(WorkPoolTaskCallback):
    def __init__(self, func_ref, *args, **kwargs):
        super(WorkPoolTaskErrorCallback, self).__init__(func_ref, *args, **kwargs)

    def execute(self, **exec_kwargs):
        if 'exception' in exec_kwargs:
            e = exec_kwargs['exception']
            self._kwargs['callback_exception'] = exec_kwargs['exception']

            if not isinstance(e, (RequestException, ConnectTimeout)):
                try:
                    tb = traceback.format_exc()
                    raise Exception(tb)
                except Exception as inner_e:
                    self._kwargs['callback_exception'] = inner_e
        return self._func_ref(*self._args, **self._kwargs)
