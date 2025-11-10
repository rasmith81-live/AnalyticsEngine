@echo off
REM Arithmetic Governance - Abstract arithmetic modifiers from KPI names
REM UPDATED: Now works with dictionary-based definitions
REM Usage: run_arithmetic_governance.bat

echo ================================================================================
echo Arithmetic Governance - KPI Modifier Abstraction (Dictionary-Based)
echo ================================================================================
echo.
echo This script will:
echo   1. Scan all KPIs for arithmetic modifiers (average, max, min, etc.)
echo   2. Remove modifiers from names and definitions
echo   3. Add aggregation_methods metadata
echo   4. Generate comprehensive reports
echo.
echo Using: analytics_metadata_service/definitions/kpis (Dictionary Format)
echo ================================================================================
echo.

cd /d "%~dp0"

REM Check if dry run
set /p DRYRUN="Run in DRY RUN mode? (Y/N, default=Y): "
if /i "%DRYRUN%"=="" set DRYRUN=Y
if /i "%DRYRUN%"=="N" (
    echo.
    echo ⚠️  WARNING: This will modify KPI files!
    echo    A backup will be created automatically.
    echo.
    set /p CONFIRM="Are you sure you want to proceed? (Y/N): "
    if /i not "%CONFIRM%"=="Y" (
        echo.
        echo Operation cancelled.
        pause
        exit /b
    )
    
    REM Set dry_run to false in config
    powershell -Command "(Get-Content config.json) -replace '\"dry_run\": true', '\"dry_run\": false' | Set-Content config.json"
) else (
    echo.
    echo Running in DRY RUN mode - no files will be modified
    echo.
    
    REM Set dry_run to true in config
    powershell -Command "(Get-Content config.json) -replace '\"dry_run\": false', '\"dry_run\": true' | Set-Content config.json"
)

echo Running arithmetic governance...
echo.
python arithmetic_governance.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================================
    echo Governance completed successfully!
    echo Check output folder for detailed reports:
    echo   - output\arithmetic_governance_report.json
    echo   - output\arithmetic_governance_report.md
    echo ================================================================================
) else (
    echo.
    echo ================================================================================
    echo Governance completed with errors.
    echo Check logs folder for details.
    echo ================================================================================
)

echo.
pause
