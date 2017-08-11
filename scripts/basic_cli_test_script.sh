#!/bin/bash
set -e

# Runs a few commands. If you don't see Success at the end, then something's wrong.

# Setup
mkdir -p scripts/temp
NS=$BMCS_CLI_NAMESPACE
BUCKET=TestScriptBucket$(( ( RANDOM % 10000 )  + 1 ))
C=$BMCS_CLI_COMPARTMENT_ID
FILE=scripts/temp/content.txt
EMPTY_FILE=scripts/temp/empty_file
ARGS="--config-file $BMCS_CLI_CONFIG_FILE"

bmcs $ARGS os ns get
bmcs $ARGS os bucket create -ns $NS --compartment-id $C --name $BUCKET
echo 'example object content!' > $FILE
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object1 --file $FILE

# Put an object with metadata and ensure that you get the metadata back.
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2":"bar2"}'
# Two greps since they're on different lines
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep foo1
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep bar2

# Put an empty file and get it back.
touch $EMPTY_FILE
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object3 --file $EMPTY_FILE
bmcs $ARGS os object get -ns $NS -bn $BUCKET --name object3 --file -

# Put a file from stdin and get it back
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object4 --file - <<< "This is some object content"
bmcs $ARGS os object get -ns $NS -bn $BUCKET --name object4 --file - | grep "This is some object content"

# Try a few variations on metadata format.
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"a b c '"'d'"'","foo2": "bar2"}' --force
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "a b c 'd'"
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1": "a b c d","foo2": "A second value."}' --force

# Two greps since they're on different lines
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "a b c d"
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "A second value."
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2":"bar 2"}' --force

# Two greps since they're on different lines
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "bar1"
bmcs $ARGS os object head -ns $NS -bn $BUCKET --name object2 | grep "bar 2"

# Invalid metadata format
set +e
bmcs $ARGS os object put -ns $NS -bn $BUCKET --name object2 --file $FILE --metadata '{"foo1":"bar1","foo2"}' --force 2>&1 | grep "Parameter 'metadata' must be in JSON format."
bmcs $ARGS os bucket create -ns $NS --compartment-id $C --name $BUCKET --metadata '{"foo1"}' 2>&1 | grep "Parameter 'metadata' must be in JSON format."
set -e

# Bucket metadata
bmcs $ARGS os bucket create -ns $NS --compartment-id $C --name ${BUCKET}_metadata --metadata '{"foo1":"bar1","foo2":"bar2"}'
# Two greps since they're on different lines
bmcs $ARGS os bucket get -ns $NS --name ${BUCKET}_metadata | grep foo1
bmcs $ARGS os bucket get -ns $NS --name ${BUCKET}_metadata | grep bar2
bmcs $ARGS os bucket delete -ns $NS --name ${BUCKET}_metadata --force

bmcs $ARGS os object list -ns $NS -bn $BUCKET
bmcs $ARGS os bucket list -ns $NS --compartment-id $C
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name object1 --force
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name object2 --force
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name object3 --force
bmcs $ARGS os object delete -ns $NS -bn $BUCKET --name object4 --force
bmcs $ARGS os bucket delete -ns $NS --name $BUCKET --force

echo "Success!"
