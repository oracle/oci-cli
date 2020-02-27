#!/bin/bash

echo ${version}
git config credential.helper 'cache --timeout=120'
git config user.email "kernlee23@gmail.com"
git config user.name "kernleee"
git checkout homebrew-ocicli
git add .
git commit -m "Releasing version ${version} [ci skip]"
# Push quietly to prevent showing the token in log
git push https://${GITHUB_USERNAME}:${GITHUB_PAT}@github.com/oracle/oci-cli.git homebrew-ocicli -f