# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from conftest import runner
import oci_cli
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import io
import os
from . import util


PASSPHRASE = "example_passphrase"
TEMP_DIR = "tests/temp"
TEMP_PRIVATE_KEY_FILE = "tests/temp/temp_private_key.pem"


def passphrase_provider():
    return PASSPHRASE


def create_temp_private_key_file(password=None):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

    if password:
        encryption_algorithm = serialization.BestAvailableEncryption(password.encode("ascii"))
    else:
        encryption_algorithm = serialization.NoEncryption()

    serialized_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=encryption_algorithm)

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    with io.open(TEMP_PRIVATE_KEY_FILE, mode='w+b') as file:
        file.write(serialized_private_key)
        file.seek(0)  # So the key can be read again


class TestPassphrase(unittest.TestCase):

    def setUp(self):
        util.unset_admin_pass_phrase()
        self.runner = runner()

    def tearDown(self):
        if os.path.exists(TEMP_PRIVATE_KEY_FILE):
            os.remove(TEMP_PRIVATE_KEY_FILE)

    def test_unencrypted_key(self):
        create_temp_private_key_file()
        result = self.invoke_example_operation(profile='TEMP_CONFIG_NO_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("NotAuthenticated" in result.output)

    def test_encrypted_key_with_passphrase_in_config(self):
        create_temp_private_key_file(password=PASSPHRASE)
        result = self.invoke_example_operation(profile='TEMP_CONFIG_WITH_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("NotAuthenticated" in result.output)

    def test_encrypted_key_with_incorrect_passphrase_in_config(self):
        create_temp_private_key_file(password="some other passphrase")
        result = self.invoke_example_operation(profile='TEMP_CONFIG_WITH_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("provided passphrase is incorrect" in result.output)

    def test_unencrypted_key_with_passphrase_in_config(self):
        create_temp_private_key_file()
        result = self.invoke_example_operation(profile='TEMP_CONFIG_WITH_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("NotAuthenticated" in result.output)

    def test_prompt_for_passphrase_correct(self):
        create_temp_private_key_file(password=PASSPHRASE)
        oci_cli.cli_util.prompt_for_passphrase = passphrase_provider
        result = self.invoke_example_operation(profile='TEMP_CONFIG_NO_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("NotAuthenticated" in result.output)

    def test_prompt_for_passphrase_incorrect(self):
        create_temp_private_key_file(password="some other passphrase")
        oci_cli.cli_util.prompt_for_passphrase = passphrase_provider
        result = self.invoke_example_operation(profile='TEMP_CONFIG_NO_PASSPHRASE')
        self.assertNotEqual(0, result.exit_code)
        assert ("provided passphrase is incorrect" in result.output)

    def invoke_example_operation(self, profile='DEFAULT'):
        return self.runner.invoke(oci_cli.cli, ['--config-file', os.environ['OCI_CLI_CONFIG_FILE'], '--profile', profile, 'os', 'ns', 'get'])


if __name__ == '__main__':
    unittest.main()
