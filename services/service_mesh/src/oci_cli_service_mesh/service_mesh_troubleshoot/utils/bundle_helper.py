# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import json
import os
import shutil
from datetime import datetime
import yaml

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import CustomResourceSummary


# Create directory if the path doesn't exist
def create_directory(hierarchy):
    if hierarchy is None:
        directory_path = os.path.join(BundleHelper.get_home_directory(), BundleHelper.get_bundle_name())
    else:
        directory_path = os.path.join(BundleHelper.get_home_directory(), BundleHelper.get_bundle_name(), hierarchy)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)
    return directory_path


# Save report dict as json
def save_as_json(ocid, hierarchy, contents):
    directory_path = create_directory(hierarchy)
    complete_file_path = os.path.join(directory_path, BundleHelper.get_report_file_name(ocid))
    with open(complete_file_path, "w") as write_file:
        json.dump(contents, write_file, indent=4, sort_keys=True)


# Save custom resource definition as yaml
def save_custom_resource_as_yaml(mesh_id, custom_resource_summary: CustomResourceSummary):
    directory_path = create_directory(custom_resource_summary.get_relative_path(mesh_id))
    complete_file_path = os.path.join(directory_path,
                                      BundleHelper.get_custom_resource_file_name(
                                          custom_resource_summary.get_name(),
                                          custom_resource_summary.get_namespace(),
                                          custom_resource_summary.get_kind()))
    with open(complete_file_path, "w") as temp_file:
        yaml.dump(custom_resource_summary.custom_resource_json, temp_file, encoding='utf-8', default_flow_style=False)


# Singleton
class BundleHelper:
    __bundle_name = None

    def __init__(self):
        if BundleHelper.__bundle_name is None:
            now = datetime.now()
            current_timestamp = now.strftime("%m-%d-%Y_%H-%M-%S")
            BundleHelper.__bundle_name = 'service-mesh-debug-report_' + current_timestamp

    @staticmethod
    def get_bundle_name():
        if BundleHelper.__bundle_name is None:
            BundleHelper()
        return BundleHelper.__bundle_name

    @staticmethod
    def get_home_directory():
        return os.path.expanduser('~')

    @staticmethod
    def dump_contents_to_file(directory_path, file_name, contents):
        # Construct the complete file path
        complete_file_path = os.path.join(directory_path, file_name)

        # Open & Write the contents to the file
        temp_file = open(complete_file_path, "w")
        temp_file.write(str(contents))
        temp_file.close()

    # Save pod as json
    @staticmethod
    def save_contents_as_json(directory_path, file_name, contents):
        complete_file_path = os.path.join(directory_path, file_name)
        with open(complete_file_path, "w") as write_file:
            json.dump(contents, write_file, indent=4, sort_keys=True)

    @staticmethod
    def get_report_file_name(ocid):
        if ocid is None:
            return 'report' + '.json'
        return 'report-' + ocid + '.json'

    @staticmethod
    def get_csv_file_name():
        return 'csv.json'

    @staticmethod
    def get_osok_log_file_name():
        return 'osok-logs.log'

    @staticmethod
    def get_olm_log_file_name():
        return 'olm-logs.log'

    @staticmethod
    def get_catalog_operator_log_file_name():
        return 'catalog-operator-logs.log'

    @staticmethod
    def get_proxy_log_file_name(name, namespace):
        return 'proxy_logs-' + name + '_' + namespace + '.log'

    @staticmethod
    def get_config_dump_file_name(name, namespace):
        return 'config_dump-' + name + '_' + namespace + '.json'

    @staticmethod
    def get_proxy_stats_file_name(name, namespace):
        return 'proxy_stats-' + name + '_' + namespace + '.json'

    @staticmethod
    def get_pod_file_name(name, namespace):
        return 'pod-' + name + '_' + namespace + '.json'

    @staticmethod
    def get_custom_resource_file_name(name, namespace, kind):
        return 'cr_' + kind + '-' + name + '_' + namespace + '.yaml'

    @staticmethod
    def get_overview_file_name():
        return 'overview.json'

    @staticmethod
    def get_install_plan_name():
        return 'install_plan_crd.json'

    @staticmethod
    def get_subscription_file_name():
        return 'subscription_crd.json'

    @staticmethod
    def get_catalog_source_file_name():
        return 'catalog_source_crd.json'

    # Compress the generated bundle in zip format
    @staticmethod
    def compress_bundle(directory_name, bundle_name):
        zip_path = os.path.join(directory_name, bundle_name)
        if not os.path.exists(zip_path):
            return False
        shutil.make_archive(root_dir=zip_path,
                            format='zip',
                            base_name=zip_path)

    # Cleanup the temporary folder
    @staticmethod
    def cleanup(directory_name, bundle_name):
        temp_file_path = os.path.join(directory_name, bundle_name)
        if os.path.exists(temp_file_path):
            shutil.rmtree(temp_file_path)
