#!/bin/bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


# This test is to demonstrate that files ending with '/' will successfully download with
# with os bulk-download without error messages.
echo "Creating test folder"
mkdir ./bulk-test && cd bulk-test
echo "Getting file"
SLASH_FILE=$(oci os object bulk-download -bn $SLASH_BUCKET --download-dir . | jq -r .data)

echo "Starting bulk download"
BULK_FILES=$(oci os object bulk-download -bn $BULK_BUCKET --download-dir . | jq -r .data)

echo "Deleting test folder"
cd .. && rm -r bulk-test
