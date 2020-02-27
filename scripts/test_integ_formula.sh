#!/bin/bash

key_loc=~/.oci/key.pem
mkdir ~/.oci

# Make the private key from our hidden environment variable
echo "${PRIVATE_KEY}" > ${key_loc}
tr ' ' '\n' < ${key_loc} > tmp && mv tmp ${key_loc}
sed -i '' '1i\
-----BEGIN RSA PRIVATE KEY-----\
' ${key_loc}
sed -i '' -e '$a\
-----END RSA PRIVATE KEY-----\
' ${key_loc}

# Run the config setup for oci
printf "~/.oci/config\n${USER_OCID}\n${TENANT_OCID}\n${REGION}\nn\n${key_loc}" | oci setup config

# Try a CLI command with response
ad_list=$(oci iam availability-domain list)
echo ${ad_list}
ad_list=$(oci iam availability-domain list | jq '.data')
if [[ -n "${ad_list}" ]];then
  exit 1
fi

# Delete our config and private key
rm -r ~/.oci
