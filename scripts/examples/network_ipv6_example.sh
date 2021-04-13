#!/bin/bash
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# list IPv6 objects associated with a subnet
function list-ipv6-objects-by-subnet() {
  SUBNET_ID=$1

  oci network ipv6 list --subnet-id $SUBNET_ID
}

# get an IPv6 entity specified by ID
function get-ipv6() {
  IPV6_ID=$1

  oci network ipv6 get --ipv6-id $IPV6_ID
}

# Unassigns and deletes the specified IPv6
function delete-ipv6() {
  IPV6_ID=$1

  oci network ipv6 delete --ipv6-id $IPV6_ID
}
