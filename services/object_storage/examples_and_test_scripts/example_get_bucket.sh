#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to get bucket in object storage.
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
set -e

#This field needs to be set in the environment
# BUCKET_NAME=""

echo "Fetching namespace."
NAMESPACE=$(oci os ns get | jq -r .data)
echo "Using namespace '$NAMESPACE'."

#Fetching bucket information and approximate number of objects in it 
DATA1=$(oci os bucket get --bucket-name $BUCKET_NAME --namespace-name  $NAMESPACE --fields 'approximateCount' | jq -r .data)

echo "Bucket Details : '$DATA1'"

#Fetching bucket information and its approximate Size 
DATA2=$(oci os bucket get --bucket-name $BUCKET_NAME --namespace-name  $NAMESPACE --fields 'approximateSize' | jq -r .data)

echo "Bucket Details : '$DATA2'"

#Fetching bucket information and its approximate Size and approximate count of objects in it
DATA3=$(oci os bucket get --bucket-name $BUCKET_NAME --namespace-name  $NAMESPACE --fields 'approximateSize' --fields 'approximateCount' | jq -r .data)

echo "Bucket Details : '$DATA3'"