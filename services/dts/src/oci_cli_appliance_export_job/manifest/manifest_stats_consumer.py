# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class ManifestStatsConsumer:
    def __init__(self):
        pass

    def consume(self, manifest_stats):
        """
        Consumes stats from manifest writer to report progress to the user
        :param manifest_stats: Object of type ManifestStats that contains information about a manifest process
        """
        print(str(manifest_stats))
