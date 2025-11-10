# Analytics Engine Scripts

This directory contains automation scripts for the Analytics Engine.

---

## 📁 Directory Structure

```
scripts/
├── kpiExcelProcessor/          ← KPI Excel/CSV Processor
│   ├── process_kpi_excel.bat   ← Process KPI files
│   ├── kpi_excel_processor.py  ← Python processor
│   └── README.md               ← Documentation
│
├── objectModelSync/            ← Object Model Governance Suite
│   ├── run_governance.bat      ← Main governance launcher
│   ├── run_full_sync.py        ← Full sync orchestrator
│   └── README.md               ← Documentation
│
├── QUICK_REFERENCE.md          ← Quick command reference
└── README.md                   ← This file
```

---

## 🚀 Quick Start

### 1. Process KPI Excel/CSV Files

Generate KPI Python files from Excel or CSV templates:

```powershell
cd kpiExcelProcessor
.\process_kpi_excel.bat "<file_path>" <MODULE_NAME> <VALUE_CHAIN>
```

**Example**:
```powershell
cd kpiExcelProcessor
.\process_kpi_excel.bat "C:\Downloads\Supply_Chain\kpis.csv" SOURCING SUPPLY_CHAIN
```

📖 **Documentation**: [kpiExcelProcessor/README.md](./kpiExcelProcessor/README.md)

---

### 2. Run Object Model Governance

Sync object models, update UML relationships, and analyze KPIs:

```powershell
cd objectModelSync
.\run_governance.bat
```

**Interactive Menu**:
1. Run ALL processes (Full Governance)
2. Main Sync only
3. Arithmetic Governance only
4. KPI Consolidation Analysis only
5. KPI Consolidation Execution only

📖 **Documentation**: [objectModelSync/README.md](./objectModelSync/README.md)

---

## 🔄 Typical Workflow

```powershell
# Step 1: Process KPI file
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
.\process_kpi_excel.bat "C:\Downloads\Supply_Chain\kpis.csv" SOURCING SUPPLY_CHAIN

# Step 2: Run governance suite
cd ..\objectModelSync
.\run_governance.bat
# Select Option 1 (Full Governance)

# Step 3: Review recommendations
notepad output\kpi_consolidation_recommendations.md

# Step 4: Execute consolidation if needed
.\run_governance.bat
# Select Option 5 (KPI Consolidation Execution)
```

---

## 📋 Available Tools

### KPI Excel Processor
**Purpose**: Bulk generate KPI Python files from Excel/CSV templates

**Features**:
- ✅ Abstracts arithmetic modifiers (average, sum, min, max)
- ✅ Abstracts time periods (daily, weekly, monthly)
- ✅ Auto-detects required objects
- ✅ Generates properly formatted Python files

**Location**: `kpiExcelProcessor/`

---

### Object Model Governance Suite
**Purpose**: Maintain consistency across object models and KPIs

**Features**:
- ✅ Sync object metadata
- ✅ Update UML relationships
- ✅ Arithmetic governance (abstract modifiers)
- ✅ KPI consolidation analysis
- ✅ Automated backups

**Location**: `objectModelSync/`

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Quick command reference card |
| [kpiExcelProcessor/README.md](./kpiExcelProcessor/README.md) | KPI processor documentation |
| [kpiExcelProcessor/KPI_EXCEL_PROCESSOR_GUIDE.md](./kpiExcelProcessor/KPI_EXCEL_PROCESSOR_GUIDE.md) | Comprehensive KPI processor guide |
| [objectModelSync/README.md](./objectModelSync/README.md) | Governance suite documentation |

---

## 🎯 Value Chains & Modules

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

### OPERATIONS
- PRODUCTION
- QUALITY
- MAINTENANCE

### FINANCE
- ACCOUNTING
- BUDGETING
- FINANCIAL_PLANNING

---

## 💡 Tips

1. **Always process KPIs before running governance** - The governance suite needs KPI files to analyze
2. **Use quotes for file paths with spaces** - `"C:\My Files\kpis.csv"`
3. **Module names are UPPERCASE** - `SOURCING`, `CUSTOMER_SERVICE`
4. **Review consolidation recommendations** - Before executing consolidation
5. **Backups are automatic** - Governance suite creates backups before changes

---

## 🆘 Help

```powershell
# KPI Processor help
cd kpiExcelProcessor
.\process_kpi_excel.bat
# or
python kpi_excel_processor.py --help

# Governance Suite help
cd objectModelSync
.\run_governance.bat
# Interactive menu with options
```

---

**Last Updated**: November 8, 2025  
**Version**: 1.0
