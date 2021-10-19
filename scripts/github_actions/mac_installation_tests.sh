# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# XCode Python version
release_version=$(curl -s https://api.github.com/repos/oracle/oci-cli/releases/latest | jq '.name' | sed 's/\"//g')

echo XCode Python CLI Installation
./scripts/install/install.sh --accept-all-defaults
if [ "$release_version" != "$(oci --version)" ]; then
  exit 1
fi


# Homebrew Python version
echo Homebrew Python CLI Installation
python3 --version
pip3 install -U pip
pip3 install -U virtualenv
rm -rf /Users/runner/lib/oracle-cli
brew update python
virtualenv -p python3 cli-3
source cli-3/bin/activate
./scripts/install/install.sh --accept-all-defaults
if [ "$release_version" != "$(oci --version)" ]; then
  exit 1
fi
deactivate

# Official Python version
echo Official Python CLI Installation
rm -rf /Users/runner/lib/oracle-cli
OPENSSL_DIR=$((brew info openssl | grep "/usr/local/Cellar") | cut -d' ' -f1)
curl -OL http://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar xzvf Python-3.7.5.tgz
cd Python-3.7.5
./configure --prefix=/usr/local --with-openssl=${OPENSSL_DIR} --enable-shared
make
make install
cd ..
./scripts/install/install.sh --accept-all-defaults
if [ "$release_version" != "$(oci --version)" ]; then
  exit 1
fi
