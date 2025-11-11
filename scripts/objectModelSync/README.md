# Object Model Synchronization Suite - Complete Documentation

**Location**: `C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync`  
**Created**: November 8, 2025  
**Version**: 1.3  
**Purpose**: Permanent cleanup and synchronization system for analytics object models

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Overview](#overview)
3. [Core Scripts](#core-scripts)
4. [Configuration](#configuration)
5. [Main Sync System](#main-sync-system)
6. [Arithmetic Governance](#arithmetic-governance)
7. [KPI Consolidation](#kpi-consolidation)
8. [Usage Examples](#usage-examples)
9. [Troubleshooting](#troubleshooting)
10. [Maintenance](#maintenance)

---

## Quick Start

### Option 1: Master Governance Script (Recommended)
```bash
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync
run_governance.bat
```

This interactive menu lets you:
- Run ALL processes in sequence (full governance)
- Run any individual process (main sync, arithmetic governance, or consolidation)
- Choose between analysis and execution for consolidation

### Option 2: Individual Scripts

**1. Verify Installation**
```bash
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync
dir
```

You should see all core scripts, configuration, and documentation files.

**2. Test Run (Dry Run)**
```bash
# Edit config.json and set "dry_run": true
python run_full_sync.py
```

This will show what would be changed without actually modifying files.

**3. First Real Sync**
```bash
# Edit config.json and set "dry_run": false
python run_full_sync.py
```

Or use individual batch files:
- `quick_sync.bat` - Main sync
- `run_arithmetic_governance.bat` - Arithmetic governance
- `run_consolidation_analysis.bat` - Consolidation analysis
- `run_consolidation_executor.bat` - Consolidation execution

---

## Overview

This suite ensures the analytics system maintains complete integrity through three main systems:

### 1. Main Synchronization System
- ✅ Analyzes all 464 KPIs to find object dependencies
- ✅ Synchronizes KPI `required_objects` metadata (100% coverage)
- ✅ Updates object model metadata (modules, KPIs, attributes, relationships)
- ✅ Creates UML relationship lines with proper cardinality
- ✅ Fixes formatting issues (comma placement, syntax)
- ✅ Validates system integrity (missing references, orphans)
- ✅ Generates comprehensive reports (HTML + Markdown)
- ✅ Creates automatic backups before changes

### 2. Arithmetic Governance System
- ✅ Identifies arithmetic modifiers in KPI names (average, max, min, etc.)
- ✅ Removes modifiers from names, codes, and definitions
- ✅ Adds `aggregation_methods` and `time_periods` metadata
- ✅ Reduces KPI proliferation by 80% for affected metrics
- ✅ Excludes comparative modifiers (rate, ratio, percentage)

### 3. KPI Consolidation System
- ✅ Identifies overlapping/duplicate KPIs (70%+ similarity)
- ✅ Generates recommendations with user approval checkboxes
- ✅ Merges metadata from consolidated KPIs
- ✅ Adds `replaces` field for audit trail
- ✅ Deletes secondary KPI files safely

---

## Core Scripts

### Main Synchronization (8 scripts)

#### 1. `run_full_sync.py` (Main Orchestrator)
- Coordinates entire sync process
- Creates backups before changes
- Runs all steps in sequence
- Generates comprehensive reports
- **Usage**: `python run_full_sync.py` or `quick_sync.bat`
- **Frequency**: Weekly or after major changes

#### 2. `analyze_objects.py` (Object Analysis)
- Analyzes all 464 KPIs
- Finds object references through text matching
- Generates name variations for matching
- **Output**: `analysis_results.json`

#### 3. `sync_kpi_required_objects.py` (KPI Sync)
- Updates all KPI `required_objects` lists
- Merges existing and new objects
- Ensures 100% coverage

#### 4. `sync_object_metadata.py` (Object Metadata Sync)
- Updates object model metadata
- Adds modules, related_kpis, key_attributes, related_objects
- Infers attributes based on object type

#### 5. `sync_uml_relationships.py` (UML Sync)
- Adds UML relationship lines
- Creates proper cardinality (1-to-many, many-to-many)
- Uses standard UML notation

#### 6. `fix_formatting.py` (Formatting Fixes)
- Fixes comma placement issues
- Ensures consistent Python syntax
- Safe and non-destructive

#### 7. `validate_integrity.py` (Validation)
- Checks for missing references
- Identifies orphaned objects
- Detects inconsistencies
- **Output**: `validation_report.json`

#### 8. `generate_report.py` (Reporting)
- Creates Markdown reports
- Generates HTML reports with styling
- Includes statistics and charts

### Arithmetic Governance (1 script)

#### 9. `arithmetic_governance.py`
- Scans all 464 KPIs for arithmetic modifiers
- Detects: average, avg, mean, median, max, maximum, min, minimum, sum, total, count
- Excludes: rate, ratio, percentage (comparative calculations)
- Removes modifiers from names, codes, definitions
- Adds `aggregation_methods` and `time_periods` metadata
- **Usage**: `python arithmetic_governance.py` or `run_arithmetic_governance.bat`
- **Frequency**: Initial setup, after imports, monthly maintenance

### KPI Consolidation (2 scripts)

#### 10. `kpi_consolidation_analyzer.py`
- Analyzes all KPIs for similarity (name 40%, description 30%, definition 30%)
- Calculates weighted similarity scores
- Detects 5 consolidation patterns (rate/ratio variants, shared modules, etc.)
- Generates recommendations markdown with checkboxes
- **Output**: `kpi_consolidation_recommendations.md`
- **Usage**: `python kpi_consolidation_analyzer.py` or `run_consolidation_analysis.bat`
- **Frequency**: Initial cleanup, quarterly maintenance

#### 11. `kpi_consolidation_executor.py`
- Reads approved recommendations (checked boxes)
- Creates automatic backups
- Merges metadata (modules, aggregation_methods, time_periods)
- Adds `replaces` field to primary KPI
- Deletes secondary KPI files
- **Output**: `kpi_consolidation_execution_report.json`
- **Usage**: `python kpi_consolidation_executor.py` or `run_consolidation_executor.bat`
- **Frequency**: After reviewing and approving recommendations

---

## Configuration

### Edit `config.json`

```json
{
  "paths": {
    "definitions_dir": "../../services/business_services/analytics_models/definitions",
    "kpis_dir": "../../services/business_services/analytics_models/definitions/kpis",
    "objects_dir": "../../services/business_services/analytics_models/definitions/object_models",
    "output_dir": "./output",
    "backup_dir": "./backups",
    "logs_dir": "./logs"
  },
  "sync_options": {
    "create_backups": true,      // Always create backups before changes
    "dry_run": false,            // Set to true to preview changes
    "batch_size": 50,            // Process files in batches
    "max_related_kpis": 30,      // Max KPIs to list per object
    "max_related_objects": 20,   // Max related objects to list
    "max_key_attributes": 20     // Max attributes to list
  },
  "validation": {
    "check_missing_references": true,
    "check_orphaned_objects": true,
    "check_circular_dependencies": true,
    "check_formatting": true,
    "fail_on_errors": false      // Continue even if errors found
  },
  "logging": {
    "level": "INFO",             // DEBUG, INFO, WARNING, ERROR
    "console_output": true,
    "file_output": true,
    "max_log_files": 10
  },
  "reporting": {
    "generate_html": true,
    "generate_markdown": true,
    "include_charts": false,
    "email_report": false
  }
}
```

### Key Configuration Options

- **`dry_run`**: Set to `true` to preview changes without modifying files
- **`create_backups`**: Always keep `true` for safety
- **`fail_on_errors`**: Set to `false` to continue processing even if some files fail
- **`max_related_kpis`**: Limit number of KPIs listed in object metadata (prevents huge lists)

---

## Main Sync System

### What It Does

The main synchronization system ensures complete bidirectional metadata:

1. **KPIs → Objects**: Every KPI knows which objects it needs (100% coverage)
2. **Objects → KPIs**: Every object knows which KPIs use it (95% coverage)
3. **Objects → Objects**: Every object knows its related objects (95% coverage)
4. **UML Documentation**: Complete visual representation of all relationships

### How It Works

**Step 1: Analysis**
```bash
python analyze_objects.py
```
- Loads all 464 KPIs
- Searches names, descriptions, formulas, definitions
- Generates object name variations (singular/plural, abbreviations)
- Finds 93 unique object references
- Outputs `analysis_results.json`

**Step 2: Sync KPI Required Objects**
```bash
python sync_kpi_required_objects.py
```
- Updates all KPI `required_objects` lists
- Merges existing and new objects
- Ensures 100% coverage

**Step 3: Sync Object Metadata**
```bash
python sync_object_metadata.py
```
- Updates 82 object models with complete metadata
- Adds modules, related_kpis, key_attributes, related_objects

**Step 4: Sync UML Relationships**
```bash
python sync_uml_relationships.py
```
- Adds UML relationship lines with proper cardinality
- Creates association, aggregation, and composition relationships

**Step 5: Fix Formatting**
```bash
python fix_formatting.py
```
- Fixes comma placement issues
- Ensures consistent Python syntax

**Step 6: Validate Integrity**
```bash
python validate_integrity.py
```
- Checks for missing references
- Identifies orphaned objects
- Generates validation report

**Step 7: Generate Reports**
```bash
python generate_report.py
```
- Creates HTML and Markdown reports
- Includes statistics and charts

### Expected Results

- **KPIs Analyzed**: 464
- **KPIs with required_objects**: 464 (100%)
- **Object Models Updated**: 82 (95%)
- **Analysis Time**: ~5 seconds
- **Total Sync Time**: ~45 seconds

---

## Arithmetic Governance

### Purpose

Enforce the design pattern that arithmetic modifiers should be abstracted into metadata rather than embedded in KPI names.

### Problem: KPI Proliferation
```
❌ AVERAGE_DEAL_SIZE
❌ MEDIAN_DEAL_SIZE  
❌ MAX_DEAL_SIZE
❌ MIN_DEAL_SIZE
❌ TOTAL_DEAL_SIZE
```
Result: 5 separate KPIs for the same metric

### Solution: Metadata Abstraction
```
✅ DEAL_SIZE (with metadata)
   - aggregation_methods: [average, median, max, min, sum, count]
   - time_periods: [daily, weekly, monthly, quarterly, annually]
```
Result: 1 flexible KPI supporting all aggregations

### Detected Modifiers

**Abstracted (11 types)**:
- `average`, `avg`, `mean`, `median`
- `max`, `maximum`, `min`, `minimum`
- `sum`, `total`, `count`

**Excluded (kept in names)**:
- `rate`, `ratio`, `percentage`, `percent`
- **Rationale**: These represent comparative calculations (comparing two components), not simple aggregation methods

### How It Works

1. **Analysis**: Scans KPI names for modifiers
2. **Name Transformation**: Removes modifier from name
3. **Code Transformation**: Removes modifier from code
4. **Definition Update**: Updates description to be more generic
5. **Metadata Addition**: Adds aggregation_methods and time_periods

### Usage

**Dry Run (Preview)**:
```bash
# Edit config.json: "dry_run": true
python arithmetic_governance.py
```

**Live Update**:
```bash
# Edit config.json: "dry_run": false
python arithmetic_governance.py
```

Or use the batch file:
```bash
run_arithmetic_governance.bat
```

### Expected Results

- **KPIs Analyzed**: 464
- **With Modifiers**: 20-30 (4-6%)
- **Updated**: 20-30
- **KPI Reduction**: 80% fewer KPIs for metrics with modifiers
- **Time**: ~5 seconds

---

## KPI Consolidation

### Purpose

Identify and consolidate overlapping/duplicate KPIs to reduce duplication and maintain a clean KPI library.

### Workflow

**Step 1: Analyze KPIs**
```bash
python kpi_consolidation_analyzer.py
```
- Scans all 464 KPIs
- Compares names, descriptions, and definitions
- Calculates similarity scores (0-100%)
- Identifies consolidation patterns
- Generates recommendations file with checkboxes

**Step 2: Review Recommendations**

Open `output/kpi_consolidation_recommendations.md` and review:

```markdown
## Recommendation #1

**Similarity**: 92.5%
**Patterns**: rate_ratio_variant, shared_modules

### Primary KPI (Keep)
- **Name**: Sales Conversion Rate
- **Code**: `SALES_CONVERSION_RATE`

### Secondary KPI (Consolidate)
- **Name**: Sales Conversion Ratio
- **Code**: `SALES_CONVERSION_RATIO`

### Action
- [ ] **Approve consolidation**
```

**To approve**: Change `[ ]` to `[x]`

**Step 3: Execute Consolidations**
```bash
python kpi_consolidation_executor.py
```
- Reads approved recommendations (checked boxes)
- Creates backup before changes
- Merges metadata (modules, aggregation_methods, time_periods)
- Adds `replaces` field to primary KPI
- Deletes secondary KPI file

### Detection Patterns

1. **Rate/Ratio Variants**: Same base name, different terminology
2. **Percentage Variants**: Spelling variations
3. **Shared Modules**: >50% module overlap
4. **Same Category**: Same business category
5. **Similar Formulas**: >70% formula similarity

### Similarity Scoring

**Weighted Formula**:
```
Overall = (Name × 0.4) + (Description × 0.3) + (Definition × 0.3)
```

**Confidence Levels**:
- **High** (>90%): Very likely duplicates - safe to consolidate
- **Medium** (70-90%): Review carefully before approving
- **Low** (<70%): Not recommended - too different

### Expected Results

- **Recommendations**: 10-30 opportunities (2-6%)
- **High Confidence**: 5-10 (>90% similarity)
- **Medium Confidence**: 5-20 (70-90% similarity)
- **Analysis Time**: ~10 seconds
- **Execution Time**: ~5 seconds

---

## Usage Examples

### Master Governance Script (Recommended)
```bash
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync
run_governance.bat
```

**Interactive Menu Options**:
1. Run ALL processes in sequence (Full Governance)
2. Main Sync only
3. Arithmetic Governance only
4. KPI Consolidation Analysis only
5. KPI Consolidation Execution only
0. Exit

**Note**: Consolidation execution (option 5) requires manual review and approval of the analysis results (option 4) before running.

### Full Sync (Individual)
```bash
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync
python run_full_sync.py
```

Or use the batch file:
```bash
quick_sync.bat
```

### Dry Run (Preview Changes)
```bash
# Edit config.json: "dry_run": true
python run_full_sync.py
```

### Individual Operations
```bash
# Run analysis only
python analyze_objects.py

# Sync KPIs only
python sync_kpi_required_objects.py

# Sync object models only
python sync_object_metadata.py

# Validate integrity
python validate_integrity.py

# Arithmetic governance
python arithmetic_governance.py
# Or: run_arithmetic_governance.bat

# KPI consolidation analysis
python kpi_consolidation_analyzer.py
# Or: run_consolidation_analysis.bat

# KPI consolidation execution
python kpi_consolidation_executor.py
# Or: run_consolidation_executor.bat
```

### Scheduled Execution
```cmd
# Windows Task Scheduler (weekly, Sunday 2 AM)
schtasks /create /tn "ObjectModelSync" /tr "python C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync\run_full_sync.py" /sc weekly /d SUN /st 02:00
```

---

## Troubleshooting

### Script Fails
1. Check `logs/sync_*.log` for errors
2. Verify Python version (3.8+)
3. Ensure definitions directory is accessible
4. Check file permissions

### Incomplete Sync
1. Run `python validate_integrity.py`
2. Review validation report
3. Run individual scripts as needed
4. Check for file locks or permissions

### Performance Issues
1. Run scripts during off-hours
2. Increase system resources
3. Process in batches (configure in config.json)
4. Check for large files or corrupted data

### Changes Not Applied
- Verify `dry_run` is set to `false` in config.json
- Check that backup was created (indicates write permissions work)
- Review logs for specific errors

### Arithmetic Governance False Positives
- Review the report
- Manually revert specific KPIs if modifier is part of domain term
- Add to exclusion list (future enhancement)

### Consolidation Wrong KPI Deleted
- Restore from automatic backup
- Review recommendations more carefully next time
- Use dry run mode first

---

## Rollback

If sync causes issues:

```bash
# List backups
dir backups

# Restore from backup
xcopy /E /I /Y backups\definitions_backup_YYYYMMDD_HHMMSS\* ..\..\services\business_services\analytics_models\definitions\
```

**When to Rollback**:
- Unexpected errors during sync
- Validation failures after sync
- Data corruption detected
- Need to revert to known good state

---

## Maintenance

### Weekly (Automated)
- Run full sync: `python run_full_sync.py`
- Review HTML report
- Check for errors/warnings
- Verify statistics

### Monthly (Manual)
- Review validation report details
- Clean old backups (keep 3 months)
- Update configuration if needed
- Check log file sizes
- Run arithmetic governance
- Run consolidation analysis

### Quarterly (Manual)
- Run KPI consolidation analysis
- Review and approve consolidations
- Execute approved consolidations
- Validate results

### After Major Changes (Immediate)
- Run full sync
- Validate results carefully
- Keep backup longer
- Document changes

---

## Output Files

### Main Sync
- `output/analysis_results.json` - Object analysis data
- `output/validation_report.json` - Validation results
- `output/sync_report.md` - Markdown report
- `output/sync_report.html` - HTML report (if enabled)

### Arithmetic Governance
- `output/arithmetic_governance_report.json` - Detailed results
- `output/arithmetic_governance_report.md` - Markdown report

### KPI Consolidation
- `output/kpi_consolidation_recommendations.md` - Review file with checkboxes
- `output/kpi_consolidation_recommendations.json` - Data for executor
- `output/kpi_consolidation_execution_report.json` - Execution results

### Backups & Logs
- `backups/definitions_backup_YYYYMMDD_HHMMSS/` - Timestamped backups
- `backups/consolidation_backup_YYYYMMDD_HHMMSS/` - Consolidation backups
- `logs/sync_YYYYMMDD_HHMMSS.log` - Execution logs

---

## Safety Features

1. **Automatic Backups**: Timestamped before every sync
2. **Dry Run Mode**: Preview changes without applying
3. **Validation**: Checks integrity before and after
4. **Rollback**: Easy restore from backups
5. **Logging**: Complete audit trail
6. **User Approval**: Consolidations require manual checkbox approval
7. **Error Handling**: Continue on errors or fail fast (configurable)

---

## Key Metrics

### KPI Metrics
- Total KPIs: 464
- KPIs with required_objects: 464 (100%)
- Average objects per KPI: ~25
- Range: 3 to 45 objects per KPI

### Object Model Metrics
- Total object models: 86
- Updated with metadata: 82 (95%)
- With UML relationships: 82 (95%)
- Not referenced: 2 (Field Visit, Stakeholder)

### Performance
- Analysis time: ~5 seconds
- KPI sync time: ~10 seconds
- Object sync time: ~8 seconds
- UML sync time: ~7 seconds
- Total sync time: ~45 seconds
- Arithmetic governance: ~5 seconds
- Consolidation analysis: ~10 seconds
- Consolidation execution: ~5 seconds

---

## Additional Documentation

- **`CHANGELOG.md`** - Version history and changes
- **`config.json`** - Configuration file with all options

---

## Version History

- **v1.3** (Nov 8, 2025) - Documentation consolidation
  - Merged guides into comprehensive README
  - Improved structure and navigation
  
- **v1.2** (Nov 8, 2025) - KPI consolidation system
  - Added analyzer and executor scripts
  - User approval workflow with checkboxes
  
- **v1.1** (Nov 8, 2025) - Arithmetic governance
  - Added modifier abstraction
  - Excluded comparative modifiers (rate, ratio, percentage)
  
- **v1.0** (Nov 8, 2025) - Initial release
  - Complete synchronization suite
  - Validation and reporting
  - Backup and rollback support

---

**Status**: ✅ Production Ready  
**Maintained By**: Analytics Engine Team  
**Last Updated**: November 8, 2025

---

## Quick Reference

| Task | Command |
|------|---------|
| **Master governance menu** | `run_governance.bat` ⭐ **RECOMMENDED** |
| Run all processes | `run_governance.bat` → Option 1 |
| Full sync | `python run_full_sync.py` or `quick_sync.bat` or menu option 2 |
| Arithmetic governance | `python arithmetic_governance.py` or `run_arithmetic_governance.bat` or menu option 3 |
| Consolidation analysis | `python kpi_consolidation_analyzer.py` or `run_consolidation_analysis.bat` or menu option 4 |
| Consolidation execution | `python kpi_consolidation_executor.py` or `run_consolidation_executor.bat` or menu option 5 |
| Dry run | Edit config.json: `"dry_run": true`, then run sync |
| Validate | `python validate_integrity.py` |
| Rollback | `xcopy /E /I /Y backups\[backup_folder]\* ..\..\...\definitions\` |
| View logs | `type logs\sync_*.log` |
| Schedule weekly | `schtasks /create /tn "ObjectModelSync" /tr "python [path]\run_full_sync.py" /sc weekly /d SUN /st 02:00` |
| **Generate SQLAlchemy models** | `.\run_generate_models.ps1` |
| **KPI validation** | `python validate_and_enhance_kpis.py` or menu option 6 |
| **Regenerate sample data** | `python regenerate_sample_data.py` or menu option 7 |

---

## SQLAlchemy Model Generation

### Purpose
Generate SQLAlchemy model classes in `base_models.py` from object model dictionary definitions.

### Usage
```powershell
.\run_generate_models.ps1
```

### What It Does
- ✅ Reads object model definitions from metadata service
- ✅ Generates SQLAlchemy model classes
- ✅ Creates proper type mappings and indexes
- ✅ Backs up existing base_models.py

### What It Does NOT Do
- ❌ Create TimescaleDB hypertables (handled by `scripts/utils/`)
- ❌ Apply database migrations (use Alembic)
- ❌ Modify existing database tables

### Workflow
1. Define object model → `definitions/object_models/my_model.py`
2. Generate SQLAlchemy → `.\run_generate_models.ps1`
3. Create migration → `alembic revision --autogenerate`
4. Apply migration → `alembic upgrade head`
5. TimescaleDB setup → Use `scripts/utils/run_migration_reset.ps1`

### Important Notes
- **TimescaleDB hypertables** are created separately using `scripts/utils/` utilities
- **Do NOT** manually add `create_hypertable` calls to Alembic migrations
- See `OBJECT_MODEL_TO_SQLALCHEMY_SYNC.md` for complete documentation

---

## KPI Validation and Enhancement (NEW)

### Purpose
Ensure all KPIs have complete, standardized definitions with formula-aware sample data for robust visualizations.

### Usage via Governance Menu
```powershell
.\run_governance.bat
# Select option 6 for KPI Validation
# Select option 7 for Sample Data Regeneration
```

### Direct Usage
```powershell
# Validate and enhance all KPIs
python validate_and_enhance_kpis.py

# Regenerate sample data only
python regenerate_sample_data.py
```

### What It Does
- ✅ Validates all 21 required KPI fields
- ✅ Adds missing fields with sensible defaults
- ✅ Generates formula-aware sample data
- ✅ Creates smart category names based on context
- ✅ Analyzes formulas for realistic value ranges
- ✅ Creates automatic backups
- ✅ Produces detailed validation reports

### Required KPI Fields (21 Total)
**Core**: code, name, description, formula, calculation_formula, category, is_active  
**Details**: full_kpi_definition, trend_analysis, diagnostic_questions, actionable_tips, visualization_suggestions, risk_warnings, tracking_tools, integration_points, change_impact_analysis  
**Metadata**: metadata_, required_objects, modules, module_code  
**Visualization**: sample_data (time_series, current, statistics, breakdown)

### Formula-Aware Sample Data
The system analyzes KPI formulas to generate realistic data:
- **Percentage KPIs** (with division): 50-75% range
- **Count KPIs**: Integer values
- **Currency KPIs**: Appropriate decimal values
- **Smart Categories**: Based on formula context (accounts, customers, products, sales, regions)

### Example
**Formula**: `(Number of Accounts Managed / Total Target Accounts) * 100`  
**Generated Categories**: Enterprise Accounts, Mid-Market, Small Business, Strategic Partners, Other  
**Value Range**: 50-75% (realistic for account coverage)

### Workflow
1. **After KPI Creation/Import** → Run validation
2. **Before Frontend Testing** → Ensure sample data exists
3. **After Formula Changes** → Regenerate sample data
4. **Monthly Maintenance** → Validate all KPIs

### Documentation
- See `KPI_VALIDATION_AND_ENHANCEMENT.md` for complete documentation
- See `KPI_ENHANCEMENT_EXAMPLE.md` for before/after examples
