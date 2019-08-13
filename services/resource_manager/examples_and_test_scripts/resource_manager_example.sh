#!/bin/bash
# This script provides a basic example of how to use the Resource Manager service in the CLI.
# The three variables at the beginning of the script must be specified accordingly:
#
#   * COMPARTMENT_ID: The OCID of the compartment where we'll create Stack and Jobs
#   * ZIP_FILE_PATH: Zip file which includes terraform configuration files
#   * WORKING_DIRECTORY: The working directory inside zip file if terraform configuration files are not in root directory.
#
# The script will demonstrate:
#
#     * Creating a new stack
#     * Creating a plan job
#     * Getting job logs
#     * Creating an apply job
#     * Getting job terraform state
#     * Creating a destroy job
#     * Deleting stack
#

set -e

PLAN_JOB_LOGS_FILE=Plan_Job_Logs.txt
JOB_TF_STATE=Job_Tf_State.txt

if [ "${COMPARTMENT_ID}" == "" ]; then
    echo $0: "COMPARTMENT_ID must be defined in the environment"
    exit 1
fi

if [ "${ZIP_FILE_PATH}" == "" ]; then
    echo $0: "ZIP_FILE_PATH must be defined in the environment"
    exit 1
fi

echo "Creating Stack"
if [ "${WORKING_DIRECTORY}" == "" ]; then
    CREATED_STACK_ID=$(oci resource-manager stack create --compartment-id $COMPARTMENT_ID --config-source $ZIP_FILE_PATH --query 'data.id' --raw-output)
else
	CREATED_STACK_ID=$(oci resource-manager stack create --compartment-id $COMPARTMENT_ID --config-source $ZIP_FILE_PATH --working-directory $WORKING_DIRECTORY --query 'data.id' --raw-output)
fi
echo "Created stack id: ${CREATED_STACK_ID}"

echo "Creating Plan Job"
CREATED_PLAN_JOB_ID=$(oci resource-manager job create --stack-id $CREATED_STACK_ID --operation PLAN --wait-for-state SUCCEEDED --query 'data.id' --raw-output)
echo "Created Plan Job Id: ${CREATED_PLAN_JOB_ID}"

echo "Getting Job Logs"
echo $(oci resource-manager job get-job-logs --job-id $CREATED_PLAN_JOB_ID) > $PLAN_JOB_LOGS_FILE
echo "Saved Job Logs to $PLAN_JOB_LOGS_FILE"

# wait for stack to be unlocked
sleep 15

echo "Creating Apply Job"
JSON_FILE=$(mktemp)
cat > ${JSON_FILE} << EOF
    { "planJobId": "$CREATED_PLAN_JOB_ID" }
EOF
CREATED_APPLY_JOB_ID=$(oci resource-manager job create --stack-id $CREATED_STACK_ID --operation APPLY --apply-job-plan-resolution file://${JSON_FILE} --wait-for-state SUCCEEDED --query 'data.id' --raw-output)
echo "Created Apply Job Id: ${CREATED_APPLY_JOB_ID}"

echo "Getting Job Terraform state"
oci resource-manager job get-job-tf-state --job-id $CREATED_APPLY_JOB_ID --file $JOB_TF_STATE
echo "Saved Job Logs to $JOB_TF_STATE"

# wait for stack to be unlocked
sleep 15

echo "Creating Destroy Job"
CREATED_DESTROY_JOB_ID=$(oci resource-manager job create --stack-id $CREATED_STACK_ID --operation DESTROY --apply-job-plan-resolution '{"isAutoApproved":"true"}' --wait-for-state SUCCEEDED --query 'data.id' --raw-output)
echo "Created Destroy Job Id: ${CREATED_DESTROY_JOB_ID}"

# wait for stack to be unlocked
sleep 15

echo "Deleting Stack"
oci resource-manager stack delete --stack-id $CREATED_STACK_ID --force
echo "Deleted Stack Id: ${CREATED_STACK_ID}"

echo "Script Finished"
