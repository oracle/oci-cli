#!/bin/bash

# Change our formula for GitHub
formula=${TRAVIS_BUILD_DIR}/ocicli.rb
sed -i '' "s@url.*@url \"https://github.com/oracle/oci-cli/archive/${version}.tar.gz\"@g" ${formula}
awk '/url.*$/ { printf("%s", $0); next } 1' ocicli.rb > tmp && mv tmp ${formula}
sed -i '' "s@.*url.*@${url}@g" ${formula}

sed -i '' "s@.*url.*@${url}  sha256 \"${SHA256}\"@g" ${formula}
awk '{sub(/  sha256/,"\n  sha256");}1' ocicli.rb > tmp && mv tmp ${formula}