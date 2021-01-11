# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest
import unittest
from tests import test_config_container
from tests import util
from tests.test_list_filter import retrieve_list_by_field_and_check, retrieve_list_and_ensure_sorted
import services.core.src.oci_cli_virtual_network as oci_cli_virtual_network

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


class TestVirtualNetwork(unittest.TestCase):

    @util.slow
    def test_all_operations(self):
        """Successfully calls every operation with basic options. The exceptions are 'vnic get' and 'vnic update', which are tested
        in test_compute.py since they require an instance.

        We also have exceptions for private-ip get/update/delete/list and attaching and detaching private IPs from VNICs, as
        these are handlde in test_secondary_private_ip.py"""
        with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('virtual_network.yml'):
            try:
                self.subtest_vcn_operations()
                self.subtest_security_list_operations()
                self.subtest_security_list_stateless_rules()
                self.subtest_subnet_operations()
                self.subtest_internet_gateway_operations()
                self.subtest_cpe_operations()
                self.subtest_dhcp_option_operations()
                self.subtest_drg_operations()
                self.subtest_drg_attachment_operations()
                self.subtest_ip_sec_connection_operations()
                self.subtest_route_table_operations()

                if hasattr(self, 'drg_capacity_issue'):
                    pytest.skip('Skipped DRG tests due to capacity issues')
            finally:
                util.vcr_mode_aware_sleep(20)
                self.subtest_delete()

    @util.log_test
    def subtest_vcn_operations(self):
        vcn_name = util.random_name('cli_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = self.invoke(
            ['vcn', 'create', '--compartment-id', util.COMPARTMENT_ID, '--display-name', vcn_name, '--cidr-block', cidr_block, '--dns-label', vcn_dns_label])
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        result = self.invoke(['vcn', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        vcn_name = vcn_name + "_updated"
        result = self.invoke(['vcn', 'update', '--vcn-id', self.vcn_ocid, '--display-name', vcn_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['vcn', 'get', '--vcn-id', self.vcn_ocid])
        util.validate_response(result, expect_etag=True)

        vcn_response = json.loads(result.output)

        assert vcn_response['data']['dns-label'] == vcn_dns_label

    @util.log_test
    def subtest_security_list_operations(self):
        sl_name = util.random_name('cli_test_security_list')
        egress_rules = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_security_list_egress_security_rules_example)
        ingress_rules = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_security_list_ingress_security_rules_example)

        result = self.invoke(
            ['security-list', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', sl_name,
             '--vcn-id', self.vcn_ocid,
             '--egress-security-rules', egress_rules,
             '--ingress-security-rules', ingress_rules
             ])
        self.sl_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'security-list', 'get', '--security-list-id', self.sl_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        result = self.invoke(
            ['security-list', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid])
        util.validate_response(result)

        self.run_list_filter_verification('security-list', sl_name)

        result = self.invoke(['security-list', 'get', '--security-list-id', self.sl_ocid])
        util.validate_response(result, expect_etag=True)

        sl_name = sl_name + "_updated"
        egress_rules_v2 = """[{"destination": "10.0.2.0/24", "protocol": "6", "tcpOptions": {"destinationPortRange": {"max": 1522, "min": 1522}}}]"""
        ingress_rules_v2 = """[{"protocol": "6", "source": "10.0.1.0/25", "tcpOptions": {"destinationPortRange": {"max": 1521, "min": 1521}}}]"""

        # TODO: A short sleep before every security list update to allow for replication.
        util.vcr_mode_aware_sleep(20)

        # Force update on all fields
        result = self.invoke(['security-list', 'update',
                              '--security-list-id', self.sl_ocid,
                              '--display-name', sl_name,
                              '--egress-security-rules', egress_rules,
                              '--ingress-security-rules', ingress_rules,
                              '--force'])
        util.validate_response(result, expect_etag=True)

        util.vcr_mode_aware_sleep(20)

        # update display name only - does not show a prompt
        result = self.invoke(['security-list', 'update', '--security-list-id', self.sl_ocid, '--display-name', sl_name])
        util.validate_response(result, expect_etag=True)

        util.vcr_mode_aware_sleep(20)

        # update egress-rules, confirm y
        result = self.invoke(['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules', egress_rules_v2], input='y')
        util.validate_response(result, json_response_expected=False)

        util.vcr_mode_aware_sleep(20)

        # update ingress-rules, confirm y
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--ingress-security-rules', ingress_rules_v2], input='y')
        util.validate_response(result, json_response_expected=False)

        util.vcr_mode_aware_sleep(20)

        # update both, confirm y
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--ingress-security-rules',
             ingress_rules, '--egress-security-rules', egress_rules], input='y')
        util.validate_response(result, json_response_expected=False)

        util.vcr_mode_aware_sleep(20)

        # update egress-rules, confirm n
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules', egress_rules_v2],
            input='n')
        assert result.exit_code != 0

        # update egress-rules, force
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules', egress_rules_v2, '--force'])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_security_list_stateless_rules(self):

        util.vcr_mode_aware_sleep(10)

        stateless_egress_rule = """[{"destination": "10.0.2.0/24", "protocol": "6", "tcpOptions": {"destinationPortRange": {"max": 2, "min": 1}}, "isStateless":"true"}]"""
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules', stateless_egress_rule,
             '--force'])
        util.validate_response(result, expect_etag=True)
        assert json.loads(result.output)["data"]["egress-security-rules"][0]["is-stateless"] is True

        util.vcr_mode_aware_sleep(20)

        explicit_stateful_egress_rule = """[{"destination": "10.0.2.0/24", "protocol": "6", "tcpOptions": {"destinationPortRange": {"max": 2, "min": 1}}, "isStateless":"false"}]"""
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules',
             explicit_stateful_egress_rule,
             '--force'])
        util.validate_response(result, expect_etag=True)
        assert json.loads(result.output)["data"]["egress-security-rules"][0]["is-stateless"] is False

        util.vcr_mode_aware_sleep(20)

        implicit_stateful_egress_rule = """[{"destination": "10.0.2.0/24", "protocol": "17", "udpOptions": {"destinationPortRange": {"max": 2, "min": 1}, "sourcePortRange": {"max": 4, "min": 3}}}]"""
        result = self.invoke(
            ['security-list', 'update', '--security-list-id', self.sl_ocid, '--egress-security-rules',
             implicit_stateful_egress_rule,
             '--force'])
        util.validate_response(result, expect_etag=True)
        assert json.loads(result.output)["data"]["egress-security-rules"][0]["is-stateless"] is None

    @util.log_test
    def subtest_subnet_operations(self):
        subnet_name = util.random_name('cli_test_subnet')
        cidr_block = "10.0.0.0/16"
        security_list_ids = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_subnet_security_list_ids_example.format(sl_id=self.sl_ocid))
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        result = self.invoke(
            ['subnet', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', subnet_name,
             '--vcn-id', self.vcn_ocid,
             '--cidr-block', cidr_block,
             '--security-list-ids', security_list_ids,
             '--dns-label', subnet_dns_label
             ])

        self.subnet_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        result = self.invoke(['subnet', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid])
        util.validate_response(result)

        self.run_list_filter_verification('subnet', subnet_name)

        subnet_name = subnet_name + "_updated"
        result = self.invoke(['subnet', 'update', '--subnet-id', self.subnet_ocid, '--display-name', subnet_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['subnet', 'get', '--subnet-id', self.subnet_ocid])
        util.validate_response(result, expect_etag=True)

        subnet_response = json.loads(result.output)

        assert subnet_response['data']['dns-label'] == subnet_dns_label

    @util.log_test
    def subtest_internet_gateway_operations(self):
        ig_name = util.random_name('cli_test_ig')

        result = self.invoke(
            ['internet-gateway', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--is-enabled', "False",
             '--display-name', ig_name,
             '--vcn-id', self.vcn_ocid
             ])
        self.ig_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'internet-gateway', 'get', '--ig-id', self.ig_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        result = self.invoke(['internet-gateway', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid])
        util.validate_response(result)

        self.run_list_filter_verification('internet-gateway', ig_name)

        ig_name = ig_name + "_updated"
        result = self.invoke(['internet-gateway', 'update', '--ig-id', self.ig_ocid, '--display-name', ig_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['internet-gateway', 'get', '--ig-id', self.ig_ocid])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_cpe_operations(self):
        cpe_name = util.random_name('cli_test_cpe')
        ip_address = "137.254.4.11"

        result = self.invoke(
            ['cpe', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', cpe_name,
             '--ip-address', ip_address,
             ])
        self.cpe_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['cpe', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        cpe_name = cpe_name + "_updated"
        result = self.invoke(['cpe', 'update', '--cpe-id', self.cpe_ocid, '--display-name', cpe_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['cpe', 'get', '--cpe-id', self.cpe_ocid])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_dhcp_option_operations(self):
        dhcp_options_name = util.random_name('cli_test_dhcp_options')
        options = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_dhcp_options_options_example)

        result = self.invoke(
            ['dhcp-options', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--vcn-id', self.vcn_ocid,
             '--display-name', dhcp_options_name,
             '--options', options
             ])
        util.validate_response(result, expect_etag=True)
        self.dhcp_options_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'dhcp-options', 'get', '--dhcp-id', self.dhcp_options_ocid], 'AVAILABLE')

        result = self.invoke(['dhcp-options', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid])
        util.validate_response(result)

        self.run_list_filter_verification('dhcp-options', dhcp_options_name)

        result = self.invoke(['dhcp-options', 'get', '--dhcp-id', self.dhcp_options_ocid])
        util.validate_response(result, expect_etag=True)

        dhcp_options_name = dhcp_options_name + "_updated"
        options_v2 = """[{"type": "DomainNameServer", "customDnsServers": ["202.44.61.10"], "serverType": "CustomDnsServer"},
            {"searchDomainNames": ["testvcn.oraclevcn.com"], "type":"SearchDomain"}]"""

        # update display name only - does not show a confirmation prompt
        result = self.invoke(['dhcp-options', 'update', '--dhcp-id', self.dhcp_options_ocid, '--display-name', dhcp_options_name])
        util.validate_response(result, expect_etag=True)

        # update options, confirm y
        result = self.invoke(
            ['dhcp-options', 'update', '--dhcp-id', self.dhcp_options_ocid, '--options', options_v2], input='y')
        util.validate_response(result, json_response_expected=False)

        # update options, confirm n
        result = self.invoke(
            ['dhcp-options', 'update', '--dhcp-id', self.dhcp_options_ocid, '--options', options], input='n')
        assert result.exit_code != 0

        util.vcr_mode_aware_sleep(20)

        # update options, force
        result = self.invoke(
            ['dhcp-options', 'update', '--dhcp-id', self.dhcp_options_ocid, '--options', options_v2, '--force'])

        util.validate_response(result, expect_etag=True)

        response = json.loads(result.output)

        # validate response contains SearchDomain option
        response_has_search_domain_option = False
        for option in response["data"]["options"]:
            if option["type"] == "SearchDomain":
                response_has_search_domain_option = True
                assert option["search-domain-names"][0] == "testvcn.oraclevcn.com"

        assert response_has_search_domain_option, "Options response should contain option of type 'SearchDomain'."

    @util.log_test
    def subtest_drg_operations(self):
        drg_name = util.random_name('cli_test_drg')

        result = self.invoke(
            ['drg', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', drg_name
             ])

        # If we have hit a limit, skip the test
        if 'Limit vcn-tenant-drg' in result.output or 'Limit tenant-drg' in result.output:
            self.drg_capacity_issue = True
            print('Unable to execute subtest_drg_operations as a DRG is not available')
            return

        self.drg_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'drg', 'get', '--drg-id', self.drg_ocid], 'AVAILABLE',
                        max_wait_seconds=600)

        result = self.invoke(['drg', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        drg_name = drg_name + "_updated"
        result = self.invoke(['drg', 'update', '--drg-id', self.drg_ocid, '--display-name', drg_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['drg', 'get', '--drg-id', self.drg_ocid])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_drg_attachment_operations(self):
        if hasattr(self, 'drg_capacity_issue'):
            print('Unable to execute subtest_drg_attachment_operations as a DRG is not available')
            return

        drg_attachment_name = util.random_name('cli_test_drg_attachment')

        result = self.invoke(
            ['drg-attachment', 'create',
             '--drg-id', self.drg_ocid,
             '--vcn-id', self.vcn_ocid,
             '--display-name', drg_attachment_name
             ])
        self.drg_attachment_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'drg-attachment', 'get', '--drg-attachment-id', self.drg_attachment_ocid], 'ATTACHED')

        result = self.invoke(['drg-attachment', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        drg_attachment_name = drg_attachment_name + "_updated"
        result = self.invoke(['drg-attachment', 'update', '--drg-attachment-id', self.drg_attachment_ocid, '--display-name', drg_attachment_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['drg-attachment', 'get', '--drg-attachment-id', self.drg_attachment_ocid])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_ip_sec_connection_operations(self):
        if hasattr(self, 'drg_capacity_issue'):
            print('Unable to execute subtest_ip_sec_connection_operations as a DRG is not available')
            return

        ipsc_name = util.random_name('cli_test_ipsc')
        routes = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_ip_sec_connection_static_routes_example)

        result = self.invoke(
            ['ip-sec-connection', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', ipsc_name,
             '--cpe-id', self.cpe_ocid,
             '--drg-id', self.drg_ocid,
             '--static-routes', routes
             ])
        if 'Limit tenant-ipsec-vpn-connection' in result.output:
            self.drg_capacity_issue = True
            print('Unable to execute subtest_ip_sec_connection_operations as an IPSec Connection is not available')
            return

        self.ipsc_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)
        util.wait_until(['network', 'ip-sec-connection', 'get', '--ipsc-id', self.ipsc_ocid], 'AVAILABLE',
                        max_wait_seconds=600)

        result = self.invoke(['ip-sec-connection', 'list', '--compartment-id', util.COMPARTMENT_ID])
        util.validate_response(result)

        ipsc_name = ipsc_name + "_updated"
        result = self.invoke(['ip-sec-connection', 'update', '--ipsc-id', self.ipsc_ocid, '--display-name', ipsc_name])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['ip-sec-connection', 'get', '--ipsc-id', self.ipsc_ocid])
        util.validate_response(result, expect_etag=True)

        result = self.invoke(['ip-sec-connection', 'get-config', '--ipsc-id', self.ipsc_ocid])
        util.validate_response(result)

        result = self.invoke(['ip-sec-connection', 'get-status', '--ipsc-id', self.ipsc_ocid])
        util.validate_response(result)

    @util.log_test
    def subtest_route_table_operations(self):
        rt_name = util.random_name('cli_test_route_table')
        rules = util.remove_outer_quotes(oci_cli_virtual_network.virtualnetwork_cli_extended.network_create_route_table_route_rules_example.format(ig_id=self.ig_ocid))

        result = self.invoke(
            ['route-table', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', rt_name,
             '--vcn-id', self.vcn_ocid,
             '--route-rules', rules
             ])
        self.rt_ocid = util.find_id_in_response(result.output)
        util.validate_response(result, expect_etag=True)

        util.wait_until(['network', 'route-table', 'get', '--rt-id', self.rt_ocid], 'AVAILABLE',
                        max_wait_seconds=300)

        result = self.invoke(['route-table', 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid])
        util.validate_response(result)

        self.run_list_filter_verification('route-table', rt_name)

        result = self.invoke(['route-table', 'get', '--rt-id', self.rt_ocid])
        util.validate_response(result, expect_etag=True)

        rt_name = rt_name + "_updated"
        rules_v2 = """[{{"cidrBlock":"0.0.0.0/1","networkEntityId":"{ig_id}"}}]""".format(ig_id=self.ig_ocid)

        # update display name only - does not show a prompt
        result = self.invoke(['route-table', 'update', '--rt-id', self.rt_ocid, '--display-name', rt_name])
        util.validate_response(result, expect_etag=True)

        util.vcr_mode_aware_sleep(20)

        # update route-rules, confirm y
        result = self.invoke(
            ['route-table', 'update', '--rt-id', self.rt_ocid, '--route-rules', rules_v2], input='y')
        util.validate_response(result, json_response_expected=False)

        # update route-rules, confirm n
        result = self.invoke(
            ['route-table', 'update', '--rt-id', self.rt_ocid, '--route-rules', rules_v2], input='n')
        assert result.exit_code != 0

        util.vcr_mode_aware_sleep(20)

        # update route-rules, force
        result = self.invoke(
            ['route-table', 'update', '--rt-id', self.rt_ocid, '--route-rules', rules, '--force'])
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_delete(self):
        error_count = 0

        if hasattr(self, 'rt_ocid'):
            max_retry = 3
            retry = 0
            try:
                while retry < max_retry:
                    try:
                        util.vcr_mode_aware_sleep(2)
                        result = self.invoke(['route-table', 'delete', '--rt-id', self.rt_ocid, '--force'])
                        util.validate_response(result)
                        break
                    except Exception as error:
                        # if the route-table no longer exists then don't try to delete it again
                        if '"status": 404' in result.output:
                            break
                        else:
                            retry += 1
                            print("Retrying route-table delete.")

                util.wait_until(['network', 'route-table', 'get', '--rt-id', self.rt_ocid], 'TERMINATED', succeed_if_not_found=True, max_wait_seconds=300)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'ipsc_ocid'):
            try:
                result = self.invoke(['ip-sec-connection', 'delete', '--ipsc-id', self.ipsc_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'ip-sec-connection', 'get', '--ipsc-id', self.ipsc_ocid], 'TERMINATED', succeed_if_not_found=True, max_wait_seconds=300)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'drg_attachment_ocid'):
            try:
                result = self.invoke(['drg-attachment', 'delete', '--drg-attachment-id', self.drg_attachment_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'drg-attachment', 'get', '--drg-attachment-id', self.drg_attachment_ocid], 'DETACHED', succeed_if_not_found=True, max_wait_seconds=600)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'drg_ocid'):
            try:
                result = self.invoke(['drg', 'delete', '--drg-id', self.drg_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'drg', 'get', '--drg-id', self.drg_ocid], 'TERMINATED', succeed_if_not_found=True, max_wait_seconds=600)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'dhcp_options_ocid'):
            try:
                result = self.invoke(['dhcp-options', 'delete', '--dhcp-id', self.dhcp_options_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'dhcp-options', 'get', '--dhcp-id', self.dhcp_options_ocid], 'TERMINATED', succeed_if_not_found=True, max_wait_seconds=600)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'cpe_ocid'):
            try:
                result = self.invoke(['cpe', 'delete', '--cpe-id', self.cpe_ocid, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'ig_ocid'):
            try:
                result = self.invoke(['internet-gateway', 'delete', '--ig-id', self.ig_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'internet-gateway', 'get', '--ig-id', self.ig_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                result = self.invoke(['subnet', 'delete', '--subnet-id', self.subnet_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'sl_ocid'):
            try:
                result = self.invoke(['security-list', 'delete', '--security-list-id', self.sl_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'security-list', 'get', '--security-list-id', self.sl_ocid], 'TERMINATED', succeed_if_not_found=True, max_wait_seconds=300)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                result = self.invoke(['vcn', 'delete', '--vcn-id', self.vcn_ocid, '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        self.assertEquals(0, error_count)

    def invoke(self, params, debug=False, ** args):
        commands = ['network'] + params

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)

    def run_list_filter_verification(self, virtual_network_subgroup_name, display_name):
        retrieve_list_by_field_and_check(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--display-name', display_name, '--all'],
            'display-name',
            display_name,
            match_at_least_one=True
        )
        retrieve_list_by_field_and_check(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--lifecycle-state', 'AVAILABLE', '--all'],
            'lifecycle-state',
            'AVAILABLE',
            match_at_least_one=True
        )

        retrieve_list_and_ensure_sorted(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--sort-by', 'DISPLAYNAME', '--sort-order', 'asc', '--all'],
            'display-name',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--sort-by', 'DISPLAYNAME', '--sort-order', 'desc', '--all'],
            'display-name',
            'desc'
        )

        retrieve_list_and_ensure_sorted(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--sort-by', 'TIMECREATED', '--sort-order', 'asc', '--all'],
            'time-created',
            'asc'
        )
        retrieve_list_and_ensure_sorted(
            ['network', virtual_network_subgroup_name, 'list', '--compartment-id', util.COMPARTMENT_ID, '--vcn-id', self.vcn_ocid, '--sort-by', 'TIMECREATED', '--sort-order', 'desc', '--all'],
            'time-created',
            'desc'
        )


if __name__ == '__main__':
    unittest.main()
