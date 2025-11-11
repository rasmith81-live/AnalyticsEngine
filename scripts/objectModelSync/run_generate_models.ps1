# Generate SQLAlchemy Models from Object Model Definitions

Write-Host "🔄 SQLAlchemy Model Generation Script" -ForegroundColor Cyan
Write-Host "======================================`n" -ForegroundColor Cyan

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)

# Activate virtual environment if it exists
$venvPath = Join-Path $projectRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "📦 Activating virtual environment..." -ForegroundColor Yellow
    & $venvPath
}

# Run generation script
$generationScript = Join-Path $scriptDir "generate_sqlalchemy_models.py"

Write-Host "`n🚀 Running model generation...`n" -ForegroundColor Green

python $generationScript

$exitCode = $LASTEXITCODE

if ($exitCode -eq 0) {
    Write-Host "`n✅ Model generation complete!" -ForegroundColor Green
    Write-Host "`n⚠️  Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Review the generated base_models.py" -ForegroundColor White
    Write-Host "  2. Create Alembic migration:" -ForegroundColor White
    Write-Host "     cd $projectRoot" -ForegroundColor Gray
    Write-Host "     alembic revision --autogenerate -m 'Add object models'" -ForegroundColor Gray
    Write-Host "  3. Review the migration file" -ForegroundColor White
    Write-Host "  4. Apply migrations:" -ForegroundColor White
    Write-Host "     alembic upgrade head" -ForegroundColor Gray
    Write-Host "  5. Test the database" -ForegroundColor White
    Write-Host "  6. If everything works, delete .bak file`n" -ForegroundColor White
} else {
    Write-Host "`n❌ Model generation failed with exit code $exitCode" -ForegroundColor Red
}
