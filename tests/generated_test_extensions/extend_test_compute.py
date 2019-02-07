# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# These mappings are used by generated tests to look up operations that have been moved in code in the CLI.
MOVED_COMMANDS = {
    ('compute', 'app_catalog_listing', 'get'): ['compute', 'pic', 'listing', 'get'],
    ('compute', 'app_catalog_listing', 'list'): ['compute', 'pic', 'listing', 'list'],
    ('compute', 'app_catalog_listing_resource_version', 'get'): ['compute', 'pic', 'version', 'get'],
    ('compute', 'app_catalog_listing_resource_version', 'list'): ['compute', 'pic', 'version', 'list'],
    ('compute', 'app_catalog_listing_resource_version_agreements', 'get-app-catalog-listing-agreements'): ['compute', 'pic', 'agreements', 'get'],
    ('compute', 'app_catalog_subscription', 'create'): ['compute', 'pic', 'subscription', 'create'],
    ('compute', 'app_catalog_subscription', 'delete'): ['compute', 'pic', 'subscription', 'delete'],
    ('compute', 'app_catalog_subscription', 'list'): ['compute', 'pic', 'subscription', 'list']
}
