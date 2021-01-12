#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# -----------------------------------------
# Create listener,backend_set,cipher_suite using individual ssl_configuration options only
# -----------------------------------------


# Requirements for running this script:
# -----------------------------------------
# The following Environment variables must be set:
#   LOAD_BALANCER_ID - The load Balancer ID to which the listener and backend should be associated
#   CIPHERS - A list of ssl_cipher_suites
#   PROTOCOLS - List of protocols to be supported
#   CERT_NAME - ssl_certificate_name (use 'oci lb certificate create' command to create a new certificate)

# Example
# -----------------------------------------
# CIPHERS='["AES128-SHA","AES256-SHA"]'
# PROTOCOLS='["TLSv1.1","TLSv1.2"]'
# CERT_NAME="testcert"

if [ -z ${LOAD_BALANCER_ID} ];then
    echo "LOAD_BALANCER_ID must be defined in your environment".
    exit 1
fi

if [ -z ${CIPHERS} ];then
    echo "CIPHERS must be defined in your environment".
    exit 1
fi 

if [ -z ${PROTOCOLS} ];then
    echo "PROTOCOLS must be defined in your environment".
    exit 1
fi

if [ -z ${CERT_NAME} ];then
    echo "CERT_NAME must be defined in your environment".
    exit 1
fi

function create_listener {
    echo "Creating listener......"
    oci lb listener create --name test_listener \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --default-backend-set-name  test_backend_set \
                            --port 80 \
                            --protocol  HTTP \
                            --protocols $PROTOCOLS \
                            --ssl-certificate-name $CERT_NAME \
                            --cipher-suite-name test_cipher \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED \
                            --wait-interval-seconds 5
    echo
}

function create_backend_set {
    echo "Creating backend_set......"
    oci lb backend-set create --name test_backend_set \
                            --health-checker-protocol HTTP \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --policy ROUND_ROBIN \
                            --health-checker-url-path 0.0.0.0 \
                            --ssl-certificate-name $CERT_NAME \
                            --cipher-suite-name test_cipher \
                            --protocols $PROTOCOLS \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED \
                            --wait-interval-seconds 5
    echo
}

function create_cipher_suite {
    echo "Creating cipher_suite......"
    oci lb ssl-cipher-suite create --name test_cipher \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --ciphers $CIPHERS \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED \
                            --wait-interval-seconds 5
    echo
}

function delete_listener {
    echo "Deleting listener......"
    oci lb listener delete --listener-name test_listener \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --force \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED
    echo
}

function delete_backend_set {
    echo "Deleting backend_set......"
    oci lb backend-set delete --backend-set-name test_backend_set \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --force \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED
    echo
}

function delete_cipher_suite {
    echo "Deleting cipher_suite......"
    oci lb ssl-cipher-suite delete --name test_cipher \
                            --load-balancer-id $LOAD_BALANCER_ID \
                            --force \
                            --wait-for-state SUCCEEDED \
                            --wait-for-state FAILED
    echo
}

create_cipher_suite
create_backend_set
create_listener
delete_listener
delete_backend_set
delete_cipher_suite
