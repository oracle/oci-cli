#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Resource Search Service in the Python CLI.
# will demonstrate:
#
#   * List all searchable resource types.
#   * Get detail of one resource type.
#   * Use free text query to search resources cross resource types.
#   * Use structured query to search resources cross resource types.
#
# Requirements for running this script:
#   - OCI CLI v2.4.27 or later (you can check this by running oci --version)

set -e

echo "List all searchable resource types"

oci search resource-type list

echo "Get detail of resource type 'Group' "

oci search resource-type get --name "Group"

echo "Search for objects with string 'searchstring' by free text search"

oci search resource  free-text-search --text "searchstring"

echo "Search for all resource object by structured query search"

oci search resource structured-search --query-text "query all resources"

echo "Success!"