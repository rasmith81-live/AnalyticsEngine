@echo off
REM KPI Consolidation Analyzer
REM Identifies overlapping KPIs and generates recommendations

echo ================================================================================
echo KPI Consolidation Analyzer
echo ================================================================================
echo.
echo This script will:
echo   1. Analyze all KPIs for similarity
echo   2. Identify consolidation opportunities
echo   3. Generate recommendations file with checkboxes
echo.
echo ================================================================================
echo.

cd /d "%~dp0"

python kpi_consolidation_analyzer.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================================
    echo Analysis complete!
    echo.
    echo Next steps:
    echo   1. Open: output\kpi_consolidation_recommendations.md
    echo   2. Review recommendations and check boxes to approve
    echo   3. Run: run_consolidation_executor.bat
    echo ================================================================================
) else (
    echo.
    echo ================================================================================
    echo Analysis failed. Check logs for details.
    echo ================================================================================
)

echo.
pause
