#!/bin/bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# -----------------------------------------
#
# This script provides an example of how use the load balancer API to create
# and IPv6 load balancer
#
# Requirements for running this script:
# -----------------------------------------
# 1.  OCI CLI v2.5.9 or later (you can check this by running oci --version)
# 2. The following Environment variables must be set:
#   COMPARTMENT_ID - The compartment ID in which the load balancer will be created
#   SUBNET_ID - The subnet ID in which the load balancer will be created (NOTE: must be regional)
#   DISPLAY_NAME - The display name for the load balancer to be created
#   LB_SHAPE - The shape of the load balancer to be created

if [[ -z "$COMPARTMENT_ID" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$SUBNET_ID" ]]; then
    echo "SUBNET_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$DISPLAY_NAME" ]]; then
    echo "DISPLAY_NAME must be defined in your environment"
    exit 1
fi

if [[ -z "$LB_SHAPE" ]]; then
    echo "LB_SHAPE must be defined in your environment"
    exit 1
fi

oci lb load-balancer create -c $COMPARTMENT_ID \
    --display-name $DISPLAY_NAME \
    --shape-name $LB_SHAPE \
    --ip-mode "IPV6" \
    --subnet-ids "[\"${SUBNET_ID}\"]"
