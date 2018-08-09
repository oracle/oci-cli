# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import sys
import ctypes


# Simple class to supress errors which occur when
# importing hashlib.
class DevNull:
    def write(self, msg):
        pass


# dummy md5 function for hashlib so it won't segfault when called after loading libcrypto.
def md5(dummy):
    raise Exception("md5 is not implemented in hashlib")
    return None


def override_libcrypto(fips_libcrypto_file):
    _bs_crypto = ctypes.CDLL(fips_libcrypto_file)
    _bs_crypto.FIPS_mode_set(ctypes.c_int(1))
    import ssl  # noqa: E402
    if not hasattr(ssl, 'FIPS_mode'):
        ssl.FIPS_mode = _bs_crypto.FIPS_mode


def patch_hashlib_md5():
    # hashlib.md5 is imported by urllib3, which is required by requests,
    # which is used by oci (python sdk).  This will cause errors so we need to
    # patch hashlib.
    stderr = sys.stderr
    try:
        sys.stderr = DevNull()
        import hashlib  # noqa: E402
    except (RuntimeError, ValueError):
        pass
    sys.stderr = stderr
    hashlib.md5 = md5
