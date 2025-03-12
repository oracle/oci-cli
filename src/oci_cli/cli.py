# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli.cli_root import cli
from oci_cli import cli_session  # noqa: F401,E402
from oci_cli import cli_setup  # noqa: F401
from oci_cli import cli_completion  # noqa: F401
from oci_cli import cli_setup_bootstrap  # noqa: F401
from oci_cli import raw_request_cli  # noqa: F401
from interactive import cli_interactive  # noqa: F401

if __name__ == '__main__':
    cli()
