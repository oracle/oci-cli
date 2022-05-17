# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from prompt_toolkit.completion import Completion
from interactive.supported_resource_types import supported_resource_types
from interactive.utils import parameter_resource_mapping
from oci_cli import cli_util
from interactive.error_messages import get_error_message


def get_oci_resources(
    ctx, param_name, word_before_cursor, bottom_toolbar, sub_string=""
):

    resource_search_client = cli_util.build_client(
        "resource_search", "resource_search", ctx
    )

    if param_name == "--availability-domain":
        completions = get_availability_domains(
            ctx, word_before_cursor, bottom_toolbar, sub_string
        )
        return completions

    if param_name == "--shape":
        completions = get_compute_shapes(
            ctx, word_before_cursor, bottom_toolbar, sub_string
        )
        return completions

    if param_name == "--image-id":
        completions = get_compute_images(
            ctx, word_before_cursor, bottom_toolbar, sub_string
        )
        return completions

    # If the condition below is True, It means the parameter is not a resource parameter or the resource is not
    # supported by the Query Search API, so just allow the user to enter a value
    if (
        param_name not in parameter_resource_mapping
        or parameter_resource_mapping[param_name]["resource_type"]
        not in supported_resource_types
    ):
        return []

    completions = []

    parameter_resource = parameter_resource_mapping[param_name]
    search_details = dict()
    search_details["type"] = "Structured"
    if (
        not sub_string or len(sub_string) < 3
    ):  # Since QRS API filter for substring len 3+, load all and the filter will happen in the client side
        search_details["query"] = (
            "query " + parameter_resource["resource_type"] + " resources"
        )  # Example is "query Compartment resources"
    else:
        search_details["query"] = (
            "query "
            + parameter_resource["resource_type"]
            + " resources where displayName =~ '"
            + sub_string
            + "'"
        )  # Example is "query Compartment resources matching 'cli_compartmen'"
    try:
        response = resource_search_client.search_resources(
            search_details=search_details, limit=500
        )
        if len(response.data.items) == 0:
            bottom_toolbar.set_toolbar_text(get_error_message("no_items_found"))
        else:
            items = response.data.items
            for item in items:
                # Filter locally if the substring is smalled than 3 characters
                if (
                    sub_string
                    and len(sub_string) < 3
                    and sub_string.lower() not in item.display_name.lower()
                ):
                    continue
                completions.append(
                    Completion(
                        item.identifier
                        if parameter_resource["field_to_use"] == "identifier"
                        else item.display_name,
                        -len(word_before_cursor),
                        display=item.display_name,
                    )
                )
    except Exception:
        bottom_toolbar.set_toolbar_text(
            get_error_message("resource_search_failed"),
            is_error=True,
        )

    return completions


def get_availability_domains(ctx, word_before_cursor, bottom_toolbar, sub_string=""):
    compartment_id = cli_util.get_tenancy_from_config(ctx)

    completions = []
    try:
        identity_client = cli_util.build_client("identity", "identity", ctx)
        response = identity_client.list_availability_domains(
            compartment_id=compartment_id
        )
        if len(response.data) == 0:
            bottom_toolbar.set_toolbar_text(get_error_message("no_items_found"))
        else:
            items = response.data
            for item in items:
                if not sub_string or sub_string.lower() in item.name.lower():
                    completions.append(
                        Completion(
                            item.name, -len(word_before_cursor), display=item.name
                        )
                    )
    except Exception:
        bottom_toolbar.set_toolbar_text(
            get_error_message("resource_search_failed"),
            is_error=True,
        )
    return completions


def get_compute_shapes(ctx, word_before_cursor, bottom_toolbar, sub_string=""):
    compartment_id = cli_util.get_tenancy_from_config(ctx)

    completions = []
    try:
        compute_client = cli_util.build_client("core", "compute", ctx)
        response = compute_client.list_shapes(compartment_id=compartment_id)
        if len(response.data) == 0:
            bottom_toolbar.set_toolbar_text(get_error_message("no_items_found"))
        else:
            items = response.data
            for item in items:
                if not sub_string or sub_string.lower() in item.shape.lower():
                    completions.append(
                        Completion(
                            item.shape, -len(word_before_cursor), display=item.shape
                        )
                    )
    except Exception:
        bottom_toolbar.set_toolbar_text(
            get_error_message("resource_search_failed"),
            is_error=True,
        )
    return completions


def get_compute_images(ctx, word_before_cursor, bottom_toolbar, sub_string=""):
    compartment_id = cli_util.get_tenancy_from_config(ctx)

    completions = []
    try:
        compute_client = cli_util.build_client("core", "compute", ctx)
        kwargs = {"lifecycle_state": "AVAILABLE"}

        response = compute_client.list_images(compartment_id=compartment_id, **kwargs)

        items = response.data
        for item in items:
            if not sub_string or sub_string.lower() in item.display_name.lower():
                completions.append(
                    Completion(
                        item.id, -len(word_before_cursor), display=item.display_name
                    )
                )
        if not completions:
            bottom_toolbar.set_toolbar_text(get_error_message("no_items_found"))
    except Exception:
        bottom_toolbar.set_toolbar_text(
            get_error_message("resource_search_failed"), is_error=True
        )
    return completions
