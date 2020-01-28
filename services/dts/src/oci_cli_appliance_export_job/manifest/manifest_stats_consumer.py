# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


class ManifestStatsConsumer:
    def __init__(self):
        pass

    def consume(self, manifest_stats):
        """
        Consumes stats from manifest writer to report progress to the user
        :param manifest_stats: Object of type ManifestStats that contains information about a manifest process
        """
        print(str(manifest_stats))
