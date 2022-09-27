# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import os
import random
import shutil
import string
import tempfile
import unittest

import unittest.mock as mock

from OpenSSL import crypto

from services.dts.src.oci_cli_dts.appliance_auth_manager import ApplianceAuthManager
from services.dts.src.oci_cli_dts.appliance_cert_manager import ApplianceCertManager
from services.dts.src.oci_cli_dts.appliance_config_manager import ApplianceConfigManager
from services.dts.src.oci_cli_dts.appliance_config_spec import ApplianceConfigSpec
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CERT_COMMON_NAME, APPLIANCE_CERT_FILE_NAME
from services.dts.src.oci_cli_dts.physicalappliance_cli_extended import validate_upload_user_credentials
from oci import exceptions, Response, Request

from test_unit_test_dts_extended import get_mock_context

APPLIANCE_CONFIG_FOLDER = "appliance_config_test"
CERT_FINGERPRINT = "AB:CD:EF:GH"


class AuthSpec:
    def __init__(self, config_spec, config_manager):
        self.appliance_config_spec = config_spec
        self.appliance_config_manager = config_manager


class PhysicalApplianceTest(unittest.TestCase):
    def setUp(self):
        """
        Create a temporary folder and use this folder as the path to create all the configs
        :return:
        """
        self.test_dir = tempfile.mkdtemp()
        self.cert_manager = mock.Mock()

    def tearDown(self):
        """
        Deletes the temporary folder where all the configs have been created
        :return:
        """
        shutil.rmtree(self.test_dir)

    def _get_auth_manager(self, auth_spec, cert_fingerprint=CERT_FINGERPRINT):
        return ApplianceAuthManager(auth_spec.appliance_config_spec, cert_fingerprint,
                                    auth_spec.appliance_config_manager, self.cert_manager)

    @staticmethod
    def _validate_init_auth(auth_spec):
        config_spec = auth_spec.appliance_config_spec
        assert os.path.exists(auth_spec.appliance_config_manager.get_base_dir())
        assert os.path.exists(auth_spec.appliance_config_manager.get_config_dir(config_spec.get_profile()))

        appliance_config = auth_spec.appliance_config_manager.get_config(config_spec.get_profile())

        if config_spec.get_endpoint()[1] == 443:
            appliance_url = "https://{}".format(config_spec.get_endpoint()[0])
        else:
            appliance_url = "https://{}:{}".format(config_spec.get_endpoint()[0], config_spec.get_endpoint()[1])

        assert appliance_config.get_appliance_url() == appliance_url
        assert appliance_config.get_access_token() == config_spec.get_access_token()
        assert appliance_config.get_appliance_serial_id() == config_spec.get_serial_id()

    def _generate_cert_file(self, auth_spec):
        config_manager = self._get_config_manager()
        config_manager.create_config_dir(auth_spec.appliance_config_spec.get_profile())
        # return self.test_dir + "/{}/{}".format(auth_spec.appliance_config_spec.get_profile(), APPLIANCE_CERT_FILE_NAME)
        return "{}/{}".format(
            config_manager.get_config_dir(auth_spec.appliance_config_spec.get_profile()), APPLIANCE_CERT_FILE_NAME)

    def _test_init_auth(self, auth_spec, validate_cert_manager_calls=True, cert_fingerprint=CERT_FINGERPRINT):
        auth_manager = self._get_auth_manager(auth_spec, cert_fingerprint)
        auth_manager.initialize_auth()
        self._validate_init_auth(auth_spec)
        if validate_cert_manager_calls:
            self.cert_manager.fetch_cert.assert_called_once_with(self._generate_cert_file(auth_spec))
            self.cert_manager.validate_cert.assert_called_once_with(self._generate_cert_file(auth_spec),
                                                                    cert_fingerprint)

    @staticmethod
    def _generate_random_string(string_len):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(string_len))

    def _get_test_auth_spec(self, config_manager, appliance_ip, port):
        config_spec = ApplianceConfigSpec(profile=self._generate_random_string(7),
                                          endpoint=(appliance_ip, port),
                                          access_token=self._generate_random_string(10),
                                          serial_id=self._generate_random_string(8))
        return AuthSpec(config_spec, config_manager)

    def _get_config_manager(self):
        return ApplianceConfigManager(self.test_dir)

    def test_init_auth_with_single_profile(self):
        auth_spec = self._get_test_auth_spec(self._get_config_manager(), "1.2.3.4", 443)
        self._test_init_auth(auth_spec)

    def test_init_auth_with_non_default_https_port(self):
        auth_spec = self._get_test_auth_spec(self._get_config_manager(), "1.2.3.4", 8443)
        self._test_init_auth(auth_spec)

    def _init_multiple_appliances(self, config_manager, num_appliances):
        specs = []
        for i in range(num_appliances):
            appliance_ip = "10.0.1.{}".format(i)
            auth_spec = self._get_test_auth_spec(config_manager, appliance_ip, 443 + i)
            self._get_auth_manager(auth_spec).initialize_auth()
            specs.append(auth_spec)
        return specs

    def test_init_auth_with_multiple_profiles(self):
        config_manager = self._get_config_manager()
        specs = self._init_multiple_appliances(config_manager, 10)
        assert len(os.listdir(config_manager.get_base_dir())) == 10

        for spec in specs:
            self._validate_init_auth(spec)

    def test_init_auth_overwrite_different_access_token(self):
        auth_spec = self._get_test_auth_spec(self._get_config_manager(), "1.2.3.4", 443)
        self._test_init_auth(auth_spec)
        modified_access_token = self._generate_random_string(10)
        auth_spec_with_different_access_token = AuthSpec(ApplianceConfigSpec(
            profile=auth_spec.appliance_config_spec.get_profile(),
            endpoint=auth_spec.appliance_config_spec.get_endpoint(),
            access_token=modified_access_token,
            serial_id=auth_spec.appliance_config_spec.get_serial_id()), auth_spec.appliance_config_manager)
        self._test_init_auth(auth_spec_with_different_access_token, False)

        modified_endpoint = ("5.6.7.8", 8443)
        auth_spec_with_different_endpoint = AuthSpec(ApplianceConfigSpec(
            profile=auth_spec.appliance_config_spec.get_profile(),
            endpoint=modified_endpoint,
            access_token=auth_spec.appliance_config_spec.get_access_token(),
            serial_id=auth_spec.appliance_config_spec.get_serial_id()), auth_spec.appliance_config_manager)
        self._test_init_auth(auth_spec_with_different_endpoint, False)

        modified_serial_id = self._generate_random_string(8)
        auth_spec_with_different_serial_id = AuthSpec(ApplianceConfigSpec(
            profile=auth_spec.appliance_config_spec.get_profile(),
            endpoint=auth_spec.appliance_config_spec.get_endpoint(),
            access_token=auth_spec.appliance_config_spec.get_access_token(),
            serial_id=modified_serial_id), auth_spec.appliance_config_manager)
        self._test_init_auth(auth_spec_with_different_serial_id, False)

    @staticmethod
    def _create_and_write_cert(cert_file, cert_common_name):
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)
        cert = crypto.X509()
        cert.get_subject().C = "US"
        cert.get_subject().ST = "CA"
        cert.get_subject().L = "Dummy"
        cert.get_subject().OU = "Dummy"
        cert.get_subject().CN = cert_common_name
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'md5')
        ssl_cert = crypto.dump_certificate(crypto.FILETYPE_PEM, cert)
        with open(cert_file, 'wb') as f:
            f.write(ssl_cert)
        return cert.digest("md5")

    def _init_auth_spec_and_cert_manager(self):
        # Mock only the fetch_cert() method of the cert_manager
        auth_spec = self._get_test_auth_spec(self._get_config_manager(), "1.2.3.4", 443)
        endpoint = auth_spec.appliance_config_spec.get_endpoint()
        # Override the mock cert manager
        self.cert_manager = ApplianceCertManager(endpoint)
        self.cert_manager.fetch_cert = mock.MagicMock()
        return auth_spec

    def test_init_auth_valid_cert_common_name_and_valid_cert_fingerprint(self):
        auth_spec = self._init_auth_spec_and_cert_manager()
        # Create a certificate and write to the cert file
        cert_fingerprint = self._create_and_write_cert(self._generate_cert_file(auth_spec), APPLIANCE_CERT_COMMON_NAME)
        self._test_init_auth(auth_spec, validate_cert_manager_calls=False, cert_fingerprint=cert_fingerprint)

    def test_init_auth_valid_cert_common_name_and_invalid_cert_fingerprint(self):
        with self.assertRaises(exceptions.RequestException):
            auth_spec = self._init_auth_spec_and_cert_manager()
            # Create a certificate and write to the cert file
            self._create_and_write_cert(self._generate_cert_file(auth_spec), APPLIANCE_CERT_COMMON_NAME)
            self._test_init_auth(auth_spec, validate_cert_manager_calls=False, cert_fingerprint="AB:CD:EF:GH")

    def test_init_auth_invalid_cert_common_name_and_valid_cert_fingerprint(self):
        with self.assertRaises(exceptions.RequestException):
            auth_spec = self._init_auth_spec_and_cert_manager()
            # Create a certificate and write to the cert file
            cert_fingerprint = self._create_and_write_cert(self._generate_cert_file(auth_spec), "Invalid Common Name")
            self._test_init_auth(auth_spec, validate_cert_manager_calls=False, cert_fingerprint=cert_fingerprint)

    def test_get_config_without_init_auth(self):
        with self.assertRaises(exceptions.InvalidConfig):
            self._get_config_manager().get_config("fake-appliance")

    def test_list_configs(self):
        config_manager = self._get_config_manager()
        assert len(config_manager.list_configs()) == 0
        specs = self._init_multiple_appliances(config_manager, 10)
        config_dict = config_manager.list_configs()
        assert len(config_dict) == len(specs)
        for spec in specs:
            assert spec.appliance_config_spec.get_profile() in config_dict
            config = config_manager.get_config(spec.appliance_config_spec.get_profile())
            assert config_dict[spec.appliance_config_spec.get_profile()] == config

    def test_delete_config(self):
        config_manager = self._get_config_manager()
        auth_spec = self._get_test_auth_spec(config_manager, "1.2.3.4", 443)
        self._test_init_auth(auth_spec)
        config_manager.delete_config(auth_spec.appliance_config_spec.get_profile())
        assert len(config_manager.list_configs()) == 0
        assert not config_manager.is_config_present(auth_spec.appliance_config_spec.get_profile())
        assert not os.path.exists(config_manager.get_config_dir(auth_spec.appliance_config_spec.get_profile()))

    def test_delete_without_init_auth(self):
        with self.assertRaises(exceptions.InvalidConfig):
            self._get_config_manager().delete_config("fake-appliance")

    def test_delete_one_of_many_configs(self):
        config_manager = self._get_config_manager()
        specs = self._init_multiple_appliances(config_manager, 10)
        appliance_profile_to_del = specs[0].appliance_config_spec.get_profile()
        config_manager.delete_config(appliance_profile_to_del)
        assert len(config_manager.list_configs()) == 9
        assert not config_manager.is_config_present(appliance_profile_to_del)
        assert not os.path.exists(config_manager.get_config_dir(appliance_profile_to_del))
        for i in range(1, len(specs)):
            assert config_manager.is_config_present(specs[i].appliance_config_spec.get_profile())

    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.get_upload_user_config')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.get_upload_user_region')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.get_user')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_obj_storage_client')
    def test_validate_upload_user_credentials(self, mock_os_client, user, region, upload_user_config):

        def mock_get_upload_user_region():
            return "test-region"

        def mock_get_user():
            return Response(200, {}, "test-user", Request("mock.method", "mock.url"))

        def mock_get_upload_user_config(ctx):
            return ctx.obj['config']

        def mock_get_namespace():
            return Response(200, {}, "test-namespace", Request("mock.method", "mock.url"))

        auth_spec = self._get_test_auth_spec(self._get_config_manager(), "1.2.3.4", 443)
        self._test_init_auth(auth_spec)

        mock_context = get_mock_context()
        user.return_value = mock_get_user()
        region.return_value = mock_get_upload_user_region()
        upload_user_config.return_value = mock_get_upload_user_config(mock_context)
        mock_os_client.return_value.get_namespace.side_effect = mock_get_namespace

        with self.assertRaises(SystemExit):
            with mock.patch('click.confirm', return_value=False):
                validate_upload_user_credentials(mock_context, 'fake-bucket', upload_user_config=None)

        mock_context.obj['config']['region'] = 'test-region'
        with mock.patch('click.confirm', return_value=True):
            validate_upload_user_credentials(mock_context, 'fake-bucket', upload_user_config=None)
