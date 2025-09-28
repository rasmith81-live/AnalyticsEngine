param(
    [Parameter(Mandatory = $true)]
    [string]$ServiceName,

    [switch]$Force
)

# Set PYTHONPATH to the project root to ensure module resolution.
$projectRoot = (Resolve-Path "$PSScriptRoot/../..").Path
$env:PYTHONPATH = $projectRoot
Write-Host ('[INFO] PYTHONPATH set to: {0}' -f $env:PYTHONPATH)

$ErrorActionPreference = "Stop"

$ServiceName = $ServiceName.ToLower()
$VersionSchema = "alembic_$ServiceName"

if (-not $Force) {
    Write-Host ('[WARNING] This will drop and recreate the ''{0}'' schema and remove revisions.' -f $ServiceName)
    Write-Host 'Press any key to continue or Ctrl+C to cancel...'
    $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | Out-Null
}

Write-Host ('[INFO] Resetting migrations and schema for service: {0}' -f $ServiceName)

docker-compose down

# Clean .pyc
Get-ChildItem -Recurse -Include *.pyc | Remove-Item -Force -ErrorAction SilentlyContinue

docker-compose up -d timescaledb redis

Start-Sleep -Seconds 2

# Load environment variables from .env file
$envFilePath = Join-Path $projectRoot ".env"
if (Test-Path $envFilePath) {
    Get-Content $envFilePath | ForEach-Object {
        if ($_ -match '^(?!#)([^=]+)=(.*)') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim()
            [System.Environment]::SetEnvironmentVariable($key, $value, 'Process')
        }
    }
    Write-Host "[INFO] Loaded environment variables from .env file."
} else {
    Write-Error "[FATAL] .env file not found at '$envFilePath'. Aborting."
    exit 1
}

Write-Host "[INFO] Executing schema reset against the 'timescaledb' container..."

Write-Host "[INFO] Dropping and recreating service schema: $ServiceName"
& docker-compose exec -T -e "PGPASSWORD=$($env:POSTGRES_PASSWORD)" timescaledb psql -v ON_ERROR_STOP=1 --host timescaledb --username $($env:POSTGRES_USER) --dbname $($env:POSTGRES_DB) -c "DROP SCHEMA IF EXISTS $ServiceName CASCADE; CREATE SCHEMA IF NOT EXISTS $ServiceName;"
if (-not $?) {
    Write-Error "[FATAL] Failed to drop/create service schema '$ServiceName'. Aborting."
    exit 1
}

Write-Host "[INFO] Dropping and recreating version schema: $VersionSchema"
& docker-compose exec -T -e "PGPASSWORD=$($env:POSTGRES_PASSWORD)" timescaledb psql -v ON_ERROR_STOP=1 --host timescaledb --username $($env:POSTGRES_USER) --dbname $($env:POSTGRES_DB) -c "DROP SCHEMA IF EXISTS $VersionSchema CASCADE; CREATE SCHEMA IF NOT EXISTS $VersionSchema;"
if (-not $?) {
    Write-Error "[FATAL] Failed to drop/create version schema '$VersionSchema'. Aborting."
    exit 1
}

Write-Host ('[SUCCESS] Schema reset for {0} completed.' -f $ServiceName)

# Optional commit prompt
if (-not $Force) {
    $commit = Read-Host "Would you like to git commit the new revision now? (y/n)"
    if ($commit -eq "y") {
        git add alembic/versions/$ServiceName/
        git commit -m "[Reset] Migration reset for $ServiceName"
        git push
    }
}