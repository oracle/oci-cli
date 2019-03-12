# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# These mappings are used by generated tests to look up operations that have been moved in code in the CLI.
MOVED_COMMANDS = {
    ('ons', 'notification-control-plane', 'topic', 'delete'): ['ons', 'topic', 'delete'],
    ('ons', 'notification-control-plane', 'topic', 'update'): ['ons', 'topic', 'update'],
    ('ons', 'notification-control-plane', 'topic', 'list'): ['ons', 'topic', 'list'],
    ('ons', 'notification-control-plane', 'topic', 'get'): ['ons', 'topic', 'get'],
    ('ons', 'notification-control-plane', 'topic', 'create'): ['ons', 'topic', 'create'],
    ('ons', 'notification-data-plane', 'publish_result', 'publish'): ['ons', 'message', 'publish'],
    ('ons', 'notification-data-plane', 'string', 'get-confirm-subscription'): ['ons', 'subscription', 'confirm'],
    ('ons', 'notification-data-plane', 'subscription', 'create'): ['ons', 'subscription', 'create'],
    ('ons', 'notification-data-plane', 'subscription', 'delete'): ['ons', 'subscription', 'delete'],
    ('ons', 'notification-data-plane', 'subscription', 'get'): ['ons', 'subscription', 'get'],
    ('ons', 'notification-data-plane', 'subscription', 'list'): ['ons', 'subscription', 'list'],
    ('ons', 'notification-data-plane', 'update_subscription_details', 'update'): ['ons', 'subscription', 'update'],
    ('ons', 'notification-data-plane', 'string', 'unsubscribe'): ['ons', 'subscription', 'unsubscribe'],
    ('ons', 'notification-data-plane', 'subscription_confirmation', 'resend'): ['ons', 'subscription', 'resend-confirmation'],
    ('ons', 'notification-data-plane', 'subscription', 'resend-confirmation'): ['ons', 'subscription', 'resend-confirmation'],
    ('ons', 'notification-data-plane', 'confirmation_result', 'get-confirm-subscription'): ['ons', 'subscription', 'confirm']
}
