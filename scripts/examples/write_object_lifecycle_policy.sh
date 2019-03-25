#!/bin/bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# This script provides an example of how to create an object lifecycle policy on a bucket.
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
set -e

COMPARTMENT_ID=""  # Your compartment OCID
BUCKET_NAME=""  # Bucket to apply the object lifecycle policy to

if [[ -z $COMPARTMENT_ID || -z $BUCKET_NAME ]]; then
	echo "Arguments required.  Set arguments at top of script."
	exit 1
fi

echo "Fetching namespace."
NAMESPACE_NAME=$(oci os ns get | jq -r .data)
if [[ -z $NAMESPACE_NAME ]]; then
	echo "Couldn't read namespace.  Check your credentials."
	exit 1
fi
echo "Using namespace '$NAMESPACE_NAME'."

echo "Creating bucket."
oci os bucket create --namespace-name $NAMESPACE_NAME --name $BUCKET_NAME --compartment-id $COMPARTMENT_ID --storage-tier Standard
echo "Created bucket."

# An object lifecycle policy's rules needs to be uploaded as a JSON array.  Each element in the array is a rule with this structure:
#
# {
#     "action": "string",
#         "isEnabled": true,
#         "name": "string",
#         "objectNameFilter": {
#             "inclusionPrefixes": [
#                 "string",
#                 "string"
#             ],
#             "inclusionPatterns": [
#                 "string",
#                 "string"
#             ],
#             "exclusionPatterns": [
#                 "string",
#                 "string"
#             ]
#         },
#         "timeAmount": 0,
#         "timeUnit": "string"
# }
#
# (Use `oci os object-lifecycle-policy put --generate-param-json-input items` to generate the structure of the rule array.)
#
# An explanation of each element:
# - action:  The action to take on objects matching this rule.  Valid values are "ARCHIVE" and "DELETE"
# - isEnabled:  A boolean that can be used to temporarily disable a rule.
# - name:  A user-friendly name for the rule.  This element has no effect on the rule's execution.
# - objectNameFilter:  An object that allows filtering object names.  A rule with a missing or empty filter will match all objects.
#     - inclusionPrefixes:  An array of string object name prefixes that will match desired objects in the bucket. For example, "/tmp/".
#     - inclusionPatterns:  An array of string object name patterns that will match desired objects in the bucket. For example, "/tmp/*"
#     - exclusionPatterns:  An array of string object name patterns that will exclude desired objects in the bucket. For example, "*log*".
#                           Exclusions take precedence over inclusions..
# - timeAmount:  An integer amount of time, specified in terms of the timeUnit below.  For example, 90 DAYS.
# - timeUnit:  The unit of time to interpret timeAmount in terms of.  Valid values are "DAYS" and "YEARS".
#
# A full lifecycle policy is an array of these rules.  You may, for example, have one rule that archives objects after 30 days, and
# another that deletes objects after 120 days.  If an object matches both of these rules, it will be deleted.
#
# A valid example lifecycle policy exists in write_object_lifecycle_policy_example/object_lifecycle_policy.json
# It will archive objects whose names begin with "/tmp/" when they reach one day old (rounded to midnight UTC),
# delete objects whose names contains ".log" but does not contain "/auth/" when they reach 14 days old,
# and archive all others after 30 days.
echo "Writing lifecycle policy."
oci os object-lifecycle-policy put --namespace $NAMESPACE_NAME --bucket-name $BUCKET_NAME --items file://scripts/examples/write_object_lifecycle_policy_example/object_lifecycle_policy.json
echo "Object lifecycle policy created successfully."

echo "Retrieving lifecycle policy."
oci os object-lifecycle-policy get --namespace $NAMESPACE_NAME --bucket-name $BUCKET_NAME
echo "Retrieved lifecycle policy."

# Overwriting or deleting a lifecycle policy immediately cancels any in-progress execution of the old policy.
echo "Deleting lifecycle policy."
oci os object-lifecycle-policy delete --namespace $NAMESPACE_NAME --bucket-name $BUCKET_NAME
echo "Deleted lifecycle policy."

echo "Deleting bucket."
oci os bucket delete --namespace $NAMESPACE_NAME --bucket-name $BUCKET_NAME
echo "Deleted bucket."
