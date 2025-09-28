param(
    [string]$ServiceName
)

$ErrorActionPreference = "Stop"
Push-Location "$PSScriptRoot/../.."

Write-Host "🔍 Resolving Alembic heads for branch '$ServiceName'..."

# Grab all Alembic heads with verbose output
$headInfo = docker-compose run --rm --entrypoint "" `
    -e SERVICE_NAME=$ServiceName `
    operations_service alembic heads --verbose

# Filter heads that belong only to the specified branch
$matchingHeads = @()
foreach ($line in $headInfo) {
    if ($line -match "Branch names:") {
        $lastBranchLine = $line
    }
    if ($line -match "^Rev:") {
        $revId = ($line -replace "Rev:\s*", "").Trim()
        if ($lastBranchLine -match "Branch names:\s*(.*)$") {
            $branches = $Matches[1].Split(",").Trim()
            if ($branches -contains $ServiceName) {
                $matchingHeads += $revId
            }
        }
    }
}

if ($matchingHeads.Count -le 1) {
    Write-Host "✅ Branch '$ServiceName' has a single head. No action needed."
    Pop-Location
    exit 0
}

Write-Host "⚠️ Detected multiple heads for branch '$ServiceName': $($matchingHeads -join ', ')"
$keepHead = Get-Random -InputObject $matchingHeads
Write-Host "🎯 Retaining head: $keepHead"

# Delete all other heads for this branch
$versionDir = "./alembic/versions"
foreach ($head in $matchingHeads) {
    if ($head -ne $keepHead) {
        $files = Get-ChildItem $versionDir -Filter "$head*.py"
        foreach ($file in $files) {
            Write-Host "🗑️  Removing conflicting revision: $($file.Name)"
            Remove-Item "$file.FullName" -Force
        }
    }
}

# Upgrade the branch head
Write-Host "🚀 Running Alembic upgrade for '$ServiceName@head'..."
docker-compose run --rm --entrypoint "" `
    -e SERVICE_NAME=$ServiceName `
    operations_service alembic upgrade "$ServiceName@head"

Pop-Location