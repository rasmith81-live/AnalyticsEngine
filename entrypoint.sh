#!/bin/sh
set -e

CERTS_DIR="/certs"
CERT_FILE="${CERTS_DIR}/server.crt"
KEY_FILE="${CERTS_DIR}/server.key"

# Check if certs exist and generate them if they don't
if [ ! -f "$CERT_FILE" ] || [ ! -f "$KEY_FILE" ]; then
    echo "Certificates not found. Generating new self-signed certificates..."
    
    mkdir -p "$CERTS_DIR"
    
    DNS_NAMES="DNS:localhost,DNS:observability_service,DNS:api_gateway,DNS:database_service,DNS:messaging_service,DNS:service_a,DNS:service_b,DNS:archival_service,DNS:simulator_service,DNS:azurite,DNS:timescaledb,DNS:redis,DNS:azurite,DNS:prometheus-pushgateway"

    openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
        -keyout "$KEY_FILE" -out "$CERT_FILE" \
        -subj "/CN=multiMicroservicePatternDev" \
        -addext "subjectAltName = $DNS_NAMES"
else
    echo "Certificates found. Skipping generation."
fi

# Set correct permissions for the certificate files if they exist
if [ -f "$KEY_FILE" ] && [ -f "$CERT_FILE" ]; then
    if [ "$(stat -c '%U' /certs/server.key)" != "appuser" ]; then
        echo "Setting certificate permissions..."
        chown appuser:appuser /certs/server.key /certs/server.crt
        chmod 600 /certs/server.key /certs/server.crt
        echo "Certificate permissions set."
    else
        echo "Certificate permissions are already correct."
    fi
fi


# Execute the command passed to this script as the non-root user
exec gosu appuser "$@"
