# Service Reorganization Script (Auto-execute)
# Renames and moves analytics services to proper locations

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Service Reorganization (Auto)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$rootPath = "C:\Users\Arthu\CascadeProjects\AnalyticsEngine"
$businessServices = Join-Path $rootPath "services\business_services"
$backendServices = Join-Path $rootPath "services\backend_services"

# Step 1: Rename analytics_models to analytics_metadata_service
$source1 = Join-Path $businessServices "analytics_models"
$target1 = Join-Path $businessServices "analytics_metadata_service"

Write-Host "Step 1: Renaming analytics_models..." -ForegroundColor Yellow
if (Test-Path $source1) {
    if (Test-Path $target1) {
        Write-Host "  [SKIP] Target already exists: $target1" -ForegroundColor Yellow
    } else {
        Rename-Item -Path $source1 -NewName "analytics_metadata_service" -ErrorAction Stop
        Write-Host "  [SUCCESS] Renamed to analytics_metadata_service" -ForegroundColor Green
    }
} else {
    Write-Host "  [SKIP] Source not found (may already be renamed)" -ForegroundColor Yellow
}
Write-Host ""

# Step 2: Move calculation_engine to backend_services
$source2 = Join-Path $businessServices "calculation_engine"
$target2 = Join-Path $backendServices "calculation_engine_service"

Write-Host "Step 2: Moving calculation_engine to backend_services..." -ForegroundColor Yellow
if (Test-Path $source2) {
    if (Test-Path $target2) {
        Write-Host "  [SKIP] Target already exists: $target2" -ForegroundColor Yellow
    } else {
        Move-Item -Path $source2 -Destination $target2 -ErrorAction Stop
        Write-Host "  [SUCCESS] Moved to backend_services/calculation_engine_service" -ForegroundColor Green
    }
} else {
    Write-Host "  [SKIP] Source not found (may already be moved)" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Reorganization Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Verify the changes:" -ForegroundColor Cyan
Write-Host "  1. Check: services/business_services/analytics_metadata_service/" -ForegroundColor White
Write-Host "  2. Check: services/backend_services/calculation_engine_service/" -ForegroundColor White
Write-Host ""

Write-Host "Next: See SERVICE_REORGANIZATION_CHECKLIST.md for post-move updates" -ForegroundColor Yellow
