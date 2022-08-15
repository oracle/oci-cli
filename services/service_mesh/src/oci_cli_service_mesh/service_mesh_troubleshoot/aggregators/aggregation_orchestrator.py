# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import json
import queue

import click
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.bundle_helper import \
    save_as_json
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.event import OperationType
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import MESH_PLURAL, \
    VS_PLURAL, VD_PLURAL, IG_PLURAL
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import MeshData
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.helper import \
    get_resource_type_from_ocid


class ReportData:
    def __init__(self, parent: str = None):
        self.data = dict()
        self.parent = parent

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, allow_nan=False)


class AggregationOrchestrator():

    def __init__(self, ocid):
        # This object will be serialized to Json. Do not add non json serializable data
        self.reports_dict = {}
        self.ocid = ocid

    def aggregate_events(self, events: queue.Queue):
        try:
            while not events.empty():
                event = events.get()
                for dest in event.store:
                    if dest not in self.reports_dict.keys():
                        self.reports_dict[dest] = ReportData(event.identifications.get(dest))
                    dest_value = self.reports_dict[dest]
                    for operation in event.operations:
                        event_type = event.event_type.value.lower()
                        if operation == OperationType.ACCUMULATE:
                            if event_type + "_count" not in dest_value.data.keys():
                                dest_value.data[event_type + "_count"] = 0
                            dest_value.data[event_type + "_count"] += 1
                        elif operation == OperationType.STORE_MULTI_EVENT:
                            if event_type not in dest_value.data.keys():
                                dest_value.data[event_type] = []
                            event_list = dest_value.data[event_type]
                            event_list.append(event.data)
                        elif operation == OperationType.STORE_SINGLE_EVENT:
                            dest_value.data[event_type] = event.data

        except Exception as error:
            click.echo('AggregationOrchestrator Exception: {}'.format(error))

        if self.ocid is None:
            for ocid, report in self.reports_dict.items():
                save_as_json(ocid, None, report.data)
        else:
            # Save the aggregated reports
            resource_type = get_resource_type_from_ocid(self.ocid)
            for ocid, report in self.reports_dict.items():
                current_resource_type = get_resource_type_from_ocid(ocid)
                if current_resource_type != resource_type:
                    continue
                relative_path = None
                if current_resource_type == MESH_PLURAL:
                    # generate mesh report
                    mesh_data = MeshData(mesh_id=ocid)
                    relative_path = mesh_data.get_mesh_hierarchy()
                elif current_resource_type == VS_PLURAL:
                    # generate vs report
                    mesh_data = MeshData(mesh_id=report.parent, vs_id=ocid)
                    relative_path = mesh_data.get_virtual_service_hierarchy()
                elif current_resource_type == VD_PLURAL:
                    # generate vd report
                    mesh_data = MeshData(mesh_id=self.reports_dict[report.parent].parent, vs_id=report.parent, vd_id=ocid)
                    relative_path = mesh_data.get_virtual_deployment_hierarchy()
                elif current_resource_type == IG_PLURAL:
                    # generate ig report
                    mesh_data = MeshData(mesh_id=report.parent, ig_id=ocid)
                    relative_path = mesh_data.get_ingress_gateway_hierarchy()

                if relative_path is not None:
                    save_as_json(ocid, relative_path, report.data)
