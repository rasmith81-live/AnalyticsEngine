#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Enhanced Docker deployment with schema evolution integration.

.DESCRIPTION
    This script integrates the schema evolution framework with the existing Docker Compose
    workflow, providing automated schema validation, migration coupling, and monitoring.

.PARAMETER ServiceName
    The name of the service to deploy (e.g., 'scor_service')

.PARAMETER Action
    Action to perform: 'deploy', 'validate', 'rollback', 'monitor', 'status'

.PARAMETER DryRun
    Perform a dry run without making actual changes

.PARAMETER Description
    Description of the deployment/changes

.PARAMETER SkipValidation
    Skip pre-deployment schema validation

.PARAMETER Force
    Force deployment despite warnings

.EXAMPLE
    .\enhanced_docker_deploy.ps1 -ServiceName scor_service -Action deploy -Description "Add priority field"
    .\enhanced_docker_deploy.ps1 -ServiceName scor_service -Action validate -DryRun
    .\enhanced_docker_deploy.ps1 -ServiceName scor_service -Action status
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$ServiceName,
    
    [Parameter(Mandatory=$true)]
    [ValidateSet('deploy', 'validate', 'rollback', 'monitor', 'status')]
    [string]$Action,
    
    [string]$Description = "Docker deployment with schema evolution",
    [switch]$DryRun,
    [switch]$SkipValidation,
    [switch]$Force,
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
        default { "White" }
    }
    Write-Host "[$now][$level] $message" -ForegroundColor $color
}

function Test-ServiceExists {
    param([string]$Service)
    
    $servicePath = Join-Path $ProjectRoot "services" $Service
    if (-not (Test-Path $servicePath)) {
        Log "ERROR" "Service path not found: $servicePath"
        return $false
    }
    return $true
}

function Test-DockerComposeService {
    param([string]$Service)
    
    $composeFile = Join-Path $ProjectRoot "docker-compose.yml"
    if (-not (Test-Path $composeFile)) {
        Log "ERROR" "docker-compose.yml not found: $composeFile"
        return $false
    }
    
    $composeContent = Get-Content $composeFile -Raw
    if ($composeContent -notmatch "$Service\s*:") {
        Log "ERROR" "Service '$Service' not found in docker-compose.yml"
        return $false
    }
    
    return $true
}

function Invoke-SchemaEvolution {
    param(
        [string]$Service,
        [string]$Description,
        [switch]$DryRun,
        [switch]$SkipValidation
    )
    
    Log "INFO" "Running schema evolution for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    $args = @(
        "tools/evolve_schema.py",
        "--service", $Service,
        "--description", $Description
    )
    
    if ($DryRun) { $args += "--dry-run" }
    if ($SkipValidation) { $args += "--skip-validation" }
    if ($Verbose) { $args += "--verbose" }
    
    Log "INFO" "Command: python $($args -join ' ')"
    
    try {
        $result = & python @args
        if ($LASTEXITCODE -ne 0) {
            throw "Schema evolution failed with exit code: $LASTEXITCODE"
        }
        Log "INFO" "Schema evolution completed successfully"
        return $true
    }
    catch {
        Log "ERROR" "Schema evolution failed: $($_.Exception.Message)"
        return $false
    }
}

function Invoke-SchemaValidation {
    param(
        [string]$Service,
        [switch]$Quick
    )
    
    Log "INFO" "Running schema validation for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    $args = @(
        "tools/validate_schema.py",
        "--service", $Service
    )
    
    if ($Quick) { $args += "--quick" }
    if ($Verbose) { $args += "--verbose" }
    
    try {
        $result = & python @args
        if ($LASTEXITCODE -ne 0) {
            Log "WARN" "Schema validation found issues"
            return $false
        }
        Log "INFO" "Schema validation passed"
        return $true
    }
    catch {
        Log "ERROR" "Schema validation failed: $($_.Exception.Message)"
        return $false
    }
}

function Start-DockerService {
    param(
        [string]$Service,
        [switch]$Rebuild
    )
    
    Log "INFO" "Starting Docker service: $Service"
    
    try {
        # Stop service if running
        Log "INFO" "Stopping existing service instance..."
        docker-compose stop $Service 2>$null
        
        if ($Rebuild) {
            Log "INFO" "Rebuilding service image..."
            docker-compose build --no-cache $Service
            if ($LASTEXITCODE -ne 0) {
                throw "Docker build failed for service: $Service"
            }
        }
        
        # Start service
        Log "INFO" "Starting service with dependencies..."
        docker-compose up -d $Service
        if ($LASTEXITCODE -ne 0) {
            throw "Docker service start failed for: $Service"
        }
        
        # Wait for health check
        Log "INFO" "Waiting for service health check..."
        $maxWait = 60
        $waited = 0
        
        do {
            Start-Sleep -Seconds 2
            $waited += 2
            $health = docker-compose ps --format json $Service | ConvertFrom-Json | Select-Object -First 1
            
            if ($health.Health -eq "healthy") {
                Log "INFO" "Service is healthy"
                return $true
            }
            elseif ($health.Health -eq "unhealthy") {
                Log "ERROR" "Service health check failed"
                return $false
            }
        } while ($waited -lt $maxWait)
        
        Log "WARN" "Service health check timeout"
        return $false
    }
    catch {
        Log "ERROR" "Docker service start failed: $($_.Exception.Message)"
        return $false
    }
}

function Get-ServiceStatus {
    param([string]$Service)
    
    Log "INFO" "Getting status for service: $Service"
    
    # Docker status
    $dockerStatus = docker-compose ps --format json $Service | ConvertFrom-Json | Select-Object -First 1
    
    Write-Host ""
    Write-Host "🐳 Docker Status:" -ForegroundColor Cyan
    Write-Host "  Service: $($dockerStatus.Service)"
    Write-Host "  State: $($dockerStatus.State)"
    Write-Host "  Health: $($dockerStatus.Health)"
    Write-Host "  Ports: $($dockerStatus.Ports)"
    
    # Schema evolution status
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    try {
        Log "INFO" "Checking schema evolution status..."
        & python "tools/deploy_to_production.py" --service $Service --status
    }
    catch {
        Log "WARN" "Could not retrieve schema evolution status"
    }
    
    # Health check
    try {
        Log "INFO" "Checking service health..."
        & python "tools/deploy_to_production.py" --service $Service --health-check
    }
    catch {
        Log "WARN" "Could not retrieve health status"
    }
}

function Start-Monitoring {
    param([string]$Service)
    
    Log "INFO" "Starting monitoring for service: $Service"
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    try {
        & python "tools/deploy_to_production.py" --service $Service --monitor-only
    }
    catch {
        Log "ERROR" "Failed to start monitoring: $($_.Exception.Message)"
    }
}

function Invoke-Rollback {
    param([string]$Service)
    
    Log "WARN" "Initiating rollback for service: $Service"
    
    if (-not $Force) {
        $response = Read-Host "⚠️  This will rollback the service. Continue? [y/N]"
        if ($response -notmatch '^[Yy]') {
            Log "INFO" "Rollback cancelled by user"
            return
        }
    }
    
    $pythonPath = $ProjectRoot
    $env:PYTHONPATH = $pythonPath
    
    try {
        & python "tools/deploy_to_production.py" --service $Service --emergency-rollback
        
        # Restart Docker service after rollback
        Log "INFO" "Restarting Docker service after rollback..."
        Start-DockerService -Service $Service -Rebuild
    }
    catch {
        Log "ERROR" "Rollback failed: $($_.Exception.Message)"
    }
}

# Main execution
function Main {
    Log "INFO" "Enhanced Docker Deploy - $Action for $ServiceName"
    Log "INFO" "Project Root: $ProjectRoot"
    
    # Validate service exists
    if (-not (Test-ServiceExists -Service $ServiceName)) {
        exit 1
    }
    
    if (-not (Test-DockerComposeService -Service $ServiceName)) {
        exit 1
    }
    
    # Set Python path
    $env:PYTHONPATH = $ProjectRoot
    Log "INFO" "PYTHONPATH set to: $ProjectRoot"
    
    switch ($Action) {
        "validate" {
            Log "INFO" "🔍 Validating schema for $ServiceName"
            
            $validationResult = Invoke-SchemaValidation -Service $ServiceName
            
            if ($validationResult) {
                Log "INFO" "✅ Schema validation passed"
                exit 0
            } else {
                Log "ERROR" "❌ Schema validation failed"
                exit 1
            }
        }
        
        "deploy" {
            Log "INFO" "🚀 Deploying $ServiceName with schema evolution"
            
            # Pre-deployment validation
            if (-not $SkipValidation) {
                Log "INFO" "Running pre-deployment validation..."
                $validationResult = Invoke-SchemaValidation -Service $ServiceName -Quick
                
                if (-not $validationResult -and -not $Force) {
                    Log "ERROR" "Pre-deployment validation failed. Use -Force to override."
                    exit 1
                }
            }
            
            # Schema evolution
            if (-not $DryRun) {
                $evolutionResult = Invoke-SchemaEvolution -Service $ServiceName -Description $Description -SkipValidation:$SkipValidation
                
                if (-not $evolutionResult) {
                    Log "ERROR" "Schema evolution failed"
                    exit 1
                }
            }
            
            # Docker deployment
            $dockerResult = Start-DockerService -Service $ServiceName -Rebuild
            
            if ($dockerResult) {
                Log "INFO" "✅ Deployment completed successfully"
                
                # Start monitoring
                Log "INFO" "Starting post-deployment monitoring..."
                Start-Monitoring -Service $ServiceName
            } else {
                Log "ERROR" "❌ Docker deployment failed"
                exit 1
            }
        }
        
        "status" {
            Log "INFO" "📊 Getting status for $ServiceName"
            Get-ServiceStatus -Service $ServiceName
        }
        
        "monitor" {
            Log "INFO" "📈 Starting monitoring for $ServiceName"
            Start-Monitoring -Service $ServiceName
        }
        
        "rollback" {
            Log "WARN" "🔄 Rolling back $ServiceName"
            Invoke-Rollback -Service $ServiceName
        }
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
