# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_sender_invitation.generated import senderinvitation_cli

senderinvitation_cli.sender_invitation_root_group.commands.pop(senderinvitation_cli.sender_invitation_group.name)
senderinvitation_cli.sender_invitation_root_group.add_command(senderinvitation_cli.create_sender_invitation)
senderinvitation_cli.sender_invitation_root_group.add_command(senderinvitation_cli.cancel_sender_invitation)
senderinvitation_cli.sender_invitation_root_group.add_command(senderinvitation_cli.get_sender_invitation)
senderinvitation_cli.sender_invitation_root_group.add_command(senderinvitation_cli.list_sender_invitations)
senderinvitation_cli.sender_invitation_root_group.add_command(senderinvitation_cli.update_sender_invitation)
