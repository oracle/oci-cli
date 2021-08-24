# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestApplicationMigrationCLI(unittest.TestCase):
    def setUp(self):
        pass

    def check_non_existing_command(self, command, subcommand):
        usage_message = 'Usage: oci application-migration {} [OPTIONS] COMMAND [ARGS]...'.format(command)
        error_message = "Error: No such command '{}'.".format(subcommand)
        result = util.invoke_command(['application-migration', command, subcommand])

        # Deliberately testing independently rather than combine into one.
        assert usage_message in result.output
        assert error_message in result.output

    def test_create_migration_ics_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-jcs-discovery-details')

    def test_create_migration_jcs_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-jcs-discovery-details')

    def test_create_migration_oac_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-oac-discovery-details')

    def test_create_migration_oic_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-oic-discovery-details')

    def test_create_migration_pcs_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-pcs-discovery-details')

    def test_create_migration_soacs_discovery_details(self):
        self.check_non_existing_command('migration', 'create-migration-soacs-discovery-details')

    def test_update_migration_ics_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-jcs-discovery-details')

    def test_update_migration_jcs_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-jcs-discovery-details')

    def test_update_migration_oac_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-oac-discovery-details')

    def test_update_migration_oic_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-oic-discovery-details')

    def test_update_migration_pcs_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-pcs-discovery-details')

    def test_update_migration_soacs_discovery_details(self):
        self.check_non_existing_command('migration', 'update-migration-soacs-discovery-details')

    def test_create_source_internal_authorization_details(self):
        self.check_non_existing_command('source', 'create-source-internal-authorization-details')

    def test_create_source_internal_source_details(self):
        self.check_non_existing_command('source', 'create-source-internal-source-details')

    def test_create_source_ocic_authorization_details(self):
        self.check_non_existing_command('source', 'create-source-ocic-authorization-details')

    def test_create_source_ocic_source_details(self):
        self.check_non_existing_command('source', 'create-source-ocic-source-details')

    def test_update_source_internal_authorization_details(self):
        self.check_non_existing_command('source', 'update-source-internal-authorization-details')

    def test_update_source_internal_source_details(self):
        self.check_non_existing_command('source', 'update-source-internal-source-details')

    def test_update_source_ocic_authorization_details(self):
        self.check_non_existing_command('source', 'update-source-ocic-authorization-details')

    def test_update_source_ocic_source_details(self):
        self.check_non_existing_command('source', 'update-source-ocic-source-details')
