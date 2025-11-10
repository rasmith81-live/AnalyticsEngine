# Push to All Remotes - AnalyticsEngine
# This script pushes changes to both organization and personal repositories

Write-Host "Pushing to all remotes..." -ForegroundColor Cyan
Write-Host ""

# Push to organization (origin)
Write-Host "Pushing to marketnova/AnalyticsEngine..." -ForegroundColor Yellow
git push origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully pushed to origin (marketnova)" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to push to origin" -ForegroundColor Red
}

Write-Host ""

# Push to personal
Write-Host "Pushing to rasmith81-live/AnalyticsEngine..." -ForegroundColor Yellow
git push personal main
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Successfully pushed to personal (rasmith81-live)" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to push to personal" -ForegroundColor Red
}

Write-Host ""
Write-Host "Done! Both repositories are now synchronized." -ForegroundColor Cyan
