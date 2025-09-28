param(
    [Parameter(Mandatory=$true)]
    [string]$ServiceName,

    [string]$Revision = "head"
)

$ErrorActionPreference = "Stop"

# Helper function for timestamped logging
function Log($level, $message) {
    $now = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
    Write-Host "[$now][$level] $message"
}

# 1. Pre-upgrade sanity check
Log "INFO" "Performing pre-upgrade sanity checks for service: '$ServiceName'"
docker-compose ps $ServiceName | Out-Null
if ($LASTEXITCODE -ne 0) {
    Log "ERROR" "Container for service '$ServiceName' is not running or is misconfigured."
    exit 1
}
Log "INFO" "Container check passed."

# Set PYTHONPATH to the project root to ensure module resolution.
$projectRoot = (Resolve-Path "$PSScriptRoot/../..").Path
$env:PYTHONPATH = $projectRoot
Log "INFO" ("PYTHONPATH set to: {0}" -f $env:PYTHONPATH)

# Get the original async DATABASE_URL from the .env file
$envFile = Join-Path $projectRoot ".env"
if (-not (Test-Path $envFile)) {
    Log "ERROR" ".env file not found at project root: $envFile"
    exit 1
}
$dbUrlLine = Get-Content $envFile | Select-String "DATABASE_URL="
$originalDbUrl = ($dbUrlLine -split '=', 2)[1].Trim()

# Create the synchronous URL for Alembic by replacing the driver
$syncDbUrl = $originalDbUrl.Replace("+asyncpg", "+psycopg2")
Log "INFO" "Using synchronous DATABASE_URL for Alembic: $syncDbUrl"

# 2. Run the upgrade
$upgradeCmd = "docker-compose run --rm -e SERVICE_NAME=$ServiceName -e DATABASE_URL=$syncDbUrl $ServiceName alembic -x branch=$ServiceName upgrade $Revision"
Log "INFO" ("Applying migration for service: '{0}' to revision: '{1}'" -f $ServiceName, $Revision)
Log "RUNNING" $upgradeCmd

Invoke-Expression $upgradeCmd

if ($LASTEXITCODE -ne 0) {
    Log "ERROR" ("Alembic upgrade failed for service: '{0}'" -f $ServiceName)
    exit $LASTEXITCODE
}

Log "SUCCESS" "Alembic upgrade command completed for service: '$ServiceName'"

# 3. Post-upgrade verification
$revCmd = "docker-compose run --rm -e SERVICE_NAME=$ServiceName -e DATABASE_URL=$syncDbUrl $ServiceName alembic -x branch=$ServiceName current"
Log "INFO" "Verifying revision with: $revCmd"
Invoke-Expression $revCmd

if ($LASTEXITCODE -ne 0) {
    Log "ERROR" ("Post-upgrade verification failed for service: '{0}'" -f $ServiceName)
    exit $LASTEXITCODE
}

Log "SUCCESS" "Database for '$ServiceName' is confirmed at the latest revision."
exit 0
