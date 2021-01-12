#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e


if [ "$RECORD_ONLY" == "1" ];then
    SKIP_BASIC_TESTS=1
fi
if [ "$SKIP_BASIC_TESTS" == "1" ];then
    echo "Skipping basic_cli_test_script"
    exit 0
fi

# Runs a few commands. If you don't see Success at the end, then something's wrong.

# Setup
mkdir -p scripts/temp
NS=$OCI_CLI_NAMESPACE
BUCKET=TestScriptBucket$(( ( RANDOM % 10000 )  + 1 ))
C=$OCI_CLI_COMPARTMENT_ID
FILE=scripts/temp/content.txt
# Note that uploading an empty file is not valid for object storage
EMPTY_FILE=scripts/temp/empty_file
LARGE_FILE_PATH=scripts/temp/large_file
LARGE_FILE_DOWNLOAD_PATH=scripts/temp/large_file_downloaded
ARGS="--config-file $OCI_CLI_CONFIG_FILE"

oci $ARGS os ns get
oci $ARGS os bucket create -ns $NS --compartment-id $C --name $BUCKET
echo 'example object content!' > $FILE
oci $ARGS os object put -ns $NS -bn $BUCKET --name object1 --file $FILE

# Put an object with metadata and ensure that you get the metadata back.
oci $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2":"bar2"}'
# Two greps since they're on different lines
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep foo1
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep bar2

# Put an empty file and get it back.
touch $EMPTY_FILE
oci $ARGS os object put -ns $NS -bn $BUCKET --name object3 --file $EMPTY_FILE
oci $ARGS os object get -ns $NS -bn $BUCKET --name object3 --file -

# Put a file from stdin with a here string and get it back. Also check we can assign metadata when putting from stdin
oci $ARGS os object put -ns $NS -bn $BUCKET --name object4 --metadata '{"foo1":"bar1","foo2":"bar2"}' --file - <<< "This is some object content"
oci $ARGS os object get -ns $NS -bn $BUCKET --name object4 --file - | grep "This is some object content"
oci $ARGS os object head -ns $NS -bn $BUCKET --name object4 | grep foo1
oci $ARGS os object head -ns $NS -bn $BUCKET --name object4 | grep bar2

# Put an empty file from stdin when piping and get it back
cat $EMPTY_FILE | oci $ARGS os object put -ns $NS -bn $BUCKET --name object5 --file -
oci $ARGS os object get -ns $NS -bn $BUCKET --name object5 --file -

# Put a file from stdin with piping and get it back. Also check we can assign metadata when piping
echo "I am the very model of a modern Major General" | oci $ARGS os object put -ns $NS -bn $BUCKET --name object5 --metadata '{"foo1":"bar1","foo2":"bar2"}' --file - --force
oci $ARGS os object get -ns $NS -bn $BUCKET --name object5 --file - | grep "I am the very model of a modern Major General"
oci $ARGS os object head -ns $NS -bn $BUCKET --name object5 | grep foo1
oci $ARGS os object head -ns $NS -bn $BUCKET --name object5 | grep bar2

# Put a large file into object storage, then get it and pipe it to another put.
# The large file is 50MiB (12,800 4k blocks)
dd if=/dev/zero of=$LARGE_FILE_PATH bs=4k count=12800
oci $ARGS os object put -ns $NS -bn $BUCKET --name object6 --file $LARGE_FILE_PATH
oci $ARGS os object get -ns $NS -bn $BUCKET --name object6 --file - | oci $ARGS os object put -ns $NS -bn $BUCKET --name object7 --file - 
oci $ARGS os object get -ns $NS -bn $BUCKET --name object7 --file $LARGE_FILE_DOWNLOAD_PATH

# Belt and suspenders (may be overkill) - compare the file and the MD5
cmp $LARGE_FILE_PATH $LARGE_FILE_DOWNLOAD_PATH
ORIGINAL_MD5=$(openssl md5 $LARGE_FILE_PATH | cut -d ' ' -f2)
FINAL_MD5=$(openssl md5 $LARGE_FILE_DOWNLOAD_PATH | cut -d ' ' -f2)
if [[ $FINAL_MD5 == $ORIGINAL_MD5 ]]; then
    echo "MD5 validated."
else
    echo "MD5 does not match."
    exit 1
fi

# Try a few variations on metadata format.
oci $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"a b c '"'d'"'","foo2": "bar2"}' --force
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "a b c 'd'"
oci $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1": "a b c d","foo2": "A second value."}' --force

# Two greps since they're on different lines
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "a b c d"
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "A second value."
oci $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2":"bar 2"}' --force

# Two greps since they're on different lines
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "bar1"
oci $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "bar 2"

# Invalid metadata format
set +e
oci $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2"}' --force 2>&1 | grep "Parameter 'metadata' must be in JSON format."
oci $ARGS os bucket create -ns $NS --compartment-id $C --name $BUCKET --metadata '{"foo1"}' 2>&1 | grep "Parameter 'metadata' must be in JSON format."
set -e

# Bucket metadata
oci $ARGS os bucket create -ns $NS --compartment-id $C --name ${BUCKET}_metadata --metadata '{"foo1":"bar1","foo2":"bar2"}'
# Two greps since they're on different lines
oci $ARGS os bucket get -ns $NS --name ${BUCKET}_metadata | grep foo1
oci $ARGS os bucket get -ns $NS --name ${BUCKET}_metadata | grep bar2
oci $ARGS os bucket delete -ns $NS --name ${BUCKET}_metadata --force

oci $ARGS os object list -ns $NS -bn $BUCKET
oci $ARGS os bucket list -ns $NS --compartment-id $C
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object1 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object2 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object3 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object4 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object5 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object6 --force
oci $ARGS os object delete -ns $NS -bn $BUCKET --name object7 --force

# Intermittently we have buckets that get stuck in this state:
# Bucket named 'TestScriptBucketxxxx' has pending multipart uploads. Stop all multipart uploads first.
set +e
multipart=$(oci $ARGS os multipart list -ns $NS -bn $BUCKET)
echo "multipart=$multipart"
object=$(echo $multipart | awk '{print $10}' | sed -e 's/,//' | sed -e 's/"//g')
upload_id=$(echo $multipart | awk '{print $14}' | sed -e 's/,//' | sed -e 's/"//g')
echo "oci $ARGS os multipart abort --force --bucket-name $BUCKET --object-name $object --upload-id $upload_id"
oci $ARGS os multipart abort --force --bucket-name $BUCKET --object-name $object --upload-id $upload_id
set -e

oci $ARGS os bucket delete -ns $NS --name $BUCKET --force

echo "Success!"
