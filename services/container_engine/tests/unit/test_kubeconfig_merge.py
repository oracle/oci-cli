# coding: utf-8
# Copyright (c) 2026, Oracle and/or its affiliates. All rights reserved.

import unittest

from services.container_engine.src.oci_cli_container_engine.containerengine_cli_extended import _merge_kubeconfig_yaml


class TestKubeconfigMerge(unittest.TestCase):
    def test_preserves_namespace_when_updating_context(self):
        destination = {
            'contexts': [{
                'name': 'cluster',
                'context': {'cluster': 'cluster', 'user': 'user', 'namespace': 'workloads'}
            }]
        }
        source = {
            'contexts': [{
                'name': 'cluster',
                'context': {'cluster': 'cluster', 'user': 'updated-user'}
            }]
        }

        _merge_kubeconfig_yaml(destination, source, 'contexts')

        assert destination['contexts'][0]['context'] == {
            'cluster': 'cluster', 'user': 'updated-user', 'namespace': 'workloads'
        }

    def test_preserves_proxy_url_when_updating_cluster(self):
        destination = {
            'clusters': [{
                'name': 'cluster',
                'cluster': {'server': 'https://old.example', 'proxy-url': 'http://proxy.example'}
            }]
        }
        source = {
            'clusters': [{
                'name': 'cluster',
                'cluster': {'server': 'https://new.example'}
            }]
        }

        _merge_kubeconfig_yaml(destination, source, 'clusters')

        assert destination['clusters'][0]['cluster'] == {
            'server': 'https://new.example', 'proxy-url': 'http://proxy.example'
        }
