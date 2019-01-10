# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import fnmatch
import os.path


# A filter which can be used to check matches against a given file path. This filter is dumb in that it has no concept of "how" it will be used (e.g. for
# inclusion or exclusion purposes), just that something does or doesn't match.
#
# The given filter (e.g. *.txt, some/kind/of/path/*.png, only-match-me.pdf) is taken relative to a given directory root. So:
#
#    *.txt is really directory-root/*.txt
#    some/kind/of/path/*.png is really directory-root/some/kind/of/path/*.png
#    only-match-me.pdf is really directory-root/only-match-me.pdf
class FilePathFilter:
    def __init__(self, directory_root, filter_value):
        self.full_filter_path = os.path.join(directory_root, filter_value)

    def match_filter(self, path_to_test):
        return fnmatch.fnmatch(path_to_test, self.full_filter_path)
