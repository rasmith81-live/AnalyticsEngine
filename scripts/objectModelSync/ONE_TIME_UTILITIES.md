# One-Time Utility Scripts

These scripts were created for specific one-time fixes and are **not part of the regular governance workflow**.

---

## Formula Restoration Scripts (November 10, 2025)

### Purpose
These scripts were created to restore formulas that were lost during the KPI migration from class-based to dictionary-based format.

### Scripts
- `restore_formulas.py` - Restore from recent backup
- `restore_formulas_from_old_backup.py` - Restore from November 8 backup

### Status
✅ **COMPLETED** - Formulas have been restored for all applicable KPIs (43 formulas restored)

### Why Not in Regular Workflow?
- This was a **one-time data correction** issue
- The validation script now **preserves existing formulas** (fixed logic)
- Future validations will not overwrite formulas
- No need to run these scripts again

### If You Need Them
The scripts are still available in this directory for reference or emergency use, but they should not be needed for regular operations.

---

## Notes

If you create other one-time utility scripts in the future, document them here with:
- Purpose
- Date created
- Status (completed/archived)
- Why it's not part of regular workflow
