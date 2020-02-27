#!/bin/bash

# OCI CLI brew formula directory
formula=/usr/local/Homebrew/Library/Taps/kern-lee/homebrew-oci-cli/ocicli.rb
formula_directory=/usr/local/Homebrew/Library/Taps/kern-lee/homebrew-oci-cli
echo ${formula}
chmod -R 777 ${formula}

# Get latest CLI release from github and edit brew formula
export version=$(curl --silent -u ${GITHUB_USERNAME}:${GITHUB_PAT} "https://api.github.com/repos/oracle/oci-cli/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
echo ${version}
sed -i '' "s@url.*@url \"https://github.com/oracle/oci-cli/archive/${version}.tar.gz\"@g" ${formula}
export url=$(grep "url" ${formula})
echo ${url}
awk '/url.*$/ { printf("%s", $0); next } 1' ${formula} > tmp && mv tmp ${formula}
sed -i '' "s@.*url.*@${url}@g" ${formula}

# Get SHA256 of the tar and edit brew formula
export SHA256=$(brew fetch ocicli --build-from-source | grep "SHA256:" -m 1 | sed 's/^.*: //')
echo ${SHA256}
sed -i '' "s@.*url.*@${url}  sha256 \"${SHA256}\"@g" ${formula}
awk '{sub(/  sha256/,"\n  sha256");}1' ${formula} > tmp && mv tmp ${formula}

# Upgrade ocicli to latest release and test
brew upgrade ocicli
brew test ocicli
brew audit --strict --online ocicli