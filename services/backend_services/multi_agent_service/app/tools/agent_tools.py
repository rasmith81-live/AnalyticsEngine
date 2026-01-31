"""
Agent Tools

MCP-style tools that agents can use to interact with the Analytics Engine
platform services and generate artifacts.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod

import httpx
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ToolResult(BaseModel):
    """Result from a tool execution."""
    success: bool
    data: Dict[str, Any] = {}
    error: Optional[str] = None


class BaseTool(ABC):
    """Base class for agent tools."""
    
    name: str
    description: str
    
    def __init__(self, service_urls: Optional[Dict[str, str]] = None):
        """
        Initialize the tool.
        
        Args:
            service_urls: Dictionary of service URLs
        """
        self.service_urls = service_urls or {
            "metadata": "http://business_metadata:8000",
            "calculation": "http://calculation_engine:8000",
            "database": "http://database_service:8000"
        }
        self.timeout = 30.0
    
    @abstractmethod
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Execute the tool with given parameters."""
        pass
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool's parameter schema."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self._get_parameters_schema()
        }
    
    @abstractmethod
    def _get_parameters_schema(self) -> Dict[str, Any]:
        """Get the parameters schema for this tool."""
        pass


class DesignValueChainTool(BaseTool):
    """Tool for designing value chain structures."""
    
    name = "design_value_chain"
    description = "Design a value chain structure with processes and activities"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the value chain"
                },
                "industry": {
                    "type": "string",
                    "description": "Target industry"
                },
                "processes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "activities": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        },
                        "required": ["name"]
                    },
                    "description": "List of processes in the value chain"
                }
            },
            "required": ["name", "processes"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Design a value chain structure."""
        name = params.get("name", "")
        industry = params.get("industry", "")
        processes = params.get("processes", [])
        
        # Build value chain structure
        nodes = []
        links = []
        
        # Root node
        root_id = f"vc_{name.lower().replace(' ', '_')}"
        nodes.append({
            "id": root_id,
            "name": name,
            "kind": "value_chain_pattern_definition",
            "industry": industry
        })
        
        # Process nodes
        prev_process_id = None
        for process in processes:
            process_id = f"proc_{process['name'].lower().replace(' ', '_')}"
            nodes.append({
                "id": process_id,
                "name": process["name"],
                "kind": "process_definition",
                "description": process.get("description", "")
            })
            
            links.append({
                "from_entity": root_id,
                "to_entity": process_id,
                "relationship_type": "contains"
            })
            
            if prev_process_id:
                links.append({
                    "from_entity": prev_process_id,
                    "to_entity": process_id,
                    "relationship_type": "flows_to"
                })
            prev_process_id = process_id
            
            # Activity nodes
            for activity in process.get("activities", []):
                activity_id = f"act_{activity.lower().replace(' ', '_')}"
                nodes.append({
                    "id": activity_id,
                    "name": activity,
                    "kind": "activity_definition"
                })
                links.append({
                    "from_entity": process_id,
                    "to_entity": activity_id,
                    "relationship_type": "contains"
                })
        
        return ToolResult(
            success=True,
            data={
                "value_chain": {
                    "name": name,
                    "industry": industry,
                    "nodes": nodes,
                    "links": links
                }
            }
        )


class DefineEntityTool(BaseTool):
    """Tool for defining business entities."""
    
    name = "define_entity"
    description = "Define a business entity with its attributes and schema"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Entity name"
                },
                "code": {
                    "type": "string",
                    "description": "Entity code (snake_case)"
                },
                "description": {
                    "type": "string",
                    "description": "Entity description"
                },
                "attributes": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "type": {"type": "string"},
                            "description": {"type": "string"},
                            "required": {"type": "boolean"}
                        },
                        "required": ["name", "type"]
                    },
                    "description": "Entity attributes"
                }
            },
            "required": ["name", "code", "attributes"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Define a business entity."""
        name = params.get("name", "")
        code = params.get("code", "")
        description = params.get("description", "")
        attributes = params.get("attributes", [])
        
        # Type mapping
        type_map = {
            "string": "VARCHAR(255)",
            "text": "TEXT",
            "integer": "INTEGER",
            "decimal": "DECIMAL(18,4)",
            "boolean": "BOOLEAN",
            "date": "DATE",
            "datetime": "TIMESTAMPTZ",
            "timestamp": "TIMESTAMPTZ",
            "uuid": "UUID",
            "json": "JSONB"
        }
        
        # Build entity definition
        columns = []
        for attr in attributes:
            columns.append({
                "name": attr["name"],
                "type": type_map.get(attr.get("type", "string"), "VARCHAR(255)"),
                "nullable": not attr.get("required", False),
                "description": attr.get("description", "")
            })
        
        entity = {
            "name": name,
            "code": code,
            "kind": "entity_definition",
            "description": description,
            "table_schema": {
                "table_name": code,
                "columns": columns
            }
        }
        
        return ToolResult(
            success=True,
            data={"entity": entity}
        )


class IdentifyKPIsTool(BaseTool):
    """Tool for identifying relevant KPIs."""
    
    name = "identify_kpis"
    description = "Identify relevant KPIs for a business domain"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Business domain (e.g., supply_chain, sales, finance)"
                },
                "industry": {
                    "type": "string",
                    "description": "Industry context"
                },
                "focus_areas": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Specific areas to focus on"
                }
            },
            "required": ["domain"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Identify relevant KPIs."""
        domain = params.get("domain", "").lower()
        industry = params.get("industry", "")
        focus_areas = params.get("focus_areas", [])
        
        # Domain-specific KPI templates
        kpi_templates = {
            "supply_chain": [
                {
                    "name": "Order Fulfillment Rate",
                    "code": "order_fulfillment_rate",
                    "formula": "(Orders Fulfilled / Total Orders) * 100",
                    "unit": "%",
                    "required_objects": ["order"]
                },
                {
                    "name": "Inventory Turnover",
                    "code": "inventory_turnover",
                    "formula": "Cost of Goods Sold / Average Inventory",
                    "unit": "ratio",
                    "required_objects": ["inventory", "cost"]
                },
                {
                    "name": "Perfect Order Rate",
                    "code": "perfect_order_rate",
                    "formula": "(Perfect Orders / Total Orders) * 100",
                    "unit": "%",
                    "required_objects": ["order"]
                }
            ],
            "sales": [
                {
                    "name": "Revenue",
                    "code": "revenue",
                    "formula": "SUM(Order.Amount)",
                    "unit": "currency",
                    "required_objects": ["order"]
                },
                {
                    "name": "Conversion Rate",
                    "code": "conversion_rate",
                    "formula": "(Conversions / Leads) * 100",
                    "unit": "%",
                    "required_objects": ["lead", "opportunity"]
                },
                {
                    "name": "Average Deal Size",
                    "code": "average_deal_size",
                    "formula": "Total Revenue / Number of Deals",
                    "unit": "currency",
                    "required_objects": ["deal"]
                }
            ],
            "finance": [
                {
                    "name": "Gross Margin",
                    "code": "gross_margin",
                    "formula": "(Revenue - COGS) / Revenue * 100",
                    "unit": "%",
                    "required_objects": ["revenue", "cost"]
                },
                {
                    "name": "Operating Margin",
                    "code": "operating_margin",
                    "formula": "Operating Income / Revenue * 100",
                    "unit": "%",
                    "required_objects": ["income", "revenue"]
                }
            ],
            "operations": [
                {
                    "name": "Overall Equipment Effectiveness",
                    "code": "oee",
                    "formula": "Availability * Performance * Quality",
                    "unit": "%",
                    "required_objects": ["equipment", "production"]
                },
                {
                    "name": "Throughput",
                    "code": "throughput",
                    "formula": "Units Produced / Time Period",
                    "unit": "units/time",
                    "required_objects": ["production"]
                }
            ],
            "customer_service": [
                {
                    "name": "Customer Satisfaction Score",
                    "code": "csat",
                    "formula": "AVG(Survey Responses)",
                    "unit": "score",
                    "required_objects": ["survey", "customer"]
                },
                {
                    "name": "Net Promoter Score",
                    "code": "nps",
                    "formula": "% Promoters - % Detractors",
                    "unit": "score",
                    "required_objects": ["survey", "customer"]
                }
            ]
        }
        
        kpis = kpi_templates.get(domain, [])
        
        if not kpis:
            kpis = [
                {
                    "name": "Revenue Growth",
                    "code": "revenue_growth",
                    "formula": "(Current Revenue - Previous Revenue) / Previous Revenue * 100",
                    "unit": "%",
                    "required_objects": ["revenue"]
                }
            ]
        
        return ToolResult(
            success=True,
            data={
                "domain": domain,
                "industry": industry,
                "kpis": kpis
            }
        )


class GenerateSchemaTool(BaseTool):
    """Tool for generating database schemas."""
    
    name = "generate_schema"
    description = "Generate TimescaleDB DDL schema for an entity"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Table name"
                },
                "columns": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "type": {"type": "string"},
                            "nullable": {"type": "boolean"},
                            "primary_key": {"type": "boolean"}
                        },
                        "required": ["name", "type"]
                    },
                    "description": "Column definitions"
                },
                "is_hypertable": {
                    "type": "boolean",
                    "description": "Create as TimescaleDB hypertable"
                },
                "time_column": {
                    "type": "string",
                    "description": "Time column for hypertable"
                }
            },
            "required": ["table_name", "columns"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Generate TimescaleDB DDL schema."""
        table_name = params.get("table_name", "")
        columns = params.get("columns", [])
        is_hypertable = params.get("is_hypertable", False)
        time_column = params.get("time_column", "created_at")
        
        # Build DDL
        ddl_parts = [f"CREATE TABLE IF NOT EXISTS {table_name} ("]
        
        column_defs = []
        for col in columns:
            col_def = f"    {col['name']} {col['type']}"
            if col.get("primary_key"):
                col_def += " PRIMARY KEY"
            elif not col.get("nullable", True):
                col_def += " NOT NULL"
            column_defs.append(col_def)
        
        ddl_parts.append(",\n".join(column_defs))
        ddl_parts.append(");")
        
        ddl = "\n".join(ddl_parts)
        
        if is_hypertable:
            ddl += f"\n\nSELECT create_hypertable('{table_name}', '{time_column}');"
        
        return ToolResult(
            success=True,
            data={
                "table_name": table_name,
                "ddl": ddl,
                "is_hypertable": is_hypertable
            }
        )


class ValidateSchemaTool(BaseTool):
    """Tool for validating database schemas."""
    
    name = "validate_schema"
    description = "Validate a database schema for correctness"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "schema_name": {
                    "type": "string",
                    "description": "Schema name to validate"
                },
                "ddl": {
                    "type": "string",
                    "description": "DDL to validate"
                }
            },
            "required": ["schema_name"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Validate a database schema."""
        schema_name = params.get("schema_name", "")
        ddl = params.get("ddl", "")
        
        issues = []
        checks = []
        
        # Basic validation
        checks.append({
            "check": "DDL syntax",
            "status": "passed" if ddl else "failed"
        })
        
        if ddl:
            if "CREATE TABLE" in ddl.upper():
                checks.append({"check": "Table creation", "status": "passed"})
            else:
                issues.append("Missing CREATE TABLE statement")
                checks.append({"check": "Table creation", "status": "failed"})
            
            if "PRIMARY KEY" in ddl.upper() or "id" in ddl.lower():
                checks.append({"check": "Primary key", "status": "passed"})
            else:
                issues.append("No primary key defined")
                checks.append({"check": "Primary key", "status": "warning"})
        
        return ToolResult(
            success=len([i for i in issues if "failed" in str(i)]) == 0,
            data={
                "schema_name": schema_name,
                "checks": checks,
                "issues": issues
            }
        )


class GenerateDocsTool(BaseTool):
    """Tool for generating documentation."""
    
    name = "generate_docs"
    description = "Generate documentation for artifacts"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "doc_type": {
                    "type": "string",
                    "enum": ["overview", "technical", "user_guide", "data_dictionary"],
                    "description": "Type of documentation"
                },
                "subject": {
                    "type": "string",
                    "description": "Subject to document"
                },
                "content": {
                    "type": "object",
                    "description": "Content to document"
                }
            },
            "required": ["doc_type", "subject"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Generate documentation."""
        doc_type = params.get("doc_type", "overview")
        subject = params.get("subject", "")
        content = params.get("content", {})
        
        if doc_type == "overview":
            doc = f"""# {subject} Overview

## Introduction

This document provides an overview of {subject}.

## Key Components

{json.dumps(content, indent=2) if content else "Components to be defined."}

## Next Steps

1. Review the design
2. Validate with stakeholders
3. Proceed to implementation
"""
        elif doc_type == "data_dictionary":
            doc = f"""# {subject} Data Dictionary

## Entities

{json.dumps(content, indent=2) if content else "Entities to be documented."}

## Relationships

Relationships between entities.

## Glossary

Business term definitions.
"""
        else:
            doc = f"""# {subject} Documentation

## Overview

Documentation for {subject}.

## Details

{json.dumps(content, indent=2) if content else "Details to be added."}
"""
        
        return ToolResult(
            success=True,
            data={
                "doc_type": doc_type,
                "subject": subject,
                "documentation": doc
            }
        )


class PersistToMetadataTool(BaseTool):
    """Tool for persisting artifacts to the Business Metadata Service."""
    
    name = "persist_to_metadata"
    description = "Persist generated artifacts to the Business Metadata Service"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "artifact_type": {
                    "type": "string",
                    "enum": ["entity", "metric", "value_chain", "relationship"],
                    "description": "Type of artifact to persist"
                },
                "artifact": {
                    "type": "object",
                    "description": "Artifact data to persist"
                }
            },
            "required": ["artifact_type", "artifact"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Persist artifact to metadata service."""
        artifact_type = params.get("artifact_type", "")
        artifact = params.get("artifact", {})
        
        # Map artifact type to API endpoint
        endpoint_map = {
            "entity": "/api/v1/metadata/entities",
            "metric": "/api/v1/metadata/metrics",
            "value_chain": "/api/v1/metadata/value-chains",
            "relationship": "/api/v1/metadata/relationships"
        }
        
        endpoint = endpoint_map.get(artifact_type)
        if not endpoint:
            return ToolResult(
                success=False,
                error=f"Unknown artifact type: {artifact_type}"
            )
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.service_urls['metadata']}{endpoint}",
                    json=artifact
                )
                response.raise_for_status()
                
                return ToolResult(
                    success=True,
                    data={
                        "artifact_type": artifact_type,
                        "persisted": True,
                        "response": response.json()
                    }
                )
        except Exception as e:
            logger.error(f"Failed to persist {artifact_type}: {e}")
            return ToolResult(
                success=False,
                error=str(e)
            )


# =============================================================================
# SERVICE INTEGRATION TOOLS
# =============================================================================

class RegisterKPIWithCalculationEngineTool(BaseTool):
    """Tool for registering KPI definitions with the Calculation Engine Service."""
    
    name = "register_kpi_with_calculation_engine"
    description = "Register a KPI definition with the Calculation Engine for execution"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "kpi_code": {
                    "type": "string",
                    "description": "Unique KPI code"
                },
                "kpi_definition": {
                    "type": "object",
                    "description": "Full KPI definition including formula, entities, and metadata"
                }
            },
            "required": ["kpi_code", "kpi_definition"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Register KPI with calculation engine."""
        kpi_code = params.get("kpi_code", "")
        kpi_definition = params.get("kpi_definition", {})
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.service_urls['calculation']}/api/v1/kpis/register",
                    json={
                        "kpi_code": kpi_code,
                        "definition": kpi_definition
                    }
                )
                response.raise_for_status()
                
                return ToolResult(
                    success=True,
                    data={
                        "kpi_code": kpi_code,
                        "registered": True,
                        "response": response.json()
                    }
                )
        except Exception as e:
            logger.error(f"Failed to register KPI {kpi_code}: {e}")
            return ToolResult(
                success=False,
                error=str(e)
            )


class ExecuteSchemaMigrationTool(BaseTool):
    """Tool for executing schema migrations via the Database Service."""
    
    name = "execute_schema_migration"
    description = "Execute DDL/schema migration via the Database Service"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "schema_name": {
                    "type": "string",
                    "description": "Name of the schema/table"
                },
                "ddl": {
                    "type": "string",
                    "description": "DDL statement to execute"
                },
                "is_hypertable": {
                    "type": "boolean",
                    "description": "Whether to create as TimescaleDB hypertable"
                }
            },
            "required": ["schema_name", "ddl"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Execute schema migration."""
        schema_name = params.get("schema_name", "")
        ddl = params.get("ddl", "")
        is_hypertable = params.get("is_hypertable", False)
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.service_urls['database']}/api/v1/migrations/execute",
                    json={
                        "schema_name": schema_name,
                        "ddl": ddl,
                        "is_hypertable": is_hypertable
                    }
                )
                response.raise_for_status()
                
                return ToolResult(
                    success=True,
                    data={
                        "schema_name": schema_name,
                        "executed": True,
                        "response": response.json()
                    }
                )
        except Exception as e:
            logger.error(f"Failed to execute schema migration for {schema_name}: {e}")
            return ToolResult(
                success=False,
                error=str(e)
            )


class CreateRelationshipTool(BaseTool):
    """Tool for creating relationships in the metadata_relationships table."""
    
    name = "create_relationship"
    description = "Create a relationship between ontology entities via the metadata_relationships API"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "from_entity": {
                    "type": "string",
                    "description": "Source entity code"
                },
                "to_entity": {
                    "type": "string",
                    "description": "Target entity code"
                },
                "relationship_type": {
                    "type": "string",
                    "enum": ["belongs_to_value_chain", "belongs_to_module", "uses"],
                    "description": "Type of relationship"
                }
            },
            "required": ["from_entity", "to_entity", "relationship_type"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Create relationship via metadata API."""
        from_entity = params.get("from_entity", "")
        to_entity = params.get("to_entity", "")
        relationship_type = params.get("relationship_type", "")
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.service_urls['metadata']}/api/v1/metadata/relationships",
                    json={
                        "from_entity": from_entity,
                        "to_entity": to_entity,
                        "relationship_type": relationship_type
                    }
                )
                response.raise_for_status()
                
                return ToolResult(
                    success=True,
                    data={
                        "from_entity": from_entity,
                        "to_entity": to_entity,
                        "relationship_type": relationship_type,
                        "created": True,
                        "response": response.json()
                    }
                )
        except Exception as e:
            logger.error(f"Failed to create relationship: {e}")
            return ToolResult(
                success=False,
                error=str(e)
            )


class PublishEventTool(BaseTool):
    """Tool for publishing events to Redis for downstream consumers."""
    
    name = "publish_event"
    description = "Publish an event to Redis pub/sub for downstream processing"
    
    def _get_parameters_schema(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Event topic/channel"
                },
                "event_type": {
                    "type": "string",
                    "description": "Type of event"
                },
                "payload": {
                    "type": "object",
                    "description": "Event payload data"
                }
            },
            "required": ["topic", "event_type", "payload"]
        }
    
    async def execute(self, params: Dict[str, Any]) -> ToolResult:
        """Publish event to messaging service."""
        topic = params.get("topic", "")
        event_type = params.get("event_type", "")
        payload = params.get("payload", {})
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.service_urls.get('messaging', 'http://messaging_service:8000')}/api/v1/events/publish",
                    json={
                        "topic": topic,
                        "event_type": event_type,
                        "payload": payload
                    }
                )
                response.raise_for_status()
                
                return ToolResult(
                    success=True,
                    data={
                        "topic": topic,
                        "event_type": event_type,
                        "published": True
                    }
                )
        except Exception as e:
            logger.error(f"Failed to publish event to {topic}: {e}")
            return ToolResult(
                success=False,
                error=str(e)
            )


# Tool registry
AVAILABLE_TOOLS = {
    "design_value_chain": DesignValueChainTool,
    "define_entity": DefineEntityTool,
    "identify_kpis": IdentifyKPIsTool,
    "generate_schema": GenerateSchemaTool,
    "validate_schema": ValidateSchemaTool,
    "generate_docs": GenerateDocsTool,
    "persist_to_metadata": PersistToMetadataTool,
    "register_kpi_with_calculation_engine": RegisterKPIWithCalculationEngineTool,
    "execute_schema_migration": ExecuteSchemaMigrationTool,
    "create_relationship": CreateRelationshipTool,
    "publish_event": PublishEventTool
}


def get_tool(name: str, service_urls: Optional[Dict[str, str]] = None) -> Optional[BaseTool]:
    """Get a tool instance by name."""
    tool_class = AVAILABLE_TOOLS.get(name)
    if tool_class:
        return tool_class(service_urls)
    return None


def get_all_tools(service_urls: Optional[Dict[str, str]] = None) -> List[BaseTool]:
    """Get all available tools."""
    return [cls(service_urls) for cls in AVAILABLE_TOOLS.values()]
