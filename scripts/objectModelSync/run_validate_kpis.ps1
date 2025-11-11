# Validate and Enhance KPI Definitions

Write-Host "🔍 KPI Validation and Enhancement Script" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)

# Activate virtual environment if it exists
$venvPath = Join-Path $projectRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
    & $venvPath
}

# Run validation script
$validationScript = Join-Path $scriptDir "validate_and_enhance_kpis.py"

Write-Host "`n🚀 Running KPI validation and enhancement...`n" -ForegroundColor Green

python $validationScript

$exitCode = $LASTEXITCODE

if ($exitCode -eq 0) {
    Write-Host "`n✅ KPI validation and enhancement complete!" -ForegroundColor Green
    Write-Host "`n📋 What was done:" -ForegroundColor Yellow
    Write-Host "  ✓ Validated all KPI definitions" -ForegroundColor White
    Write-Host "  ✓ Added missing required fields" -ForegroundColor White
    Write-Host "  ✓ Generated sample data for visualizations" -ForegroundColor White
    Write-Host "  ✓ Created backup of original files" -ForegroundColor White
    Write-Host "  ✓ Generated validation report`n" -ForegroundColor White
    
    Write-Host "⚠️  Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Review the validation report in scripts/objectModelSync/output/" -ForegroundColor White
    Write-Host "  2. Check enhanced KPI files for accuracy" -ForegroundColor White
    Write-Host "  3. Test sample data visualizations in the frontend" -ForegroundColor White
    Write-Host "  4. If issues found, restore from backup in scripts/objectModelSync/backups/`n" -ForegroundColor White
} else {
    Write-Host "`n❌ KPI validation failed with exit code $exitCode" -ForegroundColor Red
    Write-Host "Check the error messages above for details.`n" -ForegroundColor Red
}
