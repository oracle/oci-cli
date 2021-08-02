# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Because the SDK uses a vendored version of requests and urllib3, by default VCR doesn't know how to hook into it
# and so recording is not done properly. This module contains modifications to VCR's functionality so that
# it can recognise and work with SDKs vendored requests and urllib

from . import stubs

import itertools
import vcr

from oci._vendor.urllib3 import connectionpool

import unittest.mock as mock

# Save the original types for our vendored version of requests and urllib3 so we can reset/unmock them later
_OCIVendoredVerifiedHTTPSConnection = connectionpool.VerifiedHTTPSConnection
_cpoolOCIVendoredHTTPConnection = connectionpool.HTTPConnection
_cpoolOCIVendoredHTTPSConnection = connectionpool.HTTPSConnection

# Save the base VCR function references from VCR so that we can call them from inside our modified functions
original_vcr_reset_patchers_ref = vcr.patch.reset_patchers
original_cassette_patcher_builder_build_ref = vcr.patch.CassettePatcherBuilder.build


def _revised_vcr_reset_patchers():
    for patcher in original_vcr_reset_patchers_ref():
        yield patcher

    yield mock.patch.object(connectionpool, 'VerifiedHTTPSConnection', _OCIVendoredVerifiedHTTPSConnection)
    yield mock.patch.object(connectionpool, 'HTTPConnection', _cpoolOCIVendoredHTTPConnection)

    if hasattr(connectionpool.HTTPConnectionPool, 'ConnectionCls'):
        yield mock.patch.object(connectionpool.HTTPConnectionPool, 'ConnectionCls', _cpoolOCIVendoredHTTPConnection)
        yield mock.patch.object(connectionpool.HTTPSConnectionPool, 'ConnectionCls', _cpoolOCIVendoredHTTPSConnection)

    if hasattr(connectionpool, 'HTTPSConnection'):
        yield mock.patch.object(connectionpool, 'HTTPSConnection', _cpoolOCIVendoredHTTPSConnection)


def _oci_vendored(self):
    return self._urllib3_patchers(connectionpool, stubs)


def _revised_cassette_patcher_builder_build(self):
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
