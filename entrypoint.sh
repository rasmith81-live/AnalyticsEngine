#!/bin/sh
set -e

CERTS_DIR="/certs"
CERT_FILE="${CERTS_DIR}/server.crt"
KEY_FILE="${CERTS_DIR}/server.key"

# Check if certs exist and generate them if they don't
if [ ! -f "$CERT_FILE" ] || [ ! -f "$KEY_FILE" ]; then
    echo "Certificates not found. Generating new self-signed certificates..."
    
    mkdir -p "$CERTS_DIR"
    
    # Updated DNS names to match docker-compose.yml services
    DNS_NAMES="DNS:localhost,DNS:host.docker.internal"
    DNS_NAMES="${DNS_NAMES},DNS:api_gateway"
    DNS_NAMES="${DNS_NAMES},DNS:database_service"
    DNS_NAMES="${DNS_NAMES},DNS:messaging_service"
    DNS_NAMES="${DNS_NAMES},DNS:archival_service"
    DNS_NAMES="${DNS_NAMES},DNS:observability_service"
    DNS_NAMES="${DNS_NAMES},DNS:business_metadata"
    DNS_NAMES="${DNS_NAMES},DNS:calculation_engine_service"
    DNS_NAMES="${DNS_NAMES},DNS:demo_config_service"
    DNS_NAMES="${DNS_NAMES},DNS:connector_service"
    DNS_NAMES="${DNS_NAMES},DNS:ingestion_service"
    DNS_NAMES="${DNS_NAMES},DNS:metadata_ingestion_service"
    DNS_NAMES="${DNS_NAMES},DNS:conversation_service"
    DNS_NAMES="${DNS_NAMES},DNS:systems_monitor"
    DNS_NAMES="${DNS_NAMES},DNS:entity_resolution_service"
    DNS_NAMES="${DNS_NAMES},DNS:data_governance_service"
    DNS_NAMES="${DNS_NAMES},DNS:machine_learning_service"
    DNS_NAMES="${DNS_NAMES},DNS:timescaledb"
    DNS_NAMES="${DNS_NAMES},DNS:redis"
    DNS_NAMES="${DNS_NAMES},DNS:azurite"
    DNS_NAMES="${DNS_NAMES},DNS:prometheus-pushgateway"

    openssl req -x509 -newkey rsa:4096 -sha256 -days 365 -nodes \
        -keyout "$KEY_FILE" -out "$CERT_FILE" \
        -subj "/CN=AnalyticsEngineDev" \
        -addext "subjectAltName = $DNS_NAMES"
else
    echo "Certificates found. Skipping generation."
fi

# Set correct permissions for the certificate files if they exist
if [ -f "$KEY_FILE" ] && [ -f "$CERT_FILE" ]; then
    # We check if we are running as root before trying to chown
    if [ "$(id -u)" = "0" ]; then
        if [ "$(stat -c '%U' /certs/server.key)" != "appuser" ]; then
            echo "Setting certificate permissions..."
            chown appuser:appuser /certs/server.key /certs/server.crt
            chmod 600 /certs/server.key /certs/server.crt
            echo "Certificate permissions set."
        else
            echo "Certificate permissions are already correct."
        fi
    fi
fi

# Execute the command passed to this script as the non-root user
exec gosu appuser "$@"
