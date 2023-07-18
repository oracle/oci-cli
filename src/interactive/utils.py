# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import os.path

OCI_CLI_DISABLE_COLORS_ENV_VAR = "OCI_CLI_DISABLE_COLORS"

INTERACTIVE_COMMANDS_HISTORY_DIR_NAME = os.path.join(os.path.expanduser("~"), ".oci")
INTERACTIVE_COMMANDS_HISTORY_FILE_NAME = os.path.join(
    INTERACTIVE_COMMANDS_HISTORY_DIR_NAME, ".cli-interactive-history"
)
INTERACTIVE_COMMANDS_HISTORY_LIMIT = 10

# this list is maintained here since it needs to be called from different places, for example from interactive src code
# and also from the interactive unit tests as well
# they are global cli parameters which have to be excluded from the cli interactive commands
AUTHENTICATION_PARAMS = [
    "--profile",
    "--config-file",
    "--auth",
    "--region",
    "--endpoint",
    "--cert-bundle",
    "--auth-purpose",
]
DEBUG_PARAMS = ["-d", "--debug"]
AUTO_PROMPT_PARAMS = ["--cli-auto-prompt", "-i"]
ANONYMOUS_PARAMS = ["--cli-rc-file", "-?"]

parameters_to_exclude = (
    AUTHENTICATION_PARAMS + DEBUG_PARAMS + AUTO_PROMPT_PARAMS + ANONYMOUS_PARAMS
)

styles_dict = {
    "": "ansicyan",
    "oci": "#C74634",
    "bottom-toolbar": "noreverse",
    "bottom-toolbar.text": "#888888 bg:default noreverse noitalic nounderline noblink",
    "bottom-toolbar.error": "fg:ansired",
    "required-parameter": "fg:ansired",
}

parameter_resource_mapping = {
    "-c": {
        "resource_type": "Compartment",
        "field_to_use": "identifier"
        # For some resources the name should be used not the identifier like --bucket-name
    },
    "--compartment-id": {"resource_type": "Compartment", "field_to_use": "identifier"},
    "--bucket-id": {"resource_type": "Bucket", "field_to_use": "name"},
    "--bucket-name": {"resource_type": "Bucket", "field_to_use": "name"},
    "-bn": {"resource_type": "Bucket", "field_to_use": "name"},
    "--instance-id": {"resource_type": "Instance", "field_to_use": "identifier"},
    "--vcn-id": {"resource_type": "Vcn", "field_to_use": "identifier"},
    "--vnic-id": {"field_to_use": "identifier", "resource_type": "Vnic"},
    "--subnet-id": {"resource_type": "Subnet", "field_to_use": "identifier"},
    "--instance-pool-id": {
        "resource_type": "InstancePool",
        "field_to_use": "identifier",
    },
    "--db-system-id": {"resource_type": "DbSystem", "field_to_use": "identifier"},
    "--boot-volume-id": {"field_to_use": "identifier", "resource_type": "BootVolume"},
    "--policy-id": {"field_to_use": "identifier", "resource_type": "Policy"},
    "--user-id": {"field_to_use": "identifier", "resource_type": "User"},
}

# There are few commands which takes few required params from config i.e compartment-id for few IAM commands.
# Add those commands in REQUIRED_PARAM_EXCEPTION so that interactive CLI will let a user execute a command
# even without providing that required param
REQUIRED_PARAM_EXCEPTION = ["oci iam compartment list", "oci iam user list"]
MESSAGE = "Learn more about interactive features in CLI by watching our informative video on YouTube -> " \
          "https://www.youtube.com/watch?v=lX29Xw1Te54&ab_channel=OracleLearning \n" \
          "Also see https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing_topic-Using_Interactive_Mode.htm"
file_name = "suggestion_variable.txt"


def validate_commands_limit(filename):
    """
    This function validates the commands history file to make sure it does not exceed the limit
    for example if the limit is 50 commands, this function loops through the lines of the file, every command consists
    of 3 lines (one empty line, one line for timestamp and third line for the actual command),
    so if the numbers of the commands exceeds 50, the first command (The oldest) in the file will be deleted

    below is an example of one command entry in the history file

    # 2022-03-04 09:37:13.350959
    +compute instance launch

    :param filename:
    :return:
    """
    commands_counter = 0
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        if line.startswith("+"):
            commands_counter += 1
    if commands_counter > INTERACTIVE_COMMANDS_HISTORY_LIMIT:
        data = file.read().splitlines(True)
        with open(filename, "w") as file_write:
            file_write.writelines(data[3:])


def print_suggestion_message():
    value = 0
    # read value from txt file
    path = os.path.expanduser(os.path.join("~", file_name))
    if os.path.exists(path):
        # if the file exists, read the value from the file
        with open(path, "r") as f:
            value = f.read()
    # print for 1st time
    if value == 0:
        print(MESSAGE)
        value = 1
        with open(path, "w") as f:
            f.write(str(value))
