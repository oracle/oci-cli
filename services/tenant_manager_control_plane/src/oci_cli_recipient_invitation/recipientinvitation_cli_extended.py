# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_recipient_invitation.generated import recipientinvitation_cli

recipientinvitation_cli.recipient_invitation_root_group.commands.pop(recipientinvitation_cli.recipient_invitation_group.name)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.accept_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.get_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.ignore_recipient_invitation)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.list_recipient_invitations)
recipientinvitation_cli.recipient_invitation_root_group.add_command(recipientinvitation_cli.update_recipient_invitation)
