@echo off
REM ============================================================================
REM KPI Excel/CSV Processor - Batch Wrapper
REM UPDATED: Now generates dictionary-based definitions for analytics_metadata_service
REM ============================================================================
REM
REM This script processes Excel/CSV files containing KPI data and generates
REM Python KPI definition files with proper abstraction of arithmetic modifiers
REM and time periods.
REM
REM Output: Dictionary-based definitions in analytics_metadata_service/definitions
REM
REM Usage:
REM   process_kpi_excel.bat <excel_file> <module_name> <value_chain>
REM
REM Arguments:
REM   excel_file   - Path to Excel (.xlsx, .xls) or CSV (.csv) file
REM   module_name  - Module name (e.g., SOURCING, SALES, CUSTOMER_SERVICE)
REM   value_chain  - Value chain (e.g., SUPPLY_CHAIN, REVENUE, CUSTOMER_EXPERIENCE)
REM
REM Examples:
REM   process_kpi_excel.bat "C:\Downloads\kpis.csv" SOURCING SUPPLY_CHAIN
REM   process_kpi_excel.bat kpis.xlsx SALES REVENUE
REM
REM ============================================================================

setlocal enabledelayedexpansion

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    echo.
    pause
    exit /b 1
)

REM Check arguments
if "%~1"=="" (
    echo.
    echo ============================================================================
    echo KPI Excel/CSV Processor
    echo ============================================================================
    echo.
    echo Usage: process_kpi_excel.bat ^<excel_file^> ^<module_name^> ^<value_chain^>
    echo.
    echo Arguments:
    echo   excel_file   - Path to Excel or CSV file containing KPI data
    echo   module_name  - Module name to assign (e.g., SOURCING, SALES)
    echo   value_chain  - Value chain to assign (e.g., SUPPLY_CHAIN, REVENUE)
    echo.
    echo Examples:
    echo   process_kpi_excel.bat "C:\Downloads\kpis.csv" SOURCING SUPPLY_CHAIN
    echo   process_kpi_excel.bat kpis.xlsx SALES REVENUE
    echo.
    echo Available Value Chains:
    echo   - SUPPLY_CHAIN
    echo   - REVENUE
    echo   - CUSTOMER_EXPERIENCE
    echo   - OPERATIONS
    echo   - FINANCE
    echo.
    echo Common Modules:
    echo   Supply Chain: SOURCING, INVENTORY_MANAGEMENT, LOGISTICS, WAREHOUSE
    echo   Revenue: SALES, MARKETING, PRICING
    echo   Customer Experience: CUSTOMER_SERVICE, SUPPORT, RETENTION
    echo.
    echo ============================================================================
    echo.
    pause
    exit /b 1
)

if "%~2"=="" (
    echo ERROR: Module name is required
    echo Usage: process_kpi_excel.bat ^<excel_file^> ^<module_name^> ^<value_chain^>
    pause
    exit /b 1
)

if "%~3"=="" (
    echo ERROR: Value chain is required
    echo Usage: process_kpi_excel.bat ^<excel_file^> ^<module_name^> ^<value_chain^>
    pause
    exit /b 1
)

REM Store arguments
set "EXCEL_FILE=%~1"
set "MODULE_NAME=%~2"
set "VALUE_CHAIN=%~3"

REM Check if file exists
if not exist "%EXCEL_FILE%" (
    echo.
    echo ERROR: File not found: %EXCEL_FILE%
    echo.
    pause
    exit /b 1
)

REM Display processing information
echo.
echo ============================================================================
echo KPI Excel/CSV Processor
echo ============================================================================
echo.
echo Source File:  %EXCEL_FILE%
echo Module:       %MODULE_NAME%
echo Value Chain:  %VALUE_CHAIN%
echo.
echo ============================================================================
echo.

REM Confirm before processing
set /p CONFIRM="Process this file? (Y/N): "
if /i not "%CONFIRM%"=="Y" (
    echo.
    echo Operation cancelled by user.
    echo.
    pause
    exit /b 0
)

echo.
echo Starting KPI processing...
echo.

REM Run the Python processor
python "%~dp0kpi_excel_processor.py" --file "%EXCEL_FILE%" --module %MODULE_NAME% --chain %VALUE_CHAIN%

if errorlevel 1 (
    echo.
    echo ============================================================================
    echo ERROR: KPI processing failed
    echo ============================================================================
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================================
echo SUCCESS: KPI processing completed
echo ============================================================================
echo.
echo Next Steps:
echo   1. Review the generated KPI files in:
echo      services\business_services\analytics_models\definitions\kpis\
echo.
echo   2. Run the governance suite to sync object models:
echo      cd scripts\objectModelSync
echo      run_governance.bat
echo.
echo   3. Select Option 1 (Full Governance) to:
echo      - Sync object metadata
echo      - Update UML relationships
echo      - Run arithmetic governance
echo      - Analyze for KPI consolidation
echo.
echo ============================================================================
echo.

set /p RUN_GOVERNANCE="Would you like to run the governance suite now? (Y/N): "
if /i "%RUN_GOVERNANCE%"=="Y" (
    echo.
    echo Launching governance suite...
    cd /d "%~dp0..\objectModelSync"
    call run_governance.bat
)

echo.
pause
