@echo off
REM KPI Consolidation Executor
REM Executes approved consolidations from recommendations file

echo ================================================================================
echo KPI Consolidation Executor
echo ================================================================================
echo.

cd /d "%~dp0"

REM Check if recommendations exist
if not exist "output\kpi_consolidation_recommendations.md" (
    echo ❌ Error: Recommendations file not found!
    echo.
    echo Please run: run_consolidation_analysis.bat first
    echo.
    pause
    exit /b 1
)

echo This script will execute approved consolidations.
echo.
echo ⚠️  WARNING: This will modify and delete KPI files!
echo    - Merges metadata into primary KPIs
echo    - Deletes secondary KPI files
echo    - Creates automatic backup
echo.

set /p CONFIRM="Have you reviewed and approved recommendations? (Y/N): "
if /i not "%CONFIRM%"=="Y" (
    echo.
    echo Operation cancelled.
    echo Please review: output\kpi_consolidation_recommendations.md
    pause
    exit /b
)

echo.
echo Executing consolidations...
echo.

python kpi_consolidation_executor.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================================
    echo Consolidation complete!
    echo.
    echo Check output folder for execution report.
    echo.
    echo Recommended next steps:
    echo   1. Run: python validate_integrity.py
    echo   2. Run: python run_full_sync.py
    echo ================================================================================
) else (
    echo.
    echo ================================================================================
    echo Consolidation failed. Check logs for details.
    echo You can restore from backup if needed.
    echo ================================================================================
)

echo.
pause
