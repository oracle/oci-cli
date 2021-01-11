#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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
