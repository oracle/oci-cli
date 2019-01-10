# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci._vendor.urllib3 import connectionpool
from vcr.stubs import VCRHTTPConnection, VCRHTTPSConnection


class VCRRequestsHTTPConnection(VCRHTTPConnection, connectionpool.HTTPConnection):
    _baseclass = connectionpool.HTTPConnection


class VCRRequestsHTTPSConnection(VCRHTTPSConnection, connectionpool.VerifiedHTTPSConnection):
    _baseclass = connectionpool.VerifiedHTTPSConnection
