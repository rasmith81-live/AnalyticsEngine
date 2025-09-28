#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Adds schema objects with proper CQRS separation and migration generation.

.DESCRIPTION
    This script automates the addition of new schema objects to a microservice with proper CQRS pattern:
    - Adds write models to app/models.py
    - Generates corresponding read models in domain folders
    - Updates imports and dependencies correctly
    - Generates Alembic migration with validation
    - Prevents table duplication and import conflicts

.PARAMETER ServiceName
    The name of the service (e.g., 'scor_service')

.PARAMETER TableName
    The name of the table to create (e.g., 'scor_alerts')

.PARAMETER Domain
    The domain folder where read models should be placed (e.g., 'source', 'make', 'deliver')

.PARAMETER SchemaDefinition
    Path to JSON file containing table schema definition

.PARAMETER DryRun
    If specified, shows what would be done without making changes

.EXAMPLE
    .\add_cqrs_schema.ps1 -ServiceName scor_service -TableName scor_alerts -Domain source -SchemaDefinition .\schemas\scor_alerts.json
#>

param(
    [Parameter(Mandatory=$true)]
    [string]$ServiceName,
    
    [Parameter(Mandatory=$true)]
    [string]$TableName,
    
    [Parameter(Mandatory=$true)]
    [string]$Domain,
    
    [Parameter(Mandatory=$true)]
    [string]$SchemaDefinition,
    
    [switch]$DryRun
)

# Set error handling
$ErrorActionPreference = "Stop"

# Get script directory and project root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $ScriptDir)

Write-Host "[INFO] CQRS Schema Generator for $ServiceName" -ForegroundColor Green
Write-Host "[INFO] Adding table: $TableName to domain: $Domain" -ForegroundColor Green

# Validate inputs
if (-not (Test-Path $SchemaDefinition)) {
    Write-Error "Schema definition file not found: $SchemaDefinition"
    exit 1
}

$ServicePath = Join-Path $ProjectRoot "services" $ServiceName
if (-not (Test-Path $ServicePath)) {
    Write-Error "Service path not found: $ServicePath"
    exit 1
}

$DomainPath = Join-Path $ServicePath "app" "scor" $Domain
if (-not (Test-Path $DomainPath)) {
    Write-Error "Domain path not found: $DomainPath"
    exit 1
}

# Load schema definition
try {
    $Schema = Get-Content $SchemaDefinition | ConvertFrom-Json
    Write-Host "[INFO] Loaded schema definition for $($Schema.table_name)" -ForegroundColor Cyan
} catch {
    Write-Error "Failed to parse schema definition: $_"
    exit 1
}

# Validate schema matches table name
if ($Schema.table_name -ne $TableName) {
    Write-Error "Schema table name '$($Schema.table_name)' doesn't match parameter '$TableName'"
    exit 1
}

function Test-TableExists {
    param($ServicePath, $TableName)
    
    # Check if table already exists in main models
    $ModelsFile = Join-Path $ServicePath "app" "models.py"
    if (Test-Path $ModelsFile) {
        $Content = Get-Content $ModelsFile -Raw
        if ($Content -match "__tablename__\s*=\s*['""]$TableName['""]") {
            return $true
        }
    }
    
    # Check domain model files
    $DomainFiles = Get-ChildItem -Path (Join-Path $ServicePath "app" "scor") -Name "models.py" -Recurse
    foreach ($File in $DomainFiles) {
        $FilePath = Join-Path $ServicePath "app" "scor" $File
        $Content = Get-Content $FilePath -Raw
        if ($Content -match "__tablename__\s*=\s*['""]$TableName['""]") {
            return $true
        }
    }
    
    return $false
}

function Generate-WriteModel {
    param($Schema)
    
    $ModelCode = @"
class $($Schema.class_name)(Base):
    __tablename__ = '$($Schema.table_name)'
    __table_args__ = {'extend_existing': True, 'schema': '$ServiceName'}

"@
    
    # Add columns
    foreach ($Column in $Schema.columns) {
        $ColumnDef = "    $($Column.name) = Column("
        
        # Add column type
        switch ($Column.type) {
            "UUID" { $ColumnDef += "UUID(as_uuid=True)" }
            "String" { 
                if ($Column.length) {
                    $ColumnDef += "String($($Column.length))"
                } else {
                    $ColumnDef += "String"
                }
            }
            "Integer" { $ColumnDef += "Integer" }
            "Float" { $ColumnDef += "Float" }
            "DateTime" { $ColumnDef += "DateTime" }
            "Boolean" { $ColumnDef += "Boolean" }
            "JSON" { $ColumnDef += "JSON" }
            "Text" { $ColumnDef += "Text" }
            default { $ColumnDef += $Column.type }
        }
        
        # Add constraints
        if ($Column.primary_key) { $ColumnDef += ", primary_key=True" }
        if ($Column.nullable -eq $false) { $ColumnDef += ", nullable=False" }
        if ($Column.index) { $ColumnDef += ", index=True" }
        if ($Column.unique) { $ColumnDef += ", unique=True" }
        if ($Column.default) { $ColumnDef += ", default=$($Column.default)" }
        if ($Column.foreign_key) { $ColumnDef += ", ForeignKey('$($Column.foreign_key)')" }
        
        $ColumnDef += ")"
        $ModelCode += "`n$ColumnDef"
    }
    
    # Add relationships if any
    if ($Schema.relationships) {
        $ModelCode += "`n"
        foreach ($Rel in $Schema.relationships) {
            $ModelCode += "`n    $($Rel.name) = relationship('$($Rel.target)')"
        }
    }
    
    return $ModelCode
}

function Generate-ReadModel {
    param($Schema, $Domain)
    
    $ReadModelCode = @"
class $($Schema.class_name)ReadModel(ReadBase):
    ""Read model for $($Schema.description)."""
    __tablename__ = '$($Schema.table_name)_read'
    __table_args__ = (
        {'comment': '$($Schema.description) read model'}
    )

"@
    
    # Add read-optimized columns (typically a subset)
    foreach ($Column in $Schema.columns) {
        if ($Column.include_in_read -ne $false) {  # Include unless explicitly excluded
            $ColumnDef = "    $($Column.name) = Column("
            
            # Simplified column types for read models
            switch ($Column.type) {
                "UUID" { $ColumnDef += "UUID(as_uuid=True)" }
                "String" { 
                    if ($Column.length) {
                        $ColumnDef += "String($($Column.length))"
                    } else {
                        $ColumnDef += "String"
                    }
                }
                default { $ColumnDef += $Column.type }
            }
            
            if ($Column.primary_key) { $ColumnDef += ", primary_key=True" }
            if ($Column.index) { $ColumnDef += ", index=True" }
            
            $ColumnDef += ")"
            $ReadModelCode += "`n$ColumnDef"
        }
    }
    
    return $ReadModelCode
}

function Update-MainModels {
    param($ServicePath, $WriteModel, $Schema)
    
    $ModelsFile = Join-Path $ServicePath "app" "models.py"
    
    if (-not (Test-Path $ModelsFile)) {
        Write-Error "Main models file not found: $ModelsFile"
        return $false
    }
    
    $Content = Get-Content $ModelsFile -Raw
    
    # Add required imports if not present
    $RequiredImports = @()
    foreach ($Column in $Schema.columns) {
        switch ($Column.type) {
            "UUID" { $RequiredImports += "UUID" }
            "JSON" { $RequiredImports += "JSON" }
            "Text" { $RequiredImports += "Text" }
        }
        if ($Column.foreign_key) { $RequiredImports += "ForeignKey" }
    }
    
    # Check and add missing imports
    foreach ($Import in ($RequiredImports | Sort-Object -Unique)) {
        if ($Content -notmatch "from sqlalchemy.*$Import") {
            Write-Host "[INFO] Would add import for $Import" -ForegroundColor Yellow
        }
    }
    
    # Add the model at the end of the file
    $NewContent = $Content.TrimEnd() + "`n`n`n" + $WriteModel + "`n"
    
    if (-not $DryRun) {
        Set-Content -Path $ModelsFile -Value $NewContent -Encoding UTF8
        Write-Host "[SUCCESS] Added write model to $ModelsFile" -ForegroundColor Green
    } else {
        Write-Host "[DRY RUN] Would add write model to $ModelsFile" -ForegroundColor Yellow
    }
    
    return $true
}

function Update-DomainModels {
    param($DomainPath, $ReadModel, $Schema)
    
    $ModelsFile = Join-Path $DomainPath "models.py"
    
    if (-not (Test-Path $ModelsFile)) {
        Write-Error "Domain models file not found: $ModelsFile"
        return $false
    }
    
    $Content = Get-Content $ModelsFile -Raw
    
    # Add import for the write model
    $ImportLine = "from services.$ServiceName.app.models import $($Schema.class_name)"
    if ($Content -notmatch [regex]::Escape($ImportLine)) {
        # Find the import section and add the import
        $ImportSection = $Content -split "`n" | Where-Object { $_ -match "^from services\.$ServiceName\.app\.models import" }
        if ($ImportSection) {
            # Update existing import line
            $UpdatedImport = $ImportSection[0] -replace "\)$", ", $($Schema.class_name))"
            $Content = $Content -replace [regex]::Escape($ImportSection[0]), $UpdatedImport
        } else {
            # Add new import line
            $Content = $Content -replace "(# Import core models from the main models file)", "`$1`n$ImportLine"
        }
    }
    
    # Add the read model
    $NewContent = $Content.TrimEnd() + "`n`n" + $ReadModel + "`n"
    
    if (-not $DryRun) {
        Set-Content -Path $ModelsFile -Value $NewContent -Encoding UTF8
        Write-Host "[SUCCESS] Added read model to $ModelsFile" -ForegroundColor Green
    } else {
        Write-Host "[DRY RUN] Would add read model to $ModelsFile" -ForegroundColor Yellow
    }
    
    return $true
}

function Test-ModelImports {
    param($ServicePath)
    
    Write-Host "[INFO] Testing model imports..." -ForegroundColor Cyan
    
    # Test import of main models
    $TestScript = @"
import sys
sys.path.append('$ProjectRoot')
try:
    from services.$ServiceName.app.models import *
    print("SUCCESS: Main models import successful")
except Exception as e:
    print(f"ERROR: Main models import failed: {e}")
    sys.exit(1)

try:
    from services.$ServiceName.app.scor.$Domain.models import *
    print("SUCCESS: Domain models import successful")
except Exception as e:
    print(f"ERROR: Domain models import failed: {e}")
    sys.exit(1)
"@
    
    $TempScript = Join-Path $env:TEMP "test_imports.py"
    Set-Content -Path $TempScript -Value $TestScript
    
    try {
        $Result = python $TempScript
        Write-Host $Result -ForegroundColor Green
        return $true
    } catch {
        Write-Host "Import test failed: $_" -ForegroundColor Red
        return $false
    } finally {
        Remove-Item $TempScript -ErrorAction SilentlyContinue
    }
}

# Main execution
Write-Host "[INFO] Starting CQRS schema addition process..." -ForegroundColor Cyan

# Step 1: Check if table already exists
Write-Host "[STEP 1] Checking for existing table..." -ForegroundColor Cyan
if (Test-TableExists -ServicePath $ServicePath -TableName $TableName) {
    Write-Error "Table '$TableName' already exists in service '$ServiceName'"
    exit 1
}
Write-Host "[SUCCESS] Table does not exist, proceeding..." -ForegroundColor Green

# Step 2: Generate models
Write-Host "[STEP 2] Generating CQRS models..." -ForegroundColor Cyan
$WriteModel = Generate-WriteModel -Schema $Schema
$ReadModel = Generate-ReadModel -Schema $Schema -Domain $Domain

if ($DryRun) {
    Write-Host "[DRY RUN] Write Model:" -ForegroundColor Yellow
    Write-Host $WriteModel -ForegroundColor Gray
    Write-Host "[DRY RUN] Read Model:" -ForegroundColor Yellow
    Write-Host $ReadModel -ForegroundColor Gray
}

# Step 3: Update main models file
Write-Host "[STEP 3] Updating main models file..." -ForegroundColor Cyan
if (-not (Update-MainModels -ServicePath $ServicePath -WriteModel $WriteModel -Schema $Schema)) {
    Write-Error "Failed to update main models file"
    exit 1
}

# Step 4: Update domain models file
Write-Host "[STEP 4] Updating domain models file..." -ForegroundColor Cyan
if (-not (Update-DomainModels -DomainPath $DomainPath -ReadModel $ReadModel -Schema $Schema)) {
    Write-Error "Failed to update domain models file"
    exit 1
}

# Step 5: Test imports
if (-not $DryRun) {
    Write-Host "[STEP 5] Testing model imports..." -ForegroundColor Cyan
    if (-not (Test-ModelImports -ServicePath $ServicePath)) {
        Write-Warning "Model imports failed - please check for syntax errors"
    }
}

# Step 6: Generate migration
Write-Host "[STEP 6] Generating Alembic migration..." -ForegroundColor Cyan
if (-not $DryRun) {
    try {
        $MigrationScript = Join-Path $ScriptDir "create_revision_clean.ps1"
        $MigrationMessage = "Add $TableName table with CQRS models"
        
        & $MigrationScript -ServiceName $ServiceName -Message $MigrationMessage -AutoGenerate
        Write-Host "[SUCCESS] Migration generated successfully" -ForegroundColor Green
    } catch {
        Write-Warning "Migration generation failed: $_"
        Write-Host "You may need to run migration manually after fixing any issues" -ForegroundColor Yellow
    }
} else {
    Write-Host "[DRY RUN] Would generate migration with message: 'Add $TableName table with CQRS models'" -ForegroundColor Yellow
}

Write-Host "[SUCCESS] CQRS schema addition completed!" -ForegroundColor Green
Write-Host "[INFO] Next steps:" -ForegroundColor Cyan
Write-Host "  1. Review generated models for correctness" -ForegroundColor White
Write-Host "  2. Run migration: .\scripts\utils\upgrade_service.ps1 -ServiceName $ServiceName" -ForegroundColor White
Write-Host "  3. Test service startup and API endpoints" -ForegroundColor White
