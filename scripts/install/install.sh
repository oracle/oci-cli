#!/usr/bin/env bash

#
# Bash script to install the Oracle Cloud Infrastructure CLI
# Example invocation: curl -L "https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh" | bash
#
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/oracle/oci-cli/1e2df8f61fcf85fcda9e9938365e76fbbece0ca3/scripts/install/install.py"
_TTY=/dev/tty

install_script=$(mktemp -t oci_cli_install_tmp_XXXX) || exit
echo "Downloading Oracle Cloud Infrastructure CLI install script from $INSTALL_SCRIPT_URL to $install_script."
curl -# $INSTALL_SCRIPT_URL > $install_script || exit

# use default system executable on path unless we have to install one below
python_exe=python

yum_opts=""
apt_get_opts=""
accept_all_defaults=false
if [ "$1" == "--accept-all-defaults" ]; then
    accept_all_defaults=true
    yum_opts="-y"
    apt_get_opts="-y"
    echo "Running with --accept-all-defaults"
fi

# if python is not installed or is less than the required version, then install Python
need_to_install_python=true
command -v python >/dev/null 2>&1
if [ $? -eq 0 ]; then
    # python is installed so check if the version is valid
    # this python command returns an exit code of 0 if the system version is sufficient, and 1 if it is not
    python -c "import sys; v = sys.version_info; valid = v >= (2, 7, 5) if v.major == 2 else v >= (3, 5, 0); sys.exit(0) if valid else sys.exit(1)"
    if [ $? -eq 0 ]; then
        # if python is installed and meets the version requirements then we dont need to install it
        need_to_install_python=false
    else
        echo "System version of Python must be either a Python 2 version >= 2.7.5 or a Python 3 version >= 3.5.0."
    fi
else
    echo "Python not found on system PATH"
fi


if [ "$need_to_install_python" = true ]; then
    if command -v yum
    then
        echo "Attempting to install Python."
        sudo yum $yum_opts check-update
        sudo yum $yum_opts install gcc libffi-devel python-devel openssl-devel
        curl -O https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
        tar -xvzf Python-3.6.0.tgz
        cd Python-3.6.0
        ./configure
        make
        sudo make install
        cd ..
        python_exe=/usr/local/bin/python3.6
    elif command -v apt-get
    then
        echo "Attempting to install Python."
        sudo apt-get $apt_get_opts update
        sudo apt-get $apt_get_opts install python3-pip
        python_exe=python3
    else
        echo "Could not install Python based on operating system. Please install Python manually and re-run this script."
        exit 1
    fi
fi

chmod 775 $install_script
echo "Running install script."

install_args=""
if [ "$accept_all_defaults" = true ]; then
    install_args="--accept-all-defaults"
fi

$python_exe $install_script $install_args < $_TTY