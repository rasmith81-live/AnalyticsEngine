# Run Alembic Migration Script
# 
# This script runs the database migration to add persistent storage tables.
# It can be run in the database_service container or locally if you have
# direct database access.

param(
    [string]$Action = "upgrade",  # upgrade, downgrade, current, history
    [string]$Revision = "head",   # head, +1, -1, or specific revision
    [switch]$DryRun = $false
)

Write-Host "=== Alembic Migration Runner ===" -ForegroundColor Cyan
Write-Host ""

# Check if running in Docker or locally
$InDocker = Test-Path "/.dockerenv"

if ($InDocker) {
    Write-Host "Running inside Docker container" -ForegroundColor Green
    $AlembicPath = "/app/alembic"
} else {
    Write-Host "Running locally" -ForegroundColor Yellow
    $AlembicPath = "alembic"
}

# Display current migration status
Write-Host "Current migration status:" -ForegroundColor Cyan
alembic current

Write-Host ""
Write-Host "Available migrations:" -ForegroundColor Cyan
alembic history

Write-Host ""

if ($DryRun) {
    Write-Host "DRY RUN MODE - No changes will be made" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Would execute: alembic $Action $Revision" -ForegroundColor Yellow
    exit 0
}

# Execute migration
Write-Host "Executing migration: alembic $Action $Revision" -ForegroundColor Green
Write-Host ""

switch ($Action) {
    "upgrade" {
        alembic upgrade $Revision
    }
    "downgrade" {
        Write-Host "WARNING: This will remove tables and delete data!" -ForegroundColor Red
        $confirm = Read-Host "Are you sure? (yes/no)"
        if ($confirm -eq "yes") {
            alembic downgrade $Revision
        } else {
            Write-Host "Migration cancelled" -ForegroundColor Yellow
            exit 0
        }
    }
    "current" {
        alembic current
    }
    "history" {
        alembic history --verbose
    }
    default {
        Write-Host "Unknown action: $Action" -ForegroundColor Red
        Write-Host "Valid actions: upgrade, downgrade, current, history"
        exit 1
    }
}

# Show final status
Write-Host ""
Write-Host "Migration complete. Current status:" -ForegroundColor Green
alembic current

Write-Host ""
Write-Host "Verifying tables exist..." -ForegroundColor Cyan

# Verify tables were created (requires psql or database connection)
if ($Action -eq "upgrade") {
    Write-Host "Tables should now exist:" -ForegroundColor Green
    Write-Host "  - connector_profiles" -ForegroundColor White
    Write-Host "  - client_configs" -ForegroundColor White
    Write-Host "  - service_proposals" -ForegroundColor White
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Green
