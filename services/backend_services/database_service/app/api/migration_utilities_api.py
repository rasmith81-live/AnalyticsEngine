"""
Migration Utilities API Endpoints

Provides REST API for migration utilities (CQRS schema addition, validation, etc.)
Wraps PowerShell and Python scripts as API endpoints.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from pathlib import Path
import subprocess
import json
import tempfile
import asyncio
from datetime import datetime

router = APIRouter(prefix="/database/migration-utilities", tags=["Migration Utilities"])


class CQRSSchemaRequest(BaseModel):
    """Request model for CQRS schema addition."""
    service_name: str = Field(..., description="Name of the service (e.g., 'analytics_service')")
    table_name: str = Field(..., description="Name of the table to create")
    domain: str = Field(..., description="Domain folder for read models (e.g., 'scor')")
    schema_definition: Dict[str, Any] = Field(..., description="Schema definition (JSON)")
    dry_run: bool = Field(default=False, description="Preview changes without applying")


class CQRSSchemaResponse(BaseModel):
    """Response model for CQRS schema addition."""
    success: bool
    service_name: str
    table_name: str
    output: str
    errors: Optional[str] = None
    files_created: List[str] = []
    migration_file: Optional[str] = None


class CQRSValidationRequest(BaseModel):
    """Request model for CQRS validation."""
    service_name: Optional[str] = Field(None, description="Specific service to validate (None = all)")


class CQRSValidationResponse(BaseModel):
    """Response model for CQRS validation."""
    success: bool
    services_validated: int
    models_checked: int
    issues_found: int
    output: str
    errors: Optional[str] = None
    issues: List[Dict[str, Any]] = []


class MigrationCreationRequest(BaseModel):
    """Request model for migration creation."""
    service_name: str = Field(..., description="Name of the service")
    message: str = Field(..., description="Migration message/description")
    auto_generate: bool = Field(default=True, description="Auto-generate from model changes")


class MigrationCreationResponse(BaseModel):
    """Response model for migration creation."""
    success: bool
    service_name: str
    migration_file: str
    revision_id: str
    output: str
    errors: Optional[str] = None


@router.post("/add-cqrs-schema", response_model=CQRSSchemaResponse)
async def add_cqrs_schema(
    request: CQRSSchemaRequest,
    background_tasks: BackgroundTasks
):
    """
    Add CQRS schema objects with proper pattern.
    
    This endpoint wraps the `add_cqrs_schema.ps1` PowerShell script,
    automating the addition of write models, read models, and migrations.
    
    **What It Does**:
    1. Validates inputs and schema definition
    2. Adds write model to `app/models.py`
    3. Generates read model in domain folder
    4. Updates imports in `__init__.py`
    5. Creates Alembic migration
    6. Validates migration syntax
    
    **Example Request**:
    ```json
    {
        "service_name": "analytics_service",
        "table_name": "scor_processes",
        "domain": "scor",
        "schema_definition": {
            "table_name": "scor_processes",
            "class_name": "SCORProcess",
            "columns": [
                {"name": "id", "type": "String", "primary_key": true},
                {"name": "process_code", "type": "String", "nullable": false}
            ]
        },
        "dry_run": false
    }
    ```
    """
    try:
        # Save schema definition to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(request.schema_definition, f, indent=2)
            schema_file = f.name
        
        # Build PowerShell command
        script_path = Path(__file__).parent.parent.parent.parent.parent.parent / "scripts" / "utils" / "add_cqrs_schema.ps1"
        
        cmd = [
            "pwsh",
            str(script_path),
            "-ServiceName", request.service_name,
            "-TableName", request.table_name,
            "-Domain", request.domain,
            "-SchemaDefinition", schema_file
        ]
        
        if request.dry_run:
            cmd.append("-DryRun")
        
        # Execute PowerShell script
        result = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await result.communicate()
        
        # Clean up temp file
        Path(schema_file).unlink(missing_ok=True)
        
        # Parse output
        output_text = stdout.decode('utf-8')
        error_text = stderr.decode('utf-8') if stderr else None
        
        success = result.returncode == 0
        
        # Extract created files from output
        files_created = []
        migration_file = None
        
        for line in output_text.split('\n'):
            if 'Created:' in line or 'Updated:' in line:
                # Extract file path
                parts = line.split(':', 1)
                if len(parts) > 1:
                    files_created.append(parts[1].strip())
            elif 'Migration:' in line:
                parts = line.split(':', 1)
                if len(parts) > 1:
                    migration_file = parts[1].strip()
        
        return CQRSSchemaResponse(
            success=success,
            service_name=request.service_name,
            table_name=request.table_name,
            output=output_text,
            errors=error_text if not success else None,
            files_created=files_created,
            migration_file=migration_file
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"CQRS schema addition failed: {str(e)}"
        )


@router.post("/validate-cqrs", response_model=CQRSValidationResponse)
async def validate_cqrs(
    request: CQRSValidationRequest = CQRSValidationRequest()
):
    """
    Validate CQRS model consistency across services.
    
    This endpoint wraps the `validate_cqrs_models.ps1` PowerShell script,
    checking that write and read models are properly aligned.
    
    **What It Checks**:
    - Write models exist in `app/models.py`
    - Corresponding read models exist in domain folders
    - Field names match between write and read models
    - Data types are compatible
    - No orphaned models
    
    **Example Request**:
    ```json
    {
        "service_name": "analytics_service"
    }
    ```
    """
    try:
        # Build PowerShell command
        script_path = Path(__file__).parent.parent.parent.parent.parent.parent / "scripts" / "utils" / "validate_cqrs_models.ps1"
        
        cmd = ["pwsh", str(script_path)]
        
        if request.service_name:
            cmd.extend(["-ServiceName", request.service_name])
        
        # Execute PowerShell script
        result = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await result.communicate()
        
        # Parse output
        output_text = stdout.decode('utf-8')
        error_text = stderr.decode('utf-8') if stderr else None
        
        success = result.returncode == 0
        
        # Parse validation results from output
        services_validated = 0
        models_checked = 0
        issues_found = 0
        issues = []
        
        for line in output_text.split('\n'):
            if 'Services Validated:' in line:
                services_validated = int(line.split(':')[1].strip())
            elif 'Models Checked:' in line:
                models_checked = int(line.split(':')[1].strip())
            elif 'Issues Found:' in line:
                issues_found = int(line.split(':')[1].strip())
            elif '[ISSUE]' in line:
                issues.append({
                    "message": line.replace('[ISSUE]', '').strip(),
                    "severity": "error"
                })
        
        return CQRSValidationResponse(
            success=success and issues_found == 0,
            services_validated=services_validated,
            models_checked=models_checked,
            issues_found=issues_found,
            output=output_text,
            errors=error_text if not success else None,
            issues=issues
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"CQRS validation failed: {str(e)}"
        )


@router.post("/create-migration", response_model=MigrationCreationResponse)
async def create_migration(
    request: MigrationCreationRequest
):
    """
    Create a new Alembic migration for a service.
    
    This endpoint wraps the `create_revision_clean.ps1` PowerShell script,
    creating a clean Alembic migration with proper naming and validation.
    
    **What It Does**:
    1. Generates Alembic revision with timestamp
    2. Validates migration syntax
    3. Checks for conflicts with existing migrations
    4. Creates clean migration file
    
    **Example Request**:
    ```json
    {
        "service_name": "analytics_service",
        "message": "Add scor_processes table",
        "auto_generate": true
    }
    ```
    """
    try:
        # Build PowerShell command
        script_path = Path(__file__).parent.parent.parent.parent.parent.parent / "scripts" / "utils" / "create_revision_clean.ps1"
        
        cmd = [
            "pwsh",
            str(script_path),
            "-ServiceName", request.service_name,
            "-Message", request.message
        ]
        
        if not request.auto_generate:
            cmd.append("-Manual")
        
        # Execute PowerShell script
        result = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await result.communicate()
        
        # Parse output
        output_text = stdout.decode('utf-8')
        error_text = stderr.decode('utf-8') if stderr else None
        
        success = result.returncode == 0
        
        # Extract migration file and revision ID from output
        migration_file = ""
        revision_id = ""
        
        for line in output_text.split('\n'):
            if 'Migration file:' in line:
                migration_file = line.split(':', 1)[1].strip()
            elif 'Revision ID:' in line:
                revision_id = line.split(':', 1)[1].strip()
        
        return MigrationCreationResponse(
            success=success,
            service_name=request.service_name,
            migration_file=migration_file,
            revision_id=revision_id,
            output=output_text,
            errors=error_text if not success else None
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Migration creation failed: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """
    Health check for migration utilities API.
    
    Verifies that required scripts are accessible.
    """
    scripts_dir = Path(__file__).parent.parent.parent.parent.parent.parent / "scripts" / "utils"
    
    required_scripts = [
        "add_cqrs_schema.ps1",
        "validate_cqrs_models.ps1",
        "create_revision_clean.ps1"
    ]
    
    missing_scripts = []
    for script in required_scripts:
        script_path = scripts_dir / script
        if not script_path.exists():
            missing_scripts.append(script)
    
    return {
        "status": "healthy" if not missing_scripts else "degraded",
        "scripts_directory": str(scripts_dir),
        "required_scripts": required_scripts,
        "missing_scripts": missing_scripts,
        "timestamp": datetime.utcnow().isoformat()
    }
