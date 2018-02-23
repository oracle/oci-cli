#!/bin/bash
# This script provides an example of how to create a load balancer using the CLI. Two main ways to create a load balancer are shown:
#
#   - Creating a load balancer by providing all options at create time (e.g. certificates, listeners, backend sets)
#       - We also show two sub-variants: providing each option as an individual parameter (e.g. --certificiates, --listeners) and how to provide a consolidated
#         set of options using --from-json
#   - Creating a load balancer by providing the minimum options at create time and then adding related resources (e.g. certificates, listeners, backend sets)
#     post-creation
#
# Requirements for running this script:
#   - OCI CLI v2.4.13 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI
#   - OpenSSL (for certificate generation). This is not a strict requirement for normal CLI usage, just for this demo script
#   - demjson (http://deron.meranda.us/python/demjson/). This is not a strict requirement fpr normal CLI usage, it is just used to strip comments and explanatory notes from the example
#     input files which support this script

COMPARTMENT_ID=""  # Your compartment OCID
AVAILABILITY_DOMAIN_ONE="" # An availability domain, e.g. Uocm:IAD-AD-1
AVAILABILITY_DOMAIN_TWO="" # An availability domain, but different to AVAILABILITY_DOMAIN_TWO, e.g. Uocm:IAD-AD-2

CREATED_VCN=$(oci network vcn create -c $COMPARTMENT_ID --display-name createLbExampleVcn --cidr-block 10.0.0.0/16 --dns-label createLbExample --wait-for-state AVAILABLE 2>/dev/null)
VCN_ID=$(jq -r '.data.id' <<< "$CREATED_VCN")
echo "VCN OCID: ${VCN_ID}"

FIRST_CREATED_SUBNET=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN_ONE --display-name createLbSubnet --vcn-id $VCN_ID --dns-label subnetLb --cidr-block 10.0.0.0/24 --wait-for-state AVAILABLE 2>/dev/null)
FIRST_SUBNET_ID=$(jq -r '.data.id' <<< "$FIRST_CREATED_SUBNET")
echo "First Subnet OCID: $FIRST_SUBNET_ID"

SECOND_CREATED_SUBNET=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN_TWO --display-name createLbSubnet2 --vcn-id $VCN_ID --dns-label subnetLbTwo --cidr-block 10.0.1.0/24 --wait-for-state AVAILABLE 2>/dev/null)
SECOND_SUBNET_ID=$(jq -r '.data.id' <<< "$SECOND_CREATED_SUBNET")
echo "Second Subnet OCID: $SECOND_SUBNET_ID"

# We need to specify a shape when creating a load balancer. Here we are just picking the first shape
# we get from listing all the available shapes
LB_SHAPE=$(oci lb shape list -c $COMPARTMENT_ID | jq -r '.data[0].name')
echo "Load Balancer Shape: $LB_SHAPE"

# A function which creates a load balancer by providing all options at create time to the oci lb load-balancer create command. This command takes multiple complex parameters (complex
# parameters are those where the CLI expects JSON to be provided as input). For ease of use, the complex parameter input will be passed in from a file rather than trying to specify
# the strings on the command line
#
# This also provides each complex type as an individual option (e.g. --certificates, --listeners). It is also possible to provide these in a consolidated format, which is demonstrated
# by the function create_lb_with_all_options_using_from_json
function create_lb_with_all_options_as_individual_options() {
    # certificates_with_comments.json contains a description of the parameter. Since valid JSON cannot contain comments, we use jsonlint (which was installed
    # via our demjson dependency) to remove the comments and allow the CLI to use it.
    #
    # You should replace the values in certificates_with_comments.json with those appropriate for your use case (e.g. your own PEM-formatted strings)
    jsonlint -Sf scripts/create_load_balancer_example/certificates_with_comments.json > scripts/create_load_balancer_example/certificates.json

    jsonlint -Sf scripts/create_load_balancer_example/backend_sets_with_comments.json > scripts/create_load_balancer_example/backend_sets.json
    jsonlint -Sf scripts/create_load_balancer_example/listeners_with_comments.json > scripts/create_load_balancer_example/listeners.json
    # Path Route Sets are not mandatory parameter to load balancer. They enhance
    # load balancer feature set by providing traffic routing flexibility.
    # More info about the feature can be found in scripts/create_load_balancer_example/path_route_sets_with_comments.json
    jsonlint -Sf scripts/create_load_balancer_example/path_route_sets_with_comments.json > scripts/create_load_balancer_example/path_route_sets.json

    # Subnets are passed as a JSON array where each entry is a subnet OCID. For example:
    #
    #   ["ocid...", "ocid...", "ocid..."]
    #
    # Because we have these in variables already, we can pipe an array to a file and use that
    echo "[\"${FIRST_SUBNET_ID}\", \"${SECOND_SUBNET_ID}\"]" > scripts/create_load_balancer_example/subnets.json

    # Note here in our create we use --certificates, --listeners etc. to pass in each complex type
    #
    # There is some implicit sequencing in that:
    #   - The backend set information (--backend-sets) may need the name of the certificate bundle specified in --certificates
    #   - The listener information (--listeners) needs the name of one of the backend sets in --backend-sets
    #   - The listener information (--listeners) may need the name of the certificate bundle specified in --certificates
    #
    # So you need to take that into account when preparing your files for input
    CREATED_LB=$(oci lb load-balancer create -c $COMPARTMENT_ID --display-name exampleLb --shape-name $LB_SHAPE --subnet-ids file://scripts/create_load_balancer_example/subnets.json --certificates file://scripts/create_load_balancer_example/certificates.json --backend-sets file://scripts/create_load_balancer_example/backend_sets.json --listeners file://scripts/create_load_balancer_example/listeners.json --path-route-sets file://scripts/create_load_balancer_example/path_route_sets.json)
    WORK_REQUEST_ID=$(jq -r '."opc-work-request-id"' <<< "$CREATED_LB")
    echo "Create Load Balancer Work Request ID: $WORK_REQUEST_ID"

    # Creating a load balancer returns a work request. We can poll the work request to check when it completes. Once the work request
    # has completed, the load balancer is available
    WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
    WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
    echo "Work request status: $WORK_REQUEST_STATUS"
    while [[ $WORK_REQUEST_STATUS != "SUCCEEDED" ]]
    do
        WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
        WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
        echo "Work request status: $WORK_REQUEST_STATUS"
        sleep 60
    done

    # The work request will have the OCID of the load balancer in it
    LB_ID=$(jq -r '.data."load-balancer-id"' <<< "$WORK_REQUEST")
    echo "Load Balancer OCID: $LB_ID"

    # Print out information about the load balancer
    oci lb load-balancer get --load-balancer-id $LB_ID

    # Delete the load balancer, and sleep a bit to make sure it has been deleted
    oci lb load-balancer delete --load-balancer-id $LB_ID --force
    sleep 120
}

# We've seen in the create_lb_with_all_options_as_individual_options function that we can create a load balancer and provide complex parameters, such as --backend-sets,
# as separate options. However, rather than specifying complex parameters individually, we can supply them in a consolidated format - in this case by passing it in
# as a single file to the --from-json option.
#
# It is actually possible to not provide individual options to CLI commands at all and pass all parameters via --from-json, but for the purposes of this example we'll
# just show passing in the complex parameters
function create_lb_with_all_options_using_from_json() {
    jsonlint -Sf scripts/create_load_balancer_example/create_load_balancer_all_complex_params_with_comments.json > scripts/create_load_balancer_example/create_load_balancer_all_complex_params.json

    echo "[\"${FIRST_SUBNET_ID}\", \"${SECOND_SUBNET_ID}\"]" > scripts/create_load_balancer_example/subnets.json

    CREATED_LB=$(oci lb load-balancer create -c $COMPARTMENT_ID --display-name exampleLb --shape-name $LB_SHAPE --subnet-ids file://scripts/create_load_balancer_example/subnets.json --from-json file://scripts/create_load_balancer_example/create_load_balancer_all_complex_params.json)
    WORK_REQUEST_ID=$(jq -r '."opc-work-request-id"' <<< "$CREATED_LB")
    echo "Create Load Balancer Work Request ID: $WORK_REQUEST_ID"

    # Creating a load balancer returns a work request. We can poll the work request to check when it completes. Once the work request
    # has completed, the load balancer is available
    WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
    WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
    echo "Work request status: $WORK_REQUEST_STATUS"
    while [[ $WORK_REQUEST_STATUS != "SUCCEEDED" ]]
    do
        WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
        WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
        echo "Work request status: $WORK_REQUEST_STATUS"
        sleep 60
    done

    # The work request will have the OCID of the load balancer in it
    LB_ID=$(jq -r '.data."load-balancer-id"' <<< "$WORK_REQUEST")
    echo "Load Balancer OCID: $LB_ID"

    # Print out information about the load balancer
    oci lb load-balancer get --load-balancer-id $LB_ID

    # Delete the load balancer, and sleep a bit to make sure it has been deleted
    oci lb load-balancer delete --load-balancer-id $LB_ID --force
    sleep 120
}

function create_lb_with_minimum_then_add_related_resources() {
    echo "[\"${FIRST_SUBNET_ID}\", \"${SECOND_SUBNET_ID}\"]" > scripts/create_load_balancer_example/subnets.json

    # The minimum required information is the compartment, display name, load balancer shape, and subnets
    CREATED_LB=$(oci lb load-balancer create -c $COMPARTMENT_ID --display-name exampleLb --shape-name $LB_SHAPE --subnet-ids file://scripts/create_load_balancer_example/subnets.json)
    WORK_REQUEST_ID=$(jq -r '."opc-work-request-id"' <<< "$CREATED_LB")
    echo "Create Load Balancer Work Request ID: $WORK_REQUEST_ID"

    WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
    WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
    echo "Work request status: $WORK_REQUEST_STATUS"
    while [[ $WORK_REQUEST_STATUS != "SUCCEEDED" ]]
    do
        WORK_REQUEST=$(oci lb work-request get --work-request-id $WORK_REQUEST_ID)
        WORK_REQUEST_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$WORK_REQUEST")
        echo "Work request status: $WORK_REQUEST_STATUS"
        sleep 60
    done

    # Now that the load balancer is available, we can add certificates, listeners and backend sets. First
    # we'll need the load balancer's OCID so that we can use it in further commands. Remember that the OCID
    # can be obtained from the work request
    LB_ID=$(jq -r '.data."load-balancer-id"' <<< "$WORK_REQUEST")
    echo "Load Balancer OCID: $LB_ID"

    # Generate a self-signed certificate to use as part of our requests
    openssl req -newkey rsa:2048 -nodes -sha256 -keyout key.pem -x509 -days 365 -out certificate.pem -subj "/C=US/ST=WA/L=Seattle/O=Test/CN=www.example.com"

    # Here we add a certificate. Note that unlike providing it as part of the create operation, we specify the path to
    # the PEM files rather than providing the PEM-formatted strings themselves
    #
    # We can call the command multiple times to add multiple certificates
    oci lb certificate create --certificate-name my_cert_bundle --load-balancer-id $LB_ID --ca-certificate-file certificate.pem --private-key-file key.pem --public-certificate-file certificate.pem

    # Here we create a backend set and then add backends to it. Note that if we specify a SSL certificate then it should match the name we specified
    # as "oci lb certificate create"
    oci lb backend-set create --load-balancer-id $LB_ID \
        --name backendSetName \
        --policy ROUND_ROBIN \
        --health-checker-protocol HTTP \
        --health-checker-return-code 200 \
        --health-checker-url-path /healthcheck \
        --health-checker-interval-in-ms 60000 \
        --session-persistence-cookie-name myCookie \
        --session-persistence-disable-fallback false \
        --ssl-certificate-name my_cert_bundle \
        --ssl-verify-depth 3 \
        --ssl-verify-peer-certificate false

    # Now that we have our backend set, we can add backends to it by calling "oci lb backend create" multiple times
    oci lb backend create --load-balancer-id $LB_ID --backend-set-name backendSetName --ip-address 10.10.10.4 --port 80 --weight 3
    oci lb backend create --load-balancer-id $LB_ID --backend-set-name backendSetName --ip-address 10.10.10.5 --port 80 --weight 3

    # We can create Path Route Sets now since we have our backend set created.
    # Path Route Sets require backend sets to be mentioned as part of path route
    # rules. A path route set includes all path route strings and matching rules
    # that define the data routing for a particular listener. Path Route rules
    # enable routing of traffic to correct backend set eliminating the need to
    # create multiple listeners or load balancers to achieve the same.
    oci lb path-route-set create --load-balancer-id $LB_ID \
        --name PathRouteSetName \
        --path-routes '[{"backendSetName":"backendSetName", "path":"/video", "pathMatchType":{"matchType":"EXACT_MATCH"}}]' \
        --wait-for-state SUCCEEDED \
        --max-wait-seconds 300

    # Now that we have our certificates, backend set and path route set, we can add a listener. We need to specify a backend set which exists (e.g. the one we made)
    #
    # The valid values for --protocol can be found via "oci lb protocol list"
    #
    # If we specify a SSL certificate then it should match the name of a certificate we created via "oci lb certificate create"
    oci lb listener create --load-balancer-id $LB_ID \
        --default-backend-set-name backendSetName \
        --name myListener \
        --port 8080 \
        --protocol HTTP \
        --ssl-certificate-name my_cert_bundle \
        --ssl-verify-depth 3 \
        --ssl-verify-peer-certificate false \
        --path-route-set-name PathRouteSetName

    # Print out information about the load balancer
    oci lb load-balancer get --load-balancer-id $LB_ID

    # Delete the load balancer, and sleep a bit to make sure it has been deleted
    oci lb load-balancer delete --load-balancer-id $LB_ID --force
    sleep 120
}

create_lb_with_all_options_as_individual_options
create_lb_with_all_options_using_from_json
create_lb_with_minimum_then_add_related_resources

# Delete the subnets
oci network subnet delete --subnet-id $FIRST_SUBNET_ID --force --wait-for-state TERMINATED
oci network subnet delete --subnet-id $SECOND_SUBNET_ID --force --wait-for-state TERMINATED

# Delete the VCN
oci network vcn delete --vcn-id $VCN_ID --force --wait-for-state TERMINATED
