#!/bin/bash
# Creates an object of the given size in MB, uploads it to Object Storage Service,
# downloads it again, then cleans up. The time for each operation is recorded in seconds.
# Example run: ./scripts/large_file_test_script.sh 300

set -e

# Setup
mkdir -p scripts/temp
NS=$BMCS_CLI_NAMESPACE
BUCKET=TestLargeFileScriptBucket$(( ( RANDOM % 10000 )  + 1 ))
OBJECT=large_file_1.dat
C=$BMCS_CLI_COMPARTMENT_ID
FILE=scripts/temp/$OBJECT
ARGS="--config-file $BMCS_CLI_CONFIG_FILE"
SIZE_IN_MB=$1

echo Testing object put and get with object of size $SIZE_IN_MB MB.
echo Bucket Name: $BUCKET

set +e
# Clean up from any previous failed tests.
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name $OBJECT --force
bmcs $ARGS os bucket delete -ns $NS --name $BUCKET --force
set -e

bmcs $ARGS os bucket create -ns $NS --compartment-id $C --name $BUCKET

dd if=/dev/zero of=$FILE  bs=1000000  count=$SIZE_IN_MB
ORIGINAL_MD5=$(openssl md5 $FILE)
echo MD5: $ORIGINAL_MD5

SECONDS=0
echo Object Put...
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name $OBJECT --file $FILE --metadata '{"opc-meta-size-in-mb":"'$SIZE_IN_MB'"}'
rm $FILE

echo Object Put time elapsed: $SECONDS seconds

echo Object Head:
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name $OBJECT

SECONDS=0
echo Object Get...
bmcs $ARGS os object get -ns $NS -bn $BUCKET --name $OBJECT --file $FILE
echo Object Get time elapsed: $SECONDS seconds

FINAL_MD5=$(openssl md5 $FILE)
rm $FILE
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name $OBJECT --force
bmcs $ARGS os bucket delete -ns $NS --name $BUCKET --force

if [[ $FINAL_MD5 == $ORIGINAL_MD5 ]]; then
    echo "MD5 validated."
else
    echo "MD5 does not match."
    exit 1
fi

echo "Success!"
