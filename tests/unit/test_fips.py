# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from oci_cli import fips


class TestFips(unittest.TestCase):

    def test_patch_hashlib_md5(self):
        fips.patch_hashlib_md5()

        try:
            import hashlib
            hashlib.md5("dummy")
            self.fail("hashlib.md5() should have been patched and thrown an exception.")
        except Exception:
            pass

    def test_md5(self):
        try:
            fips.md5("dummy")
            self.fail("md5() should have thrown an exception.")
        except Exception:
            pass

    def test_write_devnull(self):
        output = fips.DevNull()
        output.write("dummy")

    def test_override_libcrypto(self):
        import ctypes
        import ssl
        ctypes.CDLL = CDLL
        fips.override_libcrypto("fips_libcrypto_file")
        ssl.FIPS_mode()


# Mock class returned from ctypes.CDLL
class Crypto:
    def FIPS_mode_set(self, mode):
        pass

    def FIPS_mode(self):
        return 1


# Mock return value for ctypes.CDLL
def CDLL(lib_file):
    crypto = Crypto()
    return crypto
