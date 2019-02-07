# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# These mappings are used by generated tests to look up operations that have been moved in code in the CLI.
MOVED_COMMANDS = {
    ('ons', 'notification-control-plane', 'notification-topic', 'create-topic'): ['ons', 'topic', 'create'],
    ('ons', 'notification-control-plane', 'notification-topic', 'get-topic'): ['ons', 'topic', 'get'],
    ('ons', 'notification-control-plane', 'notification-topic', 'list-topics'): ['ons', 'topic', 'list'],
    ('ons', 'notification-control-plane', 'notification-topic', 'update-topic'): ['ons', 'topic', 'update'],
    ('ons', 'notification-control-plane', 'topic', 'delete'): ['ons', 'topic', 'delete'],
    ('ons', 'notification-data-plane', 'publish-result', 'publish-message'): ['ons', 'message', 'publish'],
    ('ons', 'notification-data-plane', 'string', 'get-confirm-subscription'): ['ons', 'subscription', 'confirm'],
    ('ons', 'notification-data-plane', 'subscription', 'create'): ['ons', 'subscription', 'create'],
    ('ons', 'notification-data-plane', 'subscription', 'delete'): ['ons', 'subscription', 'delete'],
    ('ons', 'notification-data-plane', 'subscription', 'get'): ['ons', 'subscription', 'get'],
    ('ons', 'notification-data-plane', 'subscription', 'list'): ['ons', 'subscription', 'list'],
    ('ons', 'notification-data-plane', 'update-subscription-details', 'update-subscription'): ['ons', 'subscription', 'update'],
    ('ons', 'notification-data-plane', 'string', 'get-unsubscription'): ['ons', 'subscription', 'unsubscribe'],
    ('ons', 'notification-data-plane', 'subscription-confirmation', 'resend'): ['ons', 'subscription', 'resend-confirmation']
}
