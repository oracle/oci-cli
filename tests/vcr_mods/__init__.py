# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Because the SDK uses a vendored version of requests and urllib3, by default VCR doesn't know how to hook into it
# and so recording is not done properly. This module contains modifications to VCR's functionality so that
# it can recognise and work with SDKs vendored requests and urllib

from . import stubs

import itertools
import logging
import vcr

from urllib3 import connectionpool

import unittest.mock as mock

try:
    # Python 3.8+
    from importlib.metadata import version as pkg_version
except ImportError:
    from importlib_metadata import version as pkg_version

from packaging import version

logger = logging.getLogger(__name__)

try:
    # Modern urllib3 (2.0+)
    from urllib3.connection import HTTPSConnection
    _cpoolOCIVendoredHTTPSConnection = HTTPSConnection
    _OCIVendoredVerifiedHTTPSConnection = HTTPSConnection
except ImportError:
    # Legacy urllib3 (1.x)
    try:
        from urllib3.connectionpool import VerifiedHTTPSConnection as HTTPSConnection
    except ImportError:
        from urllib3.connectionpool import HTTPSConnection
    _OCIVendoredVerifiedHTTPSConnection = HTTPSConnection
    _cpoolOCIVendoredHTTPSConnection = HTTPSConnection

_cpoolOCIVendoredHTTPConnection = connectionpool.HTTPConnection

# Save the base VCR function references from VCR so that we can call them from inside our modified functions
original_vcr_reset_patchers_ref = vcr.patch.reset_patchers
original_cassette_patcher_builder_build_ref = vcr.patch.CassettePatcherBuilder.build


def get_object_storage_work_pool_vcr_patches():
    """
    When using mocked VCR responses, Object Storage bulk operations submit work to a thread pool.
    In some environments VCR patching does not reliably intercept requests made from those worker
    threads, which can cause real network calls in record_mode=none and lead to failures like
    BucketNotFound (because bucket creation is replayed, but PUTs hit the real service).

    To keep tests deterministic, execute work pool tasks synchronously while a VCR cassette is active
    and VCR is mocking.
    """
    try:
        from tests import test_config_container
        from oci_cli_object_storage.object_storage_transfer_manager import work_pool as os_work_pool
    except ImportError as exc:
        missing_module = getattr(exc, 'name', '')
        if missing_module and missing_module.startswith('oci_cli_object_storage'):
            return ()
        logger.exception("Unable to import Object Storage work pool for VCR patching.")
        raise
    except Exception:
        logger.exception("Unable to prepare Object Storage work pool VCR patch.")
        raise

    if not hasattr(os_work_pool, 'WorkPool') or not hasattr(os_work_pool, 'WorkPoolFuture'):
        message = "Object Storage work pool module does not expose WorkPool and WorkPoolFuture."
        logger.error(message)
        raise AttributeError(message)

    original_submit = os_work_pool.WorkPool.submit

    class _ImmediateAsyncResult:
        def __init__(self, thunk):
            self._success = True
            try:
                self._value = thunk()
            except Exception as exc:
                self._success = False
                self._value = exc

        def get(self):
            if self._success:
                return self._value
            raise self._value

        def ready(self):
            return True

        def successful(self):
            return self._success

    def submit(self, work_pool_task, blocking=True):
        if test_config_container.using_vcr_with_mock_responses():
            return os_work_pool.WorkPoolFuture(_ImmediateAsyncResult(work_pool_task.do_work))
        return original_submit(self, work_pool_task, blocking=blocking)

    return ((os_work_pool.WorkPool, 'submit', submit),)


def _revised_vcr_reset_patchers():
    for patcher in original_vcr_reset_patchers_ref():
        yield patcher

    if version.parse(pkg_version("urllib3")) < version.parse("2.0.0"):
        yield mock.patch.object(connectionpool, 'VerifiedHTTPSConnection', _OCIVendoredVerifiedHTTPSConnection)
    yield mock.patch.object(connectionpool, 'HTTPConnection', _cpoolOCIVendoredHTTPConnection)

    if hasattr(connectionpool.HTTPConnectionPool, 'ConnectionCls'):
        yield mock.patch.object(connectionpool.HTTPConnectionPool, 'ConnectionCls', _cpoolOCIVendoredHTTPConnection)
        yield mock.patch.object(connectionpool.HTTPSConnectionPool, 'ConnectionCls', _cpoolOCIVendoredHTTPSConnection)

    if hasattr(connectionpool, 'HTTPSConnection'):
        yield mock.patch.object(connectionpool, 'HTTPSConnection', _cpoolOCIVendoredHTTPSConnection)


def _oci_vendored(self):
    if version.parse(pkg_version("vcrpy")) > version.parse("4.3.0"):
        return self._urllib3_patchers(connectionpool, stubs=stubs, conn=None)
    return self._urllib3_patchers(connectionpool, stubs)


def _revised_cassette_patcher_builder_build(self):
    if version.parse(pkg_version("vcrpy")) > version.parse("4.3.0"):
        return itertools.chain(
            self._oci_vendored(), self._httplib(), self._requests(), self._boto3(), self._urllib3(),
            self._httplib2(), self._tornado(), self._aiohttp(),
            self._build_patchers_from_mock_triples(
                self._cassette.custom_patches
            ),
        )
    return itertools.chain(
        self._oci_vendored(), self._httplib(), self._requests(), self._boto3(), self._urllib3(),
        self._httplib2(), self._boto(), self._tornado(), self._aiohttp(),
        self._build_patchers_from_mock_triples(
            self._cassette.custom_patches
        ),
    )


# Replace base VCR functions with those that recognise the SDK's vendored requests and urllib3
vcr.patch.reset_patchers = _revised_vcr_reset_patchers
vcr.patch.CassettePatcherBuilder._oci_vendored = _oci_vendored
vcr.patch.CassettePatcherBuilder.build = _revised_cassette_patcher_builder_build
