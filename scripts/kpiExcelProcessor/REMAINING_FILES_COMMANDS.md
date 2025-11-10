# Quick Commands for Remaining Supply Chain Files

**Location**: `C:\Users\Arthu\Downloads\Supply_Chain\`

---

## 📋 Copy-Paste Commands

Navigate to processor directory first:
```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor
```

---

### Inventory Management
```powershell
python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-inventory-management.csv" --module INVENTORY_MANAGEMENT --chain SUPPLY_CHAIN
```

---

### Logistics & Transportation
```powershell
python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-logistics-transportation.csv" --module LOGISTICS --chain SUPPLY_CHAIN
```

---

### Packing
```powershell
python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-packing.csv" --module PACKING --chain SUPPLY_CHAIN
```

---

## 🔄 Run All at Once

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\kpiExcelProcessor

python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-inventory-management.csv" --module INVENTORY_MANAGEMENT --chain SUPPLY_CHAIN

python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-logistics-transportation.csv" --module LOGISTICS --chain SUPPLY_CHAIN

python kpi_excel_processor.py --file "C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-packing.csv" --module PACKING --chain SUPPLY_CHAIN
```

---

## ⏭️ After Processing All Files

Run governance suite:
```powershell
cd ..\objectModelSync
.\run_governance.bat
```

Select **Option 1** (Full Governance)

---

## 📊 Current Progress

| Module | Status |
|--------|--------|
| SOURCING | ✅ 45 KPIs |
| ISO_20400 | ✅ 22 KPIs |
| ISO_22004 | ✅ 38 KPIs |
| ISO_28000 | ✅ 38 KPIs |
| INVENTORY_MANAGEMENT | ⏳ Ready |
| LOGISTICS | ⏳ Ready |
| PACKING | ⏳ Ready |

**Total So Far**: 143 KPIs
