param(
    [Parameter(Mandatory = $true)]
    [string]$ServiceName,
    [string]$Message,
    [switch]$AutoGenerate,
    [switch]$ShowHead
)

# Strict mode for better error handling
$ErrorActionPreference = "Stop"

# Helper function for consistent logging
function Write-Log {
    param(
        [string]$Level,
        [string]$LogMessage
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Level] $LogMessage"
}

# --- Script Start ---
Write-Log "INFO" "Starting revision creation for service: '$ServiceName'."

# 1. Define paths and set environment variables
$projectRoot = (Resolve-Path "$PSScriptRoot/../..").Path
$env:PYTHONPATH = $projectRoot
Write-Log "INFO" "PYTHONPATH set to: '$env:PYTHONPATH'"

$alembicIniPath = Join-Path $projectRoot "alembic.ini"
$tempAlembicIniPath = Join-Path $projectRoot "alembic.temp.ini"

# 2. Prepare Database URL
$envFile = Join-Path $projectRoot ".env"
if (-not (Test-Path $envFile)) {
    Write-Log "ERROR" ".env file not found at: '$envFile'"
    exit 1
}
$dbUrlLine = Get-Content $envFile | Select-String "DATABASE_URL="
$originalDbUrl = ($dbUrlLine -split '=', 2)[1].Trim()
$syncDbUrl = $originalDbUrl.Replace("+asyncpg", "+psycopg2")
Write-Log "INFO" "Using synchronous DATABASE_URL for Alembic."

# 3. Default commit message if not provided
if (-not $Message) {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $Message = "Auto-revision for $ServiceName at $timestamp"
    Write-Log "INFO" "Using default message: '$Message'"
}

# 4. Create Dynamic Alembic Configuration and execute

if ($ShowHead) {
    Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [INFO] Showing current DB head for service: '$ServiceName'"
    docker-compose run --rm --entrypoint bash $ServiceName -c "alembic heads"
    return
}

try {
    # Define the service-specific version path
    $versionLocations = "alembic/versions/$ServiceName"
    Write-Log "INFO" "Dynamically setting version_locations to '$versionLocations'"

    # Read the base config and intelligently insert the dynamic version locations setting
    $configLines = [System.Collections.ArrayList](Get-Content $alembicIniPath)
    $scriptLocationLine = "script_location = alembic"
    $insertIndex = -1
    for ($i = 0; $i -lt $configLines.Count; $i++) {
        if ($configLines[$i].Trim() -eq $scriptLocationLine) {
            $insertIndex = $i
            break
        }
    }

    if ($insertIndex -eq -1) {
        Write-Log "ERROR" "Could not find '$scriptLocationLine' in alembic.ini to insert version_locations."
        exit 1
    }
    
    $versionLocationsLine = "version_locations = $versionLocations"
    $configLines.Insert($insertIndex + 1, $versionLocationsLine)
    Set-Content -Path $tempAlembicIniPath -Value ($configLines -join "`r`n")
    Write-Log "INFO" "Created temporary config at '$tempAlembicIniPath' with dynamic version path."

    # 5. Ensure the database container is running
    Write-Log "INFO" "Ensuring the timescaledb container is running..."
    docker-compose up --build -d

    # 6. Build docker-compose and alembic arguments
    $dockerComposeParams = @(
        "run", 
        "--rm",
        "--no-deps",
        "--entrypoint", "alembic",
        "-e", "SERVICE_NAME=$ServiceName",
        "-e", "DATABASE_URL=$syncDbUrl",
        $ServiceName
    )

    $alembicParams = @(
        "-c", "alembic.temp.ini", # Use the temporary, dynamic config
        "-x", "branch=$ServiceName",
        "revision",
        "-m", $Message
    )

    # Add branch-label only if it's the first revision for the service
    $serviceVersionPath = Join-Path $projectRoot "alembic/versions/$ServiceName"
    if (-not (Test-Path $serviceVersionPath) -or -not (Get-ChildItem -Path $serviceVersionPath -Filter *.py)) {
        Write-Log "INFO" "No existing revisions found for '$ServiceName'. Adding branch label."
        $alembicParams += "--branch-label", $ServiceName
    }

    if ($AutoGenerate) {
        $alembicParams += "--autogenerate"
    }

    # 6. Execute the command
    Write-Log "INFO" "Executing Alembic revision command with dynamic config..."
    & docker-compose @dockerComposeParams @alembicParams
    Write-Log "SUCCESS" "Alembic revision command completed successfully."
}
catch {
    Write-Log "ERROR" "Alembic revision command failed."
    Write-Log "ERROR" $_.Exception.Message
    exit 1
}
finally {
    # 7. Clean up the temporary config file
    if (Test-Path $tempAlembicIniPath) {
        Remove-Item $tempAlembicIniPath -Force
        Write-Log "INFO" "Cleaned up temporary config file: '$tempAlembicIniPath'"
    }
}

exit 0