# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# EASY-INSTALL-ENTRY-SCRIPT: 'oci-cli','console_scripts','oci'
# This is used be setup.py to create the oci command.
__requires__ = 'oci-cli'
import re
import sys

####################################################################
# This section is an extension to the original template used by
# setuptools.command.easy_install.ScriptWriter.

# Loading a fips_libcrypto_file must be executed prior to
# importing load_entry_point, otherwise overrides from libcrypto will not work.
# It is normal that hashlib.md5 will be disabled from this change.

# This will invoke __init__ which will configure fips by using
# the environment variable, OCI_CLI_FIPS_LIBCRYPTO_FILE.
# Note that we could import anything fromn oci_cli to invoke __init__.
# There is nothing special about this import.
from oci_cli import fips  # noqa F401

####################################################################

from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('oci-cli', 'console_scripts', 'oci')()
    )
