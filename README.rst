Oracle Cloud Infrastructure CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

About
=====
This is the command line interface for Oracle Cloud Infrastructure.

The project is open source and maintained by Oracle Corp. The home page for the project is `here`__.

__ https://docs.cloud.oracle.com/Content/API/Concepts/cliconcepts.htm

Announcements
=============

Interactive Features
--------------------
OCI CLI offers interactive features to guide you through command usage.

Enabling them allows:
    * Suggestions and autocompletion to help compose commands;
    * Color-coded suggestions to distinguish required parameters from optional parameters; and
    * Quick references display alongside suggestions to recognize command and parameter purposes.

Try the interactive features anytime with the ``-i`` option:
::

    oci -i

.. image:: https://github.com/oracle/oci-cli/blob/master/images/animation.png?raw=true
  :width: 1000
  :alt: Alternative text

Read more on `OCI Documentation`__.

__ https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing_topic-Using_Interactive_Mode.htm

Container Image
---------------
OCI CLI is now available as container images.

With a standards-compliant container runtime engine, pull and run the latest version of oci-cli from the GitHub Container Registry.

Read about setup requirements and instructions on `Working with the OCI CLI Container Image`__.

Find previous image versions on `our package page`__.

__ https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clicontainer.htm

__ https://github.com/oracle/docker-images/pkgs/container/oci-cli


Installation
============

Mac OS X
--------
::

    brew install oci-cli

`OCI Command Line Interface Installation and Configuration on Mac Instance <https://www.youtube.com/watch?v=0k2Lj0oMDK4&list=PLKCk3OyNwIzuA-dqI5vkhZVIc_cxHCkp5&index=22>`_

Linux
-----
::

    bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

`OCI Command Line Interface Installation and Configuration on Linux Instance <https://www.youtube.com/watch?v=bY3jQMMHxdw&list=PLKCk3OyNwIzuA-dqI5vkhZVIc_cxHCkp5&index=20>`_

Oracle Linux 7
--------------
::

    sudo yum install python36-oci-cli


Fedora Linux
------------
::

    sudo dnf install oci-cli

Windows
-------
::

    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1'))"

`OCI Command Line Interface Installation and Configuration on Windows Instance <https://www.youtube.com/watch?v=rEHwcJdRf8M&list=PLKCk3OyNwIzuA-dqI5vkhZVIc_cxHCkp5&index=21>`_

See the `installation guide`__ for detailed installation instructions, options and troubleshooting.

__ https://docs.cloud.oracle.com/Content/API/SDKDocs/cliinstall.htm

Offline Installation
--------------------
1. Go to the `CLI releases page`__ and locate the required CLI version.

2. For the release, go to the "Assets" area.

3. Download and copy the zip file for your Operating System to the environment where you want to install CLI.

4. Unzip the file and execute the following from inside the unzipped folder

   On Linux:
   ::

       bash install.sh --offline-install

   On Windows:
   ::

       install.ps1 -OfflineInstall

`OCI Command Line Interface (CLI) Installation on an Offline Linux Instance <https://www.youtube.com/watch?v=sWDFAOSxqHU&list=PLKCk3OyNwIzuA-dqI5vkhZVIc_cxHCkp5&index=28&t=1s>`_

`OCI Command Line Interface (CLI) Installation on an Offline Windows Instance <https://www.youtube.com/watch?v=3QtjZ0T58oc&list=PLKCk3OyNwIzuA-dqI5vkhZVIc_cxHCkp5&index=31&t=306s>`_

__ https://github.com/oracle/oci-cli/releases

Usage
=====
To get help with the command line:
::

    oci --help

or

::

    oci -h

To enable interactive features for usage guidance:
::

    oci -i


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

__ https://github.com/oracle/oci-cli/blob/master/CONTRIBUTING.md


Known Issues
============
You can find information on any known issues with the CLI here__, here__ and under the “Issues__” tab of this project's `GitHub repository`__.

__ https://docs.cloud.oracle.com/Content/knownissues.htm
__ https://github.com/oracle/oci-cli/blob/master/COMMON_ISSUES.rst
__ https://github.com/oracle/oci-cli/issues
__ https://github.com/oracle/oci-cli


License
=======
Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

This SDK and sample is dual licensed under the Universal Permissive License 1.0 and the Apache License 2.0.

See LICENSE__ for more details.

__ https://github.com/oracle/oci-cli/blob/master/LICENSE.txt
