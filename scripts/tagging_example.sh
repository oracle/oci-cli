#!/bin/bash
# This script provides an example of how use tags in the CLI in terms of:
#
#   - Managing tag namespaces and tags by performing create, read (get/list) and update operations on them
#   - Applying tags to resources
#
# Requirements for running this script:
#   - OCI CLI v2.4.14 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

TENANCY_ID=""  # Your tenancy ID
COMPARTMENT_ID=""  # Your compartment OCID
TAG_NAMESPACE_NAME="cli_example_tag_ns1" # As of the time of writing, upper case characters aren't allowed in the namespace name

##########################################################
# Tag namespace and tag create, read/list and update
##########################################################
echo "Creating Tag Namespace"
CREATED_TAG_NAMESPACE=$(oci iam tag-namespace create -c $COMPARTMENT_ID --name $TAG_NAMESPACE_NAME --description "A description of the tag namespace")
TAG_NAMESPACE_ID=$(jq -r '.data.id' <<< "$CREATED_TAG_NAMESPACE")
echo "Tag Namespace OCID: ${TAG_NAMESPACE_ID}"

# When we reference individual tags, we'll do so via their names rather than their IDs. However, for tag
# namespaces when managing tags we reference them via their OCID
echo "Creating first tag"
TAG_ONE_NAME="cli_example_tag_1"
oci iam tag create --tag-namespace-id $TAG_NAMESPACE_ID --name $TAG_ONE_NAME --description "A description of the tag"

echo "Creating second tag"
TAG_TWO_NAME="cli_example_tag_2"
oci iam tag create --tag-namespace-id $TAG_NAMESPACE_ID --name $TAG_TWO_NAME --description "A description of the tag"

# We can retrieve individual namespaces
echo "Getting tag namespace"
oci iam tag-namespace get --tag-namespace-id $TAG_NAMESPACE_ID

# We can list tag namespaces. Since this is a paginated list operation, if we want to see everything (rather than just a 
# single page of results) we can pass the --all option
echo "Listing tag namespaces in compartment $COMPARTMENT_ID"
oci iam tag-namespace list -c $COMPARTMENT_ID --all

# We can use --include-subcompartments to, for example, see namespaces defined at the root of the tenancy and
# in all compartments of the tenancy.
#
# Once again, since this is a paginated list operation we can use --all to get all the results rather than
# just a single page of results
echo "Listing tag namespaces in tenancy and sub-compartments"
oci iam tag-namespace list -c $TENANCY_ID --include-subcompartments true --all

# We can also use jq filters to only get non-retired namespaces. The filter here is:
#
#   - .data gives us the array with all the namespaces and we pipe that to select()
#   - inside the select(), .[]."is-retired" == false goes through each array element and checks if the is-retired attribute
#     is false. Note that we quote "is-retired" so that it is treated as the full attribute name
echo "Listing all non-retired tag namespaces in tenancy and sub-compartments"
ALL_TAG_NAMESPACES=$(oci iam tag-namespace list -c $TENANCY_ID --include-subcompartments true --all)
jq -r '.data | map(select(."is-retired" == false))' <<< "$ALL_TAG_NAMESPACES"

echo "Listing tags in a namespace"
oci iam tag list --tag-namespace-id $TAG_NAMESPACE_ID --all

echo "Retire tag namespace"
oci iam tag-namespace retire --tag-namespace-id $TAG_NAMESPACE_ID

echo "Listing tags in the namespace. Retiring a namespace retires all the tags in the namespace as well"
oci iam tag list --tag-namespace-id $TAG_NAMESPACE_ID --all

echo "Reactivating tag namespace"
oci iam tag-namespace reactivate --tag-namespace-id $TAG_NAMESPACE_ID

echo "Listing tags in the namespace. Note that reactivating the namespace does not reactivate the tags in that namespace, we need to do that individually"
oci iam tag list --tag-namespace-id $TAG_NAMESPACE_ID --all

echo "Reactivating tags"
oci iam tag reactivate --tag-namespace-id $TAG_NAMESPACE_ID --tag-name $TAG_ONE_NAME
oci iam tag reactivate --tag-namespace-id $TAG_NAMESPACE_ID --tag-name $TAG_TWO_NAME

echo "Retiring an individual tag"
oci iam tag retire --tag-namespace-id $TAG_NAMESPACE_ID --tag-name $TAG_ONE_NAME

echo "Reactivating the tag (again)"
oci iam tag reactivate --tag-namespace-id $TAG_NAMESPACE_ID --tag-name $TAG_ONE_NAME

# This operation can also be used to assign tags to the namespace using the --defined-tags and --freeform-tags
# parameters. We will see how these parameters are used later in the script, so for now we just update the
# description
echo "Updating tag namespace description"
oci iam tag-namespace update --tag-namespace-id $TAG_NAMESPACE_ID --description "An updated description"

# We can also update tag descriptions. Similar to tag namespaces, this operation can also be used to assign
# tags to the tag using the --defined-tags and --freeform-tags parameters
echo "Updating tag $TAG_ONE_NAME description"
oci iam tag update --tag-namespace-id $TAG_NAMESPACE_ID --tag-name $TAG_ONE_NAME --description "An updated description"

# If we create/update and then try to use tags straight away, sometimes we can get a 404. To try and avoid this, the script
# adds a short delay between the tag management operations and using the tags on resources
sleep 15

##########################################################
# Assigning tags to resources
# ---------------------------
# We can assign freeform tags (simple key-value pairs with no predefined tags or namespaces) to a resource. We
# can also assign defined tags (which need to reference a valid namespace and tags in that namespace).
#
# For either of these, we need to pass in their input as JSON to the CLI. This is possible via text on the command
# line but it is generally easier to pass these in from files; this also avoids having to escape text on the command
# line. In the below examples, we show how to pass the input as files via the file:// syntax for JSON parameters.
#
# More information on tagging can be found here: https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm
#
# Resources in the CLI which accept tags will have --freeform-tags and --defined-tags parameters. Consult the CLI
# help (https://github.com/oracle/oci-cli/blob/master/tests/output/inline_help_dump.txt) or the generic tag
# reference (https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Taggable) to
# see what resources can accept tags
##########################################################

# First prepare a JSON file for our defined tags. The structure of the file is:
#
# {
#     "<tag namespace name>": {
#         "<tag name>": "<tag value>",
#         "<tag name>": "<tag value>",
#     }
# }
# 
# Note that it should be possible to specify multiple tag namespaces in the same JSON file, in which case
# the file would look similar to:
# {
#     "<tag namespace name>": {
#         "<tag name>": "<tag value>",
#         "<tag name>": "<tag value>"
#     },
#     "<another tag namespace name>": {
#         "<tag name>": "<tag value>",
#         "<tag name>": "<tag value>"
#     }
# }
#
# Note, also, that in this input we use tag namespace names and tag names rather than OCIDs
mkdir scripts/temp
echo "{\"$TAG_NAMESPACE_NAME\": {\"$TAG_ONE_NAME\": \"some tag value\", \"$TAG_TWO_NAME\": \"other value 55\"}}" >> scripts/temp/defined_tags_1.json

# Note that we pass the JSON  via the file:// syntax. Also, the defined_tags_1.json file references the namespace and
# tags creted earlier in this example script, but the freeform_tags_1.json file just contains keys and values - since
# these are freeform they don't have to reference any existing namespace or tags
echo "Creating VCN with tags"
CREATED_VCN_WITH_TAGS=$(oci network vcn create \
-c $COMPARTMENT_ID --display-name cli_tagging_example \
--cidr-block 10.0.0.0/16 --dns-label clitagex \
--freeform-tags file://scripts/tagging_example/freeform_tags_1.json \
--defined-tags file://scripts/temp/defined_tags_1.json \
--wait-for-state AVAILABLE 2>/dev/null)
jq -r '.' <<< "$CREATED_VCN_WITH_TAGS"
VCN_ID=$(jq -r '.data.id' <<< "$CREATED_VCN_WITH_TAGS")

# Here we list all the VCNs and pipe it to jq with a filter so that only those with the DNS label applied to
# our example VCN are displayed
echo "We can list resources and see their tags"
oci network vcn list -c $COMPARTMENT_ID --all | jq -r '.data | map(select(."dns-label" == "clitagex"))'

# Prepare a defined tags file with different values
echo "{\"$TAG_NAMESPACE_NAME\": {\"$TAG_ONE_NAME\": \"some different value\"}}" > scripts/temp/defined_tags_2.json

# We can update defined tags and freeform tags. Note that this does a full replacement of the current values
# for those fields. If the --force option is not provided, you'll be prompted as to wheter you wish to proceed
# or not
echo "Update VCN and replace its current tags with different tags"
oci network vcn update --vcn-id $VCN_ID \
    --defined-tags file://scripts/temp/defined_tags_2.json \
    --freeform-tags file://scripts/tagging_example/freeform_tags_2.json \
    --force

# If we know that the tags from one resource need to be applied to another resource, we can extract those 
# by using jq, save that to a file then then use those generated files as input to another CLI command
#
# We can do this by grabbing it from a Get operation (the first command shown), or by taking the 
# value from a list (the second command shown)
oci network vcn get --vcn-id $VCN_ID | jq -r '.data."freeform-tags"' > scripts/temp/freeform_tags_copy.json

# This grabs the defined tags from the first element in the list of VCNs with the dns-label of clitagex. 
oci network vcn list -c $COMPARTMENT_ID --all | jq -r '.data | map(select(."dns-label" == "clitagex")) | .[0]."defined-tags"' > scripts/temp/defined_tags_copy.json

echo "Creating VCN with tags copied from another resource"
SECOND_CREATED_VCN_WITH_TAGS=$(oci network vcn create \
-c $COMPARTMENT_ID --display-name cli_tagging_example \
--cidr-block 10.0.0.0/16 --dns-label clitagex2 \
--freeform-tags file://scripts/temp/freeform_tags_copy.json \
--defined-tags file://scripts/temp/defined_tags_copy.json \
--wait-for-state AVAILABLE 2>/dev/null)
jq -r '.' <<< "$SECOND_CREATED_VCN_WITH_TAGS"
SECOND_VCN_ID=$(jq -r '.data.id' <<< "$SECOND_CREATED_VCN_WITH_TAGS")

# Since updating tags does a complete overwrite, if we want to preserve the existing tags and just add some new
# ones we either need:
#
#   1) Input which has been prepared elsewhere that contains the tags we need (e.g. we have created a file in
#      a text editor which contains the existing + new tags which we want to apply)
#   2) We can use jq to prepare input on the fly which contains the existing tags plus the new tags we wish
#      to apply
#
# Here we demonstrate how to do (2). The process (which we'll do on freeform and defined tags is):
#
#   - Get the resource and use jq to pull its existing tags into a file
#   - Create a new file which has merged the existing tags and new tags using jq's * operator. We choose
#     * because it can do recursive merges, which is needed for defined tags since they contain JSON objects
#     inside JSON objects. For freeform tags, since they are just key-value (i.e. just a "simple" JSON object)
#     we could use jq's + operator as we don't need a recursive merge. Using * for both scenarios is fine, though
#
oci network vcn get --vcn-id $VCN_ID | jq -r '.data."defined-tags"' > scripts/temp/defined_tags_current.json

# We use jq's -s switch (slurp) here to read the two files into a single array which contains two JSON objects
# and then run our merge via *. Array element [0] is the first file (defined_tags_current.json) and [1] is the
# second file (defined_tags_1.json). We'll then output our merged object to a file so that it can be used in
# subsequent commands
# 
# NOTE: If we find the same key between two pieces of input, the input on the right hand side will "win". This
# has implications for preserving or overwriting existing tags when producing our merged file:
#
#   - If we want to update tag values (as well as add new tags) then the file containing current tags should be
#     on the left hand side of the *
#   - If we want to add new tags but preserve any existing tag values then the file containing current tags
#     should be on the right hand side of the *
jq -s '.[1] * .[0]' scripts/temp/defined_tags_current.json scripts/temp/defined_tags_1.json > scripts/temp/defined_tags_merged.json

echo "Updating resource with merged defined tags"
oci network vcn update --vcn-id $VCN_ID --defined-tags file://scripts/temp/defined_tags_merged.json --force

oci network vcn get --vcn-id $VCN_ID | jq -r '.data."freeform-tags"' > scripts/temp/freeform_tags_current.json
jq -s '.[0] * .[1]' scripts/temp/freeform_tags_current.json scripts/tagging_example/freeform_tags_1.json > scripts/temp/freeform_tags_merged.json

echo "Updating resource with merged freeform tags"
oci network vcn update --vcn-id $VCN_ID --freeform-tags file://scripts/temp/freeform_tags_merged.json --force

# We can remove tags from a resource by passing an empty JSON object {} as the tag input
echo "Removing tags from resource"
oci network vcn update --vcn-id $VCN_ID --freeform-tags '{}' --defined-tags '{}' --force

# Now we do some cleanup by deleting the VCNs we created and retiring the tag namespace (remember that this
# will also retire tags in that namespace)

echo "Deleting VCNs"
oci network vcn delete --vcn-id $VCN_ID --force
oci network vcn delete --vcn-id $SECOND_VCN_ID --force

echo "Retiring tag namespace"
oci iam tag-namespace retire --tag-namespace-id $TAG_NAMESPACE_ID

echo "Listing tags in the namespace to confirm they have been retired"
oci iam tag list --tag-namespace-id $TAG_NAMESPACE_ID --all

echo "DONE"