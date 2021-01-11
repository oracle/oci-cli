#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to launch an instance using the OCI CLI. This script will:
#
#   * Create a VCN, subnet and internet gateway. This will enable the instance to connect to the public internet.
#     If this is not desired then the internet gateway (and associated route rule) don't need to be created.
#   * Create a network security group with a security rule. This will allow external requests to the instance through
#     80 port so that a HTTP server running on the instance will be open to public.
#   * Launch an instance. Certain assumptions are made about launching the instance
#       - The instance launched will have an available VM shape
#       - The instance launched will use the latest version of an Oracle Linux image
#
# Resources created by the script will be removed when the script is done.
#
# This script takes the following arguments:
#
#   * The compartment which owns the instance
#   * The CIDR block for the VCN and subnet (these will use the same CIDR)
#   * The path to the public SSH key which can be used for SSHing into the instance

compartment_id=$1
cidr_block=$2
ssh_authorized_keys_file=$3

if [[ -z "${compartment_id}" ]] || [[ -z "${cidr_block}" ]] || [[ -z "${ssh_authorized_keys_file}" ]]; then
    echo -e "Usage: $0 <compartment_id> <cidr_block> <ssh_authorized_keys_file>"
    echo -e ""
    echo -e "       <compartment_id>              The OCID of the compartment."
    echo -e "       <cidr_block>                  The CIDR IP address block of the VCN."
    echo -e "                                     Example: '172.16.0.0/16'."
    echo -e "       <ssh_authorized_keys_file>    A file containing one or more public SSH keys to be"
    echo -e "                                     included in the ~/.ssh/authorized_keys file for the"
    echo -e "                                     default user on the instance. Use a newline character"
    echo -e "                                     to separate multiple keys. "
    exit
fi

echo -e "Using compartment_id\n"${compartment_id}"\n"

availability_domains=$(oci iam availability-domain list \
    --compartment-id "${compartment_id}" \
    | jq -rc '.data')
availability_domain=$(echo "${availability_domains}" | jq -rc '.[0]')
availability_domain_name=$(echo "${availability_domain}" | jq -r '.name')
echo -e "Running in Availability Domain: "${availability_domain_name}"\n"${availability_domain}"\n"

echo -e "Looking up Shape ..."
shapes=$(oci compute shape list \
    --availability-domain "${availability_domain_name}" \
    --compartment-id "${compartment_id}" \
    | jq -rc '.data')
vm_shapes=$(echo "${shapes}" | jq -rc '[.[] | select(.shape | startswith("VM."))]')
shape=$(echo "${vm_shapes}" | jq -rc '.[0]')
shape_name=$(echo "${shape}" | jq -r '.shape')
echo -e "Found Shape: "${shape_name}"\n"${shape}"\n"

echo -e "Looking up Image ..."
images=$(oci compute image list \
    --compartment-id "${compartment_id}" \
    --operating-system "Oracle Linux" \
    --shape "${shape_name}" \
    | jq -rc '.data')
image=$(echo "${images}" | jq -rc '.[0]')
image_id=$(echo "${image}" | jq -r '.id')
echo -e "Found Image: "${image_id}"\n"${image}"\n"

echo -e "Creating Vcn ..."
vcn_name="py_cli_example_vcn"
vcn=$(oci network vcn create \
    --cidr-block "${cidr_block}" \
    --compartment-id "${compartment_id}" \
    --display-name "${vcn_name}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
vcn_id=$(echo "${vcn}" | jq -r '.id')
echo -e "Created Vcn: "${vcn_id}"\n"${vcn}"\n"

echo -e "Creating Subnet ..."
subnet_name="py_cli_example_subnet"
subnet=$(oci network subnet create \
    --availability-domain "${availability_domain_name}" \
    --cidr-block "${cidr_block}" \
    --compartment-id "${compartment_id}" \
    --display-name "${subnet_name}" \
    --vcn-id "${vcn_id}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
subnet_id=$(echo "${subnet}" | jq -r '.id')
echo -e "Created Subnet: "${subnet_id}"\n"${subnet}"\n"

echo -e "Creating Internet Gateway ..."
internet_gateway_name="py_cli_example_internet_gateway"
internet_gateway=$(oci network internet-gateway create \
    --compartment-id "${compartment_id}" \
    --display-name "${internet_gateway_name}" \
    --is-enabled "true" \
    --vcn-id "${vcn_id}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
internet_gateway_id=$(echo "${internet_gateway}" | jq -r '.id')
echo -e "Created Internet Gateway: "${internet_gateway_id}"\n"${internet_gateway}"\n"

echo -e "Updating Route Rules in Route Table ..."
default_route_table_id=$(echo ${vcn} | jq -r '.["default-route-table-id"]')
route_table=$(oci network route-table get \
    --rt-id "${default_route_table_id}" \
    | jq -rc '.data')
route_rules=$(echo "${route_table}" | jq -rc '.["route-rules"]')
echo -e "Current Route Rules in Route Table: "${default_route_table_id}"\n"${route_rules}"\n"
route_rule=$(echo '{
    "destination":"0.0.0.0/0",
    "destinationType":"CIDR_BLOCK",
    "networkEntityId":"'${internet_gateway_id}'"
}' | jq -rc)
route_rules=$(echo "${route_rules}" | jq -rc --arg route_rule "${route_rule}" '. + [ $route_rule | fromjson ]')
route_table=$(oci network route-table update \
    --force \
    --route-rules "${route_rules}" \
    --rt-id "${default_route_table_id}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
route_rules=$(echo "${route_table}" | jq -rc '.["route-rules"]')
echo -e "Updated Route Rules in Route Table: "${default_route_table_id}"\n"${route_rules}"\n"

echo -e "Creating Network Security Group ..."
network_security_group_name='py_cli_example_network_security_group'
network_security_group=$(oci network nsg create \
    --compartment-id "${compartment_id}" \
    --display-name "${network_security_group_name}" \
    --vcn-id "${vcn_id}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
network_security_group_id=$(echo "${network_security_group}" | jq -r '.id')
echo -e "Created Network Security Group: "${network_security_group_id}"\n"${network_security_group}"\n"

echo -e "Updating Security Rules in Network Security Group ..."
security_rules=$(oci network nsg rules list \
    --all \
    --nsg-id "${network_security_group_id}" \
    | jq -rc '.data')
security_rules=$([[ -z "${security_rules}" ]] && echo "[]" || echo "${security_rules}")
echo -e "Current Security Rules in Network Security Group: "${network_security_group_id}"\n"${security_rules}"\n"
security_rule=$(echo '{
    "description": "Incoming HTTP connections",
    "direction": "INGRESS",
    "isStateless": "false",
    "protocol": "6",
    "source": "0.0.0.0/0",
    "sourceType": "CIDR_BLOCK",
    "tcpOptions": {
        "destinationPortRange": {
            "min": "80",
            "max": "80"
        }
    }
}' | jq -rc)
security_rules=$(echo "[]" | jq -rc --arg security_rule "${security_rule}" '. + [ $security_rule | fromjson ]')
security_rules=$(oci network nsg rules add \
    --nsg-id "${network_security_group_id}" \
    --security-rules "${security_rules}" \
    | jq -rc '.data["security-rules"]')
echo -e "Updated Security Rules in Network Security Group: "${network_security_group_id}"\n"${security_rules}"\n"


echo -e "Launching Instance ..."
instance_name="py_cli_example_instance"
metadata=$(echo '{
    "py_cli_test_metadata_key1": "py_cli_test_metadata_value1"
}' | jq -rc)
extended_metadata=$(echo '{
    "py_cli_test_extended_metadata_key2": "py_cli_test_extended_metadata_value2",
    "py_cli_test_extended_metadata_map1": {
        "py_cli_test_extended_metadata_key3": "py_cli_test_extended_metadata_value3",
        "py_cli_test_extended_metadata_map2": {
            "py_cli_test_extended_metadata_key4": "py_cli_test_extended_metadata_value4"
        },
        "py_cli_test_extended_metadata_map3": {}
    }
}' | jq -rc)
network_security_group_ids=$(echo "[]" \
    | jq -rc --arg network_security_group_id "${network_security_group_id}" \
    '. + [ $network_security_group_id ]')
instance=$(oci compute instance launch \
    --availability-domain "${availability_domain_name}" \
    --compartment-id "${compartment_id}" \
    --display-name "${instance_name}" \
    --extended-metadata "${extended_metadata}" \
    --image-id "${image_id}" \
    --metadata "${metadata}" \
    --shape "${shape_name}" \
    --ssh-authorized-keys-file "${ssh_authorized_keys_file}" \
    --subnet-id "${subnet_id}" \
    --nsg-ids "${network_security_group_ids}" \
    --wait-for-state "RUNNING" 2> /dev/null \
    | jq -rc '.data')
instance_id=$(echo "${instance}" | jq -r '.id')
echo -e "Created Instance: "${instance_id}"\n"${instance}"\n"

vnics=$(oci compute instance list-vnics \
    --instance-id "${instance_id}" \
    | jq -rc '.data')
echo -e "Vnics attached to Instance: "${instance_id}"\n"${vnics}"\n"

echo -e "Terminating Instance ..."
subnet=$(oci compute instance terminate \
    --force \
    --instance-id "${instance_id}" \
    --wait-for-state "TERMINATED" 2> /dev/null)
echo -e "Terminated Instance: "${instance_id}"\n"

echo -e "Removing Security Rules in Network Security Group ..."
security_rules=$(oci network nsg rules list \
    --all \
    --nsg-id "${network_security_group_id}" \
    | jq -rc '.data')
security_rule_ids=$(echo "${security_rules}" | jq -rc '[.[] | .id]')
security_rules=$(oci network nsg rules remove \
    --nsg-id "${network_security_group_id}" \
    --security-rule-ids "${security_rule_ids}")
security_rules=$([[ -z "${security_rules}" ]] && echo "[]" || echo "${security_rules}")
echo -e "Removed Security Rules in Network Security Group: "${network_security_group_id}"\n"${security_rules}"\n"

echo -e "Deleting Network Security Group ..."
network_security_group=$(oci network nsg delete \
    --force \
    --nsg-id "${network_security_group_id}" \
    --wait-for-state "TERMINATED" 2> /dev/null)
echo -e "Deleted Network Security Group: "${network_security_group_id}"\n"

echo -e "Clearing Route Rules from Route Table ..."
route_table=$(oci network route-table update \
    --force \
    --route-rules "[]" \
    --rt-id "${default_route_table_id}" \
    --wait-for-state "AVAILABLE" 2> /dev/null \
    | jq -rc '.data')
route_rules=$(echo "${route_table}" | jq -rc '.["route-rules"]')
echo -e "Cleared Route Rules from Route Table: "${default_route_table_id}"\n"${route_rules}"\n"

echo -e "Deleting Internet Gateway ..."
internet_gateway=$(oci network internet-gateway delete \
    --force \
    --ig-id "${internet_gateway_id}" \
    --wait-for-state "TERMINATED" 2> /dev/null)
echo -e "Deleted Internet Gateway: "${internet_gateway_id}"\n"

echo -e "Deleting Subnet ..."
subnet=$(oci network subnet delete \
    --force \
    --subnet-id "${subnet_id}" \
    --wait-for-state "TERMINATED" 2> /dev/null)
echo -e "Deleted Subnet: "${subnet_id}"\n"

echo -e "Deleting Vcn ..."
vcn=$(oci network vcn delete \
    --force \
    --vcn-id "${vcn_id}" \
    --wait-for-state "TERMINATED" 2> /dev/null)
echo -e "Deleted Vcn: "${vcn_id}"\n"
