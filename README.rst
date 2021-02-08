Oracle Cloud Infrastructure CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

About
=====
This is the command line interface for Oracle Cloud Infrastructure.

The project is open source and maintained by Oracle Corp. The home page for the project is `here`__.

__ https://docs.cloud.oracle.com/Content/API/Concepts/cliconcepts.htm


Installation
============

Mac OS X
--------
::

    brew install oci-cli

Linux
-----
::

    bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

Oracle Linux 7
--------------
::

    sudo yum install python36-oci-cli

Windows
-------
::

    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1'))"

See the `installation guide`__ for detailed installation instructions, options and troubleshooting.

__ https://docs.cloud.oracle.com/Content/API/SDKDocs/cliinstall.htm


Usage
=====
To get help with the command line:
::

    oci --help

or

::

    oci -h


Examples
========
Examples can be found here__ under the section 'Example Commands'.

__ https://docs.cloud.oracle.com/Content/API/SDKDocs/cliusing.htm


Documentation
=============

Detailed documentation for CLI prerequisites, installation and configuration, and troubleshooting can be found here__.

__ https://docs.cloud.oracle.com/Content/API/Concepts/cliconcepts.htm


Help
====
See the “Questions or Feedback?” section here__.

__ https://docs.cloud.oracle.com/Content/API/SDKDocs/clitroubleshooting.htm


Changes
=======
See CHANGELOG__.

__ https://github.com/oracle/oci-cli/blob/master/CHANGELOG.rst


Contributing
============
oci-cli is an open source project. See CONTRIBUTING__ for details.

Oracle gratefully acknowledges the contributions to oci-cli that have been made by the community.

__ https://github.com/oracle/oci-cli/blob/master/CONTRIBUTING.rst


Known Issues
============
You can find information on any known issues with the CLI here__ and under the “Issues__” tab of this project's `GitHub repository`__.

__ https://docs.cloud.oracle.com/Content/knownissues.htm
__ https://github.com/oracle/oci-cli/issues
__ https://github.com/oracle/oci-cli


License
=======
Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

This SDK and sample is dual licensed under the Universal Permissive License 1.0 and the Apache License 2.0.

See LICENSE__ for more details.

__ https://github.com/oracle/oci-cli/blob/master/LICENSE.txt