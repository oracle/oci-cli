# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json


class ManifestLineItem:
    def __init__(self, path, md5, size):
        """
        This class is a model for holding the line item records in the manifest file
        """
        self.path = path
        self.size = size
        self.md5 = md5

    def __str__(self):
        return json.dumps({
            "path": self.path,
            "size": self.size,
            "md5": self.md5
        }) + "\n"
