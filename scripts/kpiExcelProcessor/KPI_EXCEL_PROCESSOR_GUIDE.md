# KPI Excel/CSV Processor Guide

## Overview

The KPI Excel/CSV Processor automates the generation of KPI Python files from Excel or CSV templates. It handles:

- ✅ **Arithmetic Abstraction** - Extracts modifiers (average, sum, min, max) into metadata
- ✅ **Time Period Abstraction** - Extracts periods (daily, weekly, monthly) into metadata
- ✅ **Object Detection** - Identifies required objects from formulas and descriptions
- ✅ **Module Assignment** - Maps KPIs to specified modules and value chains
- ✅ **Bulk Processing** - Processes entire Excel/CSV files at once

---

## Quick Start

### Command Line Usage

```powershell
# Basic syntax
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
.\process_kpi_excel.bat "<path_to_file>" <MODULE_NAME> <VALUE_CHAIN>

# Example 1: Process Sourcing KPIs
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\kpidepot.com-buying.csv" SOURCING SUPPLY_CHAIN

# Example 2: Process Sales KPIs
.\process_kpi_excel.bat "C:\Downloads\sales-kpis.xlsx" SALES REVENUE

# Example 3: Process Customer Service KPIs
.\process_kpi_excel.bat "C:\Downloads\support-kpis.csv" CUSTOMER_SERVICE CUSTOMER_EXPERIENCE
```

### Python Direct Usage

```powershell
# Direct Python call with more options
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
python kpi_excel_processor.py --file "C:\path\to\file.csv" --module SOURCING --chain SUPPLY_CHAIN

# With custom output directory
python kpi_excel_processor.py -f file.csv -m SALES -c REVENUE -o ./custom_output
```

---

## Arguments

### Required Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `<file_path>` | Path to Excel (.xlsx, .xls) or CSV (.csv) file | `"C:\Downloads\kpis.csv"` |
| `<MODULE_NAME>` | Module name (uppercase, underscores for spaces) | `SOURCING`, `CUSTOMER_SERVICE` |
| `<VALUE_CHAIN>` | Value chain assignment | `SUPPLY_CHAIN`, `REVENUE` |

### Optional Arguments (Python only)

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--output` | `-o` | Custom output directory | Auto-detect |

---

## Value Chains

### Available Value Chains

1. **SUPPLY_CHAIN** - Supply chain and operations
2. **REVENUE** - Sales, marketing, and revenue generation
3. **CUSTOMER_EXPERIENCE** - Customer service and support
4. **OPERATIONS** - General business operations
5. **FINANCE** - Financial management and accounting

---

## Module Mapping

### Supply Chain Value Chain

| Module | Description | Example KPIs |
|--------|-------------|--------------|
| `SOURCING` | Procurement and buying | Purchase Order Value, Supplier Performance |
| `INVENTORY_MANAGEMENT` | Stock and warehouse | Inventory Turnover, Stock Accuracy |
| `LOGISTICS` | Transportation and delivery | On-Time Delivery, Freight Cost |
| `WAREHOUSE` | Warehouse operations | Warehouse Utilization, Pick Accuracy |

### Revenue Value Chain

| Module | Description | Example KPIs |
|--------|-------------|--------------|
| `SALES` | Sales performance | Deal Size, Win Rate, Sales Cycle |
| `MARKETING` | Marketing effectiveness | Lead Generation, Campaign ROI |
| `PRICING` | Pricing strategy | Price Variance, Discount Rate |

### Customer Experience Value Chain

| Module | Description | Example KPIs |
|--------|-------------|--------------|
| `CUSTOMER_SERVICE` | Service quality | CSAT, First Response Time |
| `SUPPORT` | Technical support | Ticket Resolution, SLA Compliance |
| `RETENTION` | Customer retention | Churn Rate, NPS |

---

## Expected CSV/Excel Format

### Required Columns

The processor expects these columns (case-insensitive):

| Column Name | Description | Required |
|-------------|-------------|----------|
| `KPI` | KPI name | ✅ Yes |
| `Definition` | KPI description/definition | ✅ Yes |
| `Standard Formula` | Formula or calculation method | ✅ Yes |
| `Business Insights` | Optional insights | ⚪ Optional |
| `Measurement Approach` | Optional approach | ⚪ Optional |

### Example CSV Structure

```csv
KPI,Definition,Standard Formula
Average Purchase Order Value,The average value of purchase orders,Total Spend / Total Number of Purchase Orders
Backorder Rate,Percentage of orders on backorder,(Number of Backordered Items / Total Inventory Items) * 100
Supplier On-time Delivery Rate,Percentage of on-time deliveries,(Number of On-time Deliveries / Total Deliveries) * 100
```

---

## Processing Logic

### 1. Arithmetic Abstraction

The processor automatically detects and abstracts arithmetic modifiers:

**Input KPI Name**: "Average Purchase Order Value"  
**Output**:
- `code`: `PURCHASE_ORDER_VALUE` (modifier removed)
- `aggregation_methods`: `["average", "sum", "min", "max", "median"]`

### 2. Time Period Abstraction

Time periods are extracted and abstracted:

**Input**: "Monthly Sales Revenue"  
**Output**:
- `code`: `SALES_REVENUE` (period removed)
- `time_periods`: `["daily", "weekly", "monthly", "quarterly", "annually"]`

### 3. Object Detection

Required objects are identified from:
- KPI name
- Definition text
- Formula

**Example**:
- Formula: `(Number of On-time Deliveries / Total Deliveries) * 100`
- Detected Objects: `["Delivery", "Supplier"]`

### 4. File Generation

Each KPI generates a Python file:

```python
from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierOnTimeDeliveryRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_ON_TIME_DELIVERY_RATE",
            name_="Supplier On-time Delivery Rate",
            description_="Percentage of supplier deliveries on time",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=["Delivery", "Supplier"],
            formula_="(Number of On-time Deliveries / Total Deliveries) * 100",
            aggregation_methods=["average"],
            time_periods=["daily", "weekly", "monthly", "quarterly", "annually"]
        )
```

---

## Workflow

### Complete Processing Workflow

```
1. Prepare Excel/CSV file with KPI data
   ↓
2. Run: process_kpi_excel.bat <file> <module> <chain>
   ↓
3. Review generated KPI files in:
   services/business_services/analytics_models/definitions/kpis/
   ↓
4. Run governance suite:
   cd scripts/objectModelSync
   run_governance.bat → Option 1 (Full Governance)
   ↓
5. Review consolidation recommendations:
   scripts/objectModelSync/output/kpi_consolidation_recommendations.md
   ↓
6. Execute consolidation if needed:
   run_governance.bat → Option 5 (KPI Consolidation Execution)
   ↓
7. Verify object models and UML relationships
```

---

## Output

### Generated Files

1. **KPI Python Files**
   - Location: `services/business_services/analytics_models/definitions/kpis/`
   - Format: `<kpi_name>.py`
   - Example: `supplier_on_time_delivery_rate.py`

2. **Summary Report**
   - Location: `scripts/objectModelSync/<MODULE>_KPI_PROCESSING_SUMMARY.md`
   - Contains: List of all created KPIs, statistics, next steps

### Console Output

```
============================================================================
Processing KPIs for Module: SOURCING | Value Chain: SUPPLY_CHAIN
============================================================================

✓ [  1] Average Purchase Order Value                                → purchase_order_value.py
✓ [  2] Backorder Rate                                              → backorder_rate.py
✓ [  3] Supplier On-time Delivery Rate                              → supplier_on_time_delivery_rate.py
...

============================================================================
✓ Successfully created 43 KPI files
============================================================================

📄 Summary report created: scripts/objectModelSync/SOURCING_KPI_PROCESSING_SUMMARY.md

✓ All done! Created 43 KPI files for SOURCING module.

💡 Next step: Run governance suite to sync object models
   Command: cd scripts\objectModelSync && run_governance.bat
```

---

## Examples

### Example 1: Process Sourcing Module

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor

.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-buying.csv" SOURCING SUPPLY_CHAIN
```

**Result**: Creates 43 KPI files for Sourcing module

### Example 2: Process Multiple Modules

```powershell
# Process Sourcing
.\process_kpi_excel.bat "C:\Downloads\buying.csv" SOURCING SUPPLY_CHAIN

# Process Inventory
.\process_kpi_excel.bat "C:\Downloads\inventory.csv" INVENTORY_MANAGEMENT SUPPLY_CHAIN

# Process Logistics
.\process_kpi_excel.bat "C:\Downloads\logistics.csv" LOGISTICS SUPPLY_CHAIN

# Run governance once after all modules
cd objectModelSync
run_governance.bat
```

### Example 3: Custom Output Directory

```powershell
python kpi_excel_processor.py `
  --file "C:\Downloads\kpis.csv" `
  --module SALES `
  --chain REVENUE `
  --output "C:\CustomOutput\kpis"
```

---

## Troubleshooting

### Common Issues

#### Issue: "File not found"
**Solution**: Ensure the file path is correct and enclosed in quotes if it contains spaces.

```powershell
# ✗ Wrong
.\process_kpi_excel.bat C:\My Files\kpis.csv SOURCING SUPPLY_CHAIN

# ✓ Correct
.\process_kpi_excel.bat "C:\My Files\kpis.csv" SOURCING SUPPLY_CHAIN
```

#### Issue: "Python is not installed"
**Solution**: Install Python 3.7+ and ensure it's in your PATH.

```powershell
python --version  # Should show Python 3.7 or higher
```

#### Issue: "Missing required columns"
**Solution**: Ensure your CSV/Excel has at least these columns:
- `KPI`
- `Definition`
- `Standard Formula`

#### Issue: "No KPIs were processed"
**Solution**: Check that:
1. CSV/Excel file has data rows (not just headers)
2. `KPI` column is not empty
3. File encoding is UTF-8 or compatible

---

## Best Practices

### 1. File Preparation
- ✅ Use UTF-8 encoding for CSV files
- ✅ Ensure column headers match expected names
- ✅ Remove empty rows
- ✅ Clean up special characters in formulas

### 2. Module Naming
- ✅ Use UPPERCASE for module names
- ✅ Use underscores for multi-word modules: `CUSTOMER_SERVICE`
- ✅ Be consistent across related KPI files

### 3. Processing Workflow
- ✅ Process one module at a time
- ✅ Review generated files before running governance
- ✅ Run full governance suite after processing all modules
- ✅ Review consolidation recommendations carefully

### 4. Quality Checks
- ✅ Verify required objects are correctly identified
- ✅ Check that aggregation methods make sense
- ✅ Ensure time periods are appropriate
- ✅ Review generated code for syntax errors

---

## Integration with Governance Suite

After processing KPIs, run the governance suite:

```powershell
cd scripts\objectModelSync
run_governance.bat
```

**Select Option 1** (Full Governance) to:
1. ✅ Sync object metadata
2. ✅ Update UML relationships
3. ✅ Run arithmetic governance
4. ✅ Analyze for KPI consolidation

---

## Support

For issues or questions:
1. Check this guide for common solutions
2. Review the summary report for processing details
3. Check console output for specific error messages
4. Verify CSV/Excel format matches expected structure

---

**Last Updated**: November 8, 2025  
**Version**: 1.0
