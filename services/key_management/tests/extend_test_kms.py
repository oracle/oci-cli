# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

# These mappings are used by generated tests to look up operations that have been moved in code in the CLI.
MOVED_COMMANDS = {
    ('kms', 'crypto', 'encrypted_data', 'encrypt'): ['kms', 'crypto', 'encrypt'],
    ('kms', 'crypto', 'decrypted_data', 'decrypt'): ['kms', 'crypto', 'decrypt'],
    ('kms', 'crypto', 'generated_key', 'generate-data-encryption-key'): ['kms', 'crypto', 'generate-data-encryption-key'],
    ('kms', 'vault', 'cancel-deletion'): ['kms', 'management', 'vault', 'cancel-deletion'],
    ('kms', 'vault', 'schedule-deletion'): ['kms', 'management', 'vault', 'schedule-deletion'],
    ('kms', 'vault', 'get'): ['kms', 'management', 'vault', 'get'],
    ('kms', 'vault', 'create'): ['kms', 'management', 'vault', 'create'],
    ('kms', 'vault', 'list'): ['kms', 'management', 'vault', 'list'],
    ('kms', 'vault', 'delete'): ['kms', 'management', 'vault', 'delete'],
    ('kms', 'vault', 'update'): ['kms', 'management', 'vault', 'update']
}
