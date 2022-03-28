# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestDBCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'get-regional-wallet-metadata' in result.output
        assert 'get-autonomous-database-regional-wallet' not in result.output

    def test_get_regional_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate' in result.output
        assert 'update' not in result.output
        result = util.invoke_command(['db', 'autonomous-database-wallet', 'rotate'])
        assert 'Error: Missing option(s) --id' in result.output
        assert '--autonomous-database-id' not in result.output

    def test_update_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate' in result.output
        assert 'update' not in result.output
        result = util.invoke_command(['db', 'autonomous-database-wallet', 'rotate'])
        assert 'Error: Missing option(s) --id' in result.output
        assert '--autonomous-database-id' not in result.output

    def test_update_regional_wallet(self):
        result = util.invoke_command(['db', 'autonomous-database-wallet'])
        assert 'rotate-regional-wallet' in result.output
        assert 'update-autonomous-database-regional-wallet' not in result.output

    def test_delete_db_cloud_vm_cluster(self):
        result = util.invoke_command(['db', 'database', 'delete'])
        assert 'Error: Missing option(s) --database-id' in result.output

    def test_autonomous_database(self):
        result = util.invoke_command(['db', 'autonomous-database'])
        assert 'change-compartment' in result.output
        assert 'create' in result.output
        assert 'create-from-clone' in result.output
        assert 'data-safe' in result.output
        assert 'delete' in result.output
        assert 'generate-wallet' in result.output
        assert 'get' in result.output
        assert 'list' in result.output
        assert 'restore' in result.output
        assert 'start' in result.output
        assert 'stop' in result.output
        assert 'update' in result.output
        assert 'deregister-autonomous-database-data-safe' not in result.output
        assert 'register-autonomous-database-data-safe' not in result.output

    def test_autonomous_database_data_safe(self):
        result = util.invoke_command(['db', 'autonomous-database', 'data-safe'])
        assert 'register' in result.output
        assert 'deregister' in result.output
        result = util.invoke_command(['db', 'autonomous-database', 'data-safe', 'register'])
        assert 'Error: Missing option(s)' in result.output
        assert '--autonomous-database-id' in result.output
        result = util.invoke_command(['db', 'autonomous-database', 'data-safe', 'deregister'])
        assert 'Error: Missing option(s)' in result.output
        assert '--autonomous-database-id' in result.output

    def test_ocp_us_exadata_infrastructure(self):
        result = util.invoke_command(['db', 'ocp-us'])
        assert 'get-exadata-infrastructure-ocpus' not in result.output

    def test_exadata_infrastructure_ocpus(self):
        result = util.invoke_command(['db', 'exadata-infrastructure'])
        assert 'get-compute-units' in result.output
        result = util.invoke_command(['db', 'exadata-infrastructure', 'get-compute-units'])
        assert 'Error: Missing option(s)' in result.output
        assert '--autonomous-exadata-infrastructure-id' in result.output

    def test_update_vm_cluster(self):
        result = util.invoke_command(['db', 'vm-cluster', 'update'])
        assert 'version' not in result.output
        assert 'Error: Missing option(s)' in result.output
        assert '--vm-cluster-id' in result.output

    def test_patch_database(self):
        # Test by not providing mandatory args
        result = util.invoke_command(['db', 'database', 'patch'])
        assert 'Error: Missing option(s)' in result.output
        assert '--database-id' in result.output
        assert '--patch-id' not in result.output
        assert '--patch-action' not in result.output
        assert '--one-off-patches' not in result.output

        # Test by providing both RU and one-off patch, but missing database-id
        result = util.invoke_command(['db', 'database', 'patch', '--one-off-patches', 'oneOff', '--patch-id', 'patchId'])
        assert 'Error: Missing option(s)' in result.output
        assert '--database-id' in result.output

        # Test by not providing RU, one-off patch, or database-software-image-id which shall fail as none to patch provided
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId', '--one-off-patches', 'oneOff', '--patch-id', 'patchId'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId', '--one-off-patches', 'oneOff', '--patch-action', 'patchAction'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId', '--one-off-patches', 'oneOff', '--patch-id', 'patchId', '--patch-action', 'patchAction'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId', '--patch-action', 'patchAction'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output
        result = util.invoke_command(['db', 'database', 'patch', '--database-id', 'databaseId', '--patch-id', 'patchId'])
        assert 'Please specify one of the three options. 1. \'--one-off-patches\',  2. \'--database-software-image-id and --patch-action\' or 3. \'--patch-id and --patch-action\'.' in result.output

# Exacs new resource model

    def test_cloud_exa_infra(self):
        # create cloud exa infra
        result = util.invoke_command(['db', 'cloud-exa-infra', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--availability-domain' in result.output
        assert '--shape' in result.output
        assert '--display-name' in result.output
        # update cloud exa infra
        result = util.invoke_command(['db', 'cloud-exa-infra', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-exa-infra-id' in result.output
        assert '--cloud-exadata-infrastructure-id' not in result.output
        # delete cloud exa infra
        result = util.invoke_command(['db', 'cloud-exa-infra', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-exa-infra-id' in result.output
        assert '--cloud-exadata-infrastructure-id' not in result.output
        # change cloud exa infra compartment
        result = util.invoke_command(['db', 'cloud-exa-infra', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-exa-infra-id' in result.output
        assert '--compartment-id' in result.output
        assert '--cloud-exadata-infrastructure-id' not in result.output
        # get cloud exa infra
        result = util.invoke_command(['db', 'cloud-exa-infra', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-exa-infra-id' in result.output
        assert '--cloud-exadata-infrastructure-id' not in result.output
        # list cloud exa infras
        result = util.invoke_command(['db', 'cloud-exa-infra', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_cloud_vm_cluster(self):
        # create cloud vm cluster
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'create'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        assert '--cloud-exa-infra-id' in result.output
        assert '--cloud-exadata-infrastructure-id' not in result.output
        assert '--subnet-id' in result.output
        assert '--backup-subnet-id' in result.output
        assert '--cpu-core-count' in result.output
        assert '--gi-version' in result.output
        assert 'ssh-authorized-keys-file' in result.output
        assert 'ssh-public-keys' not in result.output
        assert '--display-name' in result.output
        assert '--hostname' in result.output
        # update cloud vm cluster
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # delete cloud vm cluster
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # change cloud vm cluster compartment
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        assert '--compartment-id' in result.output
        # get cloud vm cluster
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # list cloud vm clusters
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output
        # get cloud vm cluster iorm config
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'get-exadata-iorm-config'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # update cloud vm cluster iorm config
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'update-exadata-iorm-config'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # get update
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'get-update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        assert '--update-id' in result.output
        # list updates
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'list-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        # get update history
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'get-update-history'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output
        assert '--update-history-entry-id' in result.output
        # get update history entries
        result = util.invoke_command(['db', 'cloud-vm-cluster', 'list-update-histories'])
        assert 'Error: Missing option(s)' in result.output
        assert '--cloud-vm-cluster-id' in result.output

    def test_switch_exa_db_system(self):
        # switch exadata db system
        result = util.invoke_command(['db', 'system', 'switch'])
        assert 'Error: Missing option(s)' in result.output
        assert '--db-system-id' in result.output

    def test_create_db_home_irestore_vm_cluster(self):
        result = util.invoke_command(['db', 'db-home', 'create'])
        assert 'Missing a required parameter' in result.output
        assert '--db-system-id' in result.output
        assert '--vm-cluster-id' in result.output

    def test_create_db_irestore_vm_cluster(self):
        result = util.invoke_command(['db', 'database', 'create-from-backup'])
        assert 'Error: Missing option(s)' in result.output
        assert '--admin-password' in result.output
        assert '--backup-id' in result.output

        result = util.invoke_command(['db', 'database', 'create-from-backup', '--admin-password', 'password', '--backup-id', 'backupId'])
        assert 'Missing a required parameter' in result.output
        assert '--db-system-id' in result.output
        assert '--vm-cluster-id' in result.output

    def test_list_db_flex_component(self):
        result = util.invoke_command(['db', 'flex-component', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--compartment-id' in result.output

    def test_list_backups(self):
        result = util.invoke_command(['db', 'backup', 'list'])
        assert 'UsageError' in result.output
        assert '--compartment-id or --database-id must be provided' in result.output

        result = util.invoke_command(['db', 'backup', 'list', '--database-id', 'databaseId', '--compartment-id', 'compartmentId'])
        assert 'UsageError' in result.output
        assert 'You can only specify one of either' in result.output
        assert '--compartment-id or --database-id option' in result.output
