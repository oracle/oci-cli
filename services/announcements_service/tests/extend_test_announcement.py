# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# These mappings are used by generated tests to look up operations that have been moved in code in the CLI.
MOVED_COMMANDS = {
    ('announce', 'announcement', 'get'): ['announce', 'announcements', 'get'],
    ('announce', 'announcements_collection', 'list-announcements'): ['announce', 'announcements', 'list'],
    ('announce', 'announcement_user_status', 'update'): ['announce', 'user-status', 'update'],
    ('announce', 'announcement_user_status_details', 'get'): ['announce', 'user-status', 'get']
}
