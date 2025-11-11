# Migrate KPI definitions from BaseKPI class format to dictionary format

Write-Host "🔄 KPI Definition Migration Script" -ForegroundColor Cyan
Write-Host "==================================`n" -ForegroundColor Cyan

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir

# Activate virtual environment if it exists
$venvPath = Join-Path $projectRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
    & $venvPath
}

# Run migration script
$migrationScript = Join-Path $scriptDir "migrate_kpi_definitions.py"

Write-Host "`n🚀 Running migration...`n" -ForegroundColor Green

python $migrationScript

Write-Host "`n✅ Migration complete!" -ForegroundColor Green
Write-Host "`n⚠️  Next steps:" -ForegroundColor Yellow
Write-Host "  1. Review the migrated KPI files" -ForegroundColor White
Write-Host "  2. Test the metadata service" -ForegroundColor White
Write-Host "  3. If everything works, delete .bak files" -ForegroundColor White
Write-Host "  4. Commit the changes to git`n" -ForegroundColor White
