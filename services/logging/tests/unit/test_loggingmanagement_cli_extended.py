# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestLoggingManagementCliExtend(unittest.TestCase):
    def setUp(self):
        pass

    # test command change_log_log_group override by change-log-group
    # from
    #   oci logging log change_log_log_group ...
    # to
    #   oci logging log change_log_group ...

    def test_log_change_log_group(self):
        result = util.invoke_command(['logging', 'log', 'change_log_log_group'])
        assert "No such command 'change_log_log_group'" in result.output

        result = util.invoke_command(['logging', 'log', 'change-log-group'])
        assert 'Error: Missing option(s)' in result.output

    # from
    #   oci logging log-group list ... --is-compartment-id-in-subtree ...
    # to
    #   oci logging log-group list ... --compartmentidinsubtree ...

    def test_log_group_list(self):
        result = util.invoke_command(['logging', 'log-group', 'list', '--is-compartment-id-in-subtree', 'false'])
        assert 'no such option: --is-compartment-id-in-subtree' in result.output

        result = util.invoke_command(['logging', 'log-group', 'list', '--compartmentidinsubtree'])
        assert 'requires an argument' in result.output

    # from
    #   oci logging log-saved-search create ... --query-parameterconflict ...
    # to
    #   oci logging log-saved-search create ... --log-query ...

    def test_log_saved_search_create(self):
        result = util.invoke_command(['logging', 'log-saved-search', 'create', '--query-parameterconflict', 'sampleQuery'])
        assert 'no such option: --query-parameterconflict' in result.output

        result = util.invoke_command(['logging', 'log-saved-search', 'create', '--log-query'])
        assert 'requires an argument' in result.output

    # from
    #   oci logging log-saved-search update ... --query-parameterconflict ...
    # to
    #   oci logging log-saved-search update ... --log-query ...

    def test_log_saved_search_update(self):
        result = util.invoke_command(['logging', 'log-saved-search', 'update', '--query-parameterconflict', 'sampleQuery'])
        assert 'no such option: --query-parameterconflict' in result.output

        result = util.invoke_command(['logging', 'log-saved-search', 'update', '--log-query'])
        assert 'requires an argument' in result.output

    # from
    #   oci logging unified-agent-configuration change-compartment --unified-agent-configuration-id ...
    # to
    #   oci logging agent-configuration change-compartment --config-id ...

    def test_unified_agent_configuration_change_compartment(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'change-compartment', '--unified-agent-configuration-id', 'sampleId'])
        assert 'no such option: --unified-agent-configuration-id' in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'change-compartment', '--config-id'])
        assert 'requires an argument' in result.output

    # from
    #   oci logging unified-agent-configuration create --compartment-id ...
    # to
    #   oci logging agent-configuration create --compartment-id ...

    def test_agent_configuration_create(self):
        result = util.invoke_command(['logging', 'unified-agent-configurationn', 'create'])
        assert "No such command 'unified-agent-configurationn'" in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'create'])
        assert 'Error: Missing option(s)' in result.output

    # from
    #   oci logging unified-agent-configuration create-unified-agent-configuration-unified-agent-logging-configuration
    #       --service-configuration-destination, --service-configuration-sources ...
    # to
    #   oci logging agent-configuration create-log-configuration
    #       --service-conf-destination, --service-conf-sources ...

    def test_create_unified_agent_logging_configuration(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'create-unified-agent-configuration-unified-agent-logging-configuration'])
        assert "No such command 'create-unified-agent-configuration-unified-agent-logging-configuration'" in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'create-log-configuration', '--service-conf-destination', 'sampleDestination', '--service-conf-sources'])
        assert 'requires an argument' in result.output

    # from
    #   oci logging unified-agent-configuration update-unified-agent-configuration-unified-agent-logging-configuration
    #       --service-configuration-destination, --service-configuration-sources, --unified-agent-configuration-id ...
    # to
    #   oci logging agent-configuration create-log-configuration
    #       --service-conf-destination, --service-conf-sources, --config-id ..

    def test_update_unified_agent_logging_configuration(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'update-unified-agent-configuration-unified-agent-logging-configuration'])
        assert "No such command 'update-unified-agent-configuration-unified-agent-logging-configuration'" in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'update-log-configuration', '--service-conf-destination', 'sampleDestination', '--service-conf-sources', 'sampleSource', '--config-id'])
        assert 'requires an argument' in result.output

    # from
    #  oci logging unified-agent-configuration delete --unified-agent-configuration-id
    # to
    #   oci logging agent-configuration delete --config-id

    def test_agent_configuration_delete(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'delete', '--unified-agent-configuration-id', 'sampleId'])
        assert 'no such option: --unified-agent-configuration-id' in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'delete', '--config-id'])
        assert 'requires an argument' in result.output

    # from
    #  oci logging unified-agent-configuration get --unified-agent-configuration-id
    # to
    #   oci logging agent-configuration get --config-id

    def test_agent_configuration_get(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'get', '--cunified-agent-configuration-id', 'sampleId'])
        assert 'no such option: --cunified-agent-configuration-id' in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'get', '--config-id'])
        assert 'requires an argument' in result.output

    # from
    #  oci logging unified-agent-configuration update --unified-agent-configuration-id
    # to
    #   oci logging agent-configuration update --config-id

    def test_agent_configuration_update(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'update', '--unified-agent-configuration-id', 'sampleId'])
        assert 'no such option: --unified-agent-configuration-id' in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'update', '--config-id'])
        assert 'requires an argument' in result.output

    # from
    #  oci logging unified-agent-configuration list --is-compartment-id-in-subtree ...
    # to
    #   oci logging agent-configuration list --compartmentidinsubtree

    def test_agent_configuration_list(self):
        result = util.invoke_command(['logging', 'agent-configuration', 'list', '--is-compartment-id-in-subtree', 'false'])
        assert 'no such option: --is-compartment-id-in-subtree' in result.output

        result = util.invoke_command(['logging', 'agent-configuration', 'list', '--compartmentidinsubtree'])
        assert 'requires an argument' in result.output
