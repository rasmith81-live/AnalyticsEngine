# KPI Excel Processor - Quick Reference Card

## 🚀 Quick Command

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
.\process_kpi_excel.bat "<file_path>" <MODULE> <VALUE_CHAIN>
```

---

## 📋 Command Template

```powershell
.\process_kpi_excel.bat "C:\path\to\file.csv" MODULE_NAME VALUE_CHAIN
```

---

## 🎯 Common Commands

### Supply Chain Modules

```powershell
# First, navigate to the processor directory
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor

# Sourcing/Buying
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-buying.csv" SOURCING SUPPLY_CHAIN

# Inventory Management
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\inventory.csv" INVENTORY_MANAGEMENT SUPPLY_CHAIN

# Logistics
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\logistics.csv" LOGISTICS SUPPLY_CHAIN

# Warehouse
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\warehouse.csv" WAREHOUSE SUPPLY_CHAIN
```

### Revenue Modules

```powershell
# Sales
.\process_kpi_excel.bat "C:\Downloads\Sales_Management\sales.csv" SALES REVENUE

# Marketing
.\process_kpi_excel.bat "C:\Downloads\marketing.csv" MARKETING REVENUE

# Pricing
.\process_kpi_excel.bat "C:\Downloads\pricing.csv" PRICING REVENUE
```

### Customer Experience Modules

```powershell
# Customer Service
.\process_kpi_excel.bat "C:\Downloads\customer-service.csv" CUSTOMER_SERVICE CUSTOMER_EXPERIENCE

# Support
.\process_kpi_excel.bat "C:\Downloads\support.csv" SUPPORT CUSTOMER_EXPERIENCE

# Retention
.\process_kpi_excel.bat "C:\Downloads\retention.csv" RETENTION CUSTOMER_EXPERIENCE
```

---

## 🔗 Value Chain Mapping

| Value Chain | Modules |
|-------------|---------|
| **SUPPLY_CHAIN** | SOURCING, INVENTORY_MANAGEMENT, LOGISTICS, WAREHOUSE |
| **REVENUE** | SALES, MARKETING, PRICING |
| **CUSTOMER_EXPERIENCE** | CUSTOMER_SERVICE, SUPPORT, RETENTION |
| **OPERATIONS** | PRODUCTION, QUALITY, MAINTENANCE |
| **FINANCE** | ACCOUNTING, BUDGETING, FINANCIAL_PLANNING |

---

## 📁 File Locations

### Input
- Your Excel/CSV files: `C:\Users\Arthu\Downloads\`

### Output
- Generated KPI files: `services\business_services\analytics_models\definitions\kpis\`
- Summary reports: `scripts\objectModelSync\<MODULE>_KPI_PROCESSING_SUMMARY.md`

---

## ⚡ Full Workflow

```powershell
# Step 1: Process KPI Excel file
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
.\process_kpi_excel.bat "C:\Users\Arthu\Downloads\Supply_Chain\kpis.csv" SOURCING SUPPLY_CHAIN

# Step 2: Run governance suite
cd ..\objectModelSync
.\run_governance.bat
# Select Option 1 (Full Governance)

# Step 3: Review consolidation recommendations
# Check: output\kpi_consolidation_recommendations.md

# Step 4: Execute consolidation if needed
.\run_governance.bat
# Select Option 5 (KPI Consolidation Execution)
```

---

## 🛠️ Troubleshooting

### File not found
```powershell
# ✗ Wrong - missing quotes
.\process_kpi_excel.bat C:\My Files\kpis.csv SOURCING SUPPLY_CHAIN

# ✓ Correct - with quotes
.\process_kpi_excel.bat "C:\My Files\kpis.csv" SOURCING SUPPLY_CHAIN
```

### Check Python
```powershell
python --version  # Should be 3.7+
```

### Find your CSV file
```powershell
# Search for file
Get-ChildItem -Path C:\Users\Arthu\Downloads -Recurse -Filter "*.csv"
```

---

## 📊 Expected CSV Format

Your CSV should have these columns:
- `KPI` (required)
- `Definition` (required)
- `Standard Formula` (required)

Example:
```csv
KPI,Definition,Standard Formula
Purchase Order Value,Average value of orders,Total Spend / Number of Orders
Backorder Rate,Percentage on backorder,(Backordered / Total) * 100
```

---

## ✅ What Gets Created

For each KPI in your Excel/CSV:
1. ✅ Python file with proper class structure
2. ✅ Arithmetic modifiers abstracted (average, sum, min, max)
3. ✅ Time periods abstracted (daily, weekly, monthly, etc.)
4. ✅ Required objects auto-detected
5. ✅ Module and value chain assigned

---

## 🎯 Next Steps After Processing

1. **Review Generated Files**
   ```powershell
   cd services\business_services\analytics_models\definitions\kpis
   dir *.py | more
   ```

2. **Run Governance Suite**
   ```powershell
   cd scripts\objectModelSync
   .\run_governance.bat
   ```

3. **Check Summary Report**
   ```powershell
   notepad scripts\objectModelSync\SOURCING_KPI_PROCESSING_SUMMARY.md
   ```

---

## 📞 Help

```powershell
# Show help
.\process_kpi_excel.bat

# Python help
python kpi_excel_processor.py --help
```

---

**Last Updated**: November 8, 2025
