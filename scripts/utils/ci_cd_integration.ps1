#!/usr/bin/env pwsh
<#
.SYNOPSIS
    CI/CD integration script for schema evolution framework.

.DESCRIPTION
    This script provides CI/CD pipeline integration for the schema evolution framework,
    including pre-commit validation, automated testing, and deployment preparation.

.PARAMETER Action
    Action to perform: 'pre-commit', 'pre-build', 'post-build', 'pre-deploy', 'post-deploy'

.PARAMETER Services
    Comma-separated list of services to process (default: all services)

.PARAMETER Environment
    Target environment: 'development', 'staging', 'production'

.PARAMETER FailFast
    Stop on first error instead of continuing with other services

.PARAMETER GenerateReport
    Generate detailed validation report

.EXAMPLE
    .\ci_cd_integration.ps1 -Action pre-commit -Services "scor_service,operations_service"
    .\ci_cd_integration.ps1 -Action pre-deploy -Environment production -GenerateReport
#>

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('pre-commit', 'pre-build', 'post-build', 'pre-deploy', 'post-deploy', 'validate-all')]
    [string]$Action,
    
    [string]$Services = "",
    
    [ValidateSet('development', 'staging', 'production')]
    [string]$Environment = "development",
    
    [switch]$FailFast,
    [switch]$GenerateReport,
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

# Get script directory and project root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)

# Helper function for timestamped logging
function Log($level, $message) {
    $now = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
    $color = switch ($level) {
        "INFO" { "Green" }
        "WARN" { "Yellow" }
        "ERROR" { "Red" }
        "DEBUG" { "Cyan" }
        "SUCCESS" { "Green" }
        default { "White" }
    }
    Write-Host "[$now][$level] $message" -ForegroundColor $color
}

function Get-AllServices {
    $servicesDir = Join-Path $ProjectRoot "services"
    if (Test-Path $servicesDir) {
        return Get-ChildItem $servicesDir -Directory | ForEach-Object { $_.Name }
    }
    return @()
}

function Get-TargetServices {
    if ([string]::IsNullOrEmpty($Services)) {
        return Get-AllServices
    }
    return $Services -split ','
}

function Test-ServiceExists {
    param([string]$Service)
    
    $servicePath = Join-Path $ProjectRoot "services" $Service
    return Test-Path $servicePath
}

function Invoke-SchemaValidation {
    param(
        [string]$Service,
        [string]$ValidationLevel = "basic"
    )
    
    Log "INFO" "Validating schema for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    $pythonArgs = @(
        "tools/validate_schema.py",
        "--service", $Service,
        "--validation-level", $ValidationLevel
    )
    
    if ($Verbose) { $pythonArgs += "--verbose" }
    
    try {
        $output = & python @pythonArgs 2>&1
        if ($LASTEXITCODE -eq 0) {
            Log "SUCCESS" "Schema validation passed for $Service"
            return @{
                Success = $true
                Service = $Service
                Output = $output
                Issues = @()
            }
        } else {
            Log "ERROR" "Schema validation failed for $Service"
            return @{
                Success = $false
                Service = $Service
                Output = $output
                Issues = @("Validation failed")
            }
        }
    }
    catch {
        Log "ERROR" "Schema validation error for $Service`: $($_.Exception.Message)"
        return @{
            Success = $false
            Service = $Service
            Output = $_.Exception.Message
            Issues = @("Validation error: $($_.Exception.Message)")
        }
    }
}

function Invoke-ConsistencyCheck {
    param([string]$Service)
    
    Log "INFO" "Running consistency check for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    $pythonArgs = @(
        "tools/validate_schema.py",
        "--service", $Service,
        "--consistency-only"
    )
    
    if ($Verbose) { $pythonArgs += "--verbose" }
    
    try {
        $output = & python @pythonArgs 2>&1
        if ($LASTEXITCODE -eq 0) {
            Log "SUCCESS" "Consistency check passed for $Service"
            return @{
                Success = $true
                Service = $Service
                Output = $output
            }
        } else {
            Log "ERROR" "Consistency check failed for $Service"
            return @{
                Success = $false
                Service = $Service
                Output = $output
            }
        }
    }
    catch {
        Log "ERROR" "Consistency check error for $Service`: $($_.Exception.Message)"
        return @{
            Success = $false
            Service = $Service
            Output = $_.Exception.Message
        }
    }
}

function Test-MigrationReadiness {
    param([string]$Service)
    
    Log "INFO" "Testing migration readiness for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    # Check for pending migrations
    try {
        $result = & python -c "
from tools.schema_evolution.migration_coupler import MigrationCoupler
coupler = MigrationCoupler('$Service')
pending = coupler.get_pending_migrations()
print(f'PENDING_MIGRATIONS:{len(pending)}')
for migration in pending:
    print(f'MIGRATION:{migration}')
"
        
        $pendingCount = ($result | Where-Object { $_ -match "PENDING_MIGRATIONS:(\d+)" } | ForEach-Object { $matches[1] }) -as [int]
        $migrations = $result | Where-Object { $_ -match "MIGRATION:(.+)" } | ForEach-Object { $matches[1] }
        
        return @{
            Success = $true
            Service = $Service
            PendingMigrations = $pendingCount
            Migrations = $migrations
        }
    }
    catch {
        Log "ERROR" "Migration readiness check failed for $Service`: $($_.Exception.Message)"
        return @{
            Success = $false
            Service = $Service
            PendingMigrations = -1
            Migrations = @()
        }
    }
}

function Invoke-PreCommitChecks {
    param([string[]]$TargetServices)
    
    Log "INFO" "Running pre-commit checks for services: $($TargetServices -join ', ')"
    
    $results = @()
    $overallSuccess = $true
    
    foreach ($service in $TargetServices) {
        if (-not (Test-ServiceExists -Service $service)) {
            Log "WARN" "Service not found: $service"
            continue
        }
        
        Log "INFO" "Processing service: $service"
        
        # Quick validation
        $validationResult = Invoke-SchemaValidation -Service $service -ValidationLevel "quick"
        $results += $validationResult
        
        if (-not $validationResult.Success) {
            $overallSuccess = $false
            if ($FailFast) {
                Log "ERROR" "Failing fast due to validation failure in $service"
                break
            }
        }
        
        # Consistency check
        $consistencyResult = Invoke-ConsistencyCheck -Service $service
        if (-not $consistencyResult.Success) {
            $overallSuccess = $false
            Log "ERROR" "Consistency check failed for $service"
            if ($FailFast) {
                break
            }
        }
    }
    
    return @{
        Success = $overallSuccess
        Results = $results
    }
}

function Invoke-PreBuildChecks {
    param([string[]]$TargetServices)
    
    Log "INFO" "Running pre-build checks for services: $($TargetServices -join ', ')"
    
    $results = @()
    $overallSuccess = $true
    
    foreach ($service in $TargetServices) {
        if (-not (Test-ServiceExists -Service $service)) {
            Log "WARN" "Service not found: $service"
            continue
        }
        
        Log "INFO" "Processing service: $service"
        
        # Full validation
        $validationResult = Invoke-SchemaValidation -Service $service -ValidationLevel "full"
        $results += $validationResult
        
        if (-not $validationResult.Success) {
            $overallSuccess = $false
            if ($FailFast) {
                Log "ERROR" "Failing fast due to validation failure in $service"
                break
            }
        }
        
        # Schema Drift Detection
        Log "INFO" "Running schema drift detection for $service"
        try {
            $detectorArgs = @(
                "tools/schema_detector.py",
                "--service", $service
            )
            & python @detectorArgs
            $exitCode = $LASTEXITCODE

            if ($exitCode -eq 0) {
                Log "WARN" "Schema drift detected for $service. Generating migration..."
                & "$ScriptDir/create_revision_clean.ps1" -ServiceName $service -Message "Autogenerated migration due to schema drift" -AutoGenerate
                if ($LASTEXITCODE -ne 0) {
                    Log "ERROR" "Failed to automatically generate migration for $service."
                    $overallSuccess = $false
                }
            } elseif ($exitCode -eq 2) {
                Log "SUCCESS" "No schema drift detected for $service."
            } else {
                Log "ERROR" "Schema drift detection script failed for $service with exit code $exitCode."
                $overallSuccess = $false
            }
        } catch {
            Log "ERROR" "An exception occurred while running the schema drift detector for $service`: $($_.Exception.Message)"
            $overallSuccess = $false
        }

        # Migration readiness
        $migrationResult = Test-MigrationReadiness -Service $service
        if (-not $migrationResult.Success) {
            $overallSuccess = $false
            Log "ERROR" "Migration readiness check failed for $service"
            if ($FailFast) {
                break
            }
        } elseif ($migrationResult.PendingMigrations -gt 0) {
            Log "WARN" "Service $service has $($migrationResult.PendingMigrations) pending migrations"
        }
    }
    
    return @{
        Success = $overallSuccess
        Results = $results
    }
}

function Invoke-PostBuildChecks {
    param([string[]]$TargetServices)
    
    Log "INFO" "Running post-build checks for services: $($TargetServices -join ', ')"
    
    $results = @()
    $overallSuccess = $true
    
    foreach ($service in $TargetServices) {
        if (-not (Test-ServiceExists -Service $service)) {
            Log "WARN" "Service not found: $service"
            continue
        }
        
        Log "INFO" "Processing service: $service"
        
        # Verify Docker image exists
        $imageName = "supplychainanalytics-$service"
        try {
            $imageExists = docker images --format "{{.Repository}}" | Select-String -Pattern $imageName -Quiet
            if ($imageExists) {
                Log "SUCCESS" "Docker image exists for $service"
            } else {
                Log "ERROR" "Docker image not found for $service"
                $overallSuccess = $false
            }
        }
        catch {
            Log "ERROR" "Failed to check Docker image for $service"
            $overallSuccess = $false
        }
        
        # Schema validation on built image
        $validationResult = Invoke-SchemaValidation -Service $service -ValidationLevel "basic"
        $results += $validationResult
        
        if (-not $validationResult.Success) {
            $overallSuccess = $false
            if ($FailFast) {
                break
            }
        }
    }
    
    return @{
        Success = $overallSuccess
        Results = $results
    }
}

function Invoke-PreDeployChecks {
    param([string[]]$TargetServices)
    
    Log "INFO" "Running pre-deploy checks for $Environment environment"
    Log "INFO" "Target services: $($TargetServices -join ', ')"
    
    $results = @()
    $overallSuccess = $true
    
    # Environment-specific validation level
    $validationLevel = switch ($Environment) {
        "production" { "strict" }
        "staging" { "full" }
        default { "basic" }
    }
    
    foreach ($service in $TargetServices) {
        if (-not (Test-ServiceExists -Service $service)) {
            Log "WARN" "Service not found: $service"
            continue
        }
        
        Log "INFO" "Processing service: $service for $Environment deployment"
        
        # Strict validation for production
        $validationResult = Invoke-SchemaValidation -Service $service -ValidationLevel $validationLevel
        $results += $validationResult
        
        if (-not $validationResult.Success) {
            $overallSuccess = $false
            Log "ERROR" "Pre-deploy validation failed for $service"
            if ($FailFast) {
                break
            }
        }
        
        # Check deployment readiness
        if ($Environment -eq "production") {
            Log "INFO" "Running production readiness checks for $service"
            
            # Additional production checks would go here
            # - Backup verification
            # - Rollback plan validation
            # - Performance impact assessment
        }
    }
    
    return @{
        Success = $overallSuccess
        Results = $results
        Environment = $Environment
    }
}

function Invoke-PostDeployChecks {
    param([string[]]$TargetServices)
    
    Log "INFO" "Running post-deploy checks for $Environment environment"
    
    $results = @()
    $overallSuccess = $true
    
    foreach ($service in $TargetServices) {
        if (-not (Test-ServiceExists -Service $service)) {
            Log "WARN" "Service not found: $service"
            continue
        }
        
        Log "INFO" "Processing service: $service post-deployment"
        
        # Post-deployment validation
        $validationResult = Invoke-SchemaValidation -Service $service -ValidationLevel "basic"
        $results += $validationResult
        
        if (-not $validationResult.Success) {
            $overallSuccess = $false
            Log "ERROR" "Post-deploy validation failed for $service"
        }
        
        # Health check
        try {
            $pythonPath = $ProjectRoot
            $env:PYTHONPATH = $pythonPath
            
            & python "tools/deploy_to_production.py" --service $service --health-check
            Log "SUCCESS" "Health check passed for $service"
        }
        catch {
            Log "ERROR" "Health check failed for $service"
            $overallSuccess = $false
        }
    }
    
    return @{
        Success = $overallSuccess
        Results = $results
        Environment = $Environment
    }
}

function New-ValidationReport {
    param(
        [hashtable]$Results,
        [string]$Action
    )
    
    if (-not $GenerateReport) {
        return
    }
    
    Log "INFO" "Generating validation report for $Action"
    
    $reportPath = Join-Path $ProjectRoot "reports" "ci_cd_validation_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
    $reportDir = Split-Path $reportPath -Parent
    
    if (-not (Test-Path $reportDir)) {
        New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
    }
    
    $report = @{
        timestamp = (Get-Date).ToString("o")
        action = $Action
        environment = $Environment
        overall_success = $Results.Success
        services_processed = ($Results.Results | ForEach-Object { $_.Service }) -join ','
        results = $Results.Results
    }
    
    $report | ConvertTo-Json -Depth 10 | Set-Content $reportPath
    
    Log "SUCCESS" "Validation report generated: $reportPath"
}

# Main execution
function Main {
    Log "INFO" "CI/CD Integration - $Action"
    Log "INFO" "Environment: $Environment"
    Log "INFO" "Project Root: $ProjectRoot"
    
    # Set Python path
    $env:PYTHONPATH = $ProjectRoot
    
    # Get target services
    $targetServices = Get-TargetServices
    Log "INFO" "Target services: $($targetServices -join ', ')"
    
    # Execute action
    $results = switch ($Action) {
        "pre-commit" { Invoke-PreCommitChecks -TargetServices $targetServices }
        "pre-build" { Invoke-PreBuildChecks -TargetServices $targetServices }
        "post-build" { Invoke-PostBuildChecks -TargetServices $targetServices }
        "pre-deploy" { Invoke-PreDeployChecks -TargetServices $targetServices }
        "post-deploy" { Invoke-PostDeployChecks -TargetServices $targetServices }
        "validate-all" { Invoke-PreBuildChecks -TargetServices $targetServices }
    }
    
    # Generate report if requested
    New-ValidationReport -Results $results -Action $Action
    
    # Summary
    Write-Host ""
    if ($results.Success) {
        Log "SUCCESS" "✅ $Action completed successfully for all services"
        exit 0
    } else {
        Log "ERROR" "❌ $Action failed for one or more services"
        
        # Show failed services
        $failedServices = $results.Results | Where-Object { -not $_.Success } | ForEach-Object { $_.Service }
        if ($failedServices) {
            Log "ERROR" "Failed services: $($failedServices -join ', ')"
        }
        
        exit 1
    }
}

# Execute main function
try {
    Main
}
catch {
    Log "ERROR" "Script execution failed: $($_.Exception.Message)"
    if ($Verbose) {
        Log "DEBUG" $_.ScriptStackTrace
    }
    exit 1
}
