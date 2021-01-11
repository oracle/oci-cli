#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# This script provides an example of how to get Object Storage namespace of a tenancy that is not their own. This
# is useful in cross-tenant Object Storage operations. Object Storage namespace can be retrieved using the
# compartment id of the target tenancy if the user has necessary permissions to access that tenancy.
# OBJECTSTORAGE_NAMESPACE_READ permission should be available to access target tenancy's namespace.
#
# The compartment id parameter is optional. If the compartment id parameter is omitted the namespace of requesting
# user's tenant is returned. Otherwise the namespace of the given compartment's tenancy is returned.
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
set -e

if [[ -z $COMPARTMENT_ID ]]; then
	echo "COMPARTMENT_ID must be defined in the environment."
	exit 1
fi

echo "Fetching Object storage namespace."
NAMESPACE_NAME=$(oci os ns get --compartment-id $COMPARTMENT_ID | jq -r .data)
if [[ -z $NAMESPACE_NAME ]]; then
	echo "Couldn't read namespace.  Check your credentials."
	exit 1
fi
echo "Object storage namespace for compartment '$COMPARTMENT_ID' is '$NAMESPACE_NAME'."
