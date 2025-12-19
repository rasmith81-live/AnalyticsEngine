<#
.SYNOPSIS
    Prepares the environment for hybrid debugging of a specific service.

.DESCRIPTION
    This script starts all services defined in docker-compose.yml but stops the specified target service.
    This allows you to run the target service locally (e.g., in VS Code debugger) while it interacts with
    containerized dependencies (DB, Redis, other microservices).

.PARAMETER ServiceName
    The name of the service to debug (as defined in docker-compose.yml).

.PARAMETER NoDeps
    If set, only starts the specified service's dependencies (requires parsing compose file - simplistic version starts all others).

.EXAMPLE
    .\debug_service.ps1 -ServiceName calculation_engine_service

#>

param (
    [Parameter(Mandatory=$true)]
    [string]$ServiceName,
    [switch]$Reset,
    [switch]$UseMocks
)

$ErrorActionPreference = "Stop"

# Service Port Mapping (from docker-compose.yml)
$ServicePorts = @{
    "database_service"           = 8000
    "messaging_service"          = 8001
    "archival_service"           = 8005
    "observability_service"      = 8080
    "systems_monitor"            = 8010
    "entity_resolution_service"  = 8012
    "data_governance_service"    = 8013
    "machine_learning_service"   = 8014
    "business_metadata"          = 8020
    "calculation_engine_service" = 8021
    "demo_config_service"        = 8022
    "connector_service"          = 8023
    "ingestion_service"          = 8024
    "metadata_ingestion_service" = 8025
    "conversation_service"       = 8026
    "api_gateway"                = 8090
    "redis"                      = 6379
    "timescaledb"                = 5432
    "azurite"                    = 10000
    "mock_service"               = 8099
}

function Write-Log {
    param ([string]$Message)
    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message" -ForegroundColor Cyan
}

# 1. Validation
if (-not (Test-Path "docker-compose.yml")) {
    Write-Error "docker-compose.yml not found in current directory."
}

# 2. Reset if requested
if ($Reset) {
    Write-Log "Stopping and removing all containers..."
    docker-compose down
}

# 3. Determine Compose Files
$ComposeFiles = "-f docker-compose.yml"
if ($UseMocks) {
    if (Test-Path "docker-compose.mock.yml") {
        Write-Log "Enabling Mock Services..."
        $ComposeFiles += " -f docker-compose.mock.yml"
    } else {
        Write-Warning "docker-compose.mock.yml not found. Ignoring -UseMocks."
    }
}

# 4. Start all services
Write-Log "Starting services with: docker-compose $ComposeFiles up -d"
Invoke-Expression "docker-compose $ComposeFiles up -d"

# 5. Stop the target service
Write-Log "Stopping target service '$ServiceName' to allow local debugging..."
docker-compose stop $ServiceName

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to stop service '$ServiceName'. Check if the name matches an entry in docker-compose.yml."
}

# 6. Output guidance and Env Vars
Write-Log "Environment ready for hybrid debugging."
Write-Host "----------------------------------------------------------------" -ForegroundColor Green
Write-Host "Target Service: $ServiceName (Stopped in Docker)" -ForegroundColor Yellow
Write-Host "Dependencies:   RUNNING (Docker)" -ForegroundColor Green
if ($UseMocks) {
    Write-Host "Mocks:          ENABLED (Port $($ServicePorts['mock_service']))" -ForegroundColor Magenta
}
Write-Host ""
Write-Host "Use the following Environment Variables for your local debugger:" -ForegroundColor Cyan
Write-Host "(Copy and paste into your .env file or launch.json)" -ForegroundColor Gray
Write-Host ""

# Generate suggested env vars based on common patterns
# This is a heuristic - it assumes services follow standard naming for URL vars
foreach ($service in $ServicePorts.Keys) {
    if ($service -ne $ServiceName) {
        $port = $ServicePorts[$service]
        $envVarName = $service.ToUpper() + "_URL"
        # Handle special cases
        if ($service -eq "business_metadata") { $envVarName = "METADATA_SERVICE_URL" }
        if ($service -eq "redis") { 
            Write-Host "REDIS_URL=redis://localhost:$port" 
            continue
        }
        if ($service -eq "timescaledb") {
            Write-Host "DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:$port/analytics"
            continue
        }
        
        Write-Host "$envVarName=http://localhost:$port"
    }
}

Write-Host ""
Write-Host "----------------------------------------------------------------"
