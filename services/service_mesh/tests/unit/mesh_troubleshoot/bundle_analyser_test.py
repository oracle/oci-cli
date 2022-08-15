# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import io
import json
import re
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch, Mock

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.bundle_analyser import BundleAnalyser


class TestBundleAnalyzer(unittest.TestCase):

    def test_validate_csv_status(self):
        tests = [
            {
                "items": [{
                    "status": {
                        "phase": "Succeeded"
                    }
                }]
            },
            {
                "items": [{
                    "status": {
                        "phase": "Pending"
                    }
                }]
            }
        ]
        csv_file_content = tests[0]
        file_content = json.dumps(csv_file_content)
        self.csv_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.csv_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_csv_status(self)
            self.assertTrue(f.getvalue() == '\nCSV status: Succeeded\n')

        csv_file_content = tests[1]
        file_content = json.dumps(csv_file_content)
        self.csv_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.csv_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_csv_status(self)
            self.assertIsNotNone(re.search('Status of Csv did not succeed\n', f.getvalue()))

    def test_operator_services(self):
        tests = [
            {
                "operator_services": [
                    "oci-service-operator-controller-manager-service",
                    "oci-service-operator-webhook-service"
                ]
            },
            {
                "operator_services": [
                    "oci-service-operator-controller-manager-service",
                ]
            }
        ]
        report_file_content = tests[0]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.operator_services(self)
            self.assertTrue(f.getvalue() == '\nAll Operator Services are installed\n')

        report_file_content = tests[1]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.operator_services(self)
            self.assertIsNotNone(re.search('All Operator Services are not installed\n', f.getvalue()))

    def test_validate_crds(self):
        tests = [
            {
                "service_mesh_crds": [
                    "accesspolicies.servicemesh.oci.oracle.com",
                    "ingressgatewaydeployments.servicemesh.oci.oracle.com",
                    "ingressgatewayroutetables.servicemesh.oci.oracle.com",
                    "ingressgateways.servicemesh.oci.oracle.com",
                    "meshes.servicemesh.oci.oracle.com",
                    "virtualdeploymentbindings.servicemesh.oci.oracle.com",
                    "virtualdeployments.servicemesh.oci.oracle.com",
                    "virtualserviceroutetables.servicemesh.oci.oracle.com",
                    "virtualservices.servicemesh.oci.oracle.com"
                ]
            },
            {
                "service_mesh_crds": [
                    "accesspolicies.servicemesh.oci.oracle.com",
                    "ingressgatewaydeployments.servicemesh.oci.oracle.com",
                ]
            }
        ]
        report_file_content = tests[0]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_crds(self)
            self.assertTrue(f.getvalue() == '\nAll Mesh Custom Resources are installed\n')

        report_file_content = tests[1]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_crds(self)
            self.assertIsNotNone(re.search('All Mesh Crds are not installed', f.getvalue()))

    def test_validate_webhooks(self):
        tests = [
            {
                "service_mesh_webhooks": [
                    "ap-validator.servicemesh.oci.oracle.cloud.com",
                    "ig-validator.servicemesh.oci.oracle.cloud.com",
                    "igd-validator.servicemesh.oci.oracle.cloud.com",
                    "igrt-validator.servicemesh.oci.oracle.cloud.com",
                    "mesh-validator.servicemesh.oci.oracle.cloud.com",
                    "vd-validator.servicemesh.oci.oracle.cloud.com",
                    "vdb-validator.servicemesh.oci.oracle.cloud.com",
                    "vs-validator.servicemesh.oci.oracle.cloud.com",
                    "vsrt-validator.servicemesh.oci.oracle.cloud.com",
                    "proxy-injector.servicemesh.oci.oracle.com"
                ]
            },
            {
                "service_mesh_webhooks": [
                    "ap-validator.servicemesh.oci.oracle.cloud.com",
                    "ig-validator.servicemesh.oci.oracle.cloud.com",
                ]
            }
        ]
        report_file_content = tests[0]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_webhooks(self)
            self.assertTrue(f.getvalue() == '\nAll Mesh Webhooks are installed\n')

        report_file_content = tests[1]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_webhooks(self)
            self.assertIsNotNone(re.search('All Mesh webhooks are not installed', f.getvalue()))

    def test_validate_proxy_and_sidecar_version(self):
        report_file_content = {
            "pod_summary": [
                {
                    "labels": {
                        "app": "pets",
                        "pod-template-hash": "9f76cb4f5",
                        "version": "v2"
                    },
                    "mesh_id": "ocid1.mesh.oc1.iad.valid",
                    "name": "pets-v2-9f76cb4f5-f6c2q",
                    "namespace": "pet-rescue",
                    "proxy_status": {
                        "running": {
                            "startedAt": "2022-07-07T07:41:21Z"
                        }
                    },
                    "proxy_version": "0.1.520",
                    "vd_id": "ocid1.mesh.oc1.iad.valid",
                    "vdb_key": "pet-rescue/pets-v2-binding",
                    "vs_id": "ocid1.meshvirtualservice.oc1.iad.valid"
                }
            ]
        }
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_proxy_and_sidecar_version(self)
            self.assertIsNotNone(re.search('All sidecars are using same version\n', f.getvalue()))

    def test_validate_olm_version(self):
        tests = [
            {
                "olm": {
                    "version": "v0.20.0"
                }
            },
            {
                "olm": {
                    "version": "v1.20.0"
                }
            }
        ]
        report_file_content = tests[0]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_olm_version(self)
            self.assertTrue(f.getvalue() == '\nOLM version: v0.20.0\n')

        report_file_content = tests[1]
        file_content = json.dumps(report_file_content)
        self.report_json_contents = json.loads(file_content)
        f = io.StringIO()
        with patch('builtins.input', new=Mock(return_value=self.report_json_contents)):
            with redirect_stdout(f):
                BundleAnalyser.validate_olm_version(self)
            self.assertIsNotNone(re.search('OLM Version is not compatible\n', f.getvalue()))
