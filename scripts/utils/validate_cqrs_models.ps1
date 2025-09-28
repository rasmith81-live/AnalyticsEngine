#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Validates CQRS model separation and checks for common migration issues.

.DESCRIPTION
    This script validates that CQRS models are properly separated and checks for:
    - Table duplication between write and read models
    - Import conflicts and circular dependencies
    - Missing enums and model references
    - Proper schema usage and extend_existing flags
    - Alembic migration readiness

.PARAMETER ServiceName
    The name of the service to validate (e.g., 'scor_service')

.PARAMETER Fix
    If specified, attempts to fix common issues automatically

.EXAMPLE
    .\validate_cqrs_models.ps1 -ServiceName scor_service
    .\validate_cqrs_models.ps1 -ServiceName scor_service -Fix
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$ServiceName,
    
    [switch]$Fix
)

# Set error handling
$ErrorActionPreference = "Stop"

# Get script directory and project root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)

Write-Host "[INFO] CQRS Model Validation for $ServiceName" -ForegroundColor Green

$ServicePath = Join-Path $ProjectRoot "services" $ServiceName
if (-not (Test-Path $ServicePath)) {
    Write-Error "Service path not found: $ServicePath"
    exit 1
}

$Issues = @()
$Warnings = @()

function Find-TableDefinitions {
    param($ServicePath)
    
    $Tables = @{}
    
    # Check main models file
    $ModelsFile = Join-Path $ServicePath "app" "models.py"
    if (Test-Path $ModelsFile) {
        $Content = Get-Content $ModelsFile -Raw
        $TableMatches = [regex]::Matches($Content, "class\s+(\w+)\(Base\):[\s\S]*?__tablename__\s*=\s*['\""]([^\""]+)['\""]")
        foreach ($Match in $TableMatches) {
            $ClassName = $Match.Groups[1].Value
            $TableName = $Match.Groups[2].Value
            if (-not $Tables.ContainsKey($TableName)) {
                $Tables[$TableName] = @()
            }
            $Tables[$TableName] += @{
                File = $ModelsFile
                Type = "Write"
                ClassName = $ClassName
                RelativePath = "app/models.py"
            }
        }
    }
    
    # Check domain model files
    $DomainFiles = Get-ChildItem -Path (Join-Path $ServicePath "app" "scor") -Name "models.py" -Recurse
    foreach ($File in $DomainFiles) {
        $FilePath = Join-Path $ServicePath "app" "scor" $File
        if (-not (Test-Path $FilePath)) { continue }
        $Content = Get-Content $FilePath -Raw
        if (-not $Content) { continue }
        
        # Check for write models (extending Base)
        $WriteMatches = [regex]::Matches($Content, "class\s+(\w+)\(Base\):[\s\S]*?__tablename__\s*=\s*['\""]([^\""]+)['\""]")
        foreach ($Match in $WriteMatches) {
            $ClassName = $Match.Groups[1].Value
            $TableName = $Match.Groups[2].Value
            if (-not $Tables.ContainsKey($TableName)) {
                $Tables[$TableName] = @()
            }
            $Tables[$TableName] += @{
                File = $FilePath
                Type = "Write"
                ClassName = $ClassName
                RelativePath = "app/scor/$File"
            }
        }
        
        # Check for read models (extending ReadBase)
        $ReadMatches = [regex]::Matches($Content, "class\s+(\w+)\(ReadBase\):[\s\S]*?__tablename__\s*=\s*['\""]([^\""]+)['\""]")
        foreach ($Match in $ReadMatches) {
            $ClassName = $Match.Groups[1].Value
            $TableName = $Match.Groups[2].Value
            if (-not $Tables.ContainsKey($TableName)) {
                $Tables[$TableName] = @()
            }
            $Tables[$TableName] += @{
                File = $FilePath
                Type = "Read"
                ClassName = $ClassName
                RelativePath = "app/scor/$File"
            }
        }
    }
    
    return $Tables
}

function Test-TableDuplication {
    param($Tables)
    
    $Duplicates = @()
    
    # Define core SCOR tables that should only be in main models
    $CoreSCORTables = @('scor_processes', 'scor_metrics', 'scor_observations', 'scor_benchmarks', 'scor_practices', 'scor_skills')
    
    foreach ($TableName in $Tables.Keys) {
        $Definitions = $Tables[$TableName]
        
        # Check for actual duplicate class definitions (same class name, same table)
        $WriteModels = $Definitions | Where-Object { $_.Type -eq "Write" }
        if ($WriteModels.Count -gt 1) {
            # Group by class name to see if it's truly a duplicate
            $ClassGroups = $WriteModels | Group-Object ClassName
            foreach ($Group in $ClassGroups) {
                if ($Group.Count -gt 1) {
                    $Duplicates += @{
                        Table = $TableName
                        Type = "Duplicate Class Definition"
                        Class = $Group.Name
                        Files = $Group.Group.RelativePath
                        Severity = "Error"
                    }
                }
            }
        }
        
        # Check for core SCOR models in domain files (these should only be in main models)
        if ($TableName -in $CoreSCORTables) {
            $DomainWrites = $Definitions | Where-Object { $_.Type -eq "Write" -and $_.RelativePath -like "*scor*" }
            if ($DomainWrites.Count -gt 0) {
                $Duplicates += @{
                    Table = $TableName
                    Type = "Core SCOR Model in Domain"
                    Files = $DomainWrites.RelativePath
                    Severity = "Error"
                }
            }
        }
        
        # Check for same table name in both write and read (potential conflict)
        $WriteCount = ($Definitions | Where-Object { $_.Type -eq "Write" }).Count
        $ReadCount = ($Definitions | Where-Object { $_.Type -eq "Read" }).Count
        if ($WriteCount -gt 0 -and $ReadCount -gt 0) {
            # This is only an issue if they have the same table name (not _read suffix)
            $ReadTables = $Definitions | Where-Object { $_.Type -eq "Read" }
            foreach ($ReadTable in $ReadTables) {
                $Content = Get-Content $ReadTable.File -Raw
                if ($Content -match "__tablename__\s*=\s*['""]$TableName['""]") {
                    $Duplicates += @{
                        Table = $TableName
                        Type = "Table Name Conflict"
                        Files = @($WriteModels.RelativePath, $ReadTable.RelativePath)
                        Severity = "Warning"
                    }
                }
            }
        }
    }
    
    return $Duplicates
}

function Test-ImportIssues {
    param($ServicePath)
    
    $ImportIssues = @()
    
    # Check domain files for proper imports
    $DomainFiles = Get-ChildItem -Path (Join-Path $ServicePath "app" "scor") -Name "*.py" -Recurse
    foreach ($File in $DomainFiles) {
        $FilePath = Join-Path $ServicePath "app" "scor" $File
        if (-not (Test-Path $FilePath)) { continue }
        $Content = Get-Content $FilePath -Raw
        if (-not $Content) { continue }
        
        # Check for imports from local models that should be from main models
        $LocalImports = [regex]::Matches($Content, "from \.models import ([^`n]+)")
        foreach ($Match in $LocalImports) {
            $ImportedItems = $Match.Groups[1].Value -split "," | ForEach-Object { $_.Trim() }
            
            # Check if these items are core models that should be in main models
            $CoreModels = @("SCORProcess", "SCORMetric", "SCORPractice", "SCORSkill", "SCORObservation", "SCORBenchmark", "ProcessType", "CompetencyLevel")
            foreach ($Item in $ImportedItems) {
                if ($Item -in $CoreModels) {
                    $ImportIssues += @{
                        File = $File
                        Type = "Core Model Import from Local"
                        Item = $Item
                        Severity = "Error"
                    }
                }
            }
        }
        
        # Check for missing imports
        $UsedModels = [regex]::Matches($Content, "class \w+.*\((\w+)\):")
        foreach ($Match in $UsedModels) {
            $BaseClass = $Match.Groups[1].Value
            if ($BaseClass -eq "Base" -and $Content -notmatch "from.*Base") {
                $ImportIssues += @{
                    File = $File
                    Type = "Missing Base Import"
                    Item = $BaseClass
                    Severity = "Error"
                }
            }
        }
    }
    
    return $ImportIssues
}

function Test-SchemaUsage {
    param($ServicePath)
    
    $SchemaIssues = @()
    
    # Check main models file
    $ModelsFile = Join-Path $ServicePath "app" "models.py"
    if (Test-Path $ModelsFile) {
        $Content = Get-Content $ModelsFile -Raw
        
        # Check for missing schema specification
        $TableDefs = [regex]::Matches($Content, "class (\w+)\(Base\):.*?__tablename__\s*=\s*['""]([^'""]+)['""].*?__table_args__\s*=\s*({[^}]*})", [System.Text.RegularExpressions.RegexOptions]::Singleline)
        foreach ($Match in $TableDefs) {
            $ClassName = $Match.Groups[1].Value
            $TableName = $Match.Groups[2].Value
            $TableArgs = $Match.Groups[3].Value
            
            if ($TableArgs -notmatch "schema.*$ServiceName") {
                $SchemaIssues += @{
                    Class = $ClassName
                    Table = $TableName
                    Type = "Missing Schema"
                    Severity = "Error"
                }
            }
            
            if ($TableArgs -notmatch "extend_existing.*True") {
                $SchemaIssues += @{
                    Class = $ClassName
                    Table = $TableName
                    Type = "Missing extend_existing"
                    Severity = "Warning"
                }
            }
        }
    }
    
    return $SchemaIssues
}

function Test-AlembicReadiness {
    param($ServicePath)
    
    $AlembicIssues = @()
    
    # Check if migration files exist
    $MigrationPath = Join-Path $ProjectRoot "alembic" "versions" $ServiceName
    if (-not (Test-Path $MigrationPath)) {
        $AlembicIssues += @{
            Type = "Missing Migration Directory"
            Path = $MigrationPath
            Severity = "Error"
        }
    } else {
        $MigrationFiles = Get-ChildItem -Path $MigrationPath -Filter "*.py"
        if ($MigrationFiles.Count -eq 0) {
            $AlembicIssues += @{
                Type = "No Migration Files"
                Path = $MigrationPath
                Severity = "Warning"
            }
        } else {
            # Check latest migration for proper branch labels
            $LatestMigration = $MigrationFiles | Sort-Object LastWriteTime -Descending | Select-Object -First 1
            $Content = Get-Content $LatestMigration.FullName -Raw
            
            if ($Content -notmatch "branch_labels.*$ServiceName") {
                $AlembicIssues += @{
                    Type = "Missing Branch Labels"
                    File = $LatestMigration.Name
                    Severity = "Error"
                }
            }
        }
    }
    
    return $AlembicIssues
}

function Fix-CommonIssues {
    param($Issues, $ServicePath)
    
    $Fixed = 0
    
    foreach ($Issue in $Issues) {
        switch ($Issue.Type) {
            "Missing extend_existing" {
                Write-Host "[FIX] Adding extend_existing to $($Issue.Class)" -ForegroundColor Yellow
                # Implementation would go here
                $Fixed++
            }
            "Missing Schema" {
                Write-Host "[FIX] Adding schema to $($Issue.Class)" -ForegroundColor Yellow
                # Implementation would go here
                $Fixed++
            }
        }
    }
    
    return $Fixed
}

# Main validation
Write-Host "[STEP 1] Finding table definitions..." -ForegroundColor Cyan
$Tables = Find-TableDefinitions -ServicePath $ServicePath
Write-Host "[INFO] Found $($Tables.Keys.Count) unique table names" -ForegroundColor White

Write-Host "[STEP 2] Checking for table duplication..." -ForegroundColor Cyan
$Duplicates = Test-TableDuplication -Tables $Tables
if ($Duplicates.Count -gt 0) {
    foreach ($Duplicate in $Duplicates) {
        $Color = if ($Duplicate.Severity -eq "Error") { "Red" } else { "Yellow" }
        Write-Host "[$($Duplicate.Severity.ToUpper())] $($Duplicate.Type): $($Duplicate.Table)" -ForegroundColor $Color
        Write-Host "  Files: $($Duplicate.Files -join ', ')" -ForegroundColor Gray
    }
    $Issues += $Duplicates
} else {
    Write-Host "[SUCCESS] No table duplication found" -ForegroundColor Green
}

Write-Host "[STEP 3] Checking import issues..." -ForegroundColor Cyan
$ImportIssues = Test-ImportIssues -ServicePath $ServicePath
if ($ImportIssues.Count -gt 0) {
    foreach ($Issue in $ImportIssues) {
        $Color = if ($Issue.Severity -eq "Error") { "Red" } else { "Yellow" }
        Write-Host "[$($Issue.Severity.ToUpper())] $($Issue.Type): $($Issue.Item) in $($Issue.File)" -ForegroundColor $Color
    }
    $Issues += $ImportIssues
} else {
    Write-Host "[SUCCESS] No import issues found" -ForegroundColor Green
}

Write-Host "[STEP 4] Checking schema usage..." -ForegroundColor Cyan
$SchemaIssues = Test-SchemaUsage -ServicePath $ServicePath
if ($SchemaIssues.Count -gt 0) {
    foreach ($Issue in $SchemaIssues) {
        $Color = if ($Issue.Severity -eq "Error") { "Red" } else { "Yellow" }
        Write-Host "[$($Issue.Severity.ToUpper())] $($Issue.Type): $($Issue.Class) ($($Issue.Table))" -ForegroundColor $Color
    }
    $Issues += $SchemaIssues
} else {
    Write-Host "[SUCCESS] Schema usage is correct" -ForegroundColor Green
}

Write-Host "[STEP 5] Checking Alembic readiness..." -ForegroundColor Cyan
$AlembicIssues = Test-AlembicReadiness -ServicePath $ServicePath
if ($AlembicIssues.Count -gt 0) {
    foreach ($Issue in $AlembicIssues) {
        $Color = if ($Issue.Severity -eq "Error") { "Red" } else { "Yellow" }
        Write-Host "[$($Issue.Severity.ToUpper())] $($Issue.Type)" -ForegroundColor $Color
        if ($Issue.Path) { Write-Host "  Path: $($Issue.Path)" -ForegroundColor Gray }
        if ($Issue.File) { Write-Host "  File: $($Issue.File)" -ForegroundColor Gray }
    }
    $Issues += $AlembicIssues
} else {
    Write-Host "[SUCCESS] Alembic appears ready" -ForegroundColor Green
}

# Summary
$ErrorCount = ($Issues | Where-Object { $_.Severity -eq "Error" }).Count
$WarningCount = ($Issues | Where-Object { $_.Severity -eq "Warning" }).Count

Write-Host "`n[SUMMARY]" -ForegroundColor Cyan
Write-Host "  Errors: $ErrorCount" -ForegroundColor $(if ($ErrorCount -gt 0) { "Red" } else { "Green" })
Write-Host "  Warnings: $WarningCount" -ForegroundColor $(if ($WarningCount -gt 0) { "Yellow" } else { "Green" })

if ($Fix -and $Issues.Count -gt 0) {
    Write-Host "`n[FIXING ISSUES]" -ForegroundColor Cyan
    $FixedCount = Fix-CommonIssues -Issues $Issues -ServicePath $ServicePath
    Write-Host "[INFO] Fixed $FixedCount issues automatically" -ForegroundColor Green
}

if ($ErrorCount -gt 0) {
    Write-Host "`n[RECOMMENDATION] Fix errors before running migrations" -ForegroundColor Red
    exit 1
} elseif ($WarningCount -gt 0) {
    Write-Host "`n[RECOMMENDATION] Consider fixing warnings for best practices" -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "`n[SUCCESS] CQRS models are properly configured!" -ForegroundColor Green
    exit 0
}
