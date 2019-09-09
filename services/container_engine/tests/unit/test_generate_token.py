# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
