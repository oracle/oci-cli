#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Bash script to install the Oracle Cloud Infrastructure CLI
# Example invocation: bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
#
# Use --help to show a help message for this script and its parameters and exit.
#
# The order of precedence in which this scripts applies input parameters is as follows:
#           individual params > accept_all_defaults > interactive inputs
#
SHELL_INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh"
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/v3.2.1/scripts/install/install.py"
FALLBACK_INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/v2.22.0/scripts/install/install.py"
_TTY=/dev/tty
NO_TTY_REQUIRED=false

# Below is the usage text to be printed when --help is invoked on this script.
usage="$(basename "$0") [--help] [--accept-all-defaults] [--python-install-location directory_name] [--optional-features feature1,feature2]
        -- Bash script to install the Oracle Cloud Infrastructure CLI. The
           script when run without any options runs in interactive mode
           requesting for user inputs.

The following options are available:
    --accept-all-defaults
        When specified, skips all interactive prompts by selecting the default
        response.  This is a non-interactive mode which can be used in conjunction
        with other parameters that follow.
    --offline-install
        When specified, the script installs CLI without the need to go to the internet.
        This can run only as part of offline installation.
    --dependency-dir
        When input is specified, CLI install will process dependencies from input relative path
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
    --install-dir
        This input parameter allows the user to specify the directory where
        CLI installation is done.
    --exec-dir
        This input parameter allows the user to specify the directory where CLI executable is stored.
    --script-dir
        This input parameter allows the user to specify the directory where CLI scripts are stored.
    --update-path-and-enable-tab-completion
        If this flag is specified, the PATH environment variable is updated to
        include CLI executable and tab auto completion of CLI commands is enabled.
        It does require rc file path in *NIX systems which can be either given
        interactively or using the --rc-file-path option.
    --rc-file-path
        This input param is used in *NIX systems to update the corresponding shell rc file with command
        auto completion and modification to PATH environment variable with CLI executable path. It
        requires shell's rc file path. e.g. ~/.bashrc. Ideally, should be used with the
        --update-path-and-enable-tab-completion option.
    --no-tty
        If this flag is specified, CLI will not be installed with tty
    --oci-cli-version
        The version of CLI to install, e.g. 2.5.12. The default is the latest from pypi.
    --verify-checksum
        This input parameter verifies the checksum for install.py script. the checksum should be provided as a value of this parameter.
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
while [[ $# -gt 0 ]];do
key="$1"

# Rules for local vs. remote install.py:
# This is useful for testing specific versions of the installer.
# 1) if we have --use-local-cli-installer, then it will use a local install.py.
#
# These are useful for the full-install zip bundle install.
# 2) If we have a whl file, cli-deps directory and local install.py, use the local install.py.
# 3) If we have --oci-cli-version with a "preview" version and we have a local install.py, use local install.py.
#
# This is what most customers will end up doing.
# 4) Otherwise download and use the remote install.py.
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
    --offline-install)
    OFFLINE_INSTALL=true
    install_args="$install_args --offline-install"
    shift # past argument
    ;;
    --dependency-dir)
    DEPENDENCY_DIR="$2"
    install_args="$install_args --dependency-dir $DEPENDENCY_DIR"
    shift # past argument
    shift # past value
    ;;
    --install-dir)
    CLI_INSTALL_DIR="$2"
    install_args="$install_args --install-dir $CLI_INSTALL_DIR"
    shift # past argument
    shift # past value
    ;;
    --exec-dir)
    CLI_EXECUTABLE_DIR="$2"
    install_args="$install_args --exec-dir $CLI_EXECUTABLE_DIR"
    shift # past argument
    shift # past value
    ;;
    --script-dir)
    CLI_SCRIPT_DIR="$2"
    install_args="$install_args --script-dir $CLI_SCRIPT_DIR"
    shift # past argument
    shift # past value
    ;;
    --update-path-and-enable-tab-completion)
    install_args="$install_args --update-path-and-enable-tab-completion"
    shift # past argument
    ;;
    --rc-file-path)
    RC_FILE_PATH="$2"
    install_args="$install_args --rc-file-path $RC_FILE_PATH"
    shift # past argument
    shift # past value
    ;;
    --no-tty)
    NO_TTY_REQUIRED=true
    shift # past argument
    ;;
    --optional-features)
    OPTIONAL_PACKAGE_NAME="$2"
    install_args="$install_args --optional-features $OPTIONAL_PACKAGE_NAME"
    shift # past argument
    shift # past value
    ;;

    # For Internal Use: This is helpful for doing image testing installs.
    # The --use-local-cli-installer option forces use of a local version of install.py rather than downloading it from GitHub.
    # Even without this option specified, install.sh may still prefer local over remote based on
    # implicit rules for full install zip bundles.
    --use-local-cli-installer)
    base=$(basename $0)
    script_dir=$(echo $0 | sed -e "s/$base//g")
    cd ${script_dir}
    if [ -f ./install.py ];then
        install_script="./install.py"
    else
        echo "install.py script could not be found."
        exit 1
    fi
    shift # past argument
    ;;

    # When oci-cli-version is used with a remote install.py, it retrieves a specific version of install.py from GitHub.
    # Also when a remote install.py is being used, it tells install.py which oci-cli version to get from pypi.
    # When oci-cli-version is used with --use-local-cli-installer or an implicit full zip bundle install,
    # it "tells" install.py which version of the oci_cli whl file to use.
    # If we have a "preview" version and local install.py, use the local install.py.
    --oci-cli-version)
    version="$2"
    install_args="$install_args --oci-cli-version $version"
    if [[ $version == *"preview"* ]]; then
        if [ -f ./install.py ];then
            install_script="./install.py"
        fi
    else
        INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/v${version}/scripts/install/install.py"
    fi
    shift # past argument
    shift # past value
    ;;
    --dry-run)
    install_args="$install_args --dry-run"
    shift # past argument
    ;;
    --verify-checksum)
    verify_checksum=true
    checksum="$2"
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

# If offline installation enabled, then use local install,py
if [ "$OFFLINE_INSTALL" = true ]; then
  install_script="./install.py"
fi

# Some implicit logic to handle full-install packages such as preview installs.
ls ./oci_cli*.whl 2> /dev/null
if [ $? -eq 0 ];then
    if [[ -f ./install.py ]] && [[ -d ./cli-deps ]];then
        install_script="./install.py"
    fi
fi

yum_opts=""
apt_get_opts=""
if [ "$ACCEPT_ALL_DEFAULTS" = true ]; then
    yum_opts="-y"
    apt_get_opts="-y"
    echo "Running with --accept-all-defaults"
else
    echo "
    ******************************************************************************
    You have started the OCI CLI Installer in interactive mode. If you do not wish
    to run this in interactive mode, please include the --accept-all-defaults option.
    If you have the script locally and would like to know more about
    input options for this script, then you can run:
    ./install.sh -h
    If you would like to know more about input options for this script, refer to:
    https://github.com/oracle/oci-cli/blob/master/scripts/install/README.rst
    ******************************************************************************"
fi

if [ "$OFFLINE_INSTALL" = true ]; then
    echo "Starting OCI CLI Offline Installation"
fi

if [ "${install_script}" == "" ];then
    install_script=$(mktemp -t oci_cli_install_tmp_XXXX) || exit
    echo "Downloading Oracle Cloud Infrastructure CLI install script from $INSTALL_SCRIPT_URL to $install_script."
    curl -# -f $INSTALL_SCRIPT_URL > $install_script
    if [ $? -ne 0 ]; then
        INSTALL_SCRIPT_URL=$FALLBACK_INSTALL_SCRIPT_URL
        curl -# -f $INSTALL_SCRIPT_URL > $install_script
        if [ $? -ne 0 ]; then
          echo "Could not download Oracle Cloud Infrastructure CLI install script from $INSTALL_SCRIPT_URL. Please read common errors https://github.com/oracle/oci-cli/blob/master/COMMON-ISSUES.rst." && exit
        fi
        echo "Falling back to previous install.py script URL - $INSTALL_SCRIPT_URL"
    fi
fi

# use default system executable on path unless we have to install one below
python_exe=python

# This is needed for Offline installation, since Offline installation requires Python 3 to be installed
python3_is_installed=false

# if both python and python3 exist and are a sufficiently recent version, we will prefer python3
# this python command returns an exit code of 0 if the system version is sufficient, and 1 if it is not
python_version_check="import sys; valid = sys.version_info >= (3, 6, 0); sys.exit(0 if valid else 1)"
for try_python_exe in python3 python; do
    $try_python_exe -c "$python_version_check" >/dev/null 2>&1
    python_ok=$?
    if [ $python_ok -eq 0 ]; then
        # if python is installed and meets the version requirements then we dont need to install it
        python_exe=$try_python_exe
        python3_is_installed=true
        break
    elif [ $python_ok -eq 127 ]; then
        echo "$try_python_exe not found on system PATH"
    fi
done

need_to_install_python=false
if [ "${python3_is_installed}" == "false" ]; then
    echo "System version of Python must be a Python 3 version >= 3.6.0."
    if [ "${ACCEPT_ALL_DEFAULTS}" != "true" ] && [ "${NO_TTY_REQUIRED}" == "false" ] && [ "${OFFLINE_INSTALL}" != "true" ]; then
        # Ask user if they would like to upgrade to python 3
        while true
        do
          read -p "OCI CLI will only run on Python 3.6 or higher. Would you like to upgrade to Python 3? Please enter Y or N. " answer
          case $answer in
           [yY]* ) echo "Installing Python 3...";
              need_to_install_python=true
              break;;
           [nN]* ) break;;
           * )     echo "Please enter Y or N !";;
          esac
        done
    else
        need_to_install_python=true
    fi
fi

sudo_cmd="sudo"
if [ "$(whoami)" == "root" ];then
    sudo_cmd=""
fi

if [ "${OFFLINE_INSTALL}" = "true" ] && [ "$python3_is_installed" = false ]; then
  echo "Python3 not found on system PATH"
  echo "Python CLI Offline Installation requires Python3, Please install Python3 then try later"
  exit 1
fi

if [ "$need_to_install_python" = true ]; then
    # Many docker containers won't have sudo installed since they are already run as root.
    if command -v dnf 
    then
        echo "Attempting to install Python 3."
        $sudo_cmd dnf install $yum_opts python3
        python_exe=python3
    elif command -v yum
    then
        echo "Attempting to install Python 3."
        $sudo_cmd yum $yum_opts check-update
        $sudo_cmd yum $yum_opts install gcc libffi-devel python3-devel openssl-devel
        $sudo_cmd yum $yum_opts install make
        if [ $? -ne 0 ]; then
            echo "ERROR: Required native dependencies were not installed, exiting install script. If you did not receive a prompt to install native dependencies please ensure you are not piping the script into bash and are instead using the following command: bash -c \"\$(curl -L $SHELL_INSTALL_SCRIPT_URL)\""
            exit 1
        fi
    elif command -v apt-get
    then
        echo "Attempting to install Python 3."
        $sudo_cmd apt-get $apt_get_opts update
        $sudo_cmd apt-get $apt_get_opts install python3-pip
        if [ $? -ne 0 ]; then
            echo "ERROR: Python 3 was not installed, exiting install script. If you did not receive a prompt to install python please ensure you are not piping the script into bash and are instead using the following command: bash -c \"\$(curl -L $SHELL_INSTALL_SCRIPT_URL)\""
            exit 1
        fi
        python_exe=python3
    else
        echo "ERROR: Could not install Python 3 based on operating system. Please install Python 3.6+ manually and re-run this script."
        exit 1
    fi
fi

# Check if Python installation is correct
$python_exe -c "$python_version_check" >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Python is not working correctly. Please read common errors in the following link. https://github.com/oracle/oci-cli/blob/master/COMMON_ISSUES.rst" && exit
fi

# In the future native dependency setup will be done in this script.
cat /etc/os-release | grep "Ubuntu 18"
if [ "$?" = "0" ] && [ "${OFFLINE_INSTALL}" != "true" ];then
    $sudo_cmd apt-get $apt_get_opts update
    $sudo_cmd apt-get $apt_get_opts install python3-distutils
fi

chmod 775 $install_script

if [ "$verify_checksum" = true ]; then
  echo "Testing checksum of the python installation file:"
  #shasum -a 256 $install_script
  output=$(shasum -a 256 $install_script || sha256sum $install_script)
  # The output of the above command will be something like this 8ec841d987f665d43bef4af82a61aa16971ca91c53e4cd4005e606f9645fa5be /var/folders/kp/3kdz5yrd4cv3_t_qzrj7nw600000gn/T/oci_cli_install_tmp_XXXX.cvhqrtrd so take the first string
  generated_checksum=(${output// / })
  echo "Generated checksum: "${generated_checksum}
  echo "Expected checksum: "${checksum}
  if [ "$generated_checksum" = "$checksum" ];then
    echo "Check sum verification succeeded"
  else
    echo "Check sum verification failed."
    echo "Exiting the installation process..."
    exit
  fi
fi

echo "Running install script."
echo "$python_exe $install_script $install_args"
if [ "${ACCEPT_ALL_DEFAULTS}" == "true" ] || [ "${NO_TTY_REQUIRED}" == "true" ] || [ "${OFFLINE_INSTALL}" == "true" ];then
    # By removing the tty requirement, users will be able to install non-interactively over ssh
    # and in docker containers more easily.
    $python_exe $install_script $install_args
else
    $python_exe $install_script $install_args < $_TTY
fi
