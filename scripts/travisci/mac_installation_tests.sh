# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# XCode Python version
travis_fold start "XCode Python CLI Installation"
echo XCode Python CLI Installation
source $TRAVIS_BUILD_DIR/scripts/install/install.sh --accept-all-defaults
travis_fold end "XCode Python CLI Installation"


# Homebrew Python version
travis_fold start "Homebrew Python CLI Installation"
echo Homebrew Python CLI Installation
python3 --version
pip3 install -U pip
pip3 install -U virtualenv
rm -rf /Users/travis/lib/oracle-cli
brew update python
virtualenv -p python3 cli-3
source cli-3/bin/activate
source $TRAVIS_BUILD_DIR/scripts/install/install.sh --accept-all-defaults
deactivate
travis_fold end "Homebrew Python CLI Installation"

# Official Python version
travis_fold start "Official Python CLI Installation"
echo Official Python CLI Installation
rm -rf /Users/travis/lib/oracle-cli
OPENSSL_DIR=$((brew info openssl | grep "/usr/local/Cellar") | cut -d' ' -f1)
curl -OL http://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar xzvf Python-3.7.5.tgz
cd Python-3.7.5
./configure --prefix=/usr/local --with-openssl=${OPENSSL_DIR} --enable-shared
make
make install
cd ..
source $TRAVIS_BUILD_DIR/scripts/install/install.sh --accept-all-defaults
travis_fold end "Official Python CLI Installation"
