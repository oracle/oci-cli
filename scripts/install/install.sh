#!/usr/bin/env bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
#
# Bash script to install the Oracle Cloud Infrastructure CLI
# Example invocation: bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

SHELL_INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh"
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/9585506e3fa72304aa06fb3bb1417877edd5f1a8/scripts/install/install.py"
FALLBACK_INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/5a96643afa1f3c1e52cc58e4e9a7e75c60b4dda1/scripts/install/install.py"
_TTY=/dev/tty

# Below is the usage text to be printed when --help is invoked on this script.
usage="$(basename "$0") [--help] [--accept-all-defaults] [--python-install-location directory_name] [--optional-features feature1,feature2]
        -- Bash script to install the Oracle Cloud Infrastructure CLI. The
           script when run without any options runs in interactive mode
           requesting for user inputs.

The following options are available:
    --accept-all-defaults
        When specified, skips all interactive prompts by selecting the default
        response.
    --python-install-location
        Optionally specifies where to install python on systems where it is
        not present. This must be an absolute path and it will be created if
        it does not exist. This value will only be used on systems where a
        valid version of Python is not present on the system PATH.
    --optional-features
        This input param is used to specify any optional features
        that need to be installed as part of OCI CLI install .e.g. to run
        dbaas script 'create_backup_from_onprem', users need to install
        optional 'db' feature which will install dependent cxOracle package.
    --help
        show this help text and exit.

The order of precedence in which this scripts applies input parameters is as follows:
individual params > accept_all_defaults > interactive inputs"

# detect if the script is able to prompt for user input from stdin
# if it is being run by piping the script content into bash (cat install.sh | bash) prompts will fail
# (-t fd True if file descriptor fd is open and refers to a terminal)
if ! [ -t 0 ]; then
    echo "WARNING: Some interactive prompts may not function correctly if this script is piped into bash (e.g. 'curl \"$SHELL_INSTALL_SCRIPT_URL\" | bash)'"
    echo "WARNING: Script should either be downloaded and invoked directly, or be run with the following command: bash -c \"\$(curl -L $SHELL_INSTALL_SCRIPT_URL)\""
fi

# Initialize install args. Populate it with command line arguments
install_args=""
# parse script arguments
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    --python-install-location)
    PYTHON_INSTALL_LOCATION="$2"
    shift # past argument
    shift # past value
    ;;
    --accept-all-defaults)
    ACCEPT_ALL_DEFAULTS=true
    install_args="$install_args --accept-all-defaults"
    shift # past argument
    ;;
    --optional-features)
    OPTIONAL_PACKAGE_NAME="$2"
    install_args="$install_args --optional-features $OPTIONAL_PACKAGE_NAME"
    shift # past argument
    shift # past value
    ;;
    # Help text for this script. This option takes precedence over all other options
    --help|-h)
    echo "$usage"
    exit 0
    ;;
    *)    # unknown option
    echo "Failed to run install script. Unrecognized argument: $1"
    exit 1
    ;;
esac
done

yum_opts=""
apt_get_opts=""
if [ "$ACCEPT_ALL_DEFAULTS" = true ]; then
    yum_opts="-y"
    apt_get_opts="-y"
    echo "Running with --accept-all-defaults"
else
    echo "
    ******************************************************************************
    ******************************************************************************
    You have started the OCI CLI Installer in interactive mode. If you do not wish
    to run this in interactive mode or would like to know more about input options
    for this script, kill this process and invoke the commands below in your shell
    to get more help text for this script:
    curl -L -O https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh
    ./install.sh -h
    ******************************************************************************
    ******************************************************************************"
fi

install_script=$(mktemp -t oci_cli_install_tmp_XXXX) || exit
echo "Downloading Oracle Cloud Infrastructure CLI install script from $INSTALL_SCRIPT_URL to $install_script."
curl -# -f $INSTALL_SCRIPT_URL > $install_script
if [ $? -ne 0 ]; then
    INSTALL_SCRIPT_URL=$FALLBACK_INSTALL_SCRIPT_URL
    curl -# -f $INSTALL_SCRIPT_URL > $install_script || exit
    echo "Falling back to previous install.py script URL - $INSTALL_SCRIPT_URL"
fi

# use default system executable on path unless we have to install one below
python_exe=python

# if python is not installed or is less than the required version, then install Python
need_to_install_python=true
command -v python >/dev/null 2>&1
if [ $? -eq 0 ]; then
    # python is installed so check if the version is valid
    # this python command returns an exit code of 0 if the system version is sufficient, and 1 if it is not
    python -c "import sys; v = sys.version_info; valid = v >= (2, 7, 5) if v[0] == 2 else v >= (3, 5, 0); sys.exit(0) if valid else sys.exit(1)"
    if [ $? -eq 0 ]; then
        # if python is installed and meets the version requirements then we dont need to install it
        need_to_install_python=false
    else
        echo "System version of Python must be either a Python 2 version >= 2.7.5 or a Python 3 version >= 3.5.0."
    fi
else
    echo "Python not found on system PATH"
fi

# some OSes have python3 as a command but not 'python' (example: Ubuntu 16.04)
# if both python and python3 exist and are a sufficiently recent version, we will prefer python3
command -v python3 >/dev/null 2>&1
if [ $? -eq 0 ]; then
    # python is installed so check if the version is valid
    # this python command returns an exit code of 0 if the system version is sufficient, and 1 if it is not
    python3 -c "import sys; v = sys.version_info; valid = v >= (2, 7, 5) if v[0] == 2 else v >= (3, 5, 0); sys.exit(0) if valid else sys.exit(1)"
    if [ $? -eq 0 ]; then
        python_exe=python3
        # if python is installed and meets the version requirements then we dont need to install it
        need_to_install_python=false
    else
        echo "System version of Python must be either a Python 2 version >= 2.7.5 or a Python 3 version >= 3.5.0."
    fi
else
    echo "Python3 not found on system PATH"
fi


if [ "$need_to_install_python" = true ]; then
    if command -v yum
    then
        echo "Attempting to install Python."
        sudo yum $yum_opts check-update
        sudo yum $yum_opts install gcc libffi-devel python-devel openssl-devel
        if [ $? -ne 0 ]; then
            echo "ERROR: Required native dependencies were not installed, exiting install script. If you did not recieve a prompt to install native dependencies please ensure you are not piping the script into bash and are instead using the following command: bash -c \"\$(curl -L $SHELL_INSTALL_SCRIPT_URL)\""
            exit 1
        fi
        curl --tlsv1.2 -O https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
        tar -xvzf Python-3.6.5.tgz
        cd Python-3.6.5
        python_exe=/usr/local/bin/python3.6
        if [ -n "$PYTHON_INSTALL_LOCATION" ]; then
            configure_args="prefix=$PYTHON_INSTALL_LOCATION"
            python_exe="$PYTHON_INSTALL_LOCATION/bin/python3.6"
        fi
        ./configure $configure_args
        make
        sudo make install
        cd ..
    elif command -v apt-get
    then
        echo "Attempting to install Python."
        sudo apt-get $apt_get_opts update
        sudo apt-get $apt_get_opts install python3-pip
        if [ $? -ne 0 ]; then
            echo "ERROR: Python was not installed, exiting install script. If you did not recieve a prompt to install python please ensure you are not piping the script into bash and are instead using the following command: bash -c \"\$(curl -L $SHELL_INSTALL_SCRIPT_URL)\""
            exit 1
        fi
        python_exe=python3
    else
        echo "ERROR: Could not install Python based on operating system. Please install Python manually and re-run this script."
        exit 1
    fi
fi

chmod 775 $install_script
echo "Running install script."
echo "$python_exe $install_script $install_args < $_TTY"
$python_exe $install_script $install_args < $_TTY
