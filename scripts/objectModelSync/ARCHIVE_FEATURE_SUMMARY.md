# Automatic Report Archiving Feature

**Date**: November 8, 2025  
**Enhancement**: Auto-archive all governance reports before new runs

---

## 🎯 Problem Solved

Previously, when running governance suite multiple times:
- Old `kpi_consolidation_recommendations.md` would be overwritten
- Old `kpi_consolidation_execution_report.json` would be overwritten
- Old `sync_report.md` and `sync_report.html` would be overwritten
- Old `validation_report.json` would be overwritten
- No history of previous runs
- Risk of losing important governance decisions and analysis

---

## ✨ Solution Implemented

The Governance Suite now **automatically archives** all old reports before creating new ones!

### How It Works

1. **Before Analysis Starts**: Checks for existing report files
2. **Creates Archive Directory**: `output/archive/` (if doesn't exist)
3. **Moves Old Files**: Renames with timestamp and moves to archive
4. **Proceeds with Analysis**: Creates fresh reports

### Archived Files

Files are renamed with timestamp format: `YYYYMMDD_HHMMSS`

**All Report Types**:
```
output/archive/
├── kpi_consolidation_recommendations_20251108_110324.md
├── kpi_consolidation_execution_report_20251108_110324.json
├── sync_report_20251108_110704.md
├── sync_report_20251108_110704.html
└── validation_report_20251108_110704.json
```

---

## 📁 Archive Location

```
scripts/objectModelSync/output/archive/
```

All archived reports are stored here with timestamps for easy reference.

---

## 🔧 Technical Implementation

### Modified Files
1. `kpi_consolidation_analyzer.py` - Consolidation reports
2. `generate_report.py` - Sync reports
3. `validate_integrity.py` - Validation reports

### Changes Made

#### 1. Added Imports (all files)
```python
import shutil
from datetime import datetime
```

#### 2. New Archiving Methods
```python
def archive_old_reports(self):
    """Archive existing consolidation reports before creating new ones."""
    # Create archive directory
    archive_dir = self.output_dir / "archive"
    archive_dir.mkdir(exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Archive files
    files_to_archive = [
        self.output_dir / "kpi_consolidation_recommendations.md",
        self.output_dir / "kpi_consolidation_execution_report.json"
    ]
    
    for file_path in files_to_archive:
        if file_path.exists():
            archive_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            archive_path = archive_dir / archive_name
            shutil.move(str(file_path), str(archive_path))
            print(f"📦 Archived: {file_path.name} → archive/{archive_name}")
```

#### 3. Updated `run()` Method
```python
def run(self):
    """Run the complete analysis."""
    # Archive old reports first
    print("=" * 80)
    print("ARCHIVING OLD REPORTS")
    print("=" * 80)
    self.archive_old_reports()
    
    # Run analysis
    self.analyze_all_kpis()
    report_file = self.generate_markdown_report()
    # ... rest of method
```

---

## 📊 Example Output

When running consolidation analysis:

```
================================================================================
ARCHIVING OLD REPORTS
================================================================================
📦 Archived: kpi_consolidation_recommendations.md → archive/kpi_consolidation_recommendations_20251108_110324.md
📦 Archived: kpi_consolidation_execution_report.json → archive/kpi_consolidation_execution_report_20251108_110324.json
✓ Archived 2 old report(s)

================================================================================
ANALYZING KPIs
================================================================================
...
```

---

## 🎯 Benefits

1. **Preserves History**: All previous analyses are saved
2. **No Data Loss**: Old reports never overwritten
3. **Easy Comparison**: Can compare multiple analysis runs
4. **Audit Trail**: Timestamp shows when each analysis was run
5. **Automatic**: No manual archiving needed

---

## 🔄 Workflow Impact

### Before Enhancement
```
1. Run analysis → Overwrites old reports
2. Review recommendations
3. Execute consolidation
4. (Old reports lost)
```

### After Enhancement
```
1. Run analysis → Archives old reports → Creates new reports
2. Review recommendations
3. Execute consolidation
4. (Old reports preserved in archive/)
```

---

## 📝 Usage

No changes needed! Archiving happens automatically:

```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync

# Run analysis - old reports automatically archived
.\run_governance.bat
# Select Option 4 (KPI Consolidation Analysis)
```

Or directly:
```powershell
python kpi_consolidation_analyzer.py
```

---

## 🗂️ Archive Management

### View Archived Reports
```powershell
cd output\archive
dir
```

### Clean Old Archives (Manual)
```powershell
# Keep only last 5 archives
Get-ChildItem output\archive\*.md | Sort-Object LastWriteTime -Descending | Select-Object -Skip 5 | Remove-Item
Get-ChildItem output\archive\*.json | Sort-Object LastWriteTime -Descending | Select-Object -Skip 5 | Remove-Item
```

### Restore Archived Report (Manual)
```powershell
# Copy archived file back to output directory
Copy-Item "output\archive\kpi_consolidation_recommendations_20251108_110324.md" "output\kpi_consolidation_recommendations.md"
```

---

## ✅ Testing Results

**Test Date**: November 8, 2025

**Test Case**: Archive all existing reports
- ✅ Created archive directory
- ✅ Moved consolidation recommendations.md with timestamp
- ✅ Moved consolidation execution_report.json with timestamp
- ✅ Moved sync_report.md with timestamp
- ✅ Moved sync_report.html with timestamp
- ✅ Moved validation_report.json with timestamp
- ✅ All files preserved in archive/
- ✅ Ready for new governance run

**Archived Files**:
```
kpi_consolidation_recommendations_20251108_110324.md (44,670 bytes)
kpi_consolidation_execution_report_20251108_110324.json (5,149 bytes)
sync_report_20251108_110704.md (269,503 bytes)
sync_report_20251108_110704.html (273,856 bytes)
validation_report_20251108_110704.json (20,659 bytes)
```

**Total Archived**: 5 files, ~608 KB

---

## 🔮 Future Enhancements

Potential improvements:
1. **Auto-cleanup**: Automatically delete archives older than X days
2. **Compression**: Compress old archives to save space
3. **Comparison Tool**: Script to compare two archived analyses
4. **Archive Viewer**: Web interface to browse archived reports

---

## 📖 Related Documentation

- **Main README**: `README.md`
- **Consolidation Guide**: See "KPI Consolidation System" section
- **Changelog**: `CHANGELOG.md`

---

**Status**: ✅ Feature implemented and tested  
**Ready for**: Production use with all governance suite runs
