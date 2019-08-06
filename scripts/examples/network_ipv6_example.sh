#!/bin/bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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

# disable internet access for a specified IPv6 entity
function disable-internet-access() {
  IPV6_ID=$1

  oci network ipv6 update --ipv6-id $IPV6_ID --is-internet-access-allowed false
}

# Unassigns and deletes the specified IPv6
function delete-ipv6() {
  IPV6_ID=$1

  oci network ipv6 delete --ipv6-id $IPV6_ID
}
