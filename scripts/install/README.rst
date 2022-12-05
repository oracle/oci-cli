=============
CLI Installer
=============

As noted in the `CLI QuickStart <https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm>`_, using the installer script and the setup command is the fastest way to get up and running with the CLI.


The installer scripts can be used to install the CLI and its dependencies.
There are two installer scripts that will be described in more detail:
install.sh and install.ps1

install.sh and install.ps1 are the front-end, platform specific scripts for MacOS/linux and Windows. They bootstrap the installation process by making sure that an appropriate version of Python is setup.
A third script, install.py, is downloaded by install.sh/install.ps1 and contains python logic that can run on MacOS, Linux, and Windows platforms. install.py would not typically be invoked directly by end users, but is executed by install.sh and install.ps1.


install.sh
----------
This is the install script for MacOS and linux platforms.
Passwordless sudo access is required to install python and underlying system requirements.
It can be executed in interactive mode via this command:

    bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

To run the install.sh in non-interactive mode, download the script locally and then use the --accept-all-defaults option.

    curl -L -O https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh

    ./install.sh --accept-all-defaults

Here are the parameters accepted by this script:

--accept-all-defaults  When specified, skips all interactive prompts by selecting the default response.
--python-install-location  Optionally specifies where to install python on systems where it is not present. This must be an absolute path and it will be created if it does not exist. This value will only be used on systems with 'yum' where a valid version of Python is not present on the system PATH.
--install-dir  This input parameter allows the user to specify the directory where CLI installation is done.
--exec-dir  This input parameter allows the user to specify the directory where CLI executable is stored.
--script-dir  This input parameter allows the user to specify the directory where CLI scripts are stored.
--update-path-and-enable-tab-completion  If this flag is specified, the PATH environment variable is updated to include CLI executable and tab auto completion of CLI commands is enabled. It does require rc file path in NIX systems which can be either given interactively or using the --rc-file-path option.
--rc-file-path  This input param is used in NIX systems to update the corresponding shell rc file with command auto completion and modification to PATH environment variable with CLI executable path. It requires shell's rc file path. e.g. ~/.bashrc. Ideally, should be used with the --update-path-and-enable-tab-completion option.
--optional-features   This input param is used to specify any optional features that need to be installed as part of OCI CLI install.
--oci-cli-version  The version of CLI to install, e.g. 2.5.12. The default is the latest from pypi.
--help  Show a help message for this script and exit.

The order of precedence in which this scripts applies input parameters is as follows:

    individual params > accept_all_defaults > interactive inputs
    

install.ps1
-----------
This is the install script for Windows.
It can be executed in interactive mode via these command from an elevated PowerShell console:

    Set-ExecutionPolicy RemoteSigned
    
    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1'))"

To run the install.sh in non-interactive mode, download the script locally and then use the -AcceptAllDefaults option.

    (New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1') > install.ps1

    .\install.ps1 -AcceptAllDefaults

Help can be obtained via "help .\install.ps1". Here are the parameters accepted by this script:

-AcceptAllDefaults  Run the script accepting all default options. This will suppress all prompts for user input.
-PythonInstallLocation  Optionally specifies where to install python on systems where it is not present. This must be an absolute path and it will be created if it does not exist.
-OptionalFeatures  This input param is used to specify any optional features that need to be installed as part of OCI CLI install.
-InstallDir  This input parameter allows the user to specify the directory where CLI installation is done.
-ExecDir  This input parameter allows the user to specify the directory where CLI executable is stored.
-ScriptDir  This input parameter allows the user to specify the directory where CLI scripts are stored.
-UpdatePathAndEnableTabCompletion  If this flag is specified, the PATH environment variable is updated to include CLI executable and tab auto completion of CLI commands is enabled.
-OciCliVersion  The version of CLI to install, e.g. 2.5.12. The default is the latest from pypi.

The order of precedence in which this scripts applies input parameters is as follows:

    individual params > AcceptAllDefaults > interactive inputs

Checksums
-----------
install.sh   eff201279e7198101e8cbbe4cea2ca559732f3cd502e145354d7477d2a4621ce
install.ps1   8dba598ded1718cfa2e52ca8785ece31d0b573868eaec9ad2af535d43797a70c
install.py   2062e01a399a6a1f101beaf697820973e32809e20fefeb07b0a3b5416d5588ef
