# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import unittest
from tests import test_config_container
from tests import util
import os
import oci_cli
import shutil

CASSETTE_LIBRARY_DIR = 'services/identity/tests/cassettes'
DEFAULT_DIRECTORY = os.path.join(os.path.expanduser('~'), '.oci')
DB_TOKEN_DIRECTORY = os.path.join(DEFAULT_DIRECTORY, 'db-token')


class TestIdentityDbToken(unittest.TestCase):

    @test_config_container.RecordReplay('identity', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_db_token_get_integ(self):
        PRIVATE_KEY_FILENAME = os.path.join(DB_TOKEN_DIRECTORY, 'oci_db_key.pem')
        PUBLIC_KEY_FILENAME = os.path.join(DB_TOKEN_DIRECTORY, 'oci_db_key_public.pem')
        TOKEN_FILENAME = os.path.join(DB_TOKEN_DIRECTORY, 'token')
        result = self.invoke(['db-token', 'get'])
        assert result.exit_code == 0
        assert "Private key written at" in result.output
        assert "oci_db_key.pem" in result.output
        assert "db-token written at:" in result.output
        assert "token" in result.output
        assert "db-token is valid until" in result.output
        assert os.path.isfile(PRIVATE_KEY_FILENAME)
        assert os.path.isfile(PUBLIC_KEY_FILENAME)
        assert os.path.isfile(TOKEN_FILENAME)
        assert self.validate_file_permissions(PRIVATE_KEY_FILENAME)
        assert self.validate_file_permissions(PUBLIC_KEY_FILENAME)
        assert self.validate_file_permissions(TOKEN_FILENAME)

        # Optional paramater
        alternate_dir = os.path.join(DEFAULT_DIRECTORY, 'custom')
        PRIVATE_KEY_FILENAME = os.path.join(alternate_dir, 'oci_db_key.pem')
        PUBLIC_KEY_FILENAME = os.path.join(alternate_dir, 'oci_db_key_public.pem')
        TOKEN_FILENAME = os.path.join(alternate_dir, 'token')
        result = self.invoke(['db-token', 'get', '--db-token-location', alternate_dir])
        assert result.exit_code == 0
        assert "Private key written at" in result.output
        assert "oci_db_key.pem" in result.output
        assert "db-token written at:" in result.output
        assert "token" in result.output
        assert "db-token is valid until" in result.output
        assert os.path.isfile(PRIVATE_KEY_FILENAME)
        assert os.path.isfile(PUBLIC_KEY_FILENAME)
        assert os.path.isfile(TOKEN_FILENAME)
        assert self.validate_file_permissions(PRIVATE_KEY_FILENAME)
        assert self.validate_file_permissions(PUBLIC_KEY_FILENAME)
        assert self.validate_file_permissions(TOKEN_FILENAME)

        # Negative case
        result = self.invoke(['db-token', 'get', '--scope', '11'])
        assert "scope must be a db scope" in result.output
        assert result.exit_code == 1

        # Clean up
        shutil.rmtree(DB_TOKEN_DIRECTORY)
        shutil.rmtree(alternate_dir)

    def invoke(self, params, debug=False, ** args):
        commands = ['iam'] + params

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)

    def validate_file_permissions(self, filename):
        with util.capture() as out:
            oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(filename)
            return 'WARNING' not in out
