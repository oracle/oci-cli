#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides example of how to configure, update and reset IORM for Exadata

# The following enviroment variables may be populated before running the script
#   * The exadata DB System ID whose IORM configuration need to be fetched, updated or reset (required)
#   * The Objective for the IORM configuation ([LOW_LATENCY|HIGH_THROUGHPUT|BALANCED|AUTO|BASIC])
#
# The database_exadata_iorm/update_exadata_iorm_config.json needs to be populated as required
#   * The DB plan directives for the IORM configuation
#   * The Share values for the DB plan directives range from 1 - 32


set -e

# Eg: DB_SYSTEM_ID="<Exadata Db system ocid>"
if [[ -z "$DB_SYSTEM_ID" ]];then
  echo "DB_SYSTEM_ID must be defined in the environment. "
  exit 1
fi

# Eg: OBJECTIVE=[LOW_LATENCY|HIGH_THROUGHPUT|BALANCED|AUTO|BASIC]
if [[ -z "$OBJECTIVE" ]];then
  echo "OBJECTIVE is not defined, only get iorm config command will be invoked. "
fi

if [ -d ./services/database/examples_and_test_scripts/database_exadata_iorm ];then
    iorm_data="./services/database/examples_and_test_scripts/database_exadata_iorm"
elif [ -d ./database_exadata_iorm ];then
    iorm_data="./database_exadata_iorm"
fi

UPDATE_IORM_CONFIG_FILE="${iorm_data}/update_exadata_iorm_config.json"

if [[ ! -f "$UPDATE_IORM_CONFIG_FILE" ]];then
  echo "$UPDATE_IORM_CONFIG_FILE file not found, only get iorm config command will be invoked."
fi

############################################################################################################################################################

echo 'Starting Get IORM Config example'

echo 'Instantiate/Fetch IORM config for the Exadata DB system'
oci db system get-exadata-iorm-config --db-system-id $DB_SYSTEM_ID

if [[ -z "$OBJECTIVE" && ! -f "$UPDATE_IORM_CONFIG_FILE"]]; then
  echo 'OBJECTIVE or the db plan directives not found, ignoring update and reset command'
  exit 0
else 
  echo 'Update/Enable IORM configuration for the Exadata DB system'
  oci db system update-exadata-iorm-config --db-system-id ${DB_SYSTEM_ID} --objective ${OBJECTIVE} --db-plans file://${UPDATE_IORM_CONFIG_FILE}

  echo 'Reset IORM configuration for the Exadata DB system'
  oci db system update-exadata-iorm-config --db-system-id ${DB_SYSTEM_ID} --objective "" --db-plans ""
fi

echo 'End of Exadata IORM configuation example.'
