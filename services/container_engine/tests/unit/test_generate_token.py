# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util
import json


class TestGenerateToken(unittest.TestCase):
    def setUp(self):
        pass

    def test_missing_cluster_id(self):
        result = util.invoke_command(['ce', 'cluster', 'generate-token'])
        assert 'Error: Missing option(s) --cluster-id.' in result.output

    def test_generate_token(self):
        result = util.invoke_command(['ce', 'cluster', 'generate-token', '--cluster-id', 'fakeocid'])

        exec_credential = json.loads(result.output)
        assert exec_credential['apiVersion'] == "client.authentication.k8s.io/v1beta1"
        assert exec_credential['kind'] == "ExecCredential"
        assert exec_credential['status']['token']
        assert exec_credential['status']['expirationTimestamp']
