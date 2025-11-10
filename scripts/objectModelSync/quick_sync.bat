@echo off
REM Quick Sync - Run full object model synchronization
REM UPDATED: Now works with dictionary-based definitions in analytics_metadata_service
REM Usage: quick_sync.bat

echo ================================================================================
echo Object Model Synchronization - Quick Sync (Dictionary-Based)
echo ================================================================================
echo.

cd /d "%~dp0"

echo Running full synchronization...
python run_full_sync.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================================
    echo Synchronization completed successfully!
    echo Check output folder for reports.
    echo ================================================================================
) else (
    echo.
    echo ================================================================================
    echo Synchronization completed with errors.
    echo Check logs folder for details.
    echo ================================================================================
)

pause
