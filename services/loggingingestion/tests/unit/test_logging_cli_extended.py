# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestLoggingIngestionCliExtend(unittest.TestCase):
    def setUp(self):
        pass

    # from
    #   oci logging-ingestion put-logs ... --timestamp-opc-agent-processing ...
    # to
    #   oci logging-ingestion put-logs ... --agent-timestamp ...
    def test_log_change_log_group(self):
        result = util.invoke_command(['logging-ingestion', 'put-logs', '--timestamp-opc-agent-processing', '2017-09-15'])
        assert 'no such option: --timestamp-opc-agent-processing' in result.output

        result = util.invoke_command(['logging-ingestion', 'put-logs', '--agent-timestamp'])
        assert 'requires an argument' in result.output
