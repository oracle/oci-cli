# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestReplicasCliExtend(unittest.TestCase):
    def setUp(self):
        pass

    # test removed commands
    def test_removed_commands(self):
        # oci mysql replicas replica -> oci mysql replica
        result = util.invoke_command(['mysql', 'replicas'])
        assert 'No such command' in result.output
        result = util.invoke_command(['mysql', 'replica'])
        assert 'Usage: oci mysql replica [OPTIONS] COMMAND [ARGS]' in result.output
