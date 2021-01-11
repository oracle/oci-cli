# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from oci_cli.util import pymd5


class TestPyMd5(unittest.TestCase):

    def test_hexdigest(self):
        hash = pymd5.md5(b"Hello World").hexdigest()
        self.assertEquals(hash, 'b10a8db164e0754105b7a99be72e3fe5')

    def test_copy(self):
        crypto = pymd5.new(b"Hello World")
        copy = crypto.copy()
        hash = copy.hexdigest()
        self.assertEquals(hash, 'b10a8db164e0754105b7a99be72e3fe5')

    def test_new(self):
        crypto = pymd5.new(b"Hello World")
        hash = crypto.hexdigest()
        self.assertEquals(hash, 'b10a8db164e0754105b7a99be72e3fe5')

    def test_md5(self):
        md5 = pymd5.md5()

    # TODO: The tests that follow are not very useful
    def test_digest(self):
        dig = pymd5.md5(b"Hello World").digest()
        # self.assertEquals(dig, '\xb1\n\x8d\xb1d\xe0uA\x05\xb7\xa9\x9b\xe7.?\xe5')

    def test_F(self):
        pymd5.F(0, 0, 0)

    def test_G(self):
        pymd5.G(0, 0, 0)

    def test_H(self):
        pymd5.H(0, 0, 0)

    def test_I(self):
        pymd5.I(0, 0, 0)
