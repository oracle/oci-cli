# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import zipfile
import json
import re
import sys
import click
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import ITEMS, STATUS, \
    PHASE, VALID_CRDS_LIST, WEBHOOKS_LIST, IssueType, TROUBLESHOOT_DICT, OPERATOR_SERVICES_LIST, REPORT, CSV, PENDING, \
    SUCCEEDED, PROXY_VERSION, DYNAMIC_VERSION, OLM_VERSION
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.event import EventType

'''
Parse the report and bundle to analyze and provide required help to troubleshoot issues in mesh setup.
'''


class BundleAnalyser:

    def __init__(self, bundle_file_path, sdk_client=None):
        self.bundle_file_path = bundle_file_path + ".zip"
        self.sdk_client = sdk_client
        self.csv_json_contents = None
        self.report_json_contents = None
        self.report_json = None
        self.csv_json = None

    def load_contents(self):
        # load contents of report and csv file for analyzing
        bundle = zipfile.ZipFile(self.bundle_file_path, 'r')
        for filename in bundle.namelist():
            if re.search(CSV, filename):
                self.csv_json = bundle.open(filename, 'r')
                self.csv_json_contents = json.loads(self.csv_json.read())
            if re.search(REPORT, filename):
                self.report_json = bundle.open(filename, 'r')
                self.report_json_contents = json.loads(self.report_json.read())

    # OLM should be version in constant
    def validate_olm_version(self):
        OLM = EventType.OLM.value.lower()
        if OLM in self.report_json_contents:
            olm = self.report_json_contents[OLM]
            if olm is not None:
                olm_version = olm["version"]
                if olm_version == OLM_VERSION:
                    click.echo('\nOLM version: {}'.format(olm_version), file=sys.stdout)
                else:
                    click.echo(IssueType.INCOMPATIBLE_OLM_VERSION.describe())
                    click.echo("Refer - " + TROUBLESHOOT_DICT[IssueType.INCOMPATIBLE_OLM_VERSION])

    def validate_csv_status(self):
        if self.csv_json_contents is not None and ITEMS in self.csv_json_contents and len(
                self.csv_json_contents[ITEMS]) > 0:
            csv = self.csv_json_contents[ITEMS][0]
            if STATUS in csv and PHASE in csv[STATUS]:
                csv_status = csv[STATUS][PHASE]
                if csv_status == PENDING:
                    click.echo(IssueType.CSV_STATUS_NOT_SUCCEEDED.describe())
                    click.echo(TROUBLESHOOT_DICT[IssueType.CSV_STATUS_NOT_SUCCEEDED])
                elif csv_status == SUCCEEDED:
                    click.echo('\nCSV status: {}'.format(csv_status), file=sys.stdout)

    def config_version_summary(self):
        POD_SUMMARY = EventType.POD_SUMMARY.value.lower()
        if POD_SUMMARY in self.report_json_contents:
            pods_summary = self.report_json_contents[POD_SUMMARY]

            config_version_stats = {}
            if pods_summary is not None:
                for pod_summary in pods_summary:
                    config_version_stats.setdefault(pod_summary[DYNAMIC_VERSION], 0)
                    config_version_stats[pod_summary[DYNAMIC_VERSION]] += 1
                click.echo("\n|{:^20}|".format("Config Versions"))
                click.echo("|{:^10} | {:^10}|".format("Version", "Count"))
                for version, count in config_version_stats.items():
                    click.echo("|{:^10} | {:^10}|".format(version, str(count)))
                    if len(config_version_stats) > 1:
                        click.echo(IssueType.INCOMPATIBLE_VERSIONS.describe())
                        click.echo(TROUBLESHOOT_DICT[IssueType.INCOMPATIBLE_VERSIONS])
                    elif len(config_version_stats) == 1:
                        click.echo("All  configs are of the same version")

    def validate_proxy_and_sidecar_version(self):
        POD_SUMMARY = EventType.POD_SUMMARY.value.lower()
        if POD_SUMMARY in self.report_json_contents:
            pods_summary = self.report_json_contents[POD_SUMMARY]
            version_stats = {}
            if pods_summary is not None:
                for pod_summary in pods_summary:
                    version_stats.setdefault(pod_summary[PROXY_VERSION], 0)
                    version_stats[pod_summary[PROXY_VERSION]] += 1

                click.echo("\n|{:^30}|".format("Sidecar Image Versions"))
                click.echo("|{:^15} | {:^15}|".format("Version", "Count"))

                for version, count in version_stats.items():
                    click.echo("|{:^15} | {:^15}|".format(version, str(count)))
                if len(version_stats) > 1:
                    click.echo(IssueType.MULTIPLE_SIDECAR_VERSIONS.describe())
                    click.echo(TROUBLESHOOT_DICT[IssueType.MULTIPLE_SIDECAR_VERSIONS])
                elif len(version_stats) == 1:
                    click.echo("All sidecars are using same version")

    def operator_services(self):
        OPERATOR_SERVICES = EventType.OPERATOR_SERVICES.value.lower()
        if OPERATOR_SERVICES in self.report_json_contents:
            services_list = self.report_json_contents[OPERATOR_SERVICES]
            missing_services = list(set(services_list) ^ set(OPERATOR_SERVICES_LIST))
            if len(missing_services) > 0:
                click.echo(IssueType.MISSING_OPERATOR_SERVICES.describe())
                click.echo('\nServices not found: {}'.format(missing_services), file=sys.stdout)
                click.echo(TROUBLESHOOT_DICT[IssueType.MISSING_OPERATOR_SERVICES])
            else:
                click.echo('\nAll Operator Services are installed')

    def validate_crds(self):
        SERVICE_MESH_CRDS = EventType.SERVICE_MESH_CRDS.value.lower()
        if SERVICE_MESH_CRDS in self.report_json_contents:
            crds_list = self.report_json_contents[SERVICE_MESH_CRDS]
            missing_crds = list(set(crds_list) ^ set(VALID_CRDS_LIST))
            if len(missing_crds) > 0:
                click.echo(IssueType.MISSING_MESH_CRDS.describe())
                click.echo('\nCRDs not found: {}'.format(missing_crds), file=sys.stdout)
                click.echo(TROUBLESHOOT_DICT[IssueType.MISSING_MESH_CRDS])
            else:
                click.echo('\nAll Mesh Custom Resources are installed')

    def validate_webhooks(self):
        SERVICE_MESH_WEBHOOKS = EventType.SERVICE_MESH_WEBHOOKS.value.lower()
        if SERVICE_MESH_WEBHOOKS in self.report_json_contents:
            webhooks_list = self.report_json_contents[SERVICE_MESH_WEBHOOKS]
            missing_webhooks = list(set(webhooks_list) ^ set(WEBHOOKS_LIST))
            if len(missing_webhooks) > 0:
                click.echo(IssueType.MISSING_MESH_WEBHOOKS.describe())
                click.echo('\nWebhooks not found: {}'.format(missing_webhooks), file=sys.stdout)
                click.echo(TROUBLESHOOT_DICT[IssueType.MISSING_MESH_WEBHOOKS])

            else:
                click.echo('\nAll Mesh Webhooks are installed')

    def analyze(self):
        # load contents of report and csv file for analyzing
        self.load_contents()
        # Parse the report and echo suggestions
        click.echo("=============================== Mesh Report Analysis ===============================")
        # Go through the array of report pod summary and provide stats

        # Validate if pod summary is present
        if self.report_json_contents is not None:
            # validate_proxy_version()
            self.validate_olm_version()
            self.validate_proxy_and_sidecar_version()
            # validate dynamic and static config version
            self.config_version_summary()
            # Validate if Operator Services are present
            self.operator_services()
            # Validate if all the webhooks and CRDs are present
            self.validate_webhooks()
            self.validate_crds()

        return None
