# KPI Excel Processor

Automated tool for generating KPI Python files from Excel/CSV templates.

## 📁 Directory Structure

```
scripts/
├── kpiExcelProcessor/          ← You are here
│   ├── process_kpi_excel.bat   ← Main command to run
│   ├── kpi_excel_processor.py  ← Python processor
│   ├── KPI_EXCEL_PROCESSOR_GUIDE.md  ← Full documentation
│   └── README.md               ← This file
├── objectModelSync/            ← Governance suite
│   └── run_governance.bat      ← Run after processing KPIs
└── QUICK_REFERENCE.md          ← Quick command reference
```

## 🚀 Quick Start

```powershell
# Navigate to this directory
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor

# Process your KPI file
.\process_kpi_excel.bat "<path_to_csv>" <MODULE_NAME> <VALUE_CHAIN>

# Example
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-buying.csv" SOURCING SUPPLY_CHAIN
```

## 📖 Documentation

- **Full Guide**: [KPI_EXCEL_PROCESSOR_GUIDE.md](./KPI_EXCEL_PROCESSOR_GUIDE.md)
- **Quick Reference**: [../QUICK_REFERENCE.md](../QUICK_REFERENCE.md)

## 🎯 What It Does

1. ✅ Reads Excel/CSV files with KPI data
2. ✅ Abstracts arithmetic modifiers (average, sum, min, max)
3. ✅ Abstracts time periods (daily, weekly, monthly, etc.)
4. ✅ Auto-detects required objects
5. ✅ Generates Python KPI files
6. ✅ **Auto-creates or updates module definitions**
7. ✅ **Auto-creates value chain definitions (if needed)**
8. ✅ Creates summary reports

## 📋 Required Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `<file_path>` | Path to Excel/CSV | `"C:\Downloads\kpis.csv"` |
| `<MODULE_NAME>` | Module (UPPERCASE) | `SOURCING`, `SALES` |
| `<VALUE_CHAIN>` | Value chain | `SUPPLY_CHAIN`, `REVENUE` |

## 🔗 Value Chains & Modules

### SUPPLY_CHAIN
- SOURCING
- INVENTORY_MANAGEMENT
- LOGISTICS
- WAREHOUSE

### REVENUE
- SALES
- MARKETING
- PRICING

### CUSTOMER_EXPERIENCE
- CUSTOMER_SERVICE
- SUPPORT
- RETENTION

## 📤 Output

**Generated KPI Files**:
```
services/business_services/analytics_models/definitions/kpis/
├── purchase_order_value.py
├── backorder_rate.py
├── supplier_on_time_delivery_rate.py
└── ... (all your KPIs)
```

**Module Definition** (auto-created or updated):
```
services/business_services/analytics_models/definitions/modules/
└── <module_name>.py
```

**Value Chain Definition** (auto-created if needed):
```
services/business_services/analytics_models/definitions/value_chains/
└── <value_chain>.py
```

**Summary Report**:
```
scripts/objectModelSync/<MODULE>_KPI_PROCESSING_SUMMARY.md
```

## ⏭️ Next Steps

After processing KPIs:

```powershell
# Run governance suite
cd ..\objectModelSync
.\run_governance.bat

# Select Option 1 (Full Governance)
```

This will:
1. Sync object metadata
2. Update UML relationships
3. Run arithmetic governance
4. Analyze for KPI consolidation

## 💡 Tips

- Always use quotes around file paths with spaces
- Module names should be UPPERCASE
- Use underscores for multi-word modules: `CUSTOMER_SERVICE`
- Process one module at a time for better organization

## 🆘 Help

```powershell
# Show help
.\process_kpi_excel.bat

# Python help
python kpi_excel_processor.py --help
```

---

**Last Updated**: November 8, 2025
