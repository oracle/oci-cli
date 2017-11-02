# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .generated import audit_cli

audit_cli.audit_group.add_command(audit_cli.audit_event_group)
audit_cli.audit_group.add_command(audit_cli.configuration_group)
