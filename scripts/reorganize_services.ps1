# Service Reorganization Script
# Renames and moves analytics services to proper locations

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Service Reorganization Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$rootPath = "C:\Users\Arthu\CascadeProjects\AnalyticsEngine"
$businessServices = Join-Path $rootPath "services\business_services"
$backendServices = Join-Path $rootPath "services\backend_services"

# Define moves
$moves = @(
    @{
        Source = Join-Path $businessServices "analytics_models"
        Target = Join-Path $businessServices "analytics_metadata_service"
        Type = "Rename"
        Description = "Rename analytics_models to analytics_metadata_service"
    },
    @{
        Source = Join-Path $businessServices "calculation_engine"
        Target = Join-Path $backendServices "calculation_engine_service"
        Type = "Move"
        Description = "Move calculation_engine to backend_services as calculation_engine_service"
    }
)

# Verify sources exist
Write-Host "Verifying source directories..." -ForegroundColor Yellow
foreach ($move in $moves) {
    if (Test-Path $move.Source) {
        Write-Host "  [OK] $($move.Source)" -ForegroundColor Green
    } else {
        Write-Host "  [ERROR] Source not found: $($move.Source)" -ForegroundColor Red
        exit 1
    }
}
Write-Host ""

# Check if targets already exist
Write-Host "Checking target directories..." -ForegroundColor Yellow
$conflicts = $false
foreach ($move in $moves) {
    if (Test-Path $move.Target) {
        Write-Host "  [WARNING] Target already exists: $($move.Target)" -ForegroundColor Red
        $conflicts = $true
    } else {
        Write-Host "  [OK] Target available: $($move.Target)" -ForegroundColor Green
    }
}
Write-Host ""

if ($conflicts) {
    Write-Host "Conflicts detected. Please resolve manually or delete existing targets." -ForegroundColor Red
    exit 1
}

# Confirm with user
Write-Host "The following operations will be performed:" -ForegroundColor Cyan
Write-Host ""
foreach ($move in $moves) {
    Write-Host "  $($move.Type): $($move.Description)" -ForegroundColor White
    Write-Host "    From: $($move.Source)" -ForegroundColor Gray
    Write-Host "    To:   $($move.Target)" -ForegroundColor Gray
    Write-Host ""
}

$confirmation = Read-Host "Proceed with reorganization? (yes/no)"
if ($confirmation -ne "yes") {
    Write-Host "Operation cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Executing moves..." -ForegroundColor Cyan
Write-Host ""

# Execute moves
foreach ($move in $moves) {
    Write-Host "Processing: $($move.Description)..." -ForegroundColor Yellow
    
    try {
        if ($move.Type -eq "Rename") {
            # Rename in same directory
            Rename-Item -Path $move.Source -NewName (Split-Path $move.Target -Leaf) -ErrorAction Stop
            Write-Host "  [SUCCESS] Renamed successfully" -ForegroundColor Green
        } elseif ($move.Type -eq "Move") {
            # Move to different directory
            Move-Item -Path $move.Source -Destination $move.Target -ErrorAction Stop
            Write-Host "  [SUCCESS] Moved successfully" -ForegroundColor Green
        }
    } catch {
        Write-Host "  [ERROR] Failed: $_" -ForegroundColor Red
        exit 1
    }
    
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Reorganization Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  1. analytics_models -> analytics_metadata_service (business_services)" -ForegroundColor White
Write-Host "  2. calculation_engine -> calculation_engine_service (backend_services)" -ForegroundColor White
Write-Host ""

Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Update docker-compose.yml service paths" -ForegroundColor White
Write-Host "  2. Update any import statements in code" -ForegroundColor White
Write-Host "  3. Update README.md references" -ForegroundColor White
Write-Host "  4. Test services start correctly" -ForegroundColor White
Write-Host ""

Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
