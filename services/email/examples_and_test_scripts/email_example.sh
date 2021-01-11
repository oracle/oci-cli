#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides a basic example of how to use the Email Service in the CLI.
# It will demonstrate:
#
#   * Creating, retrieving, updating, moving, listing, and deleting email senders
#   * Creating, retrieving, listing, and deleting email suppressions
#   * Creating, retrieving, listing, and deleting SMTP credentials
#     See https://docs.cloud.oracle.com/iaas/Content/Email/Tasks/configuresmtpconnection.htm for more
#     information on sending emails with your IAM user
#
# The following three variables must be populated from the environment:
#
#   * TENANCY_ID: The tenancy ID where the suppressions will be created
#   * COMPARTMENT_ID: The compartment ID where email senders will be created
#   * TARGET_COMPARTMENT_ID: The compartment ID where email senders will be moved to
#   * USER_ID: The User ID to create the SMTP credentials for
#
# This script will create and delete these resources:
#
#   * SENDER_EMAIL_ADDRESS: The address of the approved sender
#   * SUPPRESSION_EMAIL_ADDRESS: The address of the email suppression
#   * an SMTP credential
#
# Note that email senders are created in the compartment which you specify, but suppressions
# are always created at the tenancy level.
#
# Requirements for running this script:
#   - OCI CLI v2.4.42 or later (you can check this by running oci --version)
#   - region set in the ~/.oci/config DEFAULT profile
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This useful utility may also
#     be used to help cater to scenarios which can't be wholly addressed by the --query option in the CLI

set -e

if [ "${TENANCY_ID}" == "" ]; then
  echo $0: "TENANCY_ID must be defined in the environment"
  exit 1
fi

if [ "${COMPARTMENT_ID}" == "" ]; then
  echo $0: "COMPARTMENT_ID must be defined in the environment"
  exit 1
fi

if [ "${TARGET_COMPARTMENT_ID}" == "" ]; then
  echo $0: "TARGET_COMPARTMENT_ID must be defined in the environment"
  exit 1
fi

if [ "${USER_ID}" == "" ]; then
  echo $0: "USER_ID must be defined in the environment"
  exit 1
fi

readonly SENDER_EMAIL_ADDRESS="cli-example-sender-email-${RANDOM}@oracle.com"
readonly SUPPRESSION_EMAIL_ADDRESS="cli-example-suppression-email-${RANDOM}@oracle.com"

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

print_header "Approved Sender Operations"
echo "Creating sender and waiting for it to become active"
SENDER_ID=$(oci email sender create -c $COMPARTMENT_ID --email-address $SENDER_EMAIL_ADDRESS --wait-for-state ACTIVE --query 'data.id' --raw-output 2>/dev/null)
echo "Getting sender"
oci email sender get --sender-id $SENDER_ID
echo "Updating sender"
oci email sender update --sender-id $SENDER_ID --freeform-tags '{"Department": "Finance"}' --force
echo "Moving Sender"
oci email sender change-compartment --sender-id $SENDER_ID --compartment-id $TARGET_COMPARTMENT_ID
echo "Listing senders"
oci email sender list -c $COMPARTMENT_ID --all
echo "Deleting sender"
oci email sender delete --sender-id $SENDER_ID --force

print_header "Suppression Operations"
echo "Creating suppression"
SUPPRESSION_ID=$(oci email suppression create -c $TENANCY_ID --email-address $SUPPRESSION_EMAIL_ADDRESS --query 'data.id' --raw-output)
echo "Getting suppression"
oci email suppression get --suppression-id $SUPPRESSION_ID
echo "Listing suppressions"
oci email suppression list -c $TENANCY_ID --email-address $SUPPRESSION_EMAIL_ADDRESS --time-created-greater-than-or-equal-to 2019-01-10T00:00:00Z
echo "Deleting suppression"
oci email suppression delete --suppression-id $SUPPRESSION_ID --force

print_header "SMTP Credential Operations"
echo "Creating SMTP credential"
SMTP_CREDENTIAL=$(oci iam smtp-credential create --user-id $USER_ID --description 'Example SMTP credential')
SMTP_CREDENTIAL_ID=$(jq -r '.data.id' <<< "$SMTP_CREDENTIAL")
SMTP_CREDENTIAL_USERNAME=$(jq -r '.data.username' <<< "$SMTP_CREDENTIAL")
SMTP_CREDENTIAL_PASSWORD=$(jq -r '.data.password' <<< "$SMTP_CREDENTIAL")
# The 'create' call is the only time the password for the credential will be returned
echo "SMTP Credential username: $SMTP_CREDENTIAL_USERNAME"
echo "SMTP Credential password: $SMTP_CREDENTIAL_PASSWORD"
echo "Listing SMTP credentials"
oci iam smtp-credential list --user-id $USER_ID
echo "Deleting SMTP credential"
oci iam smtp-credential delete --user-id $USER_ID --smtp-credential-id $SMTP_CREDENTIAL_ID --force

echo "Complete."
