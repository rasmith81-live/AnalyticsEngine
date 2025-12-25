# Migration Utilities Usage Guide

## Overview

This guide covers the migration and schema utilities in `scripts/utils/` for database schema management, CQRS pattern automation, and Alembic migration helpers.

**Target Users**: Backend developers, DevOps engineers, database administrators

---

## Quick Reference

| Utility | Purpose | Usage |
|---------|---------|-------|
| `extract_table_schemas.py` | Extract schemas from object models | `python extract_table_schemas.py --scor` |
| `add_cqrs_schema.ps1` | Add CQRS schema objects | `.\add_cqrs_schema.ps1 -ServiceName <name> -TableName <table> -Domain <domain> -SchemaDefinition <json>` |
| `validate_cqrs_models.ps1` | Validate CQRS consistency | `.\validate_cqrs_models.ps1` |
| `create_revision_clean.ps1` | Create Alembic migration | `.\create_revision_clean.ps1 -ServiceName <name> -Message "<message>"` |
| `upgrade_service.ps1` | Upgrade migrations | `.\upgrade_service.ps1 -ServiceName <name>` |

---

## 1. Schema Extraction

### Purpose
Extract `table_schema` definitions from object models and generate JSON files that can be consumed by CQRS schema scripts.

### Tool: `extract_table_schemas.py`

### Usage

**Extract SCOR schemas**:
```bash
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\utils
python extract_table_schemas.py --scor
```

**Output**:
- JSON files created in `schemas/scor/` directory
- Each file contains table definition with columns, types, and metadata

**Example Output**:
```json
{
  "table_name": "scor_processes",
  "class_name": "SCORProcess",
  "columns": [
    {
      "name": "id",
      "type": "String",
      "primary_key": true,
      "nullable": false
    },
    {
      "name": "process_code",
      "type": "String",
      "nullable": false
    }
  ],
  "_metadata": {
    "object_model_name": "SCOR Process",
    "object_model_code": "SCOR_PROCESS",
    "description": "Supply Chain Operations Reference Process",
    "module": "ASCM_SCOR"
  }
}
```

### When to Use
- After creating new object models
- Before adding tables to database
- When updating object model definitions
- As part of schema generation workflow

---

## 2. CQRS Schema Addition

### Purpose
Automate the addition of new schema objects with proper CQRS (Command Query Responsibility Segregation) pattern.

### Tool: `add_cqrs_schema.ps1`

### Features
- Adds write models to `app/models.py`
- Generates corresponding read models in domain folders
- Updates imports and dependencies
- Generates Alembic migration
- Prevents table duplication and import conflicts

### Usage

**Basic Example**:
```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\utils

.\add_cqrs_schema.ps1 `
    -ServiceName "analytics_service" `
    -TableName "scor_processes" `
    -Domain "scor" `
    -SchemaDefinition "..\..\schemas\scor\scor_process.json"
```

**Dry Run** (preview changes without applying):
```powershell
.\add_cqrs_schema.ps1 `
    -ServiceName "analytics_service" `
    -TableName "scor_processes" `
    -Domain "scor" `
    -SchemaDefinition "..\..\schemas\scor\scor_process.json" `
    -DryRun
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `ServiceName` | Yes | Name of the service (e.g., 'analytics_service') |
| `TableName` | Yes | Name of the table to create |
| `Domain` | Yes | Domain folder for read models (e.g., 'scor', 'source') |
| `SchemaDefinition` | Yes | Path to JSON schema file |
| `DryRun` | No | Preview changes without applying |

### What It Does

1. **Validates inputs**: Checks service path, domain path, schema file
2. **Checks for duplicates**: Ensures table doesn't already exist
3. **Adds write model**: Updates `app/models.py` with SQLAlchemy model
4. **Generates read model**: Creates Pydantic model in domain folder
5. **Updates imports**: Adds necessary imports to `__init__.py`
6. **Creates migration**: Generates Alembic migration script
7. **Validates migration**: Checks for syntax errors

### When to Use
- Adding new tables to a service
- Implementing new entities from Business Metadata
- Expanding domain models
- After extracting schemas from object models

---

## 3. CQRS Validation

### Purpose
Validate that CQRS pattern is correctly implemented across all services.

### Tool: `validate_cqrs_models.ps1`

### What It Checks
- Write models exist in `app/models.py`
- Corresponding read models exist in domain folders
- Field names match between write and read models
- Data types are compatible
- No orphaned models (read without write, or vice versa)

### Usage

**Validate all services**:
```powershell
cd C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\utils
.\validate_cqrs_models.ps1
```

**Validate specific service**:
```powershell
.\validate_cqrs_models.ps1 -ServiceName "analytics_service"
```

### Output Example
```
[INFO] Validating CQRS Models
[INFO] Service: analytics_service
[✓] Write Model: SCORProcess (app/models.py)
[✓] Read Model: SCORProcessRead (app/scor/models.py)
[✓] Fields match: id, process_code, name, description
[✓] Types compatible

[SUMMARY]
Services Validated: 5
Models Checked: 23
Issues Found: 0
```

### When to Use
- Before committing code changes
- After adding new models
- As part of CI/CD pipeline
- During code reviews

---

## 4. Migration Management

### Purpose
Helper scripts for Alembic migration creation, upgrade, and management.

### Tools

#### 4.1 Create Migration: `create_revision_clean.ps1`

**Purpose**: Create a new Alembic migration with proper naming and validation.

**Usage**:
```powershell
.\create_revision_clean.ps1 `
    -ServiceName "analytics_service" `
    -Message "Add scor_processes table"
```

**What It Does**:
- Generates Alembic revision with timestamp
- Validates migration syntax
- Checks for conflicts with existing migrations
- Creates clean migration file

---

#### 4.2 Upgrade Migrations: `upgrade_service.ps1`

**Purpose**: Upgrade a service's database to the latest migration.

**Usage**:
```powershell
.\upgrade_service.ps1 -ServiceName "analytics_service"
```

**Options**:
```powershell
# Upgrade to specific revision
.\upgrade_service.ps1 -ServiceName "analytics_service" -Revision "abc123"

# Dry run (show SQL without executing)
.\upgrade_service.ps1 -ServiceName "analytics_service" -DryRun
```

---

#### 4.3 Reset Migrations: `run_migration_reset.ps1`

**Purpose**: Reset migrations for a service (useful for development).

**⚠️ WARNING**: This will drop all tables and reapply migrations. Use with caution!

**Usage**:
```powershell
.\run_migration_reset.ps1 -ServiceName "analytics_service"
```

**What It Does**:
- Backs up current database state
- Drops all tables
- Reapplies migrations from scratch
- Validates final state

---

#### 4.4 Resolve Migration Conflicts: `resolve_service_heads.ps1`

**Purpose**: Resolve Alembic head conflicts when multiple branches exist.

**Usage**:
```powershell
# Check for conflicts
.\resolve_service_heads.ps1 -ServiceName "analytics_service" -CheckOnly

# Resolve conflicts (creates merge migration)
.\resolve_service_heads.ps1 -ServiceName "analytics_service"
```

**When to Use**:
- After merging branches with migrations
- When `alembic upgrade head` fails with "multiple heads"
- Before deploying to production

---

## 5. CI/CD Integration

### Purpose
Integrate migration utilities into continuous integration and deployment pipelines.

### Tool: `ci_cd_integration.ps1`

### Usage in GitHub Actions

**Example Workflow**:
```yaml
name: Validate Migrations

on:
  pull_request:
    paths:
      - 'alembic/versions/**'
      - 'services/**/app/models.py'

jobs:
  validate:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate CQRS Models
        run: |
          cd scripts/utils
          .\validate_cqrs_models.ps1
      
      - name: Check Migration Conflicts
        run: |
          cd scripts/utils
          .\resolve_service_heads.ps1 -CheckOnly
```

### When to Use
- On pull requests that modify models or migrations
- Before merging to main branch
- As part of deployment pipeline
- For automated quality checks

---

## 6. Docker Deployment

### Purpose
Deploy services with automated migration execution.

### Tool: `enhanced_docker_deploy.ps1`

### Usage

**Deploy with migrations**:
```powershell
.\enhanced_docker_deploy.ps1 `
    -ServiceName "analytics_service" `
    -Environment "staging" `
    -RunMigrations
```

**Deploy without migrations** (use existing schema):
```powershell
.\enhanced_docker_deploy.ps1 `
    -ServiceName "analytics_service" `
    -Environment "production"
```

### What It Does
1. Builds Docker image
2. Runs migration validation
3. Executes migrations (if `-RunMigrations` specified)
4. Deploys container
5. Runs health checks
6. Rolls back on failure

---

## 7. Complete Workflow Example

### Scenario: Adding a New Entity to Analytics Service

**Step 1: Define Object Model**
```python
# services/business_services/analytics_models/definitions/object_models/scor_alert.py
SCOR_ALERT = ObjectModel(
    name="SCOR Alert",
    code="SCOR_ALERT",
    table_schema={
        "table_name": "scor_alerts",
        "class_name": "SCORAlert",
        "columns": [
            {"name": "id", "type": "String", "primary_key": True},
            {"name": "alert_code", "type": "String", "nullable": False},
            {"name": "severity", "type": "String"},
            {"name": "message", "type": "Text"}
        ]
    }
)
```

**Step 2: Extract Schema**
```bash
cd scripts/utils
python extract_table_schemas.py --scor
# Output: schemas/scor/scor_alert.json
```

**Step 3: Add CQRS Schema**
```powershell
.\add_cqrs_schema.ps1 `
    -ServiceName "analytics_service" `
    -TableName "scor_alerts" `
    -Domain "scor" `
    -SchemaDefinition "..\..\schemas\scor\scor_alert.json"
```

**Step 4: Validate**
```powershell
.\validate_cqrs_models.ps1 -ServiceName "analytics_service"
```

**Step 5: Test Migration**
```powershell
.\upgrade_service.ps1 -ServiceName "analytics_service" -DryRun
```

**Step 6: Apply Migration**
```powershell
.\upgrade_service.ps1 -ServiceName "analytics_service"
```

**Step 7: Verify**
```bash
# Check database
psql -d analytics_db -c "\d scor_alerts"
```

---

## 8. Troubleshooting

### Common Issues

#### Issue: "Schema definition file not found"
**Solution**: Check file path is correct and relative to `scripts/utils/`
```powershell
# Use absolute path or correct relative path
-SchemaDefinition "C:\Full\Path\To\schema.json"
```

#### Issue: "Table already exists"
**Solution**: Table is already in database. Check `app/models.py` or use different table name.

#### Issue: "Multiple heads found"
**Solution**: Resolve migration conflicts
```powershell
.\resolve_service_heads.ps1 -ServiceName "analytics_service"
```

#### Issue: "CQRS validation failed"
**Solution**: Check that read and write models match
```powershell
.\validate_cqrs_models.ps1 -ServiceName "analytics_service"
# Review output for mismatches
```

---

## 9. Best Practices

### Schema Management
1. ✅ Always extract schemas before adding tables
2. ✅ Use dry run mode first to preview changes
3. ✅ Validate CQRS models after changes
4. ✅ Test migrations in development before production
5. ✅ Keep schema JSON files in version control

### Migration Management
1. ✅ Create descriptive migration messages
2. ✅ Review generated migration SQL before applying
3. ✅ Never edit migrations after they're committed
4. ✅ Resolve conflicts immediately when they occur
5. ✅ Back up database before major migrations

### CI/CD Integration
1. ✅ Validate migrations on every PR
2. ✅ Check for CQRS consistency automatically
3. ✅ Run migration tests in isolated environment
4. ✅ Use staging environment for migration testing
5. ✅ Automate rollback on deployment failure

---

## 10. Integration with Services

### Current Status
These utilities are **standalone tools** that must be run manually. Future integration plans include:

### Planned Integrations

**Business Metadata Service**:
- API endpoint: `POST /metadata/schemas/extract`
- Automatic schema extraction when entities are created/updated
- Event-driven workflow

**Database Service**:
- API endpoint: `POST /database/migration-utilities/add-cqrs-schema`
- Programmatic CQRS schema addition
- Migration validation API

**CI/CD Pipeline**:
- GitHub Actions workflow for automated validation
- Pre-commit hooks for CQRS validation
- Deployment pipeline integration

See `MIGRATION_UTILITIES_ANALYSIS.md` for detailed integration plan.

---

## 11. Related Documentation

- [MIGRATION_UTILITIES_ANALYSIS.md](../../MIGRATION_UTILITIES_ANALYSIS.md) - Detailed analysis and integration plan
- [BACKEND_SERVICE_USAGE_ANALYSIS.md](../../BACKEND_SERVICE_USAGE_ANALYSIS.md) - Backend service patterns
- [FEATURE_VALIDATION_REPORT.md](../../FEATURE_VALIDATION_REPORT.md) - Feature validation status
- [Database Service README](../../services/backend_services/database_service/README.md) - Database service documentation

---

## 12. Support

### Getting Help
- Check this guide first
- Review error messages carefully
- Use `-DryRun` mode to preview changes
- Consult `MIGRATION_UTILITIES_ANALYSIS.md` for integration details

### Reporting Issues
- Include full error message
- Provide command used
- Share relevant file paths
- Describe expected vs actual behavior

---

**Last Updated**: December 19, 2025  
**Version**: 1.0  
**Maintainer**: Development Team
