#!/bin/bash

set -euo pipefail

SERVICE_NAME=$1
COMMAND=${2:-upgrade}
TARGET=${3:-"$SERVICE_NAME@head"}

if [[ -z "$SERVICE_NAME" ]]; then
  echo "[ERROR] Usage: $0 <service_name> [command] [target]"
  exit 1
fi

echo "[INFO] Running Alembic '$COMMAND' for service: $SERVICE_NAME"
echo "[INFO] Target: $TARGET"

docker-compose run --rm \
  -e SERVICE_NAME=$SERVICE_NAME \
  $SERVICE_NAME \
  alembic -x branch=$SERVICE_NAME current

docker-compose run --rm \
  -e SERVICE_NAME=$SERVICE_NAME \
  $SERVICE_NAME \
  alembic -x branch=$SERVICE_NAME "$COMMAND" $TARGET

if [[ "$COMMAND" == "upgrade" || "$COMMAND" == "downgrade" ]]; then
  docker-compose run --rm \
    -e SERVICE_NAME=$SERVICE_NAME \
    $SERVICE_NAME \
    alembic -x branch=$SERVICE_NAME current
fi

echo "[SUCCESS] Alembic command '$COMMAND' completed for $SERVICE_NAME"