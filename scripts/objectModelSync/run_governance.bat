@echo off
REM Master Governance Script
REM UPDATED: Now works with dictionary-based definitions in analytics_metadata_service
REM Controls execution of all three governance processes

echo ================================================================================
echo Analytics Governance Suite (Dictionary-Based)
echo ================================================================================
echo.
echo This script manages four governance processes:
echo   1. Main Sync - Object model and KPI synchronization
echo   2. Arithmetic Governance - Abstract arithmetic modifiers from KPI names
echo   3. KPI Consolidation - Identify and consolidate duplicate KPIs
echo   4. KPI Validation - Ensure complete KPI definitions with sample data
echo.
echo Using: analytics_metadata_service/definitions (Dictionary Format)
echo ================================================================================
echo.

cd /d "%~dp0"

:MENU
echo.
echo Select an option:
echo.
echo   1 - Run ALL processes in sequence (Full Governance)
echo   2 - Main Sync only
echo   3 - Arithmetic Governance only
echo   4 - KPI Consolidation Analysis only
echo   5 - KPI Consolidation Execution only
echo   6 - KPI Validation and Enhancement only
echo   7 - Regenerate Sample Data only
echo   0 - Exit
echo.
set /p CHOICE="Enter your choice (0-7): "

if "%CHOICE%"=="0" goto END
if "%CHOICE%"=="1" goto RUN_ALL
if "%CHOICE%"=="2" goto RUN_SYNC
if "%CHOICE%"=="3" goto RUN_ARITHMETIC
if "%CHOICE%"=="4" goto RUN_CONSOLIDATION_ANALYSIS
if "%CHOICE%"=="5" goto RUN_CONSOLIDATION_EXECUTION
if "%CHOICE%"=="6" goto RUN_KPI_VALIDATION
if "%CHOICE%"=="7" goto RUN_REGENERATE_SAMPLE_DATA

echo Invalid choice. Please try again.
goto MENU

REM ============================================================================
REM Run ALL processes in sequence
REM ============================================================================
:RUN_ALL
echo.
echo ================================================================================
echo Running FULL GOVERNANCE SUITE
echo ================================================================================
echo.
echo This will run all four processes in sequence:
echo   1. Main Sync
echo   2. Arithmetic Governance
echo   3. KPI Consolidation Analysis
echo   4. KPI Validation and Enhancement
echo.
set /p CONFIRM_ALL="Continue? (Y/N): "
if /i not "%CONFIRM_ALL%"=="Y" goto MENU

echo.
echo --------------------------------------------------------------------------------
echo STEP 1/3: Main Sync
echo --------------------------------------------------------------------------------
call :RUN_SYNC_INTERNAL
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Main Sync failed. Stopping execution.
    pause
    goto MENU
)

echo.
echo --------------------------------------------------------------------------------
echo STEP 2/3: Arithmetic Governance
echo --------------------------------------------------------------------------------
call :RUN_ARITHMETIC_INTERNAL
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ⚠️  Arithmetic Governance had issues, but continuing...
)

echo.
echo --------------------------------------------------------------------------------
echo STEP 3/4: KPI Consolidation Analysis
echo --------------------------------------------------------------------------------
call :RUN_CONSOLIDATION_ANALYSIS_INTERNAL
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ⚠️  Consolidation Analysis had issues, but continuing...
)

echo.
echo --------------------------------------------------------------------------------
echo STEP 4/4: KPI Validation and Enhancement
echo --------------------------------------------------------------------------------
call :RUN_KPI_VALIDATION_INTERNAL
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ⚠️  KPI Validation had issues, but continuing...
)

echo.
echo ================================================================================
echo FULL GOVERNANCE COMPLETE
echo ================================================================================
echo.
echo Next steps:
echo   1. Review: output\kpi_consolidation_recommendations.md
echo   2. Approve consolidations by checking boxes
echo   3. Run option 5 to execute approved consolidations
echo   4. Review: output\kpi_validation_report_*.json for validation results
echo.
echo ================================================================================
pause
goto MENU

REM ============================================================================
REM Run Main Sync only
REM ============================================================================
:RUN_SYNC
call :RUN_SYNC_INTERNAL
pause
goto MENU

:RUN_SYNC_INTERNAL
echo.
echo Running Main Sync...
echo.
python run_full_sync.py
exit /b %ERRORLEVEL%

REM ============================================================================
REM Run Arithmetic Governance only
REM ============================================================================
:RUN_ARITHMETIC
call :RUN_ARITHMETIC_INTERNAL
pause
goto MENU

:RUN_ARITHMETIC_INTERNAL
echo.
set /p DRYRUN_ARITH="Run in DRY RUN mode? (Y/N, default=Y): "
if /i "%DRYRUN_ARITH%"=="" set DRYRUN_ARITH=Y

if /i "%DRYRUN_ARITH%"=="N" (
    echo.
    echo ⚠️  WARNING: This will modify KPI files!
    echo    A backup will be created automatically.
    echo.
    set /p CONFIRM_ARITH="Are you sure? (Y/N): "
    if /i not "%CONFIRM_ARITH%"=="Y" exit /b 1
    
    powershell -Command "(Get-Content config.json) -replace '\"dry_run\": true', '\"dry_run\": false' | Set-Content config.json"
) else (
    echo.
    echo Running in DRY RUN mode - no files will be modified
    echo.
    powershell -Command "(Get-Content config.json) -replace '\"dry_run\": false', '\"dry_run\": true' | Set-Content config.json"
)

python arithmetic_governance.py
set ARITH_RESULT=%ERRORLEVEL%

if %ARITH_RESULT% EQU 0 (
    echo.
    echo ✅ Arithmetic Governance completed successfully!
    echo Check output folder for reports.
) else (
    echo.
    echo ❌ Arithmetic Governance completed with errors.
)

exit /b %ARITH_RESULT%

REM ============================================================================
REM Run KPI Consolidation Analysis only
REM ============================================================================
:RUN_CONSOLIDATION_ANALYSIS
call :RUN_CONSOLIDATION_ANALYSIS_INTERNAL
pause
goto MENU

:RUN_CONSOLIDATION_ANALYSIS_INTERNAL
echo.
echo Running KPI Consolidation Analysis...
echo.
python kpi_consolidation_analyzer.py
set ANALYSIS_RESULT=%ERRORLEVEL%

if %ANALYSIS_RESULT% EQU 0 (
    echo.
    echo ✅ Analysis complete!
    echo.
    echo Next steps:
    echo   1. Open: output\kpi_consolidation_recommendations.md
    echo   2. Review recommendations and check boxes to approve
    echo   3. Run option 6 to execute approved consolidations
) else (
    echo.
    echo ❌ Analysis failed.
)

exit /b %ANALYSIS_RESULT%

REM ============================================================================
REM Run KPI Consolidation Execution only
REM ============================================================================
:RUN_CONSOLIDATION_EXECUTION
call :RUN_CONSOLIDATION_EXECUTION_INTERNAL
pause
goto MENU

:RUN_CONSOLIDATION_EXECUTION_INTERNAL
echo.
if not exist "output\kpi_consolidation_recommendations.md" (
    echo ❌ Error: Recommendations file not found!
    echo.
    echo Please run option 5 first to generate recommendations.
    exit /b 1
)

echo This will execute approved consolidations.
echo.
echo ⚠️  WARNING: This will modify and delete KPI files!
echo    - Merges metadata into primary KPIs
echo    - Deletes secondary KPI files
echo    - Creates automatic backup
echo.
set /p CONFIRM_EXEC="Have you reviewed and approved recommendations? (Y/N): "
if /i not "%CONFIRM_EXEC%"=="Y" (
    echo.
    echo Operation cancelled.
    exit /b 1
)

echo.
echo Executing consolidations...
echo.
python kpi_consolidation_executor.py
set EXEC_RESULT=%ERRORLEVEL%

if %EXEC_RESULT% EQU 0 (
    echo.
    echo ✅ Consolidation complete!
    echo.
    echo Recommended next steps:
    echo   1. Run option 2 (Main Sync) to update all references
    echo   2. Run: python validate_integrity.py
) else (
    echo.
    echo ❌ Consolidation failed.
    echo You can restore from backup if needed.
)

exit /b %EXEC_RESULT%

REM ============================================================================
REM Run KPI Validation and Enhancement
REM ============================================================================
:RUN_KPI_VALIDATION
call :RUN_KPI_VALIDATION_INTERNAL
pause
goto MENU

:RUN_KPI_VALIDATION_INTERNAL
echo.
echo Running KPI Validation and Enhancement...
echo.
echo This will:
echo   - Validate all 21 required KPI fields
echo   - Add missing fields with sensible defaults
echo   - Generate formula-aware sample data
echo   - Create automatic backup
echo.
python validate_and_enhance_kpis.py
set VALIDATION_RESULT=%ERRORLEVEL%

if %VALIDATION_RESULT% EQU 0 (
    echo.
    echo ✅ KPI Validation complete!
    echo.
    echo Check output folder for validation report.
) else (
    echo.
    echo ❌ KPI Validation failed.
)

exit /b %VALIDATION_RESULT%

REM ============================================================================
REM Regenerate Sample Data
REM ============================================================================
:RUN_REGENERATE_SAMPLE_DATA
call :RUN_REGENERATE_SAMPLE_DATA_INTERNAL
pause
goto MENU

:RUN_REGENERATE_SAMPLE_DATA_INTERNAL
echo.
echo Regenerating Sample Data for All KPIs...
echo.
echo This will:
echo   - Regenerate sample_data for all KPIs
echo   - Use formula-aware generation
echo   - Create smart category names
echo   - Create automatic backup
echo.
echo ⚠️  WARNING: This will overwrite existing sample_data!
echo.
set /p CONFIRM_REGEN="Continue? (Y/N): "
if /i not "%CONFIRM_REGEN%"=="Y" (
    echo.
    echo Operation cancelled.
    exit /b 1
)

echo.
python regenerate_sample_data.py
set REGEN_RESULT=%ERRORLEVEL%

if %REGEN_RESULT% EQU 0 (
    echo.
    echo ✅ Sample data regeneration complete!
) else (
    echo.
    echo ❌ Sample data regeneration failed.
)

exit /b %REGEN_RESULT%

REM ============================================================================
REM Exit
REM ============================================================================
:END
echo.
echo Exiting...
exit /b 0
