#!/bin/bash

set -e

start_time='2018-09-27T00:00:00Z'
end_time='2018-09-27T02:00:00Z'

{
    result=$(oci audit event list --all --stream-output --compartment-id ${COMPARTMENT_ID} --start-time ${start_time} --end-time ${end_time})
    event_count=$(echo $result | jq '[.data] | .[] | length')
} || {
    echo "Could not retrieve or parse audit event list."
    echo $result
    exit 1
}
if [ ${event_count} -le 0 ];then
    echo "No audit events were retrieved."
    exit 1
fi

i=0
while [ $i -lt $event_count ] && [ $i -lt 5 ];do
    event=$(echo "${result}" | jq "[.data] | .[][$i]")
    event_time=$(echo $event | jq '."event-time"')
    if [[ $event_time =~ 2018-09-27.* ]];then
        event_name=$(echo $event | jq '."event-name"')
        event_source=$(echo $event | jq '."event-source"')
        credential_id=$(echo $event | jq '."credential-id"')
    else
        echo "event-time, $event_time, is not valid."
        exit 1
    fi
    i=$((i+1))
done

echo "$(basename "$0") complete"
