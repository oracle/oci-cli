# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .file_path_filter import FilePathFilter


# Represents a collection of filters which are intended to be evaluated in a given order. At this stage the class has context on what each of the filters
# in its collection means (e.g all text files) and what that means (include or exclude).
class BaseFileFilterCollection(object):
    INCLUDE = 'include'
    EXCLUDE = 'exclude'

    def __init__(self, directory_root):
        self.filters = []
        self.directory_root = directory_root

    def filter_type_valid(self, filter_type):
        return filter_type == self.INCLUDE or filter_type == self.EXCLUDE

    def get_opposite_filter_type(self, filter_type):
        if filter_type == self.INCLUDE:
            return self.EXCLUDE
        else:
            return self.INCLUDE


# A filter collection where all the filters are of a single type (i.e. all includes or all excludes). Filters are
# evaluated as logical ORs, so if one matches then it is a success.
#
# As a more concrete example, let's say that we had inclusion filters for *.pdf, *.png, */specific.txt
# and my_file.txt. In that case we would match as follows:
#
#   hello.pdf would match (matches *.pdf)
#   path/image.png would match (matches *.png)
#   my_file.txt would match (matches exactly my_file.txt)
#   subfolder/my_file.txt would not match (remember we match relative to the directory root)
#   another_file.txt would not match because there is no matching filter
#   subfolder1/subfolder2/specific.txt would match (matches with */specific.txt - the * will match all other items in the path)
class SingleTypeFileFilterCollection(BaseFileFilterCollection):
    def __init__(self, directory_root, filter_type):
        super(SingleTypeFileFilterCollection, self).__init__(directory_root)

        if self.filter_type_valid(filter_type):
            self.filter_type = filter_type
        else:
            raise RuntimeError('Expected filter type to be include or exclude, but instead was: {}'.format(filter_type))

    def add_filter(self, filter_value):
        self.filters.append(
            (self.filter_type, FilePathFilter(self.directory_root, filter_value))
        )

    def get_action(self, path_to_test):
        # It is not valid to get an action when there are no filters. Callers are expected to handle this case and handle
        # input before getting to this point
        if len(self.filters) == 0:
            raise RuntimeError('There must be at least one filter to evaluate')

        matching_filter = None
        for f in self.filters:
            if f[1].match_filter(path_to_test):
                matching_filter = f
                break

        # If there is a match, then do whatever type this filter collection supports. However, if there is not a match
        # then do the opposite of the filter
        if matching_filter:
            return self.filter_type
        else:
            return self.get_opposite_filter_type(self.filter_type)
