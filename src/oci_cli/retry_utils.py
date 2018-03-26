# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from oci import exceptions
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError


DEFAULT_RETRY_STRATEGY_NAME = 'default'


def retry_on_timeouts_connection_internal_server_and_throttles(exception):
    retryable = False
    if isinstance(exception, Timeout):
        retryable = True
    elif isinstance(exception, ConnectionError):
        retryable = True
    elif isinstance(exception, exceptions.ServiceError):
        # 500+ == Internal Server Error
        # -1 == Unknown
        # 429 == TooManyRequests (throttled)
        if exception.status >= 500 or exception.status == -1 or exception.status == 429:
            retryable = True

    return retryable
