#!/bin/bash
# This script provides a basic example of how to use the Traffic Management
# feature of the DNS service in the CLI. The variables at the beginning of the
# script must be specified accordingly:
#
#   * COMPARTMENT_ID: The first argument is the OCID of the compartment where we'll create a DNS zone
#   * DNS_ZONE_NAME: The second is the name of the DNS zone to create (e.g. my-example-zone.com)
#   * STEERING_POLICY_NAME: The third is the name of the Steering Policy (e.g. "Example Load Balance Policy")
#   * DOMAIN_NAME: The fourth is the domain name within the zone to attach the policy to. The domain must be within the zone. (e.g. www.my-example-zone.com)
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)
#   - jsonlint (required for converting commented JSON files to uncommented)

set -e

COMPARTMENT_ID=""
DNS_ZONE_NAME=""
STEERING_POLICY_NAME=""
DOMAIN_NAME=""

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

echo "Creating DNS zone: $DNS_ZONE_NAME"
ZONE_ID=$(oci dns zone create -c $COMPARTMENT_ID --zone-type PRIMARY --name $DNS_ZONE_NAME --raw-output --query 'data.id')
echo "Zone ID: $ZONE_ID"

# We will create a Steering Policy that is configured to load balance responses to DNS queries for A
# records across 3 servers with different weights. If you look at the file
# scripts/examples/dns_traffic_management_example/load_balance_answers_with_comments.json you'll see
# that we have 3 answers of rtype "A" listed. Note that the third answer has "isDisabled" set to
# "true".
#
# The Steering Policy has rules defined in
# scripts/examples/dns_traffic_management_example/load_balance_rules_with_comments.json:
#
# 1. FILTER rule: Used to remove manually disabled answers (like the third answer in our example).
#
# 2. WEIGHTED rule: Used to randomly shuffle the answers with the weight values assigned to each
#    answer by name. A higher weight value will increase the probability of an answer being returned
#    first in the list of answers.
#
# 3. LIMIT rule: Used to remove answers from the list until the number of answers left is less than
#    or equal to the value defined in "defaultCount".  For example, this means that we will only
#    return 1 answer when we're done processing the policy.
echo "Creating a Traffic Management Steering Policy for load balancing"

# Use jsonlint to generate comment free JSON files since real JSON files cannot contains comments.
jsonlint -Sf scripts/examples/dns_traffic_management_example/load_balance_answers_with_comments.json > \
    scripts/examples/dns_traffic_management_example/load_balance_answers.json
jsonlint -Sf scripts/examples/dns_traffic_management_example/load_balance_rules_with_comments.json > \
    scripts/examples/dns_traffic_management_example/load_balance_rules.json

POLICY_ID=$(oci dns steering-policy create -c $COMPARTMENT_ID --display-name "$STEERING_POLICY_NAME" \
    --template LOAD_BALANCE --ttl 30 \
    --answers file://scripts/examples/dns_traffic_management_example/load_balance_answers.json \
    --rules file://scripts/examples/dns_traffic_management_example/load_balance_rules.json \
    --raw-output --query 'data.id')
echo "Steering Policy ID: $POLICY_ID"

# After we have a Steering Policy we have to create a Steering Policy Attachment to apply the policy
# to a domain within a zone.
echo "Attaching Steering Policy to domain: $DOMAIN_NAME"
ATTACHMENT_ID=$(oci dns steering-policy-attachment create --steering-policy-id $POLICY_ID --zone-id $ZONE_ID \
    --domain-name "$DOMAIN_NAME" \
    --raw-output --query 'data.id')
echo "Attachment ID: $ATTACHMENT_ID"

# At this point the policy has been applied to the specified domain and answers to DNS queries for
# A records at that domain will be computed using the policy.

# Clean up all the resources we created.
echo "Deleting Steering Policy Attachment: $ATTACHMENT_ID"
oci dns steering-policy-attachment delete --steering-policy-attachment-id $ATTACHMENT_ID --force

echo "Deleting Steering Policy: $POLICY_ID"
oci dns steering-policy delete --steering-policy-id $POLICY_ID --force

echo "Deleting DNS zone: $DNS_ZONE_NAME"
oci dns zone delete --zone-name-or-id $ZONE_ID --force

echo "SUCCESS"
