# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud
# 
# **Note**
# This API is used by an Oracle Cloud Infrastructure Python script that is packaged with the Oracle Cloud Infrastructure CLI. Oracle recommends that you use the script instead using the API directly.
# See [Migrating an On-Premises Database to Oracle Cloud Infrastructure by Creating a Backup in the Cloud](https://docs.cloud.oracle.com/iaas/Content/Database/Tasks/mig-onprembackup.htm) for more information.

# Oracle Cloud Infrastructure CLI should be installed on the database host, as described in the above documentation.
# The following environment variables must be populated before running the script:
export LC_ALL=  			# <default_language_and_character_set>
					        # Oracle recommends: en_US.UTF-8
export ORACLE_HOME= 		# <ORACLE_HOME>
export ORACLE_SID=			# <ORACLE_SID>
export ORACLE_UNQNAME=		# <ORACLE_UNQNAME>
export C=				    # <destination_compartment_OCID>
export AD=  				# <destination_availability_domain>
export PATH=				# Oracle recommends: $PATH:$ORACLE_HOME/bin

# Set script parameters:
export CONFIG=				# <config.txt_path>
					        # Oracle recommends: /home/oracle/migrate/config.txt
export OPC_INSTALLER=		# <opc_installer_module_path>
					        # Oracle recommends: /home/oracle/migrate
export TMP_DIR=				# <temporary_directory>
					        # Oracle recommends: /home/oracle/migrate/onprem_upload

# Change directory to the location of oci-cli-scripts directory
# Oracle recommends: /home/oracle/migrate/bin/oci-cli-scripts

# Execute the Python script with the necessary parameters:
./create_backup_from_onprem --config-file $CONFIG --display-name <example_display_name> --availability-domain $AD --edition <target_database_edition> --opc-installer-dir $OPC_INSTALLER --tmp-dir $TMP_DIR --compartment-id $C

