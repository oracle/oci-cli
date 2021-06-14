#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Restore an archived object and download it
# The archived object is not available for download initially. Issue the restore
# command will kick off the process and it will be available for download in about
# 1 hour.
# Example run: ./scripts/restore_archived_object.sh namespace bucket object file

set -e

# Setup
mkdir -p scripts/temp
NS=$1
BUCKET=$2
OBJECT=$3
FILE=$4

# Show time elapsed in waiting for object restoring to be completed
function show_time_elapsed () {
    num=$SECONDS
    min=0
    hour=0
    if((num>59));then
        ((sec=num%60))
        ((num=num/60))
        if((num>59));then
            ((min=num%60))
            ((num=num/60))
            ((hour=num))
        else
            ((min=num))
        fi
    else
        ((sec=num))
    fi
    echo -ne "Restoring time elapsed: $hour"h "$min"m "$sec"s.\\r
}

# Get object's restore status
STATUS=$(oci os object restore-status -ns $NS -bn $BUCKET --name $OBJECT 2>&1)
echo $STATUS

# Object is archived, call restore command to start the restoring process
if [[ $STATUS == Archived* ]] ;
then
    echo "Archived, restore the object"
    oci os object restore -ns $NS -bn $BUCKET --name $OBJECT
    STATUS=$(oci os object restore-status -ns $NS -bn $BUCKET --name $OBJECT 2>&1)
fi

# Object is in restoring process it could take up to 1 hour to be available for download
# Pulling every 10 minutes to check the status
if [[ $STATUS == Restoring* ]] ;
then
    SECONDS=0
    while [[ $STATUS == Restoring* ]]
    do
        STATUS=$(oci os object restore-status -ns $NS -bn $BUCKET --name $OBJECT 2>&1)
        show_time_elapsed
        sleep 600
    done
fi

# Object is available for download, go ahead download it
if [[ $STATUS == Available* ]] || [[ $STATUS == Restored* ]] ;
then
    oci os object get -ns $NS -bn $BUCKET --name $OBJECT --file $FILE
    echo "File is downloaded to $FILE"
fi