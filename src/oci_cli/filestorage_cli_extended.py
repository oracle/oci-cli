# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .generated import filestorage_cli

filestorage_cli.file_storage_group.add_command(filestorage_cli.file_system_group)
filestorage_cli.file_storage_group.add_command(filestorage_cli.export_set_group)
filestorage_cli.file_storage_group.add_command(filestorage_cli.mount_target_group)
filestorage_cli.file_storage_group.add_command(filestorage_cli.export_group)
filestorage_cli.file_storage_group.add_command(filestorage_cli.snapshot_group)
