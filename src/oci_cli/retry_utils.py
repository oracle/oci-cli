# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci._vendor.requests.exceptions import Timeout, ConnectionError
from oci.exceptions import ServiceError, RequestException, ConnectTimeout

DEFAULT_RETRY_STRATEGY_NAME = 'default'


def retry_on_timeouts_connection_internal_server_and_throttles(exception):
    retryable = False
    if isinstance(exception, Timeout):
        retryable = True
    elif isinstance(exception, ConnectionError):
        retryable = True
    elif isinstance(exception, RequestException):
        retryable = True
    elif isinstance(exception, ConnectTimeout):
        retryable = True
    elif isinstance(exception, ServiceError):
        # 500+ == Internal Server Error
        # -1 == Unknown
        # 429 == TooManyRequests (throttled)
        if exception.status >= 500 or exception.status == -1 or exception.status == 429:
            retryable = True

    return retryable
