#!/bin/bash
set -e

# Runs a few commands. If you don't see Success at the end, then something's wrong.

# Setup
mkdir -p scripts/temp
NS=$OCI_CLI_NAMESPACE
BUCKET=TestScriptBucket$(( ( RANDOM % 10000 )  + 1 ))
C=$OCI_CLI_COMPARTMENT_ID
FILE=scripts/temp/content.txt
EMPTY_FILE=scripts/temp/empty_file
ARGS="--config-file $OCI_CLI_CONFIG_FILE"

# test that invoking with deprecated entry point 'bmcs' still works
bmcs $ARGS os ns get
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

# Put a file from stdin and get it back. Also check we can assign metadata when putting from stdin
oci $ARGS os object put -ns $NS -bn $BUCKET --name object4 --metadata '{"foo1":"bar1","foo2":"bar2"}' --file - <<< "This is some object content"
oci $ARGS os object get -ns $NS -bn $BUCKET --name object4 --file - | grep "This is some object content"
oci $ARGS os object head -ns $NS -bn $BUCKET --name object4 | grep foo1
oci $ARGS os object head -ns $NS -bn $BUCKET --name object4 | grep bar2

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
oci $ARGS os bucket delete -ns $NS --name $BUCKET --force

echo "Success!"
