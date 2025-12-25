"""
Schema Extractor Service

Extracts table schemas from EntityDefinitions and generates JSON files.
Integrates extract_table_schemas.py functionality into the Business Metadata Service.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import time

from ..ontology_models import EntityDefinition


class SchemaExtractor:
    """
    Extract table schemas from EntityDefinitions and generate JSON files.
    
    This service provides programmatic access to schema extraction functionality,
    allowing automated schema generation when entities are created or updated.
    """
    
    def __init__(self, output_dir: Path, metrics_service=None):
        """
        Initialize SchemaExtractor.
        
        Args:
            output_dir: Directory where schema JSON files will be saved
            metrics_service: SchemaMetrics instance for tracking operations (optional)
        """
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.metrics = metrics_service
    
    async def extract_schema_from_entity(
        self, 
        entity_definition: EntityDefinition
    ) -> Dict[str, Any]:
        """
        Extract table schema from EntityDefinition.
        
        Args:
            entity_definition: EntityDefinition instance with table_schema
            
        Returns:
            Dictionary containing the table schema
            
        Raises:
            ValueError: If entity has no table_schema or schema is invalid
        """
        start_time = time.time()
        operation_id = None
        
        try:
            # Record metrics start
            if self.metrics:
                operation_id = await self.metrics.record_extraction_start(entity_definition.code)
            
            if not entity_definition.table_schema:
                raise ValueError(
                    f"Entity {entity_definition.name} does not have table_schema"
                )
            
            table_schema = entity_definition.table_schema
            
            # Validate required fields
            if not table_schema.table_name:
                raise ValueError(
                    f"Entity {entity_definition.name} table_schema missing table_name"
                )
            
            if not table_schema.class_name:
                raise ValueError(
                    f"Entity {entity_definition.name} table_schema missing class_name"
                )
            
            if not table_schema.columns:
                raise ValueError(
                    f"Entity {entity_definition.name} table_schema has no columns"
                )
            
            # Build schema dictionary
            schema = {
                "table_name": table_schema.table_name,
                "class_name": table_schema.class_name,
                "columns": [
                    {
                        "name": col.name,
                        "type": col.type,
                        "primary_key": col.primary_key,
                        "nullable": col.nullable,
                        "unique": col.unique,
                        "index": col.index,
                        "foreign_key": col.foreign_key,
                        "default": col.default
                    }
                    for col in table_schema.columns
                ],
                "_metadata": {
                    "entity_name": entity_definition.name,
                    "entity_code": entity_definition.code,
                    "description": entity_definition.description,
                    "module": entity_definition.module_code,
                    "extracted_at": datetime.utcnow().isoformat()
                }
            }
            
            # Add relationships if present
            if table_schema.relationships:
                schema["relationships"] = [
                    {
                        "name": rel.name,
                        "type": rel.type,
                        "target_entity": rel.target_entity,
                        "foreign_key": rel.foreign_key
                    }
                    for rel in table_schema.relationships
                ]
            
            # Add indexes if present
            if table_schema.indexes:
                schema["indexes"] = [
                    {
                        "name": idx.name,
                        "columns": idx.columns,
                        "unique": idx.unique
                    }
                    for idx in table_schema.indexes
                ]
            
            # Record metrics success
            if self.metrics and operation_id:
                duration_ms = (time.time() - start_time) * 1000
                await self.metrics.record_extraction_complete(
                    operation_id=operation_id,
                    entity_code=entity_definition.code,
                    duration_ms=duration_ms,
                    success=True
                )
            
            return schema
        
        except Exception as e:
            # Record metrics failure
            if self.metrics and operation_id:
                duration_ms = (time.time() - start_time) * 1000
                await self.metrics.record_extraction_complete(
                    operation_id=operation_id,
                    entity_code=entity_definition.code,
                    duration_ms=duration_ms,
                    success=False,
                    error=str(e)
                )
            raise
    
    async def save_schema_to_json(
        self, 
        schema: Dict[str, Any], 
        filename: str
    ) -> Path:
        """
        Save schema to JSON file.
        
        Args:
            schema: Schema dictionary
            filename: Output filename (without .json extension)
            
        Returns:
            Path to the saved JSON file
        """
        output_path = self.output_dir / f"{filename}.json"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        return output_path
    
    async def extract_schema_by_code(
        self, 
        entity_code: str,
        get_entity_func
    ) -> Dict[str, Any]:
        """
        Extract schema for a specific entity by code.
        
        Args:
            entity_code: Entity code to extract
            get_entity_func: Async function to retrieve entity by code
            
        Returns:
            Tuple of (schema dict, output file path)
        """
        entity = await get_entity_func(entity_code)
        
        if not entity:
            raise ValueError(f"Entity not found: {entity_code}")
        
        schema = await self.extract_schema_from_entity(entity)
        
        # Use lowercase entity code as filename
        filename = entity_code.lower()
        output_path = await self.save_schema_to_json(schema, filename)
        
        return {
            "schema": schema,
            "output_file": str(output_path),
            "entity_code": entity_code,
            "entity_name": entity.name
        }
    
    async def extract_schemas_by_module(
        self,
        module_code: str,
        get_entities_by_module_func
    ) -> List[Dict[str, Any]]:
        """
        Extract schemas for all entities in a module.
        
        Args:
            module_code: Module code (e.g., 'ASCM_SCOR')
            get_entities_by_module_func: Async function to retrieve entities by module
            
        Returns:
            List of extraction results
        """
        entities = await get_entities_by_module_func(module_code)
        
        results = []
        for entity in entities:
            try:
                schema = await self.extract_schema_from_entity(entity)
                filename = entity.code.lower()
                output_path = await self.save_schema_to_json(schema, filename)
                
                results.append({
                    "success": True,
                    "entity_code": entity.code,
                    "entity_name": entity.name,
                    "output_file": str(output_path)
                })
            except Exception as e:
                results.append({
                    "success": False,
                    "entity_code": entity.code,
                    "entity_name": entity.name,
                    "error": str(e)
                })
        
        return results
    
    async def extract_all_schemas(
        self,
        get_all_entities_func
    ) -> List[Dict[str, Any]]:
        """
        Extract schemas for all entities in the system.
        
        Args:
            get_all_entities_func: Async function to retrieve all entities
            
        Returns:
            List of extraction results
        """
        entities = await get_all_entities_func()
        
        results = []
        for entity in entities:
            try:
                schema = await self.extract_schema_from_entity(entity)
                filename = entity.code.lower()
                output_path = await self.save_schema_to_json(schema, filename)
                
                results.append({
                    "success": True,
                    "entity_code": entity.code,
                    "entity_name": entity.name,
                    "module": entity.module_code,
                    "output_file": str(output_path)
                })
            except Exception as e:
                results.append({
                    "success": False,
                    "entity_code": entity.code,
                    "entity_name": entity.name,
                    "module": entity.module_code,
                    "error": str(e)
                })
        
        return results
    
    def get_extraction_summary(
        self, 
        results: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Generate summary statistics from extraction results.
        
        Args:
            results: List of extraction results
            
        Returns:
            Summary dictionary with counts and details
        """
        total = len(results)
        successful = sum(1 for r in results if r.get("success", False))
        failed = total - successful
        
        return {
            "total_entities": total,
            "successful_extractions": successful,
            "failed_extractions": failed,
            "success_rate": (successful / total * 100) if total > 0 else 0,
            "output_directory": str(self.output_dir),
            "failed_entities": [
                {
                    "entity_code": r["entity_code"],
                    "entity_name": r["entity_name"],
                    "error": r["error"]
                }
                for r in results if not r.get("success", False)
            ]
        }
