# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from urllib3 import connectionpool
from vcr.stubs import VCRHTTPConnection, VCRHTTPSConnection

try:
    # Modern urllib3 (2.0+)
    from urllib3.connection import HTTPSConnection
    HTTPSClass = HTTPSConnection
except ImportError:
    # Legacy urllib3 (1.x)
    try:
        from urllib3.connectionpool import VerifiedHTTPSConnection as HTTPSConnection
    except ImportError:
        from urllib3.connectionpool import HTTPSConnection
    HTTPSClass = HTTPSConnection


class VCRRequestsHTTPConnection(VCRHTTPConnection, connectionpool.HTTPConnection):
    _baseclass = connectionpool.HTTPConnection


class VCRRequestsHTTPSConnection(VCRHTTPSConnection, HTTPSClass):
    _baseclass = HTTPSClass
