# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
