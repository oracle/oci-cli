#!/bin/bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# This script provides an example of how to get bucket in object storage.
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
#
# Required Environment variables (these should all be within a single region, where applicable):
# OCI_COMPARTMENT_ID - the compartment in which resources will be created
# OCI_FN_IMAGE - The URI of a publicly available image in the Oracle Cloud Infrastructure Registry (OCIR) e.g. phx.ocir.io/<tenancy-name>/<directory>/<image-name>:<image-tag>
# OCI_AVAILABILITY_DOMAIN - the AD that your networking will be in (in this example a single AD is used but multiple ADs can be specified to increase redundancy)

PREFIX="OCI_CLI_Example_"

function run() {
    startup
    echo "=== CREATING NETWORK LAYER ==="
    local subnetID=$(createNetworkLayer)
    echo "=== CREATING FUNCTIONS RESOURCES ==="
    local appID=$(createApplication ${subnetID})
    echo "app id: $appID"
    local fnID=$(createFunction ${appID})
    echo "fn id: $fnID"
    invokeFunction ${fnID}
        echo "=== DELETING FUNCTIONS RESOURCES ==="
    deleteFunction ${fnID}
    deleteApplication ${appID}
}

function startup() {

    if [[ ${OCI_COMPARTMENT_ID} == "" ]]; then
        echo "environment variable OCI_COMPARTMENT_ID must be set"
        exit 1
    fi

    if [[ ${OCI_FN_IMAGE} == "" ]]; then
        echo "environment variable OCI_FN_IMAGE must be set"
        exit 1
    fi

    if [[ ${OCI_AVAILABILITY_DOMAIN} == "" ]]; then
        echo "environment variable OCI_AVAILABILITY_DOMAIN must be set"
        exit 1
    fi

}

function createFunction() {
    local appID=$1

    local fnResp=$(oci fn function create \
        --application-id ${appID} \
        --image ${OCI_FN_IMAGE} \
        --display-name ${PREFIX}Function \
        --memory-in-mbs 128
        --wait-for-state ACTIVE \
        2>/dev/null \
    )

    local fnID=$(jq -r '.data.id' <<< ${fnResp})
    local fnEndpoint=$(jq -r '.data."invoke-endpoint"' <<< ${fnResp})

    echo ${fnID}
}

function deleteFunction() {

    local fnID=$1

    local fnResp=$(oci fn function delete \
        --function-id ${fnID} \
        --force
        2>&1 \
    )

    if [[ ${fnResp} != "" ]]; then
        echo "Function deletion failed: " ${fnResp}
        exit 1
    fi

     echo "function deleted"
}

function createApplication() {
    local subnetID=$1

    local appResp=$(oci fn application create \
        --compartment-id ${OCI_COMPARTMENT_ID} \
        --subnet-ids '["'${subnetID}'"]' \
        --display-name ${PREFIX}App \
        --wait-for-state ACTIVE \
        2>/dev/null \
    )
    local appID=$(jq -r '.data.id' <<< ${appResp})
    echo ${appID}
}

function deleteApplication() {

    local appID=$1

    local appResp=$(oci fn application delete \
        --application-id ${appID} \
        --force \
        2>&1 \
    )

    if [[ ${appResp} != "" ]]; then
        echo "Application deletion failed: " ${appResp}
        exit 1
    fi
    echo "app deleted"
}

function invokeFunction() {
    local fnID=$1
    local invokeResp=$( oci fn function invoke \
        --function-id ${fnID} \
        --file "-" \
        --body "" \
        2>&1 \
    )
    echo "invoke: $invokeResp"
}

function createNetworkLayer(){

    #Create VCN
    local vcnResp=$(oci network vcn create \
         --cidr-block '10.0.0.0/16' \
         --compartment-id ${OCI_COMPARTMENT_ID}  \
         --dns-label clivcndns \
         --wait-for-state AVAILABLE \
         --display-name ${PREFIX}VCN \
         2>/dev/null \
     )

    local vcnID=$(jq -r '.data.id' <<< ${vcnResp})
    local routeTableID=$(jq -r '.data."default-route-table-id"' <<< ${vcnResp})

    #Create Internet Gateway
    local igResp=$(oci network internet-gateway create \
        --compartment-id ${OCI_COMPARTMENT_ID} \
        --vcn-id ${vcnID} \
        --is-enabled true \
        --wait-for-state AVAILABLE \
        --display-name ${PREFIX}Gateway \
        2>/dev/null \
    )

    local gatewayID=$(jq -r '.data.id' <<< ${igResp})

    #Update default route table with gateway
    local rtResp=$(oci network route-table update \
        --rt-id ${routeTableID} \
        --route-rules '[{ "destination": "0.0.0.0/0", "destinationType": "CIDR_BLOCK", "networkEntityId": "'${gatewayID}'" }]' \
        --force \
        --wait-for-state AVAILABLE \
        2>/dev/null \
    )

    #Create a Subnet
    local snResp=$(oci network subnet create \
        --cidr-block "10.0.0.0/24" \
        --compartment-id ${OCI_COMPARTMENT_ID} \
        --vcn-id ${vcnID} \
        --availability-domain ${OCI_AVAILABILITY_DOMAIN}  \
        --display-name ${PREFIX}Subnet \
        --dns-label clisubnetdns \
        --wait-for-state AVAILABLE \
        2>/dev/null \
    )

    local subnetID=$(jq -r '.data.id' <<< ${snResp})

    echo ${subnetID}
}

# Run the example
run
