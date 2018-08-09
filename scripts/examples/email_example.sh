#!/bin/bash
# This script provides a basic example of how to use the Email Service in the Python SDK. This script accepts two
# will demonstrate:
#
#   * Creating, retrieving, listing and deleting email senders
#   * Creating, retrieving, listing and deleting email suppressions
#   * Obtaining SMTP credentials for your IAM user so that you can send emails.
#     See https://docs.us-phoenix-1.oraclecloud.com/Content/Email/Tasks/configuresmtpconnection.htm for more
#     information on sending emails
#
# The following three variables must be populated at the top of this script:
#
#   * The tenancy ID where the suppressions will be created
#   * The compartment ID where email senders will be created
#   * The User ID to create the SMTP credentials for
#   * The address of the email sender
#   * The address of the email suppression
#
# Note that email senders are created in the compartment which you specify, but the suppressions are always created at the tenancy
# level.
#
# Requirements for running this script:
#   - OCI CLI v2.4.19 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

TENANCY_ID=""
COMPARTMENT_ID=""
USER_ID=""
SENDER_EMAIL_ADDRESS="cli-example-sender-email@oracle.com"
SUPPRESSION_EMAIL_ADDRESS="cli-example-suppression-email@oracle.com"

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

print_header "Sender Operations"
SENDER_ID=$(oci email sender create -c $COMPARTMENT_ID --email-address $SENDER_EMAIL_ADDRESS --wait-for-state ACTIVE --query 'data.id' --raw-output 2>/dev/null)
oci email sender get --sender-id $SENDER_ID
oci email sender list -c $COMPARTMENT_ID --all
oci email sender delete --sender-id $SENDER_ID --force

print_header "Suppression Operations"
SUPPRESSION_ID=$(oci email suppression create -c $TENANCY_ID --email-address $SUPPRESSION_EMAIL_ADDRESS --query 'data.id' --raw-output)
oci email suppression get --suppression-id $SUPPRESSION_ID
oci email suppression list -c $TENANCY_ID --email-address $SUPPRESSION_EMAIL_ADDRESS --time-created-greater-than-or-equal-to 2018-03-10T00:00:00Z
oci email suppression delete --suppression-id $SUPPRESSION_ID --force

print_header "SMTP Credential operations"
SMTP_CREDENTIAL=$(oci iam smtp-credential create --user-id $USER_ID --description 'Example SMTP credential')
SMTP_CREDENTIAL_ID=$(jq -r '.data.id' <<< "$SMTP_CREDENTIAL")
SMTP_CREDENTIAL_USERNAME=$(jq -r '.data.username' <<< "$SMTP_CREDENTIAL")
SMTP_CREDENTIAL_PASSWORD=$(jq -r '.data.password' <<< "$SMTP_CREDENTIAL")
# The 'create' call is the only time the password for the credential will be returned
echo "SMTP Credential username: $SMTP_CREDENTIAL_USERNAME"
echo "SMTP Credential password: $SMTP_CREDENTIAL_PASSWORD"
oci iam smtp-credential list --user-id $USER_ID
oci iam smtp-credential delete --user-id $USER_ID --smtp-credential-id $SMTP_CREDENTIAL_ID --force

echo "Success!"