# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

import subprocess
import unittest
import unittest.mock as mock

import click
from oci.exceptions import RequestException, ServiceError

from services.dts.src.oci_cli_dts.verify_cli_extended import (
    # - Preparing for Appliance Data Transfers -
    check_dts_connectivity,
    check_os_connectivity,
    check_iam_users_groups_policies,
    check_bucket_belongs_to_compartment,
    # check_upload_user_credentials,
    check_dts_entitlement,
    check_dts_job_and_appliance_request,

    # - Configuring Appliance Data Imports -
    check_delivery_security_tie,
    check_appliance_reachability,

    # - Copying Data to the Import Appliance -
    check_finalized_status,

    # - Shipping the Import Appliance -
    check_return_security_tie,

    # - Monitoring the Import Appliance and Data Transfer -
    check_import_appliance_status,
)


def get_mock_context():
    mock_context = mock.MagicMock(spec=click.Context)
    mock_context.params = {}
    mock_context.obj = {}
    return mock_context


class VerifyTest(unittest.TestCase):

    def setUp(self):
        self.ctx = get_mock_context()
        self.compartment_id = "ocid1.compartment.region1..compartment-id"
        self.upload_bucket = "upload-bucket"
        self.namespace = "namespace"
        self.job_id = "ocid1.datatransferjob.region1..job-id"
        self.appliance_label = "XXXXXXXXXX"
        self.appliance_ip = "10.0.0.2"
        self.delivery_security_tie_id = "delivery-security-tie-id"
        self.return_security_tie_id = "return-security-tie-id"

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_dts_connectivity(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test is connectivity - successful response
        self.assertTrue(check_dts_connectivity(self.ctx, self.compartment_id))

        # Test is connectivity - unsuccessful response
        mock_client.list_transfer_jobs.side_effect = ServiceError(
            status=404, code="Unauthorized", headers={}, message="")
        self.assertTrue(check_dts_connectivity(self.ctx, self.compartment_id))

        # Test no connectivity - no response
        mock_client.list_transfer_jobs.side_effect = RequestException("Timeout")
        mock_client.base_client.endpoint = "http://datatransfer.r1.oracleiaas.com"
        with self.assertRaises(RequestException):
            check_dts_connectivity(self.ctx, self.compartment_id)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_os_connectivity(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test is connectivity - successful response
        self.assertTrue(check_os_connectivity(self.ctx, self.compartment_id))

        # Test is connectivity - unsuccessful response
        mock_client.get_namespace.side_effect = ServiceError(
            status=404, code="Unauthorized", headers={}, message="")
        self.assertTrue(check_os_connectivity(self.ctx, self.compartment_id))

        # Test no connectivity - no response
        mock_client.get_namespace.side_effect = RequestException("Timeout")
        mock_client.base_client.endpoint = "http://objectstorage.r1.oracleiaas.com"
        with self.assertRaises(RequestException):
            check_os_connectivity(self.ctx, self.compartment_id)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_iam_users_groups_policies(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - has required iam users, groups and policies
        self.assertTrue(check_iam_users_groups_policies(self.ctx, self.compartment_id))

        # Test raises internal service error
        mock_client.list_transfer_jobs.side_effect = ServiceError(
            status=500, code="Error", headers={}, message="", target_service="transfer_job")
        with self.assertRaises(ServiceError):
            check_iam_users_groups_policies(self.ctx, self.compartment_id)

        # Test failure - object storage unauthorized response
        mock_client.list_buckets.side_effect = ServiceError(
            status=404, code="Unauthorized", headers={}, message="", target_service="object_storage")
        with self.assertRaises(SystemExit):
            check_iam_users_groups_policies(self.ctx, self.compartment_id)

        # Test failure - data transfer service unauthorized response
        mock_client.list_transfer_jobs.side_effect = ServiceError(
            status=401, code="Unauthorized", headers={}, message="", target_service="transfer_job")
        with self.assertRaises(SystemExit):
            check_iam_users_groups_policies(self.ctx, self.compartment_id)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_bucket_belongs_to_compartment(self, mock_build_client):
        mock_client = mock_build_client.return_value

        bucket_data = mock.Mock()
        bucket_data.compartment_id = self.compartment_id
        mock_client.get_bucket.return_value.data = bucket_data

        # Test success - bucket exists and belongs to compartment
        self.assertTrue(check_bucket_belongs_to_compartment(self.ctx, self.compartment_id, self.upload_bucket))

        # Test failure - bucket does not exist
        mock_client.get_bucket.side_effect = ServiceError(status=404, code="NotFound", headers={}, message="")
        with self.assertRaises(SystemExit):
            check_bucket_belongs_to_compartment(self.ctx, self.compartment_id, self.upload_bucket)

        # Test failure - bucket exists but does not belong to the compartment
        bucket_data.compartment_id = "different-compartment-id"
        with self.assertRaises(SystemExit):
            check_bucket_belongs_to_compartment(self.ctx, self.compartment_id, self.upload_bucket)

    def test_check_upload_user_credentials(self):
        # Test absent - already unit test in test_unit_test_dts_extended.py
        pass

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_dts_entitlement(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - approved DTS entitlement found
        mock_entitlement_approved = mock.Mock()
        mock_entitlement_approved.lifecycle_state_details = "APPROVED"
        mock_entitlements = [mock_entitlement_approved]
        mock_client.list_transfer_appliance_entitlement.return_value.data = mock_entitlements
        self.assertTrue(check_dts_entitlement(self.ctx, self.compartment_id))

        # Test failure - no entitlement found
        mock_client.list_transfer_appliance_entitlement.return_value.data = []
        with self.assertRaises(SystemExit):
            check_dts_entitlement(self.ctx, self.compartment_id)

        # Test failure - entitlement found but not approved
        mock_entitlement_not_approved = mock.Mock()
        mock_entitlement_not_approved.lifecycle_state_details = "PENDING"
        mock_entitlements = [mock_entitlement_not_approved]
        mock_client.list_transfer_appliance_entitlement.return_value.data = mock_entitlements
        with self.assertRaises(SystemExit):
            check_dts_entitlement(self.ctx, self.compartment_id)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_dts_job_and_appliance_request(self, mock_build_client):
        mock_client = mock_build_client.return_value

        mock_transfer_jobs = mock.Mock()
        mock_transfer_jobs.data = [mock.Mock(id=self.job_id, upload_bucket_name=self.upload_bucket, device_type="APPLIANCE")]
        mock_client.list_transfer_jobs.return_value = mock_transfer_jobs

        mock_appliances = mock.Mock()
        mock_appliances.data = mock.Mock(transfer_appliance_objects=[mock.Mock()])
        mock_client.list_transfer_appliances.return_value = mock_appliances

        # Test success - valid transfer job and appliances exist
        self.assertTrue(check_dts_job_and_appliance_request(self.ctx, self.compartment_id, self.job_id, self.upload_bucket))

        # Test failure - no valid transfer job found
        mock_client.list_transfer_jobs.return_value.data = []
        with self.assertRaises(SystemExit):
            check_dts_job_and_appliance_request(self.ctx, self.compartment_id, self.job_id, self.upload_bucket)

        # Test failure - valid transfer job found but no appliances exist
        mock_client.list_transfer_jobs.return_value = mock_transfer_jobs
        mock_appliances.data.transfer_appliance_objects = []
        with self.assertRaises(SystemExit):
            check_dts_job_and_appliance_request(self.ctx, self.compartment_id, self.job_id, self.upload_bucket)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_delivery_security_tie(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - security tie ID matches
        appliance_data = mock.Mock()
        appliance_data.delivery_security_tie_id = self.delivery_security_tie_id
        mock_client.get_transfer_appliance.return_value.data = appliance_data
        self.assertTrue(
            check_delivery_security_tie(self.ctx, self.job_id, self.appliance_label, self.delivery_security_tie_id))

        # Test failure - security tie ID does not match
        appliance_data.delivery_security_tie_id = "different-tie-id"
        with self.assertRaises(SystemExit):
            check_delivery_security_tie(self.ctx, self.job_id, self.appliance_label, self.delivery_security_tie_id)

    @mock.patch("subprocess.check_output")
    def test_check_appliance_reachability(self, mock_check_output):
        # Test success - ping success
        mock_check_output.return_value = ""
        self.assertTrue(check_appliance_reachability(self.appliance_ip))

        # Test failure - ping failure
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "ping", output="Request timed out.")
        with self.assertRaises(SystemExit):
            check_appliance_reachability(self.appliance_ip)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_finalized_status(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - appliance in FINALIZED state
        appliance_data = mock.Mock()
        appliance_data.lifecycle_state = "FINALIZED"
        mock_client.get_transfer_appliance.return_value.data = appliance_data
        self.assertTrue(check_finalized_status(self.ctx, self.job_id, self.appliance_label))

        # Test failure - appliance not in FINALIZED state
        appliance_data.lifecycle_state = "PREPARING"
        with self.assertRaises(SystemExit):
            check_finalized_status(self.ctx, self.job_id, self.appliance_label)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_return_security_tie(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - security tie ID matches
        appliance_data = mock.Mock()
        appliance_data.return_security_tie_id = self.return_security_tie_id
        mock_client.get_transfer_appliance.return_value.data = appliance_data
        self.assertTrue(
            check_return_security_tie(self.ctx, self.job_id, self.appliance_label, self.return_security_tie_id))

        # Test failure - security tie ID does not match
        appliance_data.return_security_tie_id = "different-tie-id"
        with self.assertRaises(SystemExit):
            check_return_security_tie(self.ctx, self.job_id, self.appliance_label, self.return_security_tie_id)

    @mock.patch('oci_cli.cli_util.build_client')
    def test_check_import_appliance_status(self, mock_build_client):
        mock_client = mock_build_client.return_value

        # Test success - Appliance lifecycle state is COMPLETE
        appliance_data = mock.Mock()
        appliance_data.lifecycle_state = "COMPLETE"
        mock_client.get_transfer_appliance.return_value.data = appliance_data
        self.assertTrue(check_import_appliance_status(self.ctx, self.job_id, self.appliance_label))

        # Test success - Appliance lifecycle state is not COMPLETE
        appliance_data.lifecycle_state = "PROCESSING"
        self.assertTrue(check_import_appliance_status(self.ctx, self.job_id, self.appliance_label))

        # Test failure - Appliance lifecycle state is ERROR
        appliance_data.lifecycle_state = "ERROR"
        with self.assertRaises(SystemExit):
            check_import_appliance_status(self.ctx, self.job_id, self.appliance_label)
