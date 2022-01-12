#!/bin/bash

set -s -u

trap "exit" SIGHUP SIGINT SIGTERM

while :; do
    certbot renew --post-hook "docker restart ROUTER_CONTAINER_NAME_PLACEHOLDER"
    echo "Certbot renewal attempt is done, going sleep..."
    sleep 12h
done
