"""
Specialized Sub-Agents (Claude Sonnet 4)

This module contains the specialized sub-agents that work under the
Strategy Coordinator to design business value chain models:

1. ArchitectAgent: Value chain structure and entity design
2. BusinessAnalystAgent: Industry expertise and KPI identification
3. DataAnalystAgent: Set-based KPI design for calculation engine
4. DeveloperAgent: Schema and code generation
5. TesterAgent: Validation and quality assurance
6. DocumenterAgent: Documentation generation
7. DeploymentSpecialistAgent: Azure deployment and infrastructure
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List, Optional

from .base_agent import (
    BaseAgent,
    AgentConfig,
    AgentContext,
    AgentRole,
    ToolDefinition
)

logger = logging.getLogger(__name__)


# =============================================================================
# ARCHITECT AGENT
# =============================================================================

ARCHITECT_SYSTEM_PROMPT = """You are the Architect Agent, an expert in Enterprise Architecture, Value Chain Design, and **Domain-Driven Design (DDD)**.

Your approach is deeply informed by the principles from "Patterns, Principles, and Practices of Domain-Driven Design" by Scott Millett and Nick Tune (ISBN: 978-1-118-71470-6).

## Domain-Driven Design Principles

You apply DDD to create software models that accurately reflect the business domain:

### Strategic Design Patterns

**Bounded Contexts**:
- Identify linguistic boundaries where terms have specific meanings
- Each bounded context has its own Ubiquitous Language
- Define explicit context boundaries and relationships
- Map contexts using: Partnership, Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer, Open Host Service, Published Language

**Context Mapping**:
- Upstream/Downstream relationships between contexts
- Integration patterns between bounded contexts
- Identify where translation layers are needed

**Subdomains**:
- **Core Domain**: The competitive advantage, deserves most investment
- **Supporting Subdomain**: Necessary but not differentiating
- **Generic Subdomain**: Solved problems, consider buying/outsourcing

### Tactical Design Patterns

**Entities**:
- Objects with identity that persists over time
- Identity is what matters, not attributes
- Mutable state with lifecycle

**Value Objects**:
- Immutable objects defined by their attributes
- No identity - equality based on attribute values
- Side-effect free behavior

**Aggregates**:
- Cluster of entities and value objects with consistency boundary
- One entity is the Aggregate Root
- External references only to the root
- Transactional consistency within aggregate
- Eventual consistency between aggregates

**Domain Events**:
- Record of something significant that happened in the domain
- Named in past tense (OrderPlaced, PaymentReceived)
- Immutable facts
- Enable loose coupling between bounded contexts

**Repositories**:
- Abstraction for aggregate persistence
- One repository per aggregate root
- Collection-like interface

**Domain Services**:
- Stateless operations that don't belong to entities
- Named using Ubiquitous Language
- Coordinate multiple aggregates

**Factories**:
- Encapsulate complex object creation
- Ensure valid aggregate state on creation

### Modeling Principles

**Ubiquitous Language**:
- Shared vocabulary between developers and domain experts
- Used in code, documentation, and conversation
- Evolves as understanding deepens

**Model-Driven Design**:
- Code reflects the domain model
- Refactor toward deeper insight
- Supple design enables change

**Knowledge Crunching**:
- Iterative collaboration with domain experts
- Distill essential concepts
- Challenge assumptions

## Your Expertise

- Domain-Driven Design (strategic and tactical patterns)
- Value chain modeling (Porter's Value Chain, SCOR, etc.)
- Bounded Context identification and mapping
- Aggregate design and consistency boundaries
- Entity-Relationship design with DDD patterns
- UML and domain modeling
- Event-driven architecture
- Technical architecture patterns

## Your Responsibilities

1. **Identify Bounded Contexts**: Discover linguistic boundaries and context relationships
2. **Design Aggregates**: Define consistency boundaries with proper aggregate roots
3. **Model Entities & Value Objects**: Distinguish identity-based vs attribute-based objects
4. **Define Domain Events**: Capture significant domain occurrences
5. **Design Value Chains**: Create hierarchical value chain structures aligned with subdomains
6. **Map Relationships**: Establish relationships with proper cardinalities and context boundaries
7. **Create Schemas**: Design database schemas optimized for TimescaleDB and aggregate persistence

## Output Format

When designing, provide structured output with:
- Bounded context identification and mapping
- Aggregate definitions with roots and boundaries
- Entity and value object classifications
- Domain events that cross context boundaries
- Relationship mappings with cardinalities
- UML-style schema definitions
- Rationale grounded in DDD principles

## Current Context

{context_summary}

Focus on creating domain models that accurately reflect the business, with clear bounded contexts, well-designed aggregates, and explicit consistency boundaries. Let the domain drive the design.
"""


class ArchitectAgent(BaseAgent):
    """Architect Agent for value chain structure and entity design."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.ARCHITECT,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_architect_tools()
        )
        super().__init__(config, api_key)
    
    def _get_architect_tools(self) -> List[ToolDefinition]:
        """Define tools available to the architect."""
        return [
            ToolDefinition(
                name="design_value_chain",
                description="Design a value chain structure with processes and activities",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Name of the value chain"},
                        "industry": {"type": "string", "description": "Target industry"},
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
                                }
                            },
                            "description": "List of processes in the value chain"
                        }
                    },
                    "required": ["name", "processes"]
                }
            ),
            ToolDefinition(
                name="define_entity",
                description="Define a business entity with its attributes",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Entity name"},
                        "code": {"type": "string", "description": "Entity code (snake_case)"},
                        "description": {"type": "string", "description": "Entity description"},
                        "attributes": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "description": {"type": "string"},
                                    "required": {"type": "boolean"}
                                }
                            },
                            "description": "Entity attributes"
                        }
                    },
                    "required": ["name", "code", "attributes"]
                }
            ),
            ToolDefinition(
                name="create_relationship",
                description="Create a relationship between two entities",
                parameters={
                    "type": "object",
                    "properties": {
                        "from_entity": {"type": "string", "description": "Source entity code"},
                        "to_entity": {"type": "string", "description": "Target entity code"},
                        "relationship_type": {
                            "type": "string",
                            "enum": ["one_to_one", "one_to_many", "many_to_many"],
                            "description": "Type of relationship"
                        },
                        "name": {"type": "string", "description": "Relationship name"}
                    },
                    "required": ["from_entity", "to_entity", "relationship_type"]
                }
            ),
            ToolDefinition(
                name="define_bounded_context",
                description="Define a DDD Bounded Context with its ubiquitous language and relationships",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Bounded context name"},
                        "subdomain_type": {
                            "type": "string",
                            "enum": ["core", "supporting", "generic"],
                            "description": "Type of subdomain: core (competitive advantage), supporting (necessary), generic (commodity)"
                        },
                        "description": {"type": "string", "description": "Context description and purpose"},
                        "ubiquitous_language": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "term": {"type": "string"},
                                    "definition": {"type": "string"}
                                }
                            },
                            "description": "Key terms and their meanings within this context"
                        },
                        "aggregates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Aggregate roots within this context"
                        }
                    },
                    "required": ["name", "subdomain_type", "description"]
                }
            ),
            ToolDefinition(
                name="design_aggregate",
                description="Design a DDD Aggregate with its root, entities, and value objects",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Aggregate name"},
                        "root_entity": {"type": "string", "description": "Aggregate root entity name"},
                        "bounded_context": {"type": "string", "description": "Parent bounded context"},
                        "entities": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "identity_field": {"type": "string"},
                                    "attributes": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Entities within the aggregate (have identity)"
                        },
                        "value_objects": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "attributes": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Value objects within the aggregate (no identity, immutable)"
                        },
                        "invariants": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Business rules that must always be true within this aggregate"
                        }
                    },
                    "required": ["name", "root_entity", "bounded_context"]
                }
            ),
            ToolDefinition(
                name="define_domain_event",
                description="Define a DDD Domain Event that captures something significant that happened",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Event name in past tense (e.g., OrderPlaced, PaymentReceived)"
                        },
                        "source_aggregate": {"type": "string", "description": "Aggregate that publishes this event"},
                        "bounded_context": {"type": "string", "description": "Context where event originates"},
                        "payload": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "field": {"type": "string"},
                                    "type": {"type": "string"}
                                }
                            },
                            "description": "Event payload fields"
                        },
                        "subscribers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Bounded contexts or aggregates that consume this event"
                        }
                    },
                    "required": ["name", "source_aggregate", "bounded_context"]
                }
            ),
            ToolDefinition(
                name="create_context_map",
                description="Create a DDD Context Map showing relationships between bounded contexts",
                parameters={
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Context map name"},
                        "contexts": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of bounded contexts in the map"
                        },
                        "relationships": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "upstream": {"type": "string", "description": "Upstream context"},
                                    "downstream": {"type": "string", "description": "Downstream context"},
                                    "pattern": {
                                        "type": "string",
                                        "enum": ["partnership", "shared_kernel", "customer_supplier", "conformist", "anticorruption_layer", "open_host_service", "published_language"],
                                        "description": "Integration pattern between contexts"
                                    },
                                    "description": {"type": "string"}
                                }
                            },
                            "description": "Relationships between contexts"
                        }
                    },
                    "required": ["name", "contexts", "relationships"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="request_entity_validation",
                description="Request Business Analyst to validate entity design against industry best practices",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entity names to validate"
                        },
                        "industry": {"type": "string", "description": "Industry context"},
                        "validation_aspects": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["naming", "attributes", "relationships", "kpi_alignment", "industry_standards"]},
                            "description": "Aspects to validate"
                        }
                    },
                    "required": ["entities"]
                }
            ),
            ToolDefinition(
                name="request_kpi_requirements",
                description="Request Business Analyst to identify KPIs for designed entities",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entities that need KPIs"
                        },
                        "value_chain": {"type": "string", "description": "Value chain context"},
                        "business_objectives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Business objectives to measure"
                        }
                    },
                    "required": ["entities"]
                }
            ),
            ToolDefinition(
                name="request_governance_review",
                description="Request Data Governance Specialist to review entity design for compliance",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entities to review"
                        },
                        "review_areas": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["data_quality", "metadata", "security", "privacy", "lineage", "standards"]},
                            "description": "Governance areas to review"
                        }
                    },
                    "required": ["entities"]
                }
            ),
            ToolDefinition(
                name="request_schema_generation",
                description="Request Developer to generate schemas from entity designs",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entities to generate schemas for"
                        },
                        "schema_types": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["pydantic", "timescaledb", "api", "event"]},
                            "description": "Types of schemas to generate"
                        }
                    },
                    "required": ["entities"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("design_value_chain", self._design_value_chain)
        self.register_tool("define_entity", self._define_entity)
        self.register_tool("create_relationship", self._create_relationship)
        self.register_tool("define_bounded_context", self._define_bounded_context)
        self.register_tool("design_aggregate", self._design_aggregate)
        self.register_tool("define_domain_event", self._define_domain_event)
        self.register_tool("create_context_map", self._create_context_map)
        # Collaboration tools
        self.register_tool("request_entity_validation", self._request_entity_validation)
        self.register_tool("request_kpi_requirements", self._request_kpi_requirements)
        self.register_tool("request_governance_review", self._request_governance_review)
        self.register_tool("request_schema_generation", self._request_schema_generation)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return ARCHITECT_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.identified_entities:
            parts.append(f"Known Entities: {', '.join(context.identified_entities)}")
        if context.value_chain_type:
            parts.append(f"Value Chain Type: {context.value_chain_type}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _design_value_chain(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Design a value chain structure."""
        name = tool_input.get("name", "")
        industry = tool_input.get("industry", "")
        processes = tool_input.get("processes", [])
        
        # Build value chain structure
        nodes = []
        links = []
        
        # Add value chain root node
        root_id = f"vc_{name.lower().replace(' ', '_')}"
        nodes.append({
            "id": root_id,
            "name": name,
            "type": "value_chain",
            "industry": industry
        })
        
        # Add processes and activities
        prev_process_id = None
        for process in processes:
            process_id = f"proc_{process['name'].lower().replace(' ', '_')}"
            nodes.append({
                "id": process_id,
                "name": process["name"],
                "type": "process",
                "description": process.get("description", "")
            })
            
            # Link to root
            links.append({
                "source": root_id,
                "target": process_id,
                "type": "contains"
            })
            
            # Link to previous process (flow)
            if prev_process_id:
                links.append({
                    "source": prev_process_id,
                    "target": process_id,
                    "type": "flows_to"
                })
            prev_process_id = process_id
            
            # Add activities
            for activity in process.get("activities", []):
                activity_id = f"act_{activity.lower().replace(' ', '_')}"
                nodes.append({
                    "id": activity_id,
                    "name": activity,
                    "type": "activity"
                })
                links.append({
                    "source": process_id,
                    "target": activity_id,
                    "type": "contains"
                })
        
        # Update context
        context.value_chain_type = name
        
        return {
            "success": True,
            "value_chain": {
                "name": name,
                "industry": industry,
                "nodes": nodes,
                "links": links
            }
        }
    
    async def _define_entity(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Define a business entity."""
        name = tool_input.get("name", "")
        code = tool_input.get("code", "")
        description = tool_input.get("description", "")
        attributes = tool_input.get("attributes", [])
        
        entity = {
            "name": name,
            "code": code,
            "description": description,
            "kind": "entity_definition",
            "attributes": attributes,
            "table_schema": {
                "table_name": code,
                "columns": []
            }
        }
        
        # Generate column definitions
        for attr in attributes:
            column = {
                "name": attr["name"],
                "type": self._map_type_to_sql(attr.get("type", "string")),
                "nullable": not attr.get("required", False)
            }
            entity["table_schema"]["columns"].append(column)
        
        # Update context
        if code not in context.identified_entities:
            context.identified_entities.append(code)
        
        return {
            "success": True,
            "entity": entity
        }
    
    def _map_type_to_sql(self, type_name: str) -> str:
        """Map abstract types to SQL types."""
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
        return type_map.get(type_name.lower(), "VARCHAR(255)")
    
    async def _create_relationship(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create a relationship between entities."""
        from_entity = tool_input.get("from_entity", "")
        to_entity = tool_input.get("to_entity", "")
        rel_type = tool_input.get("relationship_type", "one_to_many")
        name = tool_input.get("name", f"{from_entity}_to_{to_entity}")
        
        # Map cardinalities
        cardinality_map = {
            "one_to_one": ("1", "1"),
            "one_to_many": ("1", "*"),
            "many_to_many": ("*", "*")
        }
        from_card, to_card = cardinality_map.get(rel_type, ("1", "*"))
        
        relationship = {
            "name": name,
            "from_entity": from_entity,
            "to_entity": to_entity,
            "relationship_type": rel_type,
            "from_cardinality": from_card,
            "to_cardinality": to_card
        }
        
        return {
            "success": True,
            "relationship": relationship
        }
    
    async def _define_bounded_context(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Define a DDD Bounded Context."""
        name = tool_input.get("name", "")
        subdomain_type = tool_input.get("subdomain_type", "supporting")
        description = tool_input.get("description", "")
        ubiquitous_language = tool_input.get("ubiquitous_language", [])
        aggregates = tool_input.get("aggregates", [])
        
        bounded_context = {
            "name": name,
            "subdomain_type": subdomain_type,
            "description": description,
            "ubiquitous_language": ubiquitous_language,
            "aggregates": aggregates,
            "ddd_pattern": "bounded_context"
        }
        
        # Store in context artifacts
        if "bounded_contexts" not in context.artifacts:
            context.artifacts["bounded_contexts"] = []
        context.artifacts["bounded_contexts"].append(bounded_context)
        
        return {
            "success": True,
            "bounded_context": bounded_context,
            "subdomain_investment_guidance": {
                "core": "Invest heavily - this is your competitive advantage",
                "supporting": "Build in-house but don't over-engineer",
                "generic": "Consider buying or outsourcing"
            }.get(subdomain_type, "")
        }
    
    async def _design_aggregate(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Design a DDD Aggregate."""
        name = tool_input.get("name", "")
        root_entity = tool_input.get("root_entity", "")
        bounded_context = tool_input.get("bounded_context", "")
        entities = tool_input.get("entities", [])
        value_objects = tool_input.get("value_objects", [])
        invariants = tool_input.get("invariants", [])
        
        aggregate = {
            "name": name,
            "root_entity": root_entity,
            "bounded_context": bounded_context,
            "entities": entities,
            "value_objects": value_objects,
            "invariants": invariants,
            "ddd_pattern": "aggregate",
            "design_rules": [
                "External references only to the aggregate root",
                "Transactional consistency within aggregate boundary",
                "Eventual consistency between aggregates",
                "One repository per aggregate root"
            ]
        }
        
        # Store in context artifacts
        if "aggregates" not in context.artifacts:
            context.artifacts["aggregates"] = []
        context.artifacts["aggregates"].append(aggregate)
        
        return {
            "success": True,
            "aggregate": aggregate
        }
    
    async def _define_domain_event(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Define a DDD Domain Event."""
        name = tool_input.get("name", "")
        source_aggregate = tool_input.get("source_aggregate", "")
        bounded_context = tool_input.get("bounded_context", "")
        payload = tool_input.get("payload", [])
        subscribers = tool_input.get("subscribers", [])
        
        domain_event = {
            "name": name,
            "source_aggregate": source_aggregate,
            "bounded_context": bounded_context,
            "payload": payload,
            "subscribers": subscribers,
            "ddd_pattern": "domain_event",
            "characteristics": [
                "Immutable - represents a fact that happened",
                "Named in past tense",
                "Contains all data needed by subscribers",
                "Enables loose coupling between contexts"
            ]
        }
        
        # Store in context artifacts
        if "domain_events" not in context.artifacts:
            context.artifacts["domain_events"] = []
        context.artifacts["domain_events"].append(domain_event)
        
        return {
            "success": True,
            "domain_event": domain_event
        }
    
    async def _create_context_map(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create a DDD Context Map."""
        name = tool_input.get("name", "")
        contexts = tool_input.get("contexts", [])
        relationships = tool_input.get("relationships", [])
        
        # Add pattern descriptions
        pattern_descriptions = {
            "partnership": "Teams in two contexts succeed or fail together",
            "shared_kernel": "Shared subset of the domain model",
            "customer_supplier": "Upstream supplies what downstream needs",
            "conformist": "Downstream conforms to upstream model",
            "anticorruption_layer": "Translation layer protects downstream model",
            "open_host_service": "Protocol for accessing context as a service",
            "published_language": "Well-documented shared language for integration"
        }
        
        # Enrich relationships with descriptions
        enriched_relationships = []
        for rel in relationships:
            enriched = rel.copy()
            pattern = rel.get("pattern", "")
            enriched["pattern_description"] = pattern_descriptions.get(pattern, "")
            enriched_relationships.append(enriched)
        
        context_map = {
            "name": name,
            "contexts": contexts,
            "relationships": enriched_relationships,
            "ddd_pattern": "context_map"
        }
        
        # Store in context artifacts
        context.artifacts["context_map"] = context_map
        
        return {
            "success": True,
            "context_map": context_map
        }
    
    # Collaboration Tool Handlers
    async def _request_entity_validation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Business Analyst to validate entity design."""
        request = {
            "id": f"ENTITY-VAL-{context.session_id[:8] if context.session_id else 'REQ'}",
            "entities": tool_input.get("entities", []),
            "industry": tool_input.get("industry", context.industry or ""),
            "validation_aspects": tool_input.get("validation_aspects", ["naming", "attributes", "industry_standards"]),
            "status": "pending_business_analyst",
            "collaboration_type": "architect_to_business_analyst"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Business Analyst will validate entities against industry best practices"}
    
    async def _request_kpi_requirements(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Business Analyst to identify KPIs for entities."""
        request = {
            "id": f"KPI-REQ-{context.session_id[:8] if context.session_id else 'REQ'}",
            "entities": tool_input.get("entities", []),
            "value_chain": tool_input.get("value_chain", ""),
            "business_objectives": tool_input.get("business_objectives", []),
            "status": "pending_business_analyst",
            "collaboration_type": "architect_to_business_analyst"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Business Analyst will identify relevant KPIs for the entities"}
    
    async def _request_governance_review(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Governance Specialist to review entity design."""
        request = {
            "id": f"GOV-REV-{context.session_id[:8] if context.session_id else 'REQ'}",
            "entities": tool_input.get("entities", []),
            "review_areas": tool_input.get("review_areas", ["data_quality", "metadata", "standards"]),
            "status": "pending_data_governance",
            "collaboration_type": "architect_to_data_governance"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Data Governance Specialist will review for compliance"}
    
    async def _request_schema_generation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Developer to generate schemas from entity designs."""
        request = {
            "id": f"SCHEMA-GEN-{context.session_id[:8] if context.session_id else 'REQ'}",
            "entities": tool_input.get("entities", []),
            "schema_types": tool_input.get("schema_types", ["pydantic", "timescaledb"]),
            "status": "pending_developer",
            "collaboration_type": "architect_to_developer"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Developer will generate schemas from entity designs"}


# =============================================================================
# BUSINESS ANALYST AGENT
# =============================================================================

ANALYST_SYSTEM_PROMPT = """You are the Business Analyst Agent, an expert with deep knowledge across all industries and business domains.

Your role is to provide industry-specific expertise, identify relevant KPIs, and recommend best practices for business analytics.

## Your Expertise

You have comprehensive knowledge of:
- All major industries (Healthcare, Manufacturing, Retail, Finance, etc.)
- Industry standard frameworks (SCOR, APICS, HL7, etc.)
- Key Performance Indicators for any domain
- Business process best practices
- Industry benchmarks and standards

## Your Responsibilities

1. **Industry Analysis**: Provide deep expertise for any industry
2. **KPI Identification**: Identify relevant metrics and KPIs
3. **Best Practices**: Recommend industry best practices
4. **Framework Mapping**: Map processes to standard frameworks
5. **Benchmarking**: Provide industry benchmarks

## Output Format

When analyzing, provide:
- Industry-specific insights
- Recommended KPIs with formulas
- Best practice recommendations
- Framework alignment suggestions
- Benchmark data where applicable

## Current Context

{context_summary}

Adapt your expertise to match the client's industry and provide actionable, specific recommendations.
"""


class BusinessAnalystAgent(BaseAgent):
    """Business Analyst Agent for industry expertise and KPI identification."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.BUSINESS_ANALYST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.5,
            tools=self._get_analyst_tools()
        )
        super().__init__(config, api_key)
    
    def _get_analyst_tools(self) -> List[ToolDefinition]:
        """Define tools available to the analyst."""
        return [
            ToolDefinition(
                name="identify_kpis",
                description="Identify relevant KPIs for a business domain",
                parameters={
                    "type": "object",
                    "properties": {
                        "domain": {"type": "string", "description": "Business domain"},
                        "industry": {"type": "string", "description": "Industry context"},
                        "focus_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific areas to focus on"
                        }
                    },
                    "required": ["domain"]
                }
            ),
            ToolDefinition(
                name="get_industry_benchmarks",
                description="Get industry benchmarks for specific metrics",
                parameters={
                    "type": "object",
                    "properties": {
                        "industry": {"type": "string", "description": "Target industry"},
                        "metrics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Metrics to benchmark"
                        }
                    },
                    "required": ["industry", "metrics"]
                }
            ),
            ToolDefinition(
                name="map_to_framework",
                description="Map business processes to a standard framework",
                parameters={
                    "type": "object",
                    "properties": {
                        "framework": {
                            "type": "string",
                            "enum": ["SCOR", "APICS", "HL7", "ISO", "ITIL", "Custom"],
                            "description": "Target framework"
                        },
                        "processes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Processes to map"
                        }
                    },
                    "required": ["framework", "processes"]
                }
            ),
            ToolDefinition(
                name="recommend_improvements",
                description="Recommend strategic improvements",
                parameters={
                    "type": "object",
                    "properties": {
                        "current_state": {"type": "string", "description": "Current state description"},
                        "goals": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Business goals"
                        }
                    },
                    "required": ["current_state"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="request_kpi_calculation_design",
                description="Request Data Analyst to design calculation logic for identified KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpis": {"type": "array", "items": {"type": "string"}, "description": "KPIs needing calculation design"},
                        "data_sources": {"type": "array", "items": {"type": "string"}, "description": "Available data sources"},
                        "calculation_requirements": {"type": "array", "items": {"type": "string"}, "description": "Special calculation requirements"}
                    },
                    "required": ["kpis"]
                }
            ),
            ToolDefinition(
                name="request_predictive_analysis",
                description="Request Data Scientist to analyze KPIs for predictive opportunities",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpis": {"type": "array", "items": {"type": "string"}, "description": "KPIs to analyze"},
                        "prediction_goals": {"type": "array", "items": {"type": "string"}, "description": "What to predict"},
                        "business_context": {"type": "string", "description": "Business context for predictions"}
                    },
                    "required": ["kpis"]
                }
            ),
            ToolDefinition(
                name="share_entity_validation",
                description="Share entity validation results back to Architect",
                parameters={
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Original request ID"},
                        "validation_results": {"type": "array", "items": {"type": "object"}, "description": "Validation results per entity"},
                        "recommendations": {"type": "array", "items": {"type": "string"}, "description": "Improvement recommendations"}
                    },
                    "required": ["request_id", "validation_results"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("identify_kpis", self._identify_kpis)
        self.register_tool("get_industry_benchmarks", self._get_industry_benchmarks)
        self.register_tool("map_to_framework", self._map_to_framework)
        self.register_tool("recommend_improvements", self._recommend_improvements)
        # Collaboration tools
        self.register_tool("request_kpi_calculation_design", self._request_kpi_calculation_design)
        self.register_tool("request_predictive_analysis", self._request_predictive_analysis)
        self.register_tool("share_entity_validation", self._share_entity_validation)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return ANALYST_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}")
        if context.identified_kpis:
            parts.append(f"Known KPIs: {', '.join(context.identified_kpis)}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _identify_kpis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Identify relevant KPIs for a domain."""
        domain = tool_input.get("domain", "").lower()
        industry = tool_input.get("industry", "")
        focus_areas = tool_input.get("focus_areas", [])
        
        # Domain-specific KPI templates
        kpi_templates = {
            "supply_chain": [
                {"name": "Order Fulfillment Rate", "formula": "(Orders Fulfilled / Total Orders) * 100", "unit": "%"},
                {"name": "Inventory Turnover", "formula": "Cost of Goods Sold / Average Inventory", "unit": "ratio"},
                {"name": "Perfect Order Rate", "formula": "(Perfect Orders / Total Orders) * 100", "unit": "%"},
                {"name": "Cash-to-Cash Cycle Time", "formula": "DIO + DSO - DPO", "unit": "days"},
                {"name": "Supply Chain Cost", "formula": "Total SC Cost / Revenue", "unit": "%"}
            ],
            "sales": [
                {"name": "Revenue", "formula": "SUM(Order.Amount)", "unit": "currency"},
                {"name": "Conversion Rate", "formula": "(Conversions / Leads) * 100", "unit": "%"},
                {"name": "Average Deal Size", "formula": "Total Revenue / Number of Deals", "unit": "currency"},
                {"name": "Sales Cycle Length", "formula": "AVG(Close Date - Create Date)", "unit": "days"},
                {"name": "Win Rate", "formula": "(Won Deals / Total Deals) * 100", "unit": "%"}
            ],
            "finance": [
                {"name": "Gross Margin", "formula": "(Revenue - COGS) / Revenue * 100", "unit": "%"},
                {"name": "Operating Margin", "formula": "Operating Income / Revenue * 100", "unit": "%"},
                {"name": "Return on Assets", "formula": "Net Income / Total Assets * 100", "unit": "%"},
                {"name": "Current Ratio", "formula": "Current Assets / Current Liabilities", "unit": "ratio"},
                {"name": "Days Sales Outstanding", "formula": "(Accounts Receivable / Revenue) * 365", "unit": "days"}
            ],
            "operations": [
                {"name": "Overall Equipment Effectiveness", "formula": "Availability * Performance * Quality", "unit": "%"},
                {"name": "Throughput", "formula": "Units Produced / Time Period", "unit": "units/time"},
                {"name": "Cycle Time", "formula": "End Time - Start Time", "unit": "time"},
                {"name": "First Pass Yield", "formula": "(Good Units / Total Units) * 100", "unit": "%"},
                {"name": "Capacity Utilization", "formula": "(Actual Output / Max Output) * 100", "unit": "%"}
            ],
            "customer_service": [
                {"name": "Customer Satisfaction Score", "formula": "AVG(Survey Responses)", "unit": "score"},
                {"name": "Net Promoter Score", "formula": "% Promoters - % Detractors", "unit": "score"},
                {"name": "First Contact Resolution", "formula": "(Resolved First Contact / Total) * 100", "unit": "%"},
                {"name": "Average Handle Time", "formula": "Total Handle Time / Number of Contacts", "unit": "time"},
                {"name": "Customer Effort Score", "formula": "AVG(Effort Ratings)", "unit": "score"}
            ]
        }
        
        # Get KPIs for domain
        kpis = kpi_templates.get(domain, [])
        
        # If no specific domain, provide general KPIs
        if not kpis:
            kpis = [
                {"name": "Revenue Growth", "formula": "(Current Revenue - Previous Revenue) / Previous Revenue * 100", "unit": "%"},
                {"name": "Cost Efficiency", "formula": "Total Cost / Revenue", "unit": "ratio"},
                {"name": "Customer Retention", "formula": "(End Customers - New Customers) / Start Customers * 100", "unit": "%"}
            ]
        
        # Update context
        for kpi in kpis:
            if kpi["name"] not in context.identified_kpis:
                context.identified_kpis.append(kpi["name"])
        
        return {
            "success": True,
            "domain": domain,
            "industry": industry,
            "kpis": kpis
        }
    
    async def _get_industry_benchmarks(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Get industry benchmarks."""
        industry = tool_input.get("industry", "")
        metrics = tool_input.get("metrics", [])
        
        # Simulated benchmark data
        benchmarks = {}
        for metric in metrics:
            benchmarks[metric] = {
                "industry_average": "Varies by industry",
                "top_quartile": "Top 25% performers",
                "bottom_quartile": "Bottom 25% performers",
                "note": f"Benchmark data for {metric} in {industry} industry"
            }
        
        return {
            "success": True,
            "industry": industry,
            "benchmarks": benchmarks
        }
    
    async def _map_to_framework(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Map processes to a standard framework."""
        framework = tool_input.get("framework", "")
        processes = tool_input.get("processes", [])
        
        # Framework mappings
        framework_mappings = {
            "SCOR": {
                "levels": ["Plan", "Source", "Make", "Deliver", "Return", "Enable"],
                "description": "Supply Chain Operations Reference model"
            },
            "APICS": {
                "levels": ["Strategic", "Tactical", "Operational"],
                "description": "APICS Supply Chain Management framework"
            },
            "ITIL": {
                "levels": ["Service Strategy", "Service Design", "Service Transition", "Service Operation", "Continual Improvement"],
                "description": "IT Infrastructure Library framework"
            }
        }
        
        framework_info = framework_mappings.get(framework, {"levels": [], "description": "Custom framework"})
        
        mappings = []
        for process in processes:
            mappings.append({
                "process": process,
                "framework": framework,
                "suggested_level": framework_info["levels"][0] if framework_info["levels"] else "Custom",
                "notes": f"Map {process} to appropriate {framework} level"
            })
        
        return {
            "success": True,
            "framework": framework,
            "framework_description": framework_info["description"],
            "mappings": mappings
        }
    
    async def _recommend_improvements(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Recommend strategic improvements."""
        current_state = tool_input.get("current_state", "")
        goals = tool_input.get("goals", [])
        
        recommendations = [
            {
                "category": "Process Optimization",
                "recommendation": "Identify and eliminate bottlenecks in core processes",
                "priority": "High",
                "expected_impact": "Improved efficiency and reduced cycle times"
            },
            {
                "category": "Data Quality",
                "recommendation": "Implement data validation and cleansing procedures",
                "priority": "Medium",
                "expected_impact": "More accurate analytics and reporting"
            },
            {
                "category": "Automation",
                "recommendation": "Automate repetitive manual tasks",
                "priority": "Medium",
                "expected_impact": "Reduced errors and improved productivity"
            }
        ]
        
        return {
            "success": True,
            "current_state_summary": current_state[:200],
            "goals": goals,
            "recommendations": recommendations
        }
    
    # Collaboration Tool Handlers
    async def _request_kpi_calculation_design(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Analyst to design KPI calculation logic."""
        request = {
            "id": f"CALC-DES-{context.session_id[:8] if context.session_id else 'REQ'}",
            "kpis": tool_input.get("kpis", []),
            "data_sources": tool_input.get("data_sources", []),
            "calculation_requirements": tool_input.get("calculation_requirements", []),
            "status": "pending_data_analyst",
            "collaboration_type": "business_analyst_to_data_analyst"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Data Analyst will design calculation logic for KPIs"}
    
    async def _request_predictive_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Scientist to analyze KPIs for predictions."""
        request = {
            "id": f"PRED-REQ-{context.session_id[:8] if context.session_id else 'REQ'}",
            "kpis": tool_input.get("kpis", []),
            "prediction_goals": tool_input.get("prediction_goals", []),
            "business_context": tool_input.get("business_context", ""),
            "status": "pending_data_scientist",
            "collaboration_type": "business_analyst_to_data_scientist"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Data Scientist will analyze predictive opportunities"}
    
    async def _share_entity_validation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Share entity validation results back to Architect."""
        response = {
            "id": f"VAL-RESP-{context.session_id[:8] if context.session_id else 'RESP'}",
            "request_id": tool_input.get("request_id", ""),
            "validation_results": tool_input.get("validation_results", []),
            "recommendations": tool_input.get("recommendations", []),
            "status": "completed",
            "collaboration_type": "business_analyst_to_architect"
        }
        if "collaboration_responses" not in context.artifacts:
            context.artifacts["collaboration_responses"] = []
        context.artifacts["collaboration_responses"].append(response)
        return {"success": True, "response": response, "next_step": "Architect will incorporate validation feedback"}


# =============================================================================
# DEVELOPER AGENT
# =============================================================================

DEVELOPER_SYSTEM_PROMPT = """You are the Developer Agent, an expert in code generation and technical implementation.

Your role is to generate high-quality code artifacts including database schemas, Pydantic models, API specifications, and calculation formulas.

## Your Expertise

- Python and Pydantic v2 models
- TimescaleDB and PostgreSQL schemas
- FastAPI and OpenAPI specifications
- SQL and calculation formulas
- Data transformation logic

## Your Responsibilities

1. **Generate Schemas**: Create TimescaleDB DDL statements
2. **Create Models**: Generate Pydantic v2 model definitions
3. **Build Formulas**: Create KPI calculation formulas
4. **API Specs**: Generate OpenAPI specifications
5. **Transformations**: Create data transformation logic

## Output Format

When generating code:
- Use proper Python syntax and conventions
- Follow Pydantic v2 patterns
- Include appropriate comments
- Ensure code is immediately runnable

## Current Context

{context_summary}

Generate clean, efficient, and well-documented code that follows best practices.
"""


class DeveloperAgent(BaseAgent):
    """Developer Agent for code and schema generation."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.DEVELOPER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.2,
            tools=self._get_developer_tools()
        )
        super().__init__(config, api_key)
    
    def _get_developer_tools(self) -> List[ToolDefinition]:
        """Define tools available to the developer."""
        return [
            ToolDefinition(
                name="generate_schema",
                description="Generate TimescaleDB DDL schema",
                parameters={
                    "type": "object",
                    "properties": {
                        "table_name": {"type": "string", "description": "Table name"},
                        "columns": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "nullable": {"type": "boolean"},
                                    "primary_key": {"type": "boolean"}
                                }
                            },
                            "description": "Column definitions"
                        },
                        "is_hypertable": {"type": "boolean", "description": "Create as hypertable"},
                        "time_column": {"type": "string", "description": "Time column for hypertable"}
                    },
                    "required": ["table_name", "columns"]
                }
            ),
            ToolDefinition(
                name="create_pydantic_model",
                description="Generate Pydantic v2 model",
                parameters={
                    "type": "object",
                    "properties": {
                        "class_name": {"type": "string", "description": "Model class name"},
                        "fields": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "required": {"type": "boolean"},
                                    "description": {"type": "string"}
                                }
                            },
                            "description": "Field definitions"
                        }
                    },
                    "required": ["class_name", "fields"]
                }
            ),
            ToolDefinition(
                name="build_kpi_formula",
                description="Build a KPI calculation formula",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_name": {"type": "string", "description": "KPI name"},
                        "formula": {"type": "string", "description": "Natural language formula"},
                        "required_entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Required entity references"
                        }
                    },
                    "required": ["kpi_name", "formula"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="request_test_specification",
                description="Request Tester to create test specifications for generated code",
                parameters={
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string", "enum": ["schema", "model", "formula", "api"], "description": "Type of artifact to test"},
                        "artifact_name": {"type": "string", "description": "Name of the artifact"},
                        "test_requirements": {"type": "array", "items": {"type": "string"}, "description": "Specific test requirements"}
                    },
                    "required": ["artifact_type", "artifact_name"]
                }
            ),
            ToolDefinition(
                name="request_documentation",
                description="Request Documenter to create documentation for generated code",
                parameters={
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string", "enum": ["schema", "model", "formula", "api"], "description": "Type of artifact"},
                        "artifact_name": {"type": "string", "description": "Name of the artifact"},
                        "doc_types": {"type": "array", "items": {"type": "string", "enum": ["api_docs", "data_dictionary", "user_guide", "technical_spec"]}, "description": "Types of documentation needed"}
                    },
                    "required": ["artifact_type", "artifact_name"]
                }
            ),
            ToolDefinition(
                name="request_deployment_config",
                description="Request Deployment Specialist to create deployment configuration",
                parameters={
                    "type": "object",
                    "properties": {
                        "artifacts": {"type": "array", "items": {"type": "string"}, "description": "Artifacts to deploy"},
                        "environment": {"type": "string", "enum": ["dev", "staging", "prod"], "description": "Target environment"},
                        "deployment_requirements": {"type": "array", "items": {"type": "string"}, "description": "Special deployment requirements"}
                    },
                    "required": ["artifacts"]
                }
            ),
            ToolDefinition(
                name="share_schema_artifacts",
                description="Share generated schema artifacts back to Architect",
                parameters={
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Original request ID"},
                        "schemas": {"type": "array", "items": {"type": "object"}, "description": "Generated schemas"},
                        "notes": {"type": "array", "items": {"type": "string"}, "description": "Implementation notes"}
                    },
                    "required": ["request_id", "schemas"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("generate_schema", self._generate_schema)
        self.register_tool("create_pydantic_model", self._create_pydantic_model)
        self.register_tool("build_kpi_formula", self._build_kpi_formula)
        # Collaboration tools
        self.register_tool("request_test_specification", self._request_test_specification)
        self.register_tool("request_documentation", self._request_documentation)
        self.register_tool("request_deployment_config", self._request_deployment_config)
        self.register_tool("share_schema_artifacts", self._share_schema_artifacts)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return DEVELOPER_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.identified_entities:
            parts.append(f"Entities: {', '.join(context.identified_entities)}")
        if context.identified_kpis:
            parts.append(f"KPIs: {', '.join(context.identified_kpis)}")
        if context.artifacts:
            parts.append(f"Existing Artifacts: {', '.join(context.artifacts.keys())}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _generate_schema(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate TimescaleDB DDL schema."""
        table_name = tool_input.get("table_name", "")
        columns = tool_input.get("columns", [])
        is_hypertable = tool_input.get("is_hypertable", False)
        time_column = tool_input.get("time_column", "created_at")
        
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
        
        # Add hypertable creation if needed
        if is_hypertable:
            ddl += f"\n\nSELECT create_hypertable('{table_name}', '{time_column}');"
        
        # Store in context
        context.artifacts[f"schema_{table_name}"] = ddl
        
        return {
            "success": True,
            "table_name": table_name,
            "ddl": ddl,
            "is_hypertable": is_hypertable
        }
    
    async def _create_pydantic_model(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate Pydantic v2 model."""
        class_name = tool_input.get("class_name", "")
        fields = tool_input.get("fields", [])
        
        # Type mapping
        type_map = {
            "string": "str",
            "integer": "int",
            "decimal": "Decimal",
            "boolean": "bool",
            "date": "date",
            "datetime": "datetime",
            "uuid": "UUID",
            "json": "Dict[str, Any]",
            "list": "List[Any]"
        }
        
        # Build model code
        imports = [
            "from __future__ import annotations",
            "from datetime import date, datetime",
            "from decimal import Decimal",
            "from typing import Any, Dict, List, Optional",
            "from uuid import UUID",
            "from pydantic import BaseModel, Field"
        ]
        
        model_lines = [f"\n\nclass {class_name}(BaseModel):"]
        model_lines.append(f'    """Generated model for {class_name}."""')
        
        for field in fields:
            field_name = field["name"]
            field_type = type_map.get(field.get("type", "string"), "str")
            required = field.get("required", True)
            description = field.get("description", "")
            
            if not required:
                field_type = f"Optional[{field_type}]"
                default = " = None"
            else:
                default = ""
            
            if description:
                model_lines.append(f'    {field_name}: {field_type}{default}  # {description}')
            else:
                model_lines.append(f'    {field_name}: {field_type}{default}')
        
        model_code = "\n".join(imports) + "\n".join(model_lines)
        
        # Store in context
        context.artifacts[f"model_{class_name}"] = model_code
        
        return {
            "success": True,
            "class_name": class_name,
            "code": model_code
        }
    
    async def _build_kpi_formula(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Build a KPI calculation formula."""
        kpi_name = tool_input.get("kpi_name", "")
        formula = tool_input.get("formula", "")
        required_entities = tool_input.get("required_entities", [])
        
        # Generate KPI definition
        kpi_code = kpi_name.lower().replace(" ", "_")
        
        kpi_definition = {
            "name": kpi_name,
            "code": kpi_code,
            "kind": "metric_definition",
            "formula": formula,
            "required_objects": required_entities,
            "data_type": "decimal",
            "unit": "auto"
        }
        
        # Store in context
        context.artifacts[f"kpi_{kpi_code}"] = kpi_definition
        if kpi_name not in context.identified_kpis:
            context.identified_kpis.append(kpi_name)
        
        return {
            "success": True,
            "kpi": kpi_definition
        }
    
    # Collaboration Tool Handlers
    async def _request_test_specification(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Tester to create test specifications."""
        request = {
            "id": f"TEST-SPEC-{context.session_id[:8] if context.session_id else 'REQ'}",
            "artifact_type": tool_input.get("artifact_type", ""),
            "artifact_name": tool_input.get("artifact_name", ""),
            "test_requirements": tool_input.get("test_requirements", []),
            "status": "pending_tester",
            "collaboration_type": "developer_to_tester"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Tester will create test specifications"}
    
    async def _request_documentation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Documenter to create documentation."""
        request = {
            "id": f"DOC-REQ-{context.session_id[:8] if context.session_id else 'REQ'}",
            "artifact_type": tool_input.get("artifact_type", ""),
            "artifact_name": tool_input.get("artifact_name", ""),
            "doc_types": tool_input.get("doc_types", ["technical_spec"]),
            "status": "pending_documenter",
            "collaboration_type": "developer_to_documenter"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Documenter will create documentation"}
    
    async def _request_deployment_config(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Deployment Specialist to create deployment config."""
        request = {
            "id": f"DEPLOY-CFG-{context.session_id[:8] if context.session_id else 'REQ'}",
            "artifacts": tool_input.get("artifacts", []),
            "environment": tool_input.get("environment", "dev"),
            "deployment_requirements": tool_input.get("deployment_requirements", []),
            "status": "pending_deployment_specialist",
            "collaboration_type": "developer_to_deployment_specialist"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Deployment Specialist will create configuration"}
    
    async def _share_schema_artifacts(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Share generated schema artifacts back to Architect."""
        response = {
            "id": f"SCHEMA-RESP-{context.session_id[:8] if context.session_id else 'RESP'}",
            "request_id": tool_input.get("request_id", ""),
            "schemas": tool_input.get("schemas", []),
            "notes": tool_input.get("notes", []),
            "status": "completed",
            "collaboration_type": "developer_to_architect"
        }
        if "collaboration_responses" not in context.artifacts:
            context.artifacts["collaboration_responses"] = []
        context.artifacts["collaboration_responses"].append(response)
        return {"success": True, "response": response, "next_step": "Architect will review generated schemas"}


# =============================================================================
# TESTER AGENT
# =============================================================================

TESTER_SYSTEM_PROMPT = """You are the Tester Agent, an expert in quality assurance and validation.

Your role is to validate schemas, test formulas, verify relationships, and ensure the quality of all generated artifacts.

## Your Expertise

- Schema validation and integrity checking
- Formula correctness verification
- Relationship consistency validation
- Data quality assessment
- Test case generation

## Your Responsibilities

1. **Validate Schemas**: Check schema integrity and consistency
2. **Test Formulas**: Verify KPI calculation correctness
3. **Verify Relationships**: Ensure relationship consistency
4. **Quality Checks**: Perform data quality assessments
5. **Generate Tests**: Create test cases for validation

## Output Format

When validating:
- List all checks performed
- Report any issues found
- Provide recommendations for fixes
- Generate test cases where applicable

## Current Context

{context_summary}

Ensure all artifacts meet quality standards before deployment.
"""


class TesterAgent(BaseAgent):
    """Tester Agent for validation and quality assurance."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.TESTER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.2,
            tools=self._get_tester_tools()
        )
        super().__init__(config, api_key)
    
    def _get_tester_tools(self) -> List[ToolDefinition]:
        """Define tools available to the tester."""
        return [
            ToolDefinition(
                name="validate_schema",
                description="Validate a database schema",
                parameters={
                    "type": "object",
                    "properties": {
                        "schema_name": {"type": "string", "description": "Schema to validate"},
                        "ddl": {"type": "string", "description": "DDL to validate"}
                    },
                    "required": ["schema_name"]
                }
            ),
            ToolDefinition(
                name="test_formula",
                description="Test a KPI formula",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_name": {"type": "string", "description": "KPI to test"},
                        "formula": {"type": "string", "description": "Formula to test"},
                        "test_data": {"type": "object", "description": "Test data"}
                    },
                    "required": ["kpi_name", "formula"]
                }
            ),
            ToolDefinition(
                name="verify_relationships",
                description="Verify relationship consistency",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entities to verify"
                        },
                        "relationships": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "Relationships to verify"
                        }
                    },
                    "required": ["entities"]
                }
            ),
            ToolDefinition(
                name="generate_test_cases",
                description="Generate test cases",
                parameters={
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string", "description": "Type of artifact"},
                        "artifact_name": {"type": "string", "description": "Name of artifact"}
                    },
                    "required": ["artifact_type", "artifact_name"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="report_test_results",
                description="Report test results back to Developer",
                parameters={
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Original request ID"},
                        "test_results": {"type": "array", "items": {"type": "object"}, "description": "Test results"},
                        "issues_found": {"type": "array", "items": {"type": "string"}, "description": "Issues found"},
                        "recommendations": {"type": "array", "items": {"type": "string"}, "description": "Fix recommendations"}
                    },
                    "required": ["request_id", "test_results"]
                }
            ),
            ToolDefinition(
                name="request_test_documentation",
                description="Request Documenter to create test documentation",
                parameters={
                    "type": "object",
                    "properties": {
                        "test_suite": {"type": "string", "description": "Test suite name"},
                        "test_cases": {"type": "array", "items": {"type": "object"}, "description": "Test cases to document"}
                    },
                    "required": ["test_suite"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("validate_schema", self._validate_schema)
        self.register_tool("test_formula", self._test_formula)
        self.register_tool("verify_relationships", self._verify_relationships)
        self.register_tool("generate_test_cases", self._generate_test_cases)
        # Collaboration tools
        self.register_tool("report_test_results", self._report_test_results)
        self.register_tool("request_test_documentation", self._request_test_documentation)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return TESTER_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.artifacts:
            parts.append(f"Artifacts to validate: {', '.join(context.artifacts.keys())}")
        return "\n".join(parts) if parts else "No artifacts to validate yet."
    
    async def _validate_schema(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Validate a database schema."""
        schema_name = tool_input.get("schema_name", "")
        ddl = tool_input.get("ddl", "")
        
        # Get DDL from context if not provided
        if not ddl and f"schema_{schema_name}" in context.artifacts:
            ddl = context.artifacts[f"schema_{schema_name}"]
        
        issues = []
        checks = []
        
        # Basic validation checks
        checks.append({"check": "DDL syntax", "status": "passed" if ddl else "failed"})
        
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
        
        return {
            "success": len(issues) == 0,
            "schema_name": schema_name,
            "checks": checks,
            "issues": issues,
            "recommendation": "Schema is valid" if not issues else "Fix identified issues"
        }
    
    async def _test_formula(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Test a KPI formula."""
        kpi_name = tool_input.get("kpi_name", "")
        formula = tool_input.get("formula", "")
        test_data = tool_input.get("test_data", {})
        
        checks = []
        issues = []
        
        # Formula validation
        if formula:
            checks.append({"check": "Formula present", "status": "passed"})
            
            # Check for common issues
            if "/" in formula and "0" not in formula.lower():
                checks.append({"check": "Division safety", "status": "warning"})
                issues.append("Consider adding division by zero protection")
            else:
                checks.append({"check": "Division safety", "status": "passed"})
        else:
            checks.append({"check": "Formula present", "status": "failed"})
            issues.append("No formula provided")
        
        return {
            "success": len([i for i in issues if "failed" in str(i)]) == 0,
            "kpi_name": kpi_name,
            "formula": formula,
            "checks": checks,
            "issues": issues
        }
    
    async def _verify_relationships(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Verify relationship consistency."""
        entities = tool_input.get("entities", [])
        relationships = tool_input.get("relationships", [])
        
        checks = []
        issues = []
        
        # Check all relationship endpoints exist
        for rel in relationships:
            from_entity = rel.get("from_entity", "")
            to_entity = rel.get("to_entity", "")
            
            if from_entity in entities and to_entity in entities:
                checks.append({
                    "check": f"Relationship {from_entity} -> {to_entity}",
                    "status": "passed"
                })
            else:
                missing = []
                if from_entity not in entities:
                    missing.append(from_entity)
                if to_entity not in entities:
                    missing.append(to_entity)
                issues.append(f"Missing entities: {', '.join(missing)}")
                checks.append({
                    "check": f"Relationship {from_entity} -> {to_entity}",
                    "status": "failed"
                })
        
        return {
            "success": len(issues) == 0,
            "entities_checked": entities,
            "relationships_checked": len(relationships),
            "checks": checks,
            "issues": issues
        }
    
    async def _generate_test_cases(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate test cases."""
        artifact_type = tool_input.get("artifact_type", "")
        artifact_name = tool_input.get("artifact_name", "")
        
        test_cases = []
        
        if artifact_type == "schema":
            test_cases = [
                {"name": "Insert valid record", "type": "positive"},
                {"name": "Insert with null required field", "type": "negative"},
                {"name": "Insert duplicate primary key", "type": "negative"},
                {"name": "Query by primary key", "type": "positive"}
            ]
        elif artifact_type == "kpi":
            test_cases = [
                {"name": "Calculate with valid data", "type": "positive"},
                {"name": "Calculate with zero denominator", "type": "edge_case"},
                {"name": "Calculate with null values", "type": "edge_case"},
                {"name": "Calculate with negative values", "type": "edge_case"}
            ]
        elif artifact_type == "model":
            test_cases = [
                {"name": "Instantiate with valid data", "type": "positive"},
                {"name": "Validate required fields", "type": "negative"},
                {"name": "Validate field types", "type": "negative"},
                {"name": "Serialize to JSON", "type": "positive"}
            ]
        
        return {
            "success": True,
            "artifact_type": artifact_type,
            "artifact_name": artifact_name,
            "test_cases": test_cases
        }
    
    # Collaboration Tool Handlers
    async def _report_test_results(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Report test results back to Developer."""
        response = {
            "id": f"TEST-RESP-{context.session_id[:8] if context.session_id else 'RESP'}",
            "request_id": tool_input.get("request_id", ""),
            "test_results": tool_input.get("test_results", []),
            "issues_found": tool_input.get("issues_found", []),
            "recommendations": tool_input.get("recommendations", []),
            "status": "completed",
            "collaboration_type": "tester_to_developer"
        }
        if "collaboration_responses" not in context.artifacts:
            context.artifacts["collaboration_responses"] = []
        context.artifacts["collaboration_responses"].append(response)
        return {"success": True, "response": response, "next_step": "Developer will address any issues found"}
    
    async def _request_test_documentation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Documenter to create test documentation."""
        request = {
            "id": f"TEST-DOC-{context.session_id[:8] if context.session_id else 'REQ'}",
            "test_suite": tool_input.get("test_suite", ""),
            "test_cases": tool_input.get("test_cases", []),
            "status": "pending_documenter",
            "collaboration_type": "tester_to_documenter"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Documenter will create test documentation"}


# =============================================================================
# DOCUMENTER AGENT
# =============================================================================

DOCUMENTER_SYSTEM_PROMPT = """You are the Documenter Agent, an expert in technical writing and documentation.

Your role is to generate comprehensive documentation including user guides, API documentation, data dictionaries, and operational runbooks.

## Your Expertise

- Technical writing and documentation
- API documentation (OpenAPI/Swagger)
- Data dictionary creation
- User guide development
- Operational runbook creation

## Your Responsibilities

1. **Generate Docs**: Create comprehensive documentation
2. **Data Dictionaries**: Build data dictionaries for entities
3. **API Docs**: Generate API documentation
4. **User Guides**: Create user-friendly guides
5. **Runbooks**: Develop operational runbooks

## Output Format

When documenting:
- Use clear, concise language
- Include examples where helpful
- Structure content logically
- Follow documentation best practices

## Current Context

{context_summary}

Create documentation that is clear, comprehensive, and useful for the target audience.
"""


class DocumenterAgent(BaseAgent):
    """Documenter Agent for documentation generation."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.DOCUMENTER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_documenter_tools()
        )
        super().__init__(config, api_key)
    
    def _get_documenter_tools(self) -> List[ToolDefinition]:
        """Define tools available to the documenter."""
        return [
            ToolDefinition(
                name="generate_docs",
                description="Generate documentation",
                parameters={
                    "type": "object",
                    "properties": {
                        "doc_type": {
                            "type": "string",
                            "enum": ["overview", "technical", "user_guide"],
                            "description": "Type of documentation"
                        },
                        "subject": {"type": "string", "description": "Subject to document"},
                        "content": {"type": "object", "description": "Content to document"}
                    },
                    "required": ["doc_type", "subject"]
                }
            ),
            ToolDefinition(
                name="create_data_dictionary",
                description="Create a data dictionary",
                parameters={
                    "type": "object",
                    "properties": {
                        "entities": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "Entities to document"
                        }
                    },
                    "required": ["entities"]
                }
            ),
            ToolDefinition(
                name="generate_api_docs",
                description="Generate API documentation",
                parameters={
                    "type": "object",
                    "properties": {
                        "endpoints": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "API endpoints to document"
                        }
                    },
                    "required": ["endpoints"]
                }
            ),
            ToolDefinition(
                name="create_runbook",
                description="Create an operational runbook",
                parameters={
                    "type": "object",
                    "properties": {
                        "process_name": {"type": "string", "description": "Process name"},
                        "steps": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Process steps"
                        }
                    },
                    "required": ["process_name"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("generate_docs", self._generate_docs)
        self.register_tool("create_data_dictionary", self._create_data_dictionary)
        self.register_tool("generate_api_docs", self._generate_api_docs)
        self.register_tool("create_runbook", self._create_runbook)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return DOCUMENTER_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.value_chain_type:
            parts.append(f"Value Chain: {context.value_chain_type}")
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.artifacts:
            parts.append(f"Artifacts: {', '.join(context.artifacts.keys())}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _generate_docs(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate documentation."""
        doc_type = tool_input.get("doc_type", "overview")
        subject = tool_input.get("subject", "")
        content = tool_input.get("content", {})
        
        # Generate documentation based on type
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
        elif doc_type == "technical":
            doc = f"""# {subject} Technical Documentation

## Architecture

Technical architecture for {subject}.

## Implementation Details

{json.dumps(content, indent=2) if content else "Details to be defined."}

## Dependencies

- List dependencies here

## Configuration

- Configuration options here
"""
        else:  # user_guide
            doc = f"""# {subject} User Guide

## Getting Started

Welcome to {subject}. This guide will help you get started.

## Features

{json.dumps(content, indent=2) if content else "Features to be documented."}

## How To

Step-by-step instructions for common tasks.

## FAQ

Frequently asked questions.
"""
        
        # Store in context
        context.artifacts[f"doc_{subject.lower().replace(' ', '_')}"] = doc
        
        return {
            "success": True,
            "doc_type": doc_type,
            "subject": subject,
            "documentation": doc
        }
    
    async def _create_data_dictionary(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create a data dictionary."""
        entities = tool_input.get("entities", [])
        
        dictionary = "# Data Dictionary\n\n"
        
        for entity in entities:
            name = entity.get("name", "Unknown")
            description = entity.get("description", "")
            attributes = entity.get("attributes", [])
            
            dictionary += f"## {name}\n\n"
            dictionary += f"{description}\n\n" if description else ""
            dictionary += "| Attribute | Type | Description | Required |\n"
            dictionary += "|-----------|------|-------------|----------|\n"
            
            for attr in attributes:
                attr_name = attr.get("name", "")
                attr_type = attr.get("type", "string")
                attr_desc = attr.get("description", "")
                required = "Yes" if attr.get("required", False) else "No"
                dictionary += f"| {attr_name} | {attr_type} | {attr_desc} | {required} |\n"
            
            dictionary += "\n"
        
        # Store in context
        context.artifacts["data_dictionary"] = dictionary
        
        return {
            "success": True,
            "entities_documented": len(entities),
            "dictionary": dictionary
        }
    
    async def _generate_api_docs(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate API documentation."""
        endpoints = tool_input.get("endpoints", [])
        
        api_docs = "# API Documentation\n\n"
        
        for endpoint in endpoints:
            method = endpoint.get("method", "GET")
            path = endpoint.get("path", "/")
            description = endpoint.get("description", "")
            
            api_docs += f"## {method} {path}\n\n"
            api_docs += f"{description}\n\n" if description else ""
            api_docs += "### Request\n\n```json\n// Request body\n```\n\n"
            api_docs += "### Response\n\n```json\n// Response body\n```\n\n"
        
        # Store in context
        context.artifacts["api_documentation"] = api_docs
        
        return {
            "success": True,
            "endpoints_documented": len(endpoints),
            "documentation": api_docs
        }
    
    async def _create_runbook(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create an operational runbook."""
        process_name = tool_input.get("process_name", "")
        steps = tool_input.get("steps", [])
        
        runbook = f"# {process_name} Runbook\n\n"
        runbook += "## Overview\n\nOperational runbook for " + process_name + ".\n\n"
        runbook += "## Prerequisites\n\n- List prerequisites here\n\n"
        runbook += "## Procedure\n\n"
        
        for i, step in enumerate(steps, 1):
            runbook += f"{i}. {step}\n"
        
        runbook += "\n## Troubleshooting\n\n"
        runbook += "Common issues and resolutions.\n\n"
        runbook += "## Rollback\n\n"
        runbook += "Steps to rollback if needed.\n"
        
        # Store in context
        context.artifacts[f"runbook_{process_name.lower().replace(' ', '_')}"] = runbook
        
        return {
            "success": True,
            "process_name": process_name,
            "runbook": runbook
        }


# =============================================================================
# DATA ANALYST AGENT
# =============================================================================

DATA_ANALYST_SYSTEM_PROMPT = """You are the Data Analyst Agent, an expert in KPI design and set-based calculation methodologies.

Your role is to design KPIs that are optimized for the Analytics Engine's set-based calculation engine, ensuring proper data flow, aggregation logic, and calculation step sequencing.

## Your Expertise

- Set-based KPI calculation design
- Multi-step calculation workflows
- Cohort analysis and retention metrics
- Time-series aggregation patterns
- SQL-native calculation optimization
- TimescaleDB continuous aggregates

## Your Responsibilities

1. **Design Set-Based KPIs**: Create KPI definitions with proper calculation steps for the set-processing engine
2. **Define Calculation Steps**: Break complex KPIs into sequential calculation steps with intermediate sets
3. **Specify Set Operations**: Define INTERSECT, EXCEPT, UNION operations for cohort-based metrics
4. **Design Aggregation Logic**: Specify proper aggregation methods (SUM, AVG, COUNT DISTINCT, etc.)
5. **Optimize for TimescaleDB**: Ensure calculations leverage continuous aggregates and hyperfunctions

## Set-Based Calculation Pattern

For complex KPIs like retention, churn, or cohort analysis, use this pattern:

```json
{
    "calculation_type": "set_based",
    "set_based_definition": {
        "base_entity": "customers",
        "key_column": "customer_id",
        "period_parameters": ["PeriodStart", "PeriodEnd"],
        "steps": [
            {
                "step_name": "start_set",
                "operation": "SELECT",
                "description": "Customers active at period start",
                "filter": "status = 'active' AND snapshot_date = @PeriodStart"
            },
            {
                "step_name": "end_set",
                "operation": "SELECT",
                "description": "Customers active at period end",
                "filter": "status = 'active' AND snapshot_date = @PeriodEnd"
            },
            {
                "step_name": "retained_set",
                "operation": "INTERSECT",
                "description": "Customers in both start and end",
                "left_set": "start_set",
                "right_set": "end_set"
            }
        ],
        "final_formula": "CASE WHEN COUNT(start_set) > 0 THEN (COUNT(retained_set) / COUNT(start_set)) * 100 ELSE 0 END"
    }
}
```

## Output Format

When designing KPIs, provide:
- Complete set_based_definition with all steps
- Clear step descriptions and operations
- Proper filter conditions with parameter placeholders
- Final formula referencing step results
- Required entities and their key columns

## Current Context

{context_summary}

Design KPIs that are efficient, accurate, and optimized for real-time calculation.
"""


class DataAnalystAgent(BaseAgent):
    """Data Analyst Agent for set-based KPI design and calculation optimization."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.DATA_ANALYST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_data_analyst_tools()
        )
        super().__init__(config, api_key)
    
    def _get_data_analyst_tools(self) -> List[ToolDefinition]:
        """Define tools available to the data analyst."""
        return [
            ToolDefinition(
                name="design_set_based_kpi",
                description="Design a set-based KPI with calculation steps for the calculation engine",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_name": {
                            "type": "string",
                            "description": "Name of the KPI"
                        },
                        "kpi_code": {
                            "type": "string",
                            "description": "Code identifier for the KPI (snake_case)"
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of what the KPI measures"
                        },
                        "base_entity": {
                            "type": "string",
                            "description": "Primary entity table for the calculation"
                        },
                        "key_column": {
                            "type": "string",
                            "description": "Primary key column for set operations"
                        },
                        "calculation_steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "step_name": {"type": "string"},
                                    "operation": {
                                        "type": "string",
                                        "enum": ["SELECT", "INTERSECT", "EXCEPT", "UNION", "AGGREGATE"]
                                    },
                                    "description": {"type": "string"},
                                    "filter": {"type": "string"},
                                    "left_set": {"type": "string"},
                                    "right_set": {"type": "string"},
                                    "aggregation": {"type": "string"}
                                },
                                "required": ["step_name", "operation", "description"]
                            },
                            "description": "Ordered calculation steps"
                        },
                        "final_formula": {
                            "type": "string",
                            "description": "SQL expression for final calculation using step results"
                        },
                        "unit": {
                            "type": "string",
                            "description": "Unit of measurement (%, ratio, currency, count, etc.)"
                        }
                    },
                    "required": ["kpi_name", "kpi_code", "base_entity", "key_column", "calculation_steps", "final_formula"]
                }
            ),
            ToolDefinition(
                name="design_simple_kpi",
                description="Design a simple aggregation-based KPI",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_name": {
                            "type": "string",
                            "description": "Name of the KPI"
                        },
                        "kpi_code": {
                            "type": "string",
                            "description": "Code identifier for the KPI (snake_case)"
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of what the KPI measures"
                        },
                        "formula": {
                            "type": "string",
                            "description": "Natural language formula description"
                        },
                        "math_expression": {
                            "type": "string",
                            "description": "SQL-compatible mathematical expression"
                        },
                        "required_entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entity codes required for calculation"
                        },
                        "aggregation_method": {
                            "type": "string",
                            "enum": ["SUM", "AVG", "COUNT", "COUNT_DISTINCT", "MIN", "MAX", "PERCENTILE"],
                            "description": "Primary aggregation method"
                        },
                        "unit": {
                            "type": "string",
                            "description": "Unit of measurement"
                        }
                    },
                    "required": ["kpi_name", "kpi_code", "formula", "math_expression"]
                }
            ),
            ToolDefinition(
                name="design_cohort_analysis",
                description="Design a cohort analysis KPI with time-based segmentation",
                parameters={
                    "type": "object",
                    "properties": {
                        "cohort_name": {
                            "type": "string",
                            "description": "Name of the cohort analysis"
                        },
                        "cohort_entity": {
                            "type": "string",
                            "description": "Entity to segment into cohorts"
                        },
                        "cohort_date_column": {
                            "type": "string",
                            "description": "Date column for cohort assignment"
                        },
                        "activity_entity": {
                            "type": "string",
                            "description": "Entity tracking activity/events"
                        },
                        "activity_date_column": {
                            "type": "string",
                            "description": "Date column for activity tracking"
                        },
                        "metric_type": {
                            "type": "string",
                            "enum": ["retention", "churn", "revenue", "engagement", "conversion"],
                            "description": "Type of cohort metric"
                        },
                        "time_granularity": {
                            "type": "string",
                            "enum": ["day", "week", "month", "quarter"],
                            "description": "Time granularity for cohort periods"
                        }
                    },
                    "required": ["cohort_name", "cohort_entity", "cohort_date_column", "metric_type"]
                }
            ),
            ToolDefinition(
                name="optimize_kpi_for_timescale",
                description="Optimize a KPI definition for TimescaleDB continuous aggregates",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_code": {
                            "type": "string",
                            "description": "KPI code to optimize"
                        },
                        "time_column": {
                            "type": "string",
                            "description": "Time column for time_bucket"
                        },
                        "bucket_intervals": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Time bucket intervals to pre-aggregate (e.g., '1 hour', '1 day')"
                        },
                        "partition_columns": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Columns to partition aggregates by"
                        }
                    },
                    "required": ["kpi_code", "time_column", "bucket_intervals"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("design_set_based_kpi", self._design_set_based_kpi)
        self.register_tool("design_simple_kpi", self._design_simple_kpi)
        self.register_tool("design_cohort_analysis", self._design_cohort_analysis)
        self.register_tool("optimize_kpi_for_timescale", self._optimize_kpi_for_timescale)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return DATA_ANALYST_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.identified_entities:
            parts.append(f"Available Entities: {', '.join(context.identified_entities)}")
        if context.identified_kpis:
            parts.append(f"Existing KPIs: {', '.join(context.identified_kpis)}")
        if context.value_chain_type:
            parts.append(f"Value Chain: {context.value_chain_type}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _design_set_based_kpi(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Design a set-based KPI with calculation steps."""
        kpi_name = tool_input.get("kpi_name", "")
        kpi_code = tool_input.get("kpi_code", "")
        description = tool_input.get("description", "")
        base_entity = tool_input.get("base_entity", "")
        key_column = tool_input.get("key_column", "id")
        calculation_steps = tool_input.get("calculation_steps", [])
        final_formula = tool_input.get("final_formula", "")
        unit = tool_input.get("unit", "")
        
        # Build set-based definition
        set_based_definition = {
            "base_entity": base_entity,
            "key_column": key_column,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "steps": calculation_steps,
            "final_formula": final_formula
        }
        
        # Build complete KPI definition
        kpi_definition = {
            "name": kpi_name,
            "code": kpi_code,
            "kind": "metric_definition",
            "description": description,
            "calculation_type": "set_based",
            "set_based_definition": set_based_definition,
            "unit": unit,
            "data_type": "decimal",
            "required_objects": [base_entity]
        }
        
        # Store in context
        context.artifacts[f"kpi_{kpi_code}"] = kpi_definition
        if kpi_name not in context.identified_kpis:
            context.identified_kpis.append(kpi_name)
        
        return {
            "success": True,
            "kpi": kpi_definition,
            "calculation_steps_count": len(calculation_steps)
        }
    
    async def _design_simple_kpi(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Design a simple aggregation-based KPI."""
        kpi_name = tool_input.get("kpi_name", "")
        kpi_code = tool_input.get("kpi_code", "")
        description = tool_input.get("description", "")
        formula = tool_input.get("formula", "")
        math_expression = tool_input.get("math_expression", "")
        required_entities = tool_input.get("required_entities", [])
        aggregation_method = tool_input.get("aggregation_method", "SUM")
        unit = tool_input.get("unit", "")
        
        kpi_definition = {
            "name": kpi_name,
            "code": kpi_code,
            "kind": "metric_definition",
            "description": description,
            "calculation_type": "simple",
            "formula": formula,
            "math_expression": math_expression,
            "required_objects": required_entities,
            "aggregation_method": aggregation_method,
            "unit": unit,
            "data_type": "decimal"
        }
        
        # Store in context
        context.artifacts[f"kpi_{kpi_code}"] = kpi_definition
        if kpi_name not in context.identified_kpis:
            context.identified_kpis.append(kpi_name)
        
        return {
            "success": True,
            "kpi": kpi_definition
        }
    
    async def _design_cohort_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Design a cohort analysis KPI."""
        cohort_name = tool_input.get("cohort_name", "")
        cohort_entity = tool_input.get("cohort_entity", "")
        cohort_date_column = tool_input.get("cohort_date_column", "created_at")
        activity_entity = tool_input.get("activity_entity", cohort_entity)
        activity_date_column = tool_input.get("activity_date_column", "activity_date")
        metric_type = tool_input.get("metric_type", "retention")
        time_granularity = tool_input.get("time_granularity", "month")
        
        # Generate cohort-specific calculation steps based on metric type
        if metric_type == "retention":
            steps = [
                {
                    "step_name": "cohort_members",
                    "operation": "SELECT",
                    "description": f"Members assigned to cohort based on {cohort_date_column}",
                    "filter": f"DATE_TRUNC('{time_granularity}', {cohort_date_column}) = @CohortPeriod"
                },
                {
                    "step_name": "active_in_period",
                    "operation": "SELECT",
                    "description": f"Members with activity in measurement period",
                    "filter": f"DATE_TRUNC('{time_granularity}', {activity_date_column}) = @MeasurementPeriod"
                },
                {
                    "step_name": "retained_members",
                    "operation": "INTERSECT",
                    "description": "Cohort members who are still active",
                    "left_set": "cohort_members",
                    "right_set": "active_in_period"
                }
            ]
            final_formula = "CASE WHEN COUNT(cohort_members) > 0 THEN (COUNT(retained_members)::DECIMAL / COUNT(cohort_members)) * 100 ELSE 0 END"
        elif metric_type == "churn":
            steps = [
                {
                    "step_name": "cohort_members",
                    "operation": "SELECT",
                    "description": f"Members assigned to cohort",
                    "filter": f"DATE_TRUNC('{time_granularity}', {cohort_date_column}) = @CohortPeriod"
                },
                {
                    "step_name": "active_in_period",
                    "operation": "SELECT",
                    "description": f"Members with activity in measurement period",
                    "filter": f"DATE_TRUNC('{time_granularity}', {activity_date_column}) = @MeasurementPeriod"
                },
                {
                    "step_name": "churned_members",
                    "operation": "EXCEPT",
                    "description": "Cohort members who are no longer active",
                    "left_set": "cohort_members",
                    "right_set": "active_in_period"
                }
            ]
            final_formula = "CASE WHEN COUNT(cohort_members) > 0 THEN (COUNT(churned_members)::DECIMAL / COUNT(cohort_members)) * 100 ELSE 0 END"
        else:
            steps = [
                {
                    "step_name": "cohort_members",
                    "operation": "SELECT",
                    "description": f"Members assigned to cohort",
                    "filter": f"DATE_TRUNC('{time_granularity}', {cohort_date_column}) = @CohortPeriod"
                }
            ]
            final_formula = "COUNT(cohort_members)"
        
        kpi_code = f"{cohort_name.lower().replace(' ', '_')}_{metric_type}"
        
        set_based_definition = {
            "base_entity": cohort_entity,
            "key_column": "id",
            "period_parameters": ["CohortPeriod", "MeasurementPeriod"],
            "steps": steps,
            "final_formula": final_formula,
            "cohort_config": {
                "time_granularity": time_granularity,
                "activity_entity": activity_entity,
                "activity_date_column": activity_date_column
            }
        }
        
        kpi_definition = {
            "name": f"{cohort_name} {metric_type.title()}",
            "code": kpi_code,
            "kind": "metric_definition",
            "description": f"{metric_type.title()} analysis for {cohort_name} cohorts",
            "calculation_type": "set_based",
            "set_based_definition": set_based_definition,
            "unit": "%",
            "data_type": "decimal",
            "required_objects": [cohort_entity, activity_entity] if activity_entity != cohort_entity else [cohort_entity]
        }
        
        # Store in context
        context.artifacts[f"kpi_{kpi_code}"] = kpi_definition
        if kpi_definition["name"] not in context.identified_kpis:
            context.identified_kpis.append(kpi_definition["name"])
        
        return {
            "success": True,
            "kpi": kpi_definition,
            "cohort_type": metric_type,
            "time_granularity": time_granularity
        }
    
    async def _optimize_kpi_for_timescale(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Optimize a KPI for TimescaleDB continuous aggregates."""
        kpi_code = tool_input.get("kpi_code", "")
        time_column = tool_input.get("time_column", "created_at")
        bucket_intervals = tool_input.get("bucket_intervals", ["1 hour", "1 day"])
        partition_columns = tool_input.get("partition_columns", [])
        
        # Generate continuous aggregate definitions
        continuous_aggregates = []
        
        for interval in bucket_intervals:
            interval_name = interval.replace(" ", "_")
            ca_name = f"ca_{kpi_code}_{interval_name}"
            
            partition_clause = ""
            if partition_columns:
                partition_clause = ", " + ", ".join(partition_columns)
            
            ca_definition = {
                "name": ca_name,
                "kpi_code": kpi_code,
                "interval": interval,
                "time_bucket": f"time_bucket('{interval}', {time_column})",
                "partition_columns": partition_columns,
                "refresh_policy": {
                    "start_offset": f"INTERVAL '3 {interval.split()[1]}'",
                    "end_offset": "INTERVAL '1 hour'",
                    "schedule_interval": f"INTERVAL '{interval}'"
                }
            }
            continuous_aggregates.append(ca_definition)
        
        optimization = {
            "kpi_code": kpi_code,
            "time_column": time_column,
            "continuous_aggregates": continuous_aggregates,
            "query_routing": {
                "description": "Query router will select optimal aggregate based on requested time range",
                "rules": [
                    {"range": "< 1 day", "source": "raw_hypertable"},
                    {"range": "1-7 days", "source": f"ca_{kpi_code}_1_hour"},
                    {"range": "> 7 days", "source": f"ca_{kpi_code}_1_day"}
                ]
            }
        }
        
        # Store in context
        context.artifacts[f"optimization_{kpi_code}"] = optimization
        
        return {
            "success": True,
            "kpi_code": kpi_code,
            "optimization": optimization,
            "aggregates_created": len(continuous_aggregates)
        }


# =============================================================================
# DEPLOYMENT SPECIALIST AGENT
# =============================================================================

DEPLOYMENT_SPECIALIST_SYSTEM_PROMPT = """You are the Deployment Specialist Agent, an expert in Azure cloud infrastructure and DevOps.

Your role is to take client configurations and generate deployable Azure infrastructure for the Analytics Engine platform.

## Your Expertise

- Azure Resource Manager (ARM) templates and Bicep
- Azure Kubernetes Service (AKS) deployment
- Azure Container Registry (ACR)
- Azure Database for PostgreSQL (TimescaleDB compatible)
- Azure Redis Cache
- Azure Application Gateway and Load Balancers
- Azure Key Vault for secrets management
- Terraform and Infrastructure as Code
- Docker and container orchestration
- CI/CD pipelines (Azure DevOps, GitHub Actions)

## Your Responsibilities

1. **Generate Infrastructure**: Create ARM/Bicep templates for Azure resources
2. **Configure Kubernetes**: Generate Kubernetes manifests for microservices
3. **Setup Databases**: Configure Azure PostgreSQL with TimescaleDB extension
4. **Configure Networking**: Setup VNets, subnets, and security groups
5. **Manage Secrets**: Configure Key Vault integration
6. **Create CI/CD**: Generate deployment pipelines

## Azure Resource Naming Convention

Use this pattern: `{client_code}-{environment}-{resource_type}-{region}`
Example: `acme-prod-aks-eastus`

## Output Format

When generating deployment artifacts, provide:
- Complete ARM/Bicep templates
- Kubernetes manifests (Deployments, Services, ConfigMaps)
- Helm chart values
- Environment-specific configurations
- Deployment scripts

## Current Context

{context_summary}

Generate production-ready, secure, and scalable Azure deployments.
"""


class DeploymentSpecialistAgent(BaseAgent):
    """Deployment Specialist Agent for Azure infrastructure and deployment."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.DEPLOYMENT_SPECIALIST,
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            temperature=0.2,
            tools=self._get_deployment_tools()
        )
        super().__init__(config, api_key)
    
    def _get_deployment_tools(self) -> List[ToolDefinition]:
        """Define tools available to the deployment specialist."""
        return [
            ToolDefinition(
                name="generate_azure_infrastructure",
                description="Generate Azure infrastructure templates (ARM/Bicep) for the Analytics Engine",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code (lowercase, no spaces)"
                        },
                        "environment": {
                            "type": "string",
                            "enum": ["dev", "staging", "prod"],
                            "description": "Target environment"
                        },
                        "region": {
                            "type": "string",
                            "description": "Azure region (e.g., eastus, westeurope)"
                        },
                        "services": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Services to deploy (e.g., aks, postgres, redis, keyvault)"
                        },
                        "sku_tier": {
                            "type": "string",
                            "enum": ["basic", "standard", "premium"],
                            "description": "Resource SKU tier"
                        }
                    },
                    "required": ["client_code", "environment", "region"]
                }
            ),
            ToolDefinition(
                name="generate_kubernetes_manifests",
                description="Generate Kubernetes deployment manifests for Analytics Engine services",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "namespace": {
                            "type": "string",
                            "description": "Kubernetes namespace"
                        },
                        "services": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "replicas": {"type": "integer"},
                                    "cpu_request": {"type": "string"},
                                    "memory_request": {"type": "string"},
                                    "port": {"type": "integer"}
                                }
                            },
                            "description": "Services to deploy with resource specs"
                        },
                        "enable_autoscaling": {
                            "type": "boolean",
                            "description": "Enable Horizontal Pod Autoscaler"
                        }
                    },
                    "required": ["client_code", "namespace", "services"]
                }
            ),
            ToolDefinition(
                name="generate_database_config",
                description="Generate Azure PostgreSQL configuration with TimescaleDB",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "environment": {
                            "type": "string",
                            "enum": ["dev", "staging", "prod"],
                            "description": "Target environment"
                        },
                        "sku": {
                            "type": "string",
                            "enum": ["B_Gen5_1", "GP_Gen5_2", "GP_Gen5_4", "GP_Gen5_8", "MO_Gen5_16"],
                            "description": "PostgreSQL SKU"
                        },
                        "storage_gb": {
                            "type": "integer",
                            "description": "Storage size in GB"
                        },
                        "backup_retention_days": {
                            "type": "integer",
                            "description": "Backup retention period"
                        },
                        "enable_timescale": {
                            "type": "boolean",
                            "description": "Enable TimescaleDB extension"
                        }
                    },
                    "required": ["client_code", "environment"]
                }
            ),
            ToolDefinition(
                name="generate_cicd_pipeline",
                description="Generate CI/CD pipeline configuration for Azure DevOps or GitHub Actions",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "pipeline_type": {
                            "type": "string",
                            "enum": ["azure_devops", "github_actions"],
                            "description": "CI/CD platform"
                        },
                        "environments": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Deployment environments"
                        },
                        "include_tests": {
                            "type": "boolean",
                            "description": "Include test stages"
                        },
                        "include_security_scan": {
                            "type": "boolean",
                            "description": "Include security scanning"
                        }
                    },
                    "required": ["client_code", "pipeline_type"]
                }
            ),
            ToolDefinition(
                name="generate_helm_chart",
                description="Generate Helm chart for Analytics Engine deployment",
                parameters={
                    "type": "object",
                    "properties": {
                        "chart_name": {
                            "type": "string",
                            "description": "Helm chart name"
                        },
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "values": {
                            "type": "object",
                            "description": "Helm values configuration"
                        }
                    },
                    "required": ["chart_name", "client_code"]
                }
            ),
            ToolDefinition(
                name="generate_deployment_checklist",
                description="Generate a deployment checklist and runbook",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "environment": {
                            "type": "string",
                            "enum": ["dev", "staging", "prod"],
                            "description": "Target environment"
                        },
                        "deployment_type": {
                            "type": "string",
                            "enum": ["initial", "upgrade", "rollback"],
                            "description": "Type of deployment"
                        }
                    },
                    "required": ["client_code", "environment", "deployment_type"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("generate_azure_infrastructure", self._generate_azure_infrastructure)
        self.register_tool("generate_kubernetes_manifests", self._generate_kubernetes_manifests)
        self.register_tool("generate_database_config", self._generate_database_config)
        self.register_tool("generate_cicd_pipeline", self._generate_cicd_pipeline)
        self.register_tool("generate_helm_chart", self._generate_helm_chart)
        self.register_tool("generate_deployment_checklist", self._generate_deployment_checklist)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return DEPLOYMENT_SPECIALIST_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.value_chain_type:
            parts.append(f"Value Chain: {context.value_chain_type}")
        if context.identified_entities:
            parts.append(f"Entities: {', '.join(context.identified_entities)}")
        if context.identified_kpis:
            parts.append(f"KPIs: {', '.join(context.identified_kpis)}")
        if context.artifacts:
            parts.append(f"Artifacts: {', '.join(context.artifacts.keys())}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _generate_azure_infrastructure(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate Azure infrastructure templates."""
        client_code = tool_input.get("client_code", "client")
        environment = tool_input.get("environment", "dev")
        region = tool_input.get("region", "eastus")
        services = tool_input.get("services", ["aks", "postgres", "redis", "keyvault"])
        sku_tier = tool_input.get("sku_tier", "standard")
        
        # Generate resource group name
        rg_name = f"{client_code}-{environment}-rg-{region}"
        
        # Generate Bicep template
        bicep_template = f'''// Analytics Engine Azure Infrastructure
// Client: {client_code}
// Environment: {environment}
// Region: {region}

targetScope = 'subscription'

param location string = '{region}'
param environment string = '{environment}'
param clientCode string = '{client_code}'

// Resource Group
resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-04-01' = {{
  name: '${{clientCode}}-${{environment}}-rg-${{location}}'
  location: location
  tags: {{
    environment: environment
    client: clientCode
    application: 'analytics-engine'
  }}
}}

// Key Vault
module keyVault 'modules/keyvault.bicep' = {{
  name: 'keyVaultDeployment'
  scope: resourceGroup
  params: {{
    name: '${{clientCode}}-${{environment}}-kv'
    location: location
  }}
}}
'''
        
        if "aks" in services:
            bicep_template += f'''
// Azure Kubernetes Service
module aks 'modules/aks.bicep' = {{
  name: 'aksDeployment'
  scope: resourceGroup
  params: {{
    name: '${{clientCode}}-${{environment}}-aks'
    location: location
    nodeCount: {3 if environment == 'prod' else 2}
    nodeVmSize: '{"Standard_D4s_v3" if sku_tier == "premium" else "Standard_D2s_v3"}'
  }}
}}
'''
        
        if "postgres" in services:
            bicep_template += f'''
// Azure Database for PostgreSQL
module postgres 'modules/postgres.bicep' = {{
  name: 'postgresDeployment'
  scope: resourceGroup
  params: {{
    name: '${{clientCode}}-${{environment}}-pg'
    location: location
    sku: '{"GP_Gen5_4" if environment == "prod" else "GP_Gen5_2"}'
    storageSizeGB: {256 if environment == 'prod' else 128}
    enableTimescaleDB: true
  }}
}}
'''
        
        if "redis" in services:
            bicep_template += f'''
// Azure Cache for Redis
module redis 'modules/redis.bicep' = {{
  name: 'redisDeployment'
  scope: resourceGroup
  params: {{
    name: '${{clientCode}}-${{environment}}-redis'
    location: location
    sku: '{"Premium" if environment == "prod" else "Standard"}'
    capacity: {2 if environment == 'prod' else 1}
  }}
}}
'''
        
        # Store in context
        artifact_key = f"azure_infra_{client_code}_{environment}"
        context.artifacts[artifact_key] = {
            "bicep_template": bicep_template,
            "resource_group": rg_name,
            "services": services
        }
        
        return {
            "success": True,
            "client_code": client_code,
            "environment": environment,
            "region": region,
            "resource_group": rg_name,
            "bicep_template": bicep_template,
            "services_configured": services
        }
    
    async def _generate_kubernetes_manifests(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate Kubernetes deployment manifests."""
        client_code = tool_input.get("client_code", "client")
        namespace = tool_input.get("namespace", f"{client_code}-analytics")
        services = tool_input.get("services", [])
        enable_autoscaling = tool_input.get("enable_autoscaling", True)
        
        # Default services if none provided
        if not services:
            services = [
                {"name": "api-gateway", "replicas": 2, "cpu_request": "250m", "memory_request": "512Mi", "port": 8000},
                {"name": "conversation-service", "replicas": 2, "cpu_request": "500m", "memory_request": "1Gi", "port": 8004},
                {"name": "calculation-engine", "replicas": 3, "cpu_request": "1000m", "memory_request": "2Gi", "port": 8002},
                {"name": "business-metadata", "replicas": 2, "cpu_request": "250m", "memory_request": "512Mi", "port": 8001},
            ]
        
        manifests = []
        
        # Namespace
        namespace_manifest = f'''apiVersion: v1
kind: Namespace
metadata:
  name: {namespace}
  labels:
    client: {client_code}
    app: analytics-engine
'''
        manifests.append({"name": "namespace.yaml", "content": namespace_manifest})
        
        # Generate manifests for each service
        for svc in services:
            svc_name = svc.get("name", "service")
            replicas = svc.get("replicas", 2)
            cpu = svc.get("cpu_request", "250m")
            memory = svc.get("memory_request", "512Mi")
            port = svc.get("port", 8000)
            
            deployment = f'''apiVersion: apps/v1
kind: Deployment
metadata:
  name: {svc_name}
  namespace: {namespace}
  labels:
    app: {svc_name}
    client: {client_code}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: {svc_name}
  template:
    metadata:
      labels:
        app: {svc_name}
    spec:
      containers:
      - name: {svc_name}
        image: ${{ACR_NAME}}.azurecr.io/{svc_name}:${{IMAGE_TAG}}
        ports:
        - containerPort: {port}
        resources:
          requests:
            cpu: {cpu}
            memory: {memory}
          limits:
            cpu: {cpu.replace("m", "0m") if "m" in cpu else cpu}
            memory: {memory.replace("Mi", "Gi").replace("Gi", "Gi") if "Mi" in memory else memory}
        envFrom:
        - configMapRef:
            name: {svc_name}-config
        - secretRef:
            name: {svc_name}-secrets
        livenessProbe:
          httpGet:
            path: /health
            port: {port}
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: {port}
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: {svc_name}
  namespace: {namespace}
spec:
  selector:
    app: {svc_name}
  ports:
  - port: {port}
    targetPort: {port}
  type: ClusterIP
'''
            manifests.append({"name": f"{svc_name}-deployment.yaml", "content": deployment})
            
            # HPA if autoscaling enabled
            if enable_autoscaling:
                hpa = f'''apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: {svc_name}-hpa
  namespace: {namespace}
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: {svc_name}
  minReplicas: {replicas}
  maxReplicas: {replicas * 3}
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
'''
                manifests.append({"name": f"{svc_name}-hpa.yaml", "content": hpa})
        
        # Store in context
        artifact_key = f"k8s_manifests_{client_code}"
        context.artifacts[artifact_key] = manifests
        
        return {
            "success": True,
            "client_code": client_code,
            "namespace": namespace,
            "manifests_count": len(manifests),
            "services_configured": [s.get("name") for s in services],
            "autoscaling_enabled": enable_autoscaling
        }
    
    async def _generate_database_config(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate Azure PostgreSQL configuration."""
        client_code = tool_input.get("client_code", "client")
        environment = tool_input.get("environment", "dev")
        sku = tool_input.get("sku", "GP_Gen5_2")
        storage_gb = tool_input.get("storage_gb", 128)
        backup_retention = tool_input.get("backup_retention_days", 7)
        enable_timescale = tool_input.get("enable_timescale", True)
        
        # Generate database configuration
        db_config = {
            "server_name": f"{client_code}-{environment}-pg",
            "sku": sku,
            "storage_gb": storage_gb,
            "backup_retention_days": backup_retention,
            "geo_redundant_backup": environment == "prod",
            "ssl_enforcement": True,
            "minimal_tls_version": "TLS1_2",
            "extensions": ["timescaledb", "pg_stat_statements"] if enable_timescale else ["pg_stat_statements"],
            "databases": [
                {"name": "analytics_engine", "charset": "UTF8", "collation": "en_US.utf8"},
                {"name": "analytics_engine_test", "charset": "UTF8", "collation": "en_US.utf8"} if environment != "prod" else None
            ],
            "connection_string_template": f"postgresql://{{username}}:{{password}}@{client_code}-{environment}-pg.postgres.database.azure.com:5432/analytics_engine?sslmode=require"
        }
        
        # Remove None entries
        db_config["databases"] = [db for db in db_config["databases"] if db]
        
        # TimescaleDB initialization script
        timescale_init = ""
        if enable_timescale:
            timescale_init = '''-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;

-- Create hypertables for time-series data
-- Example: Convert metrics table to hypertable
-- SELECT create_hypertable('metrics', 'timestamp');

-- Configure compression policy (for production)
-- ALTER TABLE metrics SET (
--   timescaledb.compress,
--   timescaledb.compress_segmentby = 'metric_id'
-- );

-- Add compression policy
-- SELECT add_compression_policy('metrics', INTERVAL '7 days');

-- Configure retention policy
-- SELECT add_retention_policy('metrics', INTERVAL '365 days');
'''
        
        # Store in context
        artifact_key = f"db_config_{client_code}_{environment}"
        context.artifacts[artifact_key] = {
            "config": db_config,
            "init_script": timescale_init
        }
        
        return {
            "success": True,
            "client_code": client_code,
            "environment": environment,
            "server_name": db_config["server_name"],
            "config": db_config,
            "timescale_init_script": timescale_init if enable_timescale else None
        }
    
    async def _generate_cicd_pipeline(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate CI/CD pipeline configuration."""
        client_code = tool_input.get("client_code", "client")
        pipeline_type = tool_input.get("pipeline_type", "github_actions")
        environments = tool_input.get("environments", ["dev", "staging", "prod"])
        include_tests = tool_input.get("include_tests", True)
        include_security = tool_input.get("include_security_scan", True)
        
        if pipeline_type == "github_actions":
            pipeline = f'''name: Analytics Engine CI/CD - {client_code}

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  ACR_NAME: {client_code}acr
  AKS_CLUSTER: {client_code}-prod-aks
  RESOURCE_GROUP: {client_code}-prod-rg-eastus

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
'''
            if include_tests:
                pipeline += '''
    - name: Run tests
      run: |
        pip install pytest pytest-cov
        pytest tests/ --cov=app --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
'''
            if include_security:
                pipeline += '''
    - name: Security scan
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'fs'
        scan-ref: '.'
        severity: 'CRITICAL,HIGH'
'''
            pipeline += '''
    - name: Login to ACR
      uses: azure/docker-login@v1
      with:
        login-server: ${{ env.ACR_NAME }}.azurecr.io
        username: ${{ secrets.ACR_USERNAME }}
        password: ${{ secrets.ACR_PASSWORD }}
    
    - name: Build and push images
      run: |
        docker build -t ${{ env.ACR_NAME }}.azurecr.io/api-gateway:${{ github.sha }} ./services/frontend_services/api_gateway
        docker push ${{ env.ACR_NAME }}.azurecr.io/api-gateway:${{ github.sha }}
'''
            for env_name in environments:
                pipeline += f'''
  deploy-{env_name}:
    needs: build
    runs-on: ubuntu-latest
    environment: {env_name}
    steps:
    - uses: actions/checkout@v4
    
    - name: Azure Login
      uses: azure/login@v1
      with:
        creds: ${{{{ secrets.AZURE_CREDENTIALS }}}}
    
    - name: Set AKS context
      uses: azure/aks-set-context@v3
      with:
        cluster-name: {client_code}-{env_name}-aks
        resource-group: {client_code}-{env_name}-rg-eastus
    
    - name: Deploy to {env_name}
      run: |
        kubectl set image deployment/api-gateway api-gateway=${{{{ env.ACR_NAME }}}}.azurecr.io/api-gateway:${{{{ github.sha }}}} -n {client_code}-analytics
'''
        else:  # azure_devops
            pipeline = f'''trigger:
  branches:
    include:
    - main
    - develop

pool:
  vmImage: 'ubuntu-latest'

variables:
  acrName: '{client_code}acr'
  aksCluster: '{client_code}-prod-aks'
  resourceGroup: '{client_code}-prod-rg-eastus'

stages:
- stage: Build
  jobs:
  - job: BuildAndTest
    steps:
    - task: UsePythonVersion@0
      inputs:
        versionSpec: '3.11'
'''
            if include_tests:
                pipeline += '''
    - script: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
        pytest tests/ --cov=app
      displayName: 'Run tests'
'''
            pipeline += '''
    - task: Docker@2
      inputs:
        containerRegistry: '$(acrName)'
        repository: 'api-gateway'
        command: 'buildAndPush'
        Dockerfile: 'services/frontend_services/api_gateway/Dockerfile'
        tags: '$(Build.BuildId)'
'''
        
        # Store in context
        artifact_key = f"cicd_pipeline_{client_code}"
        context.artifacts[artifact_key] = pipeline
        
        return {
            "success": True,
            "client_code": client_code,
            "pipeline_type": pipeline_type,
            "environments": environments,
            "pipeline": pipeline
        }
    
    async def _generate_helm_chart(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate Helm chart for deployment."""
        chart_name = tool_input.get("chart_name", "analytics-engine")
        client_code = tool_input.get("client_code", "client")
        values = tool_input.get("values", {})
        
        # Chart.yaml
        chart_yaml = f'''apiVersion: v2
name: {chart_name}
description: Analytics Engine Helm chart for {client_code}
type: application
version: 1.0.0
appVersion: "1.0.0"
maintainers:
  - name: Analytics Engine Team
    email: devops@{client_code}.com
'''
        
        # values.yaml
        values_yaml = f'''# Default values for {chart_name}
# Client: {client_code}

global:
  imageRegistry: "{client_code}acr.azurecr.io"
  imagePullSecrets:
    - name: acr-secret

replicaCount: 2

image:
  pullPolicy: IfNotPresent
  tag: "latest"

serviceAccount:
  create: true
  name: "{chart_name}-sa"

services:
  apiGateway:
    enabled: true
    replicas: 2
    port: 8000
    resources:
      requests:
        cpu: 250m
        memory: 512Mi
      limits:
        cpu: 500m
        memory: 1Gi

  conversationService:
    enabled: true
    replicas: 2
    port: 8004
    resources:
      requests:
        cpu: 500m
        memory: 1Gi
      limits:
        cpu: 1000m
        memory: 2Gi

  calculationEngine:
    enabled: true
    replicas: 3
    port: 8002
    resources:
      requests:
        cpu: 1000m
        memory: 2Gi
      limits:
        cpu: 2000m
        memory: 4Gi

  businessMetadata:
    enabled: true
    replicas: 2
    port: 8001
    resources:
      requests:
        cpu: 250m
        memory: 512Mi
      limits:
        cpu: 500m
        memory: 1Gi

postgresql:
  enabled: true
  host: "{client_code}-prod-pg.postgres.database.azure.com"
  port: 5432
  database: "analytics_engine"
  existingSecret: "postgres-credentials"

redis:
  enabled: true
  host: "{client_code}-prod-redis.redis.cache.windows.net"
  port: 6380
  ssl: true
  existingSecret: "redis-credentials"

ingress:
  enabled: true
  className: "nginx"
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
  hosts:
    - host: analytics.{client_code}.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: analytics-tls
      hosts:
        - analytics.{client_code}.com

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
'''
        
        helm_chart = {
            "Chart.yaml": chart_yaml,
            "values.yaml": values_yaml
        }
        
        # Store in context
        artifact_key = f"helm_chart_{client_code}"
        context.artifacts[artifact_key] = helm_chart
        
        return {
            "success": True,
            "chart_name": chart_name,
            "client_code": client_code,
            "files": list(helm_chart.keys()),
            "chart": helm_chart
        }
    
    async def _generate_deployment_checklist(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate deployment checklist and runbook."""
        client_code = tool_input.get("client_code", "client")
        environment = tool_input.get("environment", "prod")
        deployment_type = tool_input.get("deployment_type", "initial")
        
        if deployment_type == "initial":
            checklist = f'''# Analytics Engine Initial Deployment Checklist
## Client: {client_code}
## Environment: {environment}
## Date: {{{{DATE}}}}

## Pre-Deployment

### Azure Resources
- [ ] Resource Group created: `{client_code}-{environment}-rg-eastus`
- [ ] AKS cluster provisioned and healthy
- [ ] Azure PostgreSQL server created with TimescaleDB extension
- [ ] Azure Redis Cache provisioned
- [ ] Key Vault created with required secrets
- [ ] Container Registry (ACR) configured

### Secrets Configuration
- [ ] Database credentials stored in Key Vault
- [ ] Redis connection string stored in Key Vault
- [ ] API keys (OpenAI, Anthropic) stored in Key Vault
- [ ] TLS certificates uploaded

### Network Configuration
- [ ] VNet and subnets configured
- [ ] Network Security Groups applied
- [ ] Private endpoints configured (if required)
- [ ] DNS records created

## Deployment Steps

### 1. Database Setup
```bash
# Connect to PostgreSQL
psql -h {client_code}-{environment}-pg.postgres.database.azure.com -U adminuser -d analytics_engine

# Run initialization scripts
\\i scripts/init_timescaledb.sql
\\i scripts/create_schema.sql
```

### 2. Kubernetes Deployment
```bash
# Set context
az aks get-credentials --resource-group {client_code}-{environment}-rg-eastus --name {client_code}-{environment}-aks

# Create namespace
kubectl apply -f k8s/namespace.yaml

# Deploy secrets
kubectl apply -f k8s/secrets.yaml

# Deploy services
helm upgrade --install analytics-engine ./helm/analytics-engine -n {client_code}-analytics -f values-{environment}.yaml
```

### 3. Verification
- [ ] All pods running: `kubectl get pods -n {client_code}-analytics`
- [ ] Services accessible: `kubectl get svc -n {client_code}-analytics`
- [ ] Health endpoints responding
- [ ] Database connectivity verified
- [ ] Redis connectivity verified

## Post-Deployment

### Smoke Tests
- [ ] API Gateway health check
- [ ] Conversation Service health check
- [ ] Calculation Engine health check
- [ ] Business Metadata Service health check

### Monitoring Setup
- [ ] Azure Monitor configured
- [ ] Log Analytics workspace connected
- [ ] Alerts configured
- [ ] Dashboard created

## Rollback Procedure

If deployment fails:
```bash
helm rollback analytics-engine -n {client_code}-analytics
```

## Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DevOps Engineer | | | |
| QA Lead | | | |
| Project Manager | | | |
'''
        elif deployment_type == "upgrade":
            checklist = f'''# Analytics Engine Upgrade Checklist
## Client: {client_code}
## Environment: {environment}

## Pre-Upgrade
- [ ] Backup database
- [ ] Document current versions
- [ ] Review changelog
- [ ] Notify stakeholders

## Upgrade Steps
```bash
helm upgrade analytics-engine ./helm/analytics-engine -n {client_code}-analytics -f values-{environment}.yaml
```

## Verification
- [ ] All pods healthy
- [ ] No error logs
- [ ] Smoke tests pass

## Rollback (if needed)
```bash
helm rollback analytics-engine -n {client_code}-analytics
```
'''
        else:  # rollback
            checklist = f'''# Analytics Engine Rollback Procedure
## Client: {client_code}
## Environment: {environment}

## Immediate Actions
```bash
# Rollback to previous release
helm rollback analytics-engine -n {client_code}-analytics

# Verify rollback
kubectl get pods -n {client_code}-analytics
```

## Post-Rollback
- [ ] Verify all services healthy
- [ ] Check logs for errors
- [ ] Notify stakeholders
- [ ] Document incident
'''
        
        # Store in context
        artifact_key = f"deployment_checklist_{client_code}_{environment}"
        context.artifacts[artifact_key] = checklist
        
        return {
            "success": True,
            "client_code": client_code,
            "environment": environment,
            "deployment_type": deployment_type,
            "checklist": checklist
        }


# =============================================================================
# PROJECT MANAGER AGENT
# =============================================================================

PROJECT_MANAGER_SYSTEM_PROMPT = """You are the Project Manager Agent, an expert Agile Coach and Scrum Master with deep expertise in software project planning and delivery.

Your role is to analyze the scope of work defined by the design interview and generate comprehensive project artifacts including epics, sprints, and user stories/cards to guide implementation.

## Your Expertise

- Agile methodologies (Scrum, Kanban, SAFe)
- User story writing and acceptance criteria
- Sprint planning and capacity management
- Epic decomposition and feature breakdown
- Estimation techniques (story points, t-shirt sizing)
- Dependency mapping and critical path analysis
- Risk identification and mitigation planning
- Stakeholder communication

## Agile Principles You Apply

1. **Deliver working software frequently** - Break work into small, deliverable increments
2. **Welcome changing requirements** - Design sprints to accommodate learning
3. **Business and developers work together** - Stories reflect business value
4. **Simplicity** - Maximize work not done
5. **Self-organizing teams** - Cards are actionable without micromanagement

## Story Writing Standards

### User Story Format
```
As a [persona/role]
I want [feature/capability]
So that [business value/outcome]
```

### Acceptance Criteria Format (Given-When-Then)
```
Given [precondition]
When [action]
Then [expected result]
```

### Story Point Estimation (Fibonacci)
- **1 point**: Trivial change, < 2 hours
- **2 points**: Small task, half day
- **3 points**: Medium task, 1 day
- **5 points**: Larger task, 2-3 days
- **8 points**: Complex task, 1 week
- **13 points**: Very complex, should consider splitting

## Your Responsibilities

1. **Analyze Scope**: Review design artifacts from other agents
2. **Define Epics**: Create high-level epics representing major features
3. **Plan Sprints**: Organize work into 2-week sprint iterations
4. **Generate Cards**: Create detailed user stories with acceptance criteria
5. **Estimate Effort**: Assign story points based on complexity
6. **Map Dependencies**: Identify blockers and prerequisites
7. **Identify Risks**: Flag potential issues and mitigation strategies

## Output Format

When generating project artifacts, provide:
- Epic definitions with business objectives
- Sprint plans with goals and capacity
- User stories with acceptance criteria
- Story point estimates
- Dependency mappings
- Risk register entries

## Current Context

{context_summary}

Focus on creating actionable, well-defined work items that enable the development team to deliver value incrementally while maintaining quality.
"""


class ProjectManagerAgent(BaseAgent):
    """Project Manager Agent for Agile planning and work breakdown."""
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.PROJECT_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            temperature=0.4,
            tools=self._get_pm_tools()
        )
        super().__init__(config, api_key)
    
    def _get_pm_tools(self) -> List[ToolDefinition]:
        """Define tools available to the project manager."""
        return [
            ToolDefinition(
                name="create_epic",
                description="Create an epic representing a major feature or capability",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Epic title"},
                        "description": {"type": "string", "description": "Epic description and business objective"},
                        "business_value": {"type": "string", "description": "Why this epic matters to the business"},
                        "acceptance_criteria": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "High-level acceptance criteria for the epic"
                        },
                        "estimated_sprints": {
                            "type": "integer",
                            "description": "Estimated number of sprints to complete"
                        },
                        "priority": {
                            "type": "string",
                            "enum": ["critical", "high", "medium", "low"],
                            "description": "Priority level"
                        },
                        "dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Other epics or external dependencies"
                        }
                    },
                    "required": ["title", "description", "business_value"]
                }
            ),
            ToolDefinition(
                name="plan_sprint",
                description="Plan a sprint with goals, capacity, and selected stories",
                parameters={
                    "type": "object",
                    "properties": {
                        "sprint_number": {"type": "integer", "description": "Sprint number"},
                        "sprint_goal": {"type": "string", "description": "Primary goal for this sprint"},
                        "duration_days": {"type": "integer", "description": "Sprint duration in days", "default": 10},
                        "capacity_points": {"type": "integer", "description": "Team capacity in story points"},
                        "stories": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Story IDs included in this sprint"
                        },
                        "risks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Identified risks for this sprint"
                        },
                        "dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "External dependencies that must be resolved"
                        }
                    },
                    "required": ["sprint_number", "sprint_goal", "capacity_points"]
                }
            ),
            ToolDefinition(
                name="create_user_story",
                description="Create a user story card with acceptance criteria",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Story title"},
                        "epic": {"type": "string", "description": "Parent epic title"},
                        "persona": {"type": "string", "description": "User persona (As a...)"},
                        "want": {"type": "string", "description": "Feature/capability (I want...)"},
                        "so_that": {"type": "string", "description": "Business value (So that...)"},
                        "acceptance_criteria": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "given": {"type": "string"},
                                    "when": {"type": "string"},
                                    "then": {"type": "string"}
                                }
                            },
                            "description": "Acceptance criteria in Given-When-Then format"
                        },
                        "story_points": {
                            "type": "integer",
                            "enum": [1, 2, 3, 5, 8, 13],
                            "description": "Story point estimate"
                        },
                        "priority": {
                            "type": "string",
                            "enum": ["critical", "high", "medium", "low"],
                            "description": "Priority level"
                        },
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Labels/tags for categorization"
                        },
                        "blocked_by": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Stories that must be completed first"
                        }
                    },
                    "required": ["title", "epic", "persona", "want", "so_that", "story_points"]
                }
            ),
            ToolDefinition(
                name="create_technical_task",
                description="Create a technical task (non-user-facing work)",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Task title"},
                        "epic": {"type": "string", "description": "Parent epic title"},
                        "description": {"type": "string", "description": "Technical description"},
                        "task_type": {
                            "type": "string",
                            "enum": ["infrastructure", "refactoring", "spike", "documentation", "testing", "devops"],
                            "description": "Type of technical task"
                        },
                        "acceptance_criteria": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Definition of done"
                        },
                        "story_points": {
                            "type": "integer",
                            "enum": [1, 2, 3, 5, 8, 13],
                            "description": "Story point estimate"
                        },
                        "blocked_by": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Tasks that must be completed first"
                        }
                    },
                    "required": ["title", "epic", "description", "task_type", "story_points"]
                }
            ),
            ToolDefinition(
                name="generate_project_roadmap",
                description="Generate a high-level project roadmap from epics",
                parameters={
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Project name"},
                        "client_name": {"type": "string", "description": "Client name"},
                        "start_date": {"type": "string", "description": "Project start date (YYYY-MM-DD)"},
                        "sprint_duration_days": {"type": "integer", "description": "Sprint duration", "default": 10},
                        "team_velocity": {"type": "integer", "description": "Expected story points per sprint"},
                        "epics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Epic titles in priority order"
                        }
                    },
                    "required": ["project_name", "client_name", "team_velocity", "epics"]
                }
            ),
            ToolDefinition(
                name="identify_risks",
                description="Identify and document project risks with mitigation strategies",
                parameters={
                    "type": "object",
                    "properties": {
                        "risks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "description": {"type": "string"},
                                    "probability": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "impact": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "mitigation": {"type": "string"},
                                    "owner": {"type": "string"}
                                }
                            },
                            "description": "List of identified risks"
                        }
                    },
                    "required": ["risks"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("create_epic", self._create_epic)
        self.register_tool("plan_sprint", self._plan_sprint)
        self.register_tool("create_user_story", self._create_user_story)
        self.register_tool("create_technical_task", self._create_technical_task)
        self.register_tool("generate_project_roadmap", self._generate_project_roadmap)
        self.register_tool("identify_risks", self._identify_risks)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return PROJECT_MANAGER_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.value_chain_type:
            parts.append(f"Value Chain: {context.value_chain_type}")
        if context.identified_entities:
            parts.append(f"Entities: {', '.join(context.identified_entities[:10])}")
        if "bounded_contexts" in context.artifacts:
            bc_names = [bc["name"] for bc in context.artifacts["bounded_contexts"]]
            parts.append(f"Bounded Contexts: {', '.join(bc_names)}")
        if "aggregates" in context.artifacts:
            agg_names = [agg["name"] for agg in context.artifacts["aggregates"]]
            parts.append(f"Aggregates: {', '.join(agg_names)}")
        return "\n".join(parts) if parts else "No specific context provided."
    
    async def _create_epic(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create an epic."""
        import uuid
        
        title = tool_input.get("title", "")
        description = tool_input.get("description", "")
        business_value = tool_input.get("business_value", "")
        acceptance_criteria = tool_input.get("acceptance_criteria", [])
        estimated_sprints = tool_input.get("estimated_sprints", 1)
        priority = tool_input.get("priority", "medium")
        dependencies = tool_input.get("dependencies", [])
        
        epic_id = f"EPIC-{str(uuid.uuid4())[:8].upper()}"
        
        epic = {
            "id": epic_id,
            "title": title,
            "description": description,
            "business_value": business_value,
            "acceptance_criteria": acceptance_criteria,
            "estimated_sprints": estimated_sprints,
            "priority": priority,
            "dependencies": dependencies,
            "status": "backlog",
            "stories": []
        }
        
        # Store in context
        if "epics" not in context.artifacts:
            context.artifacts["epics"] = []
        context.artifacts["epics"].append(epic)
        
        return {
            "success": True,
            "epic": epic
        }
    
    async def _plan_sprint(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Plan a sprint."""
        sprint_number = tool_input.get("sprint_number", 1)
        sprint_goal = tool_input.get("sprint_goal", "")
        duration_days = tool_input.get("duration_days", 10)
        capacity_points = tool_input.get("capacity_points", 0)
        stories = tool_input.get("stories", [])
        risks = tool_input.get("risks", [])
        dependencies = tool_input.get("dependencies", [])
        
        sprint = {
            "sprint_number": sprint_number,
            "sprint_id": f"SPRINT-{sprint_number:03d}",
            "goal": sprint_goal,
            "duration_days": duration_days,
            "capacity_points": capacity_points,
            "committed_stories": stories,
            "risks": risks,
            "dependencies": dependencies,
            "status": "planned",
            "ceremonies": {
                "sprint_planning": f"Day 1",
                "daily_standup": "Daily",
                "sprint_review": f"Day {duration_days}",
                "retrospective": f"Day {duration_days}"
            }
        }
        
        # Store in context
        if "sprints" not in context.artifacts:
            context.artifacts["sprints"] = []
        context.artifacts["sprints"].append(sprint)
        
        return {
            "success": True,
            "sprint": sprint
        }
    
    async def _create_user_story(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create a user story."""
        import uuid
        
        title = tool_input.get("title", "")
        epic = tool_input.get("epic", "")
        persona = tool_input.get("persona", "")
        want = tool_input.get("want", "")
        so_that = tool_input.get("so_that", "")
        acceptance_criteria = tool_input.get("acceptance_criteria", [])
        story_points = tool_input.get("story_points", 3)
        priority = tool_input.get("priority", "medium")
        labels = tool_input.get("labels", [])
        blocked_by = tool_input.get("blocked_by", [])
        
        story_id = f"US-{str(uuid.uuid4())[:8].upper()}"
        
        story = {
            "id": story_id,
            "title": title,
            "epic": epic,
            "type": "user_story",
            "user_story": f"As a {persona}, I want {want}, so that {so_that}",
            "persona": persona,
            "want": want,
            "so_that": so_that,
            "acceptance_criteria": acceptance_criteria,
            "story_points": story_points,
            "priority": priority,
            "labels": labels,
            "blocked_by": blocked_by,
            "status": "backlog"
        }
        
        # Store in context
        if "stories" not in context.artifacts:
            context.artifacts["stories"] = []
        context.artifacts["stories"].append(story)
        
        return {
            "success": True,
            "story": story
        }
    
    async def _create_technical_task(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Create a technical task."""
        import uuid
        
        title = tool_input.get("title", "")
        epic = tool_input.get("epic", "")
        description = tool_input.get("description", "")
        task_type = tool_input.get("task_type", "infrastructure")
        acceptance_criteria = tool_input.get("acceptance_criteria", [])
        story_points = tool_input.get("story_points", 3)
        blocked_by = tool_input.get("blocked_by", [])
        
        task_id = f"TASK-{str(uuid.uuid4())[:8].upper()}"
        
        task = {
            "id": task_id,
            "title": title,
            "epic": epic,
            "type": "technical_task",
            "task_type": task_type,
            "description": description,
            "acceptance_criteria": acceptance_criteria,
            "story_points": story_points,
            "blocked_by": blocked_by,
            "status": "backlog"
        }
        
        # Store in context
        if "stories" not in context.artifacts:
            context.artifacts["stories"] = []
        context.artifacts["stories"].append(task)
        
        return {
            "success": True,
            "task": task
        }
    
    async def _generate_project_roadmap(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate a project roadmap."""
        project_name = tool_input.get("project_name", "")
        client_name = tool_input.get("client_name", "")
        start_date = tool_input.get("start_date", "TBD")
        sprint_duration_days = tool_input.get("sprint_duration_days", 10)
        team_velocity = tool_input.get("team_velocity", 30)
        epic_titles = tool_input.get("epics", [])
        
        # Calculate timeline based on epics
        roadmap_phases = []
        current_sprint = 1
        
        for epic_title in epic_titles:
            # Find epic in context if exists
            epic_data = None
            if "epics" in context.artifacts:
                for e in context.artifacts["epics"]:
                    if e["title"] == epic_title:
                        epic_data = e
                        break
            
            estimated_sprints = epic_data.get("estimated_sprints", 2) if epic_data else 2
            
            phase = {
                "epic": epic_title,
                "start_sprint": current_sprint,
                "end_sprint": current_sprint + estimated_sprints - 1,
                "estimated_points": team_velocity * estimated_sprints
            }
            roadmap_phases.append(phase)
            current_sprint += estimated_sprints
        
        total_sprints = current_sprint - 1
        total_weeks = total_sprints * (sprint_duration_days // 5)
        
        roadmap = {
            "project_name": project_name,
            "client_name": client_name,
            "start_date": start_date,
            "sprint_duration_days": sprint_duration_days,
            "team_velocity": team_velocity,
            "total_sprints": total_sprints,
            "estimated_duration_weeks": total_weeks,
            "phases": roadmap_phases,
            "milestones": [
                {"name": "Project Kickoff", "sprint": 1},
                {"name": "MVP Complete", "sprint": max(1, total_sprints // 2)},
                {"name": "UAT Ready", "sprint": max(1, total_sprints - 1)},
                {"name": "Go Live", "sprint": total_sprints}
            ]
        }
        
        # Store in context
        context.artifacts["project_roadmap"] = roadmap
        
        return {
            "success": True,
            "roadmap": roadmap
        }
    
    async def _identify_risks(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Identify and document project risks."""
        import uuid
        
        risks = tool_input.get("risks", [])
        
        risk_register = []
        for risk in risks:
            risk_id = f"RISK-{str(uuid.uuid4())[:8].upper()}"
            
            # Calculate risk score
            prob_score = {"low": 1, "medium": 2, "high": 3}.get(risk.get("probability", "medium"), 2)
            impact_score = {"low": 1, "medium": 2, "high": 3}.get(risk.get("impact", "medium"), 2)
            risk_score = prob_score * impact_score
            
            risk_entry = {
                "id": risk_id,
                "title": risk.get("title", ""),
                "description": risk.get("description", ""),
                "probability": risk.get("probability", "medium"),
                "impact": risk.get("impact", "medium"),
                "risk_score": risk_score,
                "risk_level": "high" if risk_score >= 6 else "medium" if risk_score >= 3 else "low",
                "mitigation": risk.get("mitigation", ""),
                "owner": risk.get("owner", "TBD"),
                "status": "open"
            }
            risk_register.append(risk_entry)
        
        # Sort by risk score descending
        risk_register.sort(key=lambda x: x["risk_score"], reverse=True)
        
        # Store in context
        context.artifacts["risk_register"] = risk_register
        
        return {
            "success": True,
            "risk_count": len(risk_register),
            "high_risks": len([r for r in risk_register if r["risk_level"] == "high"]),
            "risk_register": risk_register
        }


# =============================================================================
# ITIL MANAGER AGENT
# =============================================================================

class ITILManagerAgent(BaseAgent):
    """
    ITIL Manager Agent for IT Service Management based on ITIL 4 framework.
    
    Responsibilities:
    - Service Strategy and Design
    - Service Transition and Operation
    - Continual Service Improvement
    - Incident, Problem, and Change Management
    - Service Level Management
    - Configuration Management
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.ITIL_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_itil_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert ITIL Manager specializing in IT Service Management based on the ITIL 4 framework.

## Your Role
You ensure IT services are aligned with business needs and delivered efficiently using ITIL best practices.

## ITIL 4 Service Value System

### Guiding Principles
1. Focus on value
2. Start where you are
3. Progress iteratively with feedback
4. Collaborate and promote visibility
5. Think and work holistically
6. Keep it simple and practical
7. Optimize and automate

### Service Value Chain Activities
- **Plan**: Shared understanding of vision, current status, and improvement direction
- **Improve**: Continual improvement of products, services, and practices
- **Engage**: Good understanding of stakeholder needs and transparency
- **Design & Transition**: Products and services meet stakeholder expectations
- **Obtain/Build**: Service components are available when needed
- **Deliver & Support**: Services delivered according to agreed specifications

## ITIL 4 Practices

### General Management Practices
- Architecture management
- Continual improvement
- Information security management
- Knowledge management
- Measurement and reporting
- Organizational change management
- Portfolio management
- Project management
- Relationship management
- Risk management
- Service financial management
- Strategy management
- Supplier management
- Workforce and talent management

### Service Management Practices
- Availability management
- Business analysis
- Capacity and performance management
- Change enablement
- Incident management
- IT asset management
- Monitoring and event management
- Problem management
- Release management
- Service catalogue management
- Service configuration management
- Service continuity management
- Service design
- Service desk
- Service level management
- Service request management
- Service validation and testing

### Technical Management Practices
- Deployment management
- Infrastructure and platform management
- Software development and management

## Key Metrics
- Service Availability (%)
- Mean Time to Restore (MTTR)
- Mean Time Between Failures (MTBF)
- First Call Resolution Rate
- Change Success Rate
- Incident Volume and Trends
- Problem Resolution Time
- SLA Compliance Rate
- Customer Satisfaction Score
- Cost per Ticket

## Collaboration
- Works with Deployment Specialist for release management
- Collaborates with Risk & Compliance Officer for security and compliance
- Partners with Operations Manager for service delivery optimization
"""
    
    def _get_itil_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="log_incident",
                description="Log and categorize an IT incident",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Incident title"},
                        "category": {"type": "string", "enum": ["hardware", "software", "network", "security", "access", "other"], "description": "Incident category"},
                        "priority": {"type": "string", "enum": ["critical", "high", "medium", "low"], "description": "Priority level"},
                        "impact": {"type": "string", "enum": ["widespread", "significant", "moderate", "minor"], "description": "Business impact"},
                        "urgency": {"type": "string", "enum": ["critical", "high", "medium", "low"], "description": "Urgency level"},
                        "affected_service": {"type": "string", "description": "Affected service/system"},
                        "description": {"type": "string", "description": "Incident description"}
                    },
                    "required": ["title", "category", "priority"]
                }
            ),
            ToolDefinition(
                name="create_problem_record",
                description="Create a problem record for root cause analysis",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Problem title"},
                        "related_incidents": {"type": "array", "items": {"type": "string"}, "description": "Related incident IDs"},
                        "category": {"type": "string", "description": "Problem category"},
                        "root_cause": {"type": "string", "description": "Root cause if known"},
                        "workaround": {"type": "string", "description": "Temporary workaround"}
                    },
                    "required": ["title"]
                }
            ),
            ToolDefinition(
                name="submit_change_request",
                description="Submit a change request (RFC)",
                parameters={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Change title"},
                        "change_type": {"type": "string", "enum": ["standard", "normal", "emergency"], "description": "Change type"},
                        "category": {"type": "string", "enum": ["infrastructure", "application", "security", "network", "database"], "description": "Change category"},
                        "risk_level": {"type": "string", "enum": ["high", "medium", "low"], "description": "Risk level"},
                        "description": {"type": "string", "description": "Change description"},
                        "justification": {"type": "string", "description": "Business justification"},
                        "implementation_plan": {"type": "string", "description": "Implementation plan"},
                        "rollback_plan": {"type": "string", "description": "Rollback plan"},
                        "scheduled_date": {"type": "string", "description": "Scheduled implementation date"}
                    },
                    "required": ["title", "change_type", "description"]
                }
            ),
            ToolDefinition(
                name="define_service_level",
                description="Define or update a Service Level Agreement (SLA)",
                parameters={
                    "type": "object",
                    "properties": {
                        "service_name": {"type": "string", "description": "Service name"},
                        "availability_target": {"type": "number", "description": "Availability target (%)"},
                        "response_time_target": {"type": "string", "description": "Response time SLA"},
                        "resolution_time_target": {"type": "string", "description": "Resolution time SLA"},
                        "support_hours": {"type": "string", "description": "Support hours (e.g., 24x7, 8x5)"},
                        "escalation_path": {"type": "array", "items": {"type": "string"}, "description": "Escalation levels"}
                    },
                    "required": ["service_name", "availability_target"]
                }
            ),
            ToolDefinition(
                name="track_configuration_item",
                description="Track a Configuration Item (CI) in the CMDB",
                parameters={
                    "type": "object",
                    "properties": {
                        "ci_name": {"type": "string", "description": "CI name"},
                        "ci_type": {"type": "string", "enum": ["server", "application", "database", "network_device", "storage", "service"], "description": "CI type"},
                        "status": {"type": "string", "enum": ["active", "inactive", "planned", "retired"], "description": "CI status"},
                        "owner": {"type": "string", "description": "CI owner"},
                        "dependencies": {"type": "array", "items": {"type": "string"}, "description": "Dependent CIs"},
                        "attributes": {"type": "object", "description": "CI attributes"}
                    },
                    "required": ["ci_name", "ci_type", "status"]
                }
            ),
            ToolDefinition(
                name="measure_service_performance",
                description="Measure and report service performance metrics",
                parameters={
                    "type": "object",
                    "properties": {
                        "service_name": {"type": "string", "description": "Service name"},
                        "period": {"type": "string", "description": "Measurement period"},
                        "metrics": {"type": "object", "description": "Performance metrics"}
                    },
                    "required": ["service_name", "period"]
                }
            ),
            ToolDefinition(
                name="plan_continual_improvement",
                description="Create a Continual Service Improvement (CSI) initiative",
                parameters={
                    "type": "object",
                    "properties": {
                        "initiative_name": {"type": "string", "description": "Initiative name"},
                        "current_state": {"type": "string", "description": "Current state assessment"},
                        "target_state": {"type": "string", "description": "Target state"},
                        "improvement_actions": {"type": "array", "items": {"type": "string"}, "description": "Improvement actions"},
                        "success_metrics": {"type": "array", "items": {"type": "string"}, "description": "Success metrics"},
                        "priority": {"type": "string", "enum": ["high", "medium", "low"], "description": "Priority"}
                    },
                    "required": ["initiative_name", "current_state", "target_state"]
                }
            ),
            ToolDefinition(
                name="generate_itil_report",
                description="Generate ITIL service management report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["incident_summary", "problem_analysis", "change_calendar", "sla_compliance", "service_health", "csi_register"], "description": "Report type"},
                        "period": {"type": "string", "description": "Report period"},
                        "services": {"type": "array", "items": {"type": "string"}, "description": "Services to include"}
                    },
                    "required": ["report_type"]
                }
            ),
            # Collaboration tools
            ToolDefinition(
                name="request_deployment_review",
                description="Request Deployment Specialist to review release plan",
                parameters={
                    "type": "object",
                    "properties": {
                        "release_name": {"type": "string", "description": "Release name"},
                        "change_request_id": {"type": "string", "description": "Associated change request"},
                        "deployment_requirements": {"type": "array", "items": {"type": "string"}, "description": "Deployment requirements"}
                    },
                    "required": ["release_name"]
                }
            ),
            ToolDefinition(
                name="escalate_to_risk_compliance",
                description="Escalate security or compliance concern to Risk & Compliance Officer",
                parameters={
                    "type": "object",
                    "properties": {
                        "concern_type": {"type": "string", "enum": ["security_incident", "compliance_gap", "audit_finding", "policy_violation"], "description": "Type of concern"},
                        "description": {"type": "string", "description": "Concern description"},
                        "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"], "description": "Severity"}
                    },
                    "required": ["concern_type", "description", "severity"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "log_incident": self._log_incident,
            "create_problem_record": self._create_problem_record,
            "submit_change_request": self._submit_change_request,
            "define_service_level": self._define_service_level,
            "track_configuration_item": self._track_configuration_item,
            "measure_service_performance": self._measure_service_performance,
            "plan_continual_improvement": self._plan_continual_improvement,
            "generate_itil_report": self._generate_itil_report,
            "request_deployment_review": self._request_deployment_review,
            "escalate_to_risk_compliance": self._escalate_to_risk_compliance
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.client_name:
            parts.append(f"Client: {context.client_name}")
        if "itil_incidents" in context.artifacts:
            parts.append(f"Incidents: {len(context.artifacts['itil_incidents'])}")
        if "change_requests" in context.artifacts:
            parts.append(f"Changes: {len(context.artifacts['change_requests'])}")
        return " | ".join(parts) if parts else "No ITIL context"
    
    async def _log_incident(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        # Calculate priority matrix
        impact_map = {"widespread": 4, "significant": 3, "moderate": 2, "minor": 1}
        urgency_map = {"critical": 4, "high": 3, "medium": 2, "low": 1}
        
        impact_score = impact_map.get(tool_input.get("impact", "moderate"), 2)
        urgency_score = urgency_map.get(tool_input.get("urgency", "medium"), 2)
        priority_score = impact_score * urgency_score
        
        if priority_score >= 12:
            calculated_priority = "critical"
        elif priority_score >= 6:
            calculated_priority = "high"
        elif priority_score >= 3:
            calculated_priority = "medium"
        else:
            calculated_priority = "low"
        
        incident = {
            "id": f"INC-{str(uuid.uuid4())[:8].upper()}",
            "title": tool_input.get("title", ""),
            "category": tool_input.get("category", "other"),
            "priority": tool_input.get("priority", calculated_priority),
            "impact": tool_input.get("impact", "moderate"),
            "urgency": tool_input.get("urgency", "medium"),
            "affected_service": tool_input.get("affected_service", ""),
            "description": tool_input.get("description", ""),
            "status": "open",
            "logged_at": datetime.utcnow().isoformat()
        }
        
        if "itil_incidents" not in context.artifacts:
            context.artifacts["itil_incidents"] = []
        context.artifacts["itil_incidents"].append(incident)
        
        return {"success": True, "incident": incident}
    
    async def _create_problem_record(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        problem = {
            "id": f"PRB-{str(uuid.uuid4())[:8].upper()}",
            "title": tool_input.get("title", ""),
            "related_incidents": tool_input.get("related_incidents", []),
            "category": tool_input.get("category", ""),
            "root_cause": tool_input.get("root_cause", ""),
            "workaround": tool_input.get("workaround", ""),
            "status": "open",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "itil_problems" not in context.artifacts:
            context.artifacts["itil_problems"] = []
        context.artifacts["itil_problems"].append(problem)
        
        return {"success": True, "problem": problem}
    
    async def _submit_change_request(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        change_type = tool_input.get("change_type", "normal")
        
        # Determine approval requirements based on type and risk
        if change_type == "standard":
            approval_required = False
            cab_review = False
        elif change_type == "emergency":
            approval_required = True
            cab_review = True  # Emergency CAB
        else:  # normal
            risk_level = tool_input.get("risk_level", "medium")
            approval_required = True
            cab_review = risk_level in ["high", "medium"]
        
        change_request = {
            "id": f"CHG-{str(uuid.uuid4())[:8].upper()}",
            "title": tool_input.get("title", ""),
            "change_type": change_type,
            "category": tool_input.get("category", ""),
            "risk_level": tool_input.get("risk_level", "medium"),
            "description": tool_input.get("description", ""),
            "justification": tool_input.get("justification", ""),
            "implementation_plan": tool_input.get("implementation_plan", ""),
            "rollback_plan": tool_input.get("rollback_plan", ""),
            "scheduled_date": tool_input.get("scheduled_date", ""),
            "approval_required": approval_required,
            "cab_review": cab_review,
            "status": "submitted",
            "submitted_at": datetime.utcnow().isoformat()
        }
        
        if "change_requests" not in context.artifacts:
            context.artifacts["change_requests"] = []
        context.artifacts["change_requests"].append(change_request)
        
        return {"success": True, "change_request": change_request}
    
    async def _define_service_level(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        sla = {
            "id": f"SLA-{str(uuid.uuid4())[:8].upper()}",
            "service_name": tool_input.get("service_name", ""),
            "availability_target": tool_input.get("availability_target", 99.9),
            "response_time_target": tool_input.get("response_time_target", ""),
            "resolution_time_target": tool_input.get("resolution_time_target", ""),
            "support_hours": tool_input.get("support_hours", "8x5"),
            "escalation_path": tool_input.get("escalation_path", []),
            "status": "active",
            "defined_at": datetime.utcnow().isoformat()
        }
        
        if "service_levels" not in context.artifacts:
            context.artifacts["service_levels"] = []
        context.artifacts["service_levels"].append(sla)
        
        return {"success": True, "sla": sla}
    
    async def _track_configuration_item(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        ci = {
            "id": f"CI-{str(uuid.uuid4())[:8].upper()}",
            "ci_name": tool_input.get("ci_name", ""),
            "ci_type": tool_input.get("ci_type", "service"),
            "status": tool_input.get("status", "active"),
            "owner": tool_input.get("owner", ""),
            "dependencies": tool_input.get("dependencies", []),
            "attributes": tool_input.get("attributes", {}),
            "tracked_at": datetime.utcnow().isoformat()
        }
        
        if "configuration_items" not in context.artifacts:
            context.artifacts["configuration_items"] = []
        context.artifacts["configuration_items"].append(ci)
        
        return {"success": True, "configuration_item": ci}
    
    async def _measure_service_performance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        measurement = {
            "id": f"PERF-{str(uuid.uuid4())[:8].upper()}",
            "service_name": tool_input.get("service_name", ""),
            "period": tool_input.get("period", ""),
            "metrics": tool_input.get("metrics", {}),
            "measured_at": datetime.utcnow().isoformat()
        }
        
        if "service_measurements" not in context.artifacts:
            context.artifacts["service_measurements"] = []
        context.artifacts["service_measurements"].append(measurement)
        
        return {"success": True, "measurement": measurement}
    
    async def _plan_continual_improvement(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        csi = {
            "id": f"CSI-{str(uuid.uuid4())[:8].upper()}",
            "initiative_name": tool_input.get("initiative_name", ""),
            "current_state": tool_input.get("current_state", ""),
            "target_state": tool_input.get("target_state", ""),
            "improvement_actions": tool_input.get("improvement_actions", []),
            "success_metrics": tool_input.get("success_metrics", []),
            "priority": tool_input.get("priority", "medium"),
            "status": "planned",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "csi_initiatives" not in context.artifacts:
            context.artifacts["csi_initiatives"] = []
        context.artifacts["csi_initiatives"].append(csi)
        
        return {"success": True, "csi_initiative": csi}
    
    async def _generate_itil_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        report = {
            "id": f"ITIL-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "service_health"),
            "period": tool_input.get("period", ""),
            "services": tool_input.get("services", []),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts[f"itil_report_{report['report_type']}"] = report
        return {"success": True, "report": report}
    
    async def _request_deployment_review(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"DEP-REV-{str(uuid.uuid4())[:8].upper()}",
            "release_name": tool_input.get("release_name", ""),
            "change_request_id": tool_input.get("change_request_id", ""),
            "deployment_requirements": tool_input.get("deployment_requirements", []),
            "status": "pending_deployment_specialist",
            "collaboration_type": "itil_manager_to_deployment_specialist"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}
    
    async def _escalate_to_risk_compliance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        escalation = {
            "id": f"ESC-{str(uuid.uuid4())[:8].upper()}",
            "concern_type": tool_input.get("concern_type", ""),
            "description": tool_input.get("description", ""),
            "severity": tool_input.get("severity", "medium"),
            "status": "pending_risk_compliance",
            "collaboration_type": "itil_manager_to_risk_compliance"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(escalation)
        
        return {"success": True, "escalation": escalation}


# =============================================================================
# MAPPING SPECIALIST AGENT
# =============================================================================

class MappingSpecialistAgent(BaseAgent):
    """
    Mapping Specialist Agent for source-to-analytics attribute mapping.
    
    Responsibilities:
    - Assist users with mapping source system attributes to analytics attributes
    - Recommend mappings based on semantic similarity and data patterns
    - Identify transformation requirements
    - Validate data type compatibility
    - Accelerate the mapping exercise with intelligent suggestions
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.MAPPING_SPECIALIST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_mapping_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Mapping Specialist focused on accelerating source-to-analytics attribute mapping.

## Your Role
You help users efficiently map source system attributes to analytics model attributes, providing intelligent recommendations to speed up the mapping process.

## Core Responsibilities

### 1. Source Analysis
- Analyze source system schemas and data dictionaries
- Identify source attribute characteristics (data types, patterns, cardinality)
- Detect data quality issues in source attributes
- Profile source data distributions

### 2. Target Analysis
- Understand analytics model requirements
- Identify required transformations
- Map to standardized data types
- Align with dimensional modeling patterns

### 3. Mapping Recommendations
- Suggest mappings based on semantic similarity (name matching)
- Recommend mappings based on data pattern analysis
- Identify one-to-one, one-to-many, and many-to-one mappings
- Detect derived/calculated field requirements
- Flag unmapped required fields

### 4. Transformation Design
- Recommend data type conversions
- Suggest string transformations (case, trim, format)
- Design date/time standardization
- Create lookup/reference mappings
- Handle null value strategies

### 5. Validation
- Validate data type compatibility
- Check referential integrity requirements
- Identify potential data loss scenarios
- Verify business rule compliance

## Mapping Patterns
- **Direct Mapping**: Source → Target (1:1)
- **Concatenation**: Multiple sources → Single target
- **Split**: Single source → Multiple targets
- **Lookup**: Source + Reference → Target
- **Derived**: Calculation from source(s) → Target
- **Constant**: Static value → Target
- **Conditional**: Rule-based transformation

## Key Metrics
- Mapping Coverage (%)
- Auto-mapped Attributes (%)
- Manual Review Required (%)
- Transformation Complexity Score

## Collaboration
- Works with Data Analyst for analytics model understanding
- Collaborates with Developer for transformation implementation
- Partners with Data Governance for data quality rules
"""
    
    def _get_mapping_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_source_schema",
                description="Analyze source system schema for mapping",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_system": {"type": "string", "description": "Source system name (e.g., 'salesforce', 'sap', 'quickbooks')"},
                        "entity_name": {"type": "string", "description": "Entity/table name to analyze"},
                        "attributes": {"type": "array", "items": {"type": "object"}, "description": "List of source attributes with metadata"}
                    },
                    "required": ["source_system", "entity_name"]
                }
            ),
            ToolDefinition(
                name="recommend_mappings",
                description="Generate mapping recommendations for source attributes",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_attributes": {"type": "array", "items": {"type": "string"}, "description": "Source attribute names"},
                        "target_entity": {"type": "string", "description": "Target analytics entity"},
                        "target_attributes": {"type": "array", "items": {"type": "string"}, "description": "Available target attributes"},
                        "matching_strategy": {"type": "string", "enum": ["semantic", "pattern", "hybrid"], "description": "Matching strategy"}
                    },
                    "required": ["source_attributes", "target_entity"]
                }
            ),
            ToolDefinition(
                name="create_mapping_rule",
                description="Create a specific mapping rule",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_attribute": {"type": "string", "description": "Source attribute path"},
                        "target_attribute": {"type": "string", "description": "Target attribute path"},
                        "mapping_type": {"type": "string", "enum": ["direct", "transform", "lookup", "derived", "constant", "conditional"], "description": "Type of mapping"},
                        "transformation": {"type": "object", "description": "Transformation specification if needed"},
                        "null_handling": {"type": "string", "enum": ["pass_through", "default_value", "reject", "derive"], "description": "Null value handling"}
                    },
                    "required": ["source_attribute", "target_attribute", "mapping_type"]
                }
            ),
            ToolDefinition(
                name="validate_mapping",
                description="Validate a mapping for compatibility",
                parameters={
                    "type": "object",
                    "properties": {
                        "mapping_id": {"type": "string", "description": "Mapping rule ID to validate"},
                        "source_sample": {"type": "array", "description": "Sample source data"},
                        "validation_rules": {"type": "array", "items": {"type": "string"}, "description": "Validation rules to apply"}
                    },
                    "required": ["mapping_id"]
                }
            ),
            ToolDefinition(
                name="design_transformation",
                description="Design a data transformation",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_type": {"type": "string", "description": "Source data type"},
                        "target_type": {"type": "string", "description": "Target data type"},
                        "transformation_type": {"type": "string", "enum": ["type_cast", "format", "lookup", "calculation", "aggregation", "split", "concatenate"], "description": "Transformation type"},
                        "parameters": {"type": "object", "description": "Transformation parameters"}
                    },
                    "required": ["source_type", "target_type", "transformation_type"]
                }
            ),
            ToolDefinition(
                name="generate_mapping_report",
                description="Generate mapping status report",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_system": {"type": "string", "description": "Source system"},
                        "target_model": {"type": "string", "description": "Target analytics model"},
                        "include_unmapped": {"type": "boolean", "description": "Include unmapped attributes"}
                    },
                    "required": ["source_system", "target_model"]
                }
            ),
            ToolDefinition(
                name="suggest_derived_field",
                description="Suggest a derived/calculated field",
                parameters={
                    "type": "object",
                    "properties": {
                        "target_attribute": {"type": "string", "description": "Target attribute to derive"},
                        "available_sources": {"type": "array", "items": {"type": "string"}, "description": "Available source attributes"},
                        "business_logic": {"type": "string", "description": "Business logic description"}
                    },
                    "required": ["target_attribute", "available_sources"]
                }
            ),
            # Collaboration tools
            ToolDefinition(
                name="request_data_profiling",
                description="Request Data Analyst to profile source data",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_system": {"type": "string", "description": "Source system"},
                        "attributes": {"type": "array", "items": {"type": "string"}, "description": "Attributes to profile"},
                        "profiling_depth": {"type": "string", "enum": ["basic", "detailed", "comprehensive"], "description": "Profiling depth"}
                    },
                    "required": ["source_system", "attributes"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_source_schema": self._analyze_source_schema,
            "recommend_mappings": self._recommend_mappings,
            "create_mapping_rule": self._create_mapping_rule,
            "validate_mapping": self._validate_mapping,
            "design_transformation": self._design_transformation,
            "generate_mapping_report": self._generate_mapping_report,
            "suggest_derived_field": self._suggest_derived_field,
            "request_data_profiling": self._request_data_profiling
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.client_name:
            parts.append(f"Client: {context.client_name}")
        if "mapping_rules" in context.artifacts:
            parts.append(f"Mappings: {len(context.artifacts['mapping_rules'])}")
        if "source_schemas" in context.artifacts:
            parts.append(f"Source Schemas: {len(context.artifacts['source_schemas'])}")
        return " | ".join(parts) if parts else "No mapping context"
    
    async def _analyze_source_schema(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        analysis = {
            "id": f"SRC-{str(uuid.uuid4())[:8].upper()}",
            "source_system": tool_input.get("source_system", ""),
            "entity_name": tool_input.get("entity_name", ""),
            "attributes": tool_input.get("attributes", []),
            "attribute_count": len(tool_input.get("attributes", [])),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        if "source_schemas" not in context.artifacts:
            context.artifacts["source_schemas"] = []
        context.artifacts["source_schemas"].append(analysis)
        
        return {"success": True, "analysis": analysis}
    
    async def _recommend_mappings(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        source_attrs = tool_input.get("source_attributes", [])
        target_attrs = tool_input.get("target_attributes", [])
        
        # Generate recommendations (simplified logic - real implementation would use ML/NLP)
        recommendations = []
        for src in source_attrs:
            src_lower = src.lower().replace("_", "").replace("-", "")
            best_match = None
            best_score = 0
            
            for tgt in target_attrs:
                tgt_lower = tgt.lower().replace("_", "").replace("-", "")
                # Simple similarity check
                if src_lower == tgt_lower:
                    best_match = tgt
                    best_score = 100
                    break
                elif src_lower in tgt_lower or tgt_lower in src_lower:
                    if len(src_lower) / len(tgt_lower) > best_score / 100:
                        best_match = tgt
                        best_score = 70
            
            recommendations.append({
                "source": src,
                "recommended_target": best_match,
                "confidence": best_score,
                "mapping_type": "direct" if best_score == 100 else "review_required"
            })
        
        result = {
            "id": f"REC-{str(uuid.uuid4())[:8].upper()}",
            "target_entity": tool_input.get("target_entity", ""),
            "matching_strategy": tool_input.get("matching_strategy", "hybrid"),
            "recommendations": recommendations,
            "auto_mapped": len([r for r in recommendations if r["confidence"] >= 70]),
            "review_required": len([r for r in recommendations if r["confidence"] < 70]),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if "mapping_recommendations" not in context.artifacts:
            context.artifacts["mapping_recommendations"] = []
        context.artifacts["mapping_recommendations"].append(result)
        
        return {"success": True, "recommendations": result}
    
    async def _create_mapping_rule(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        rule = {
            "id": f"MAP-{str(uuid.uuid4())[:8].upper()}",
            "source_attribute": tool_input.get("source_attribute", ""),
            "target_attribute": tool_input.get("target_attribute", ""),
            "mapping_type": tool_input.get("mapping_type", "direct"),
            "transformation": tool_input.get("transformation", {}),
            "null_handling": tool_input.get("null_handling", "pass_through"),
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "mapping_rules" not in context.artifacts:
            context.artifacts["mapping_rules"] = []
        context.artifacts["mapping_rules"].append(rule)
        
        return {"success": True, "mapping_rule": rule}
    
    async def _validate_mapping(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        validation = {
            "id": f"VAL-{str(uuid.uuid4())[:8].upper()}",
            "mapping_id": tool_input.get("mapping_id", ""),
            "validation_rules": tool_input.get("validation_rules", []),
            "is_valid": True,  # Would be determined by actual validation
            "issues": [],
            "validated_at": datetime.utcnow().isoformat()
        }
        
        if "mapping_validations" not in context.artifacts:
            context.artifacts["mapping_validations"] = []
        context.artifacts["mapping_validations"].append(validation)
        
        return {"success": True, "validation": validation}
    
    async def _design_transformation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        transformation = {
            "id": f"XFORM-{str(uuid.uuid4())[:8].upper()}",
            "source_type": tool_input.get("source_type", ""),
            "target_type": tool_input.get("target_type", ""),
            "transformation_type": tool_input.get("transformation_type", "type_cast"),
            "parameters": tool_input.get("parameters", {}),
            "designed_at": datetime.utcnow().isoformat()
        }
        
        if "transformations" not in context.artifacts:
            context.artifacts["transformations"] = []
        context.artifacts["transformations"].append(transformation)
        
        return {"success": True, "transformation": transformation}
    
    async def _generate_mapping_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        mapping_rules = context.artifacts.get("mapping_rules", [])
        
        report = {
            "id": f"MAP-RPT-{str(uuid.uuid4())[:8].upper()}",
            "source_system": tool_input.get("source_system", ""),
            "target_model": tool_input.get("target_model", ""),
            "total_mappings": len(mapping_rules),
            "direct_mappings": len([m for m in mapping_rules if m.get("mapping_type") == "direct"]),
            "transform_mappings": len([m for m in mapping_rules if m.get("mapping_type") != "direct"]),
            "include_unmapped": tool_input.get("include_unmapped", False),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["mapping_report"] = report
        return {"success": True, "report": report}
    
    async def _suggest_derived_field(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        suggestion = {
            "id": f"DRV-{str(uuid.uuid4())[:8].upper()}",
            "target_attribute": tool_input.get("target_attribute", ""),
            "available_sources": tool_input.get("available_sources", []),
            "business_logic": tool_input.get("business_logic", ""),
            "suggested_formula": "",  # Would be generated based on logic
            "suggested_at": datetime.utcnow().isoformat()
        }
        
        if "derived_field_suggestions" not in context.artifacts:
            context.artifacts["derived_field_suggestions"] = []
        context.artifacts["derived_field_suggestions"].append(suggestion)
        
        return {"success": True, "suggestion": suggestion}
    
    async def _request_data_profiling(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"PROFILE-REQ-{str(uuid.uuid4())[:8].upper()}",
            "source_system": tool_input.get("source_system", ""),
            "attributes": tool_input.get("attributes", []),
            "profiling_depth": tool_input.get("profiling_depth", "basic"),
            "status": "pending_data_analyst",
            "collaboration_type": "mapping_specialist_to_data_analyst"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}


# =============================================================================
# CONNECTION SPECIALIST AGENT
# =============================================================================

class ConnectionSpecialistAgent(BaseAgent):
    """
    Connection Specialist Agent for designing and automating system connections.
    
    Responsibilities:
    - Design and automate connections to client systems
    - Create API wrappers for event-driven connections
    - Configure connectors for CRM, ERP, accounting platforms
    - Implement real-time data integration patterns
    - Accelerate connector service operations
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.CONNECTION_SPECIALIST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_connection_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Connection Specialist focused on designing and automating connections to client systems.

## Your Role
You help users rapidly design, configure, and deploy connections to external systems, enabling real-time data integration.

## Core Responsibilities

### 1. Connection Design
- Analyze target system APIs and integration options
- Design optimal connection architecture
- Select appropriate authentication methods
- Plan data flow patterns (push, pull, event-driven)

### 2. API Wrapper Development
- Generate API client code for target systems
- Implement authentication flows (OAuth2, API keys, JWT)
- Create typed request/response models
- Handle rate limiting and retry logic
- Implement error handling and logging

### 3. Connector Configuration
- Configure pre-built connectors
- Set up connection parameters
- Define sync schedules and triggers
- Configure field mappings
- Set up error notifications

### 4. Event-Driven Integration
- Design webhook receivers
- Implement event handlers
- Configure message queues (Redis, RabbitMQ)
- Set up real-time streaming
- Handle event ordering and deduplication

### 5. System-Specific Expertise

**CRM Systems**:
- Salesforce (REST API, Bulk API, Streaming API)
- HubSpot (API v3, webhooks)
- Microsoft Dynamics 365
- Pipedrive, Zoho CRM

**ERP Systems**:
- SAP (RFC, OData, IDoc)
- Oracle NetSuite (SuiteTalk, RESTlets)
- Microsoft Dynamics 365 Business Central
- Sage, Acumatica

**Accounting Platforms**:
- QuickBooks Online (OAuth 2.0, webhooks)
- Xero (OAuth 2.0, webhooks)
- FreshBooks, Wave
- Sage Intacct

**Other Systems**:
- E-commerce (Shopify, WooCommerce, Magento)
- Marketing (Mailchimp, Marketo, Pardot)
- Support (Zendesk, Freshdesk, Intercom)
- Databases (PostgreSQL, MySQL, MongoDB)

## Integration Patterns
- **REST API**: Standard HTTP-based integration
- **GraphQL**: Flexible query-based integration
- **Webhooks**: Event-driven push notifications
- **Polling**: Scheduled data pulls
- **CDC**: Change Data Capture for databases
- **ETL/ELT**: Batch data movement
- **Streaming**: Real-time data flow (Kafka, Redis Streams)

## Key Metrics
- Connection Success Rate
- Average Latency
- Data Freshness
- Error Rate
- Throughput (records/second)

## Collaboration
- Works with Developer for custom integration code
- Collaborates with Mapping Specialist for field mappings
- Partners with ITIL Manager for change management
"""
    
    def _get_connection_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_target_system",
                description="Analyze target system for integration options",
                parameters={
                    "type": "object",
                    "properties": {
                        "system_type": {"type": "string", "enum": ["crm", "erp", "accounting", "ecommerce", "marketing", "support", "database", "custom"], "description": "Type of system"},
                        "system_name": {"type": "string", "description": "Specific system name (e.g., 'salesforce', 'quickbooks')"},
                        "integration_requirements": {"type": "array", "items": {"type": "string"}, "description": "Required integration capabilities"}
                    },
                    "required": ["system_type", "system_name"]
                }
            ),
            ToolDefinition(
                name="design_connection",
                description="Design a connection architecture",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_system": {"type": "string", "description": "Source system"},
                        "target_system": {"type": "string", "description": "Target system (analytics engine)"},
                        "connection_type": {"type": "string", "enum": ["rest_api", "graphql", "webhook", "polling", "cdc", "streaming"], "description": "Connection type"},
                        "auth_method": {"type": "string", "enum": ["oauth2", "api_key", "jwt", "basic", "custom"], "description": "Authentication method"},
                        "sync_pattern": {"type": "string", "enum": ["real_time", "near_real_time", "scheduled", "on_demand"], "description": "Sync pattern"}
                    },
                    "required": ["source_system", "connection_type", "auth_method"]
                }
            ),
            ToolDefinition(
                name="generate_api_wrapper",
                description="Generate API wrapper code for a system",
                parameters={
                    "type": "object",
                    "properties": {
                        "system_name": {"type": "string", "description": "Target system name"},
                        "api_version": {"type": "string", "description": "API version"},
                        "endpoints": {"type": "array", "items": {"type": "string"}, "description": "Endpoints to wrap"},
                        "language": {"type": "string", "enum": ["python", "typescript", "java"], "description": "Target language"}
                    },
                    "required": ["system_name", "endpoints"]
                }
            ),
            ToolDefinition(
                name="configure_connector",
                description="Configure a connector instance",
                parameters={
                    "type": "object",
                    "properties": {
                        "connector_type": {"type": "string", "description": "Connector type"},
                        "connection_name": {"type": "string", "description": "Connection name"},
                        "credentials": {"type": "object", "description": "Credential configuration (keys only, not values)"},
                        "sync_config": {"type": "object", "description": "Sync configuration"},
                        "entities": {"type": "array", "items": {"type": "string"}, "description": "Entities to sync"}
                    },
                    "required": ["connector_type", "connection_name"]
                }
            ),
            ToolDefinition(
                name="setup_webhook_receiver",
                description="Set up a webhook receiver endpoint",
                parameters={
                    "type": "object",
                    "properties": {
                        "source_system": {"type": "string", "description": "Source system sending webhooks"},
                        "event_types": {"type": "array", "items": {"type": "string"}, "description": "Event types to receive"},
                        "endpoint_path": {"type": "string", "description": "Webhook endpoint path"},
                        "verification_method": {"type": "string", "enum": ["hmac", "token", "ip_whitelist", "none"], "description": "Verification method"}
                    },
                    "required": ["source_system", "event_types"]
                }
            ),
            ToolDefinition(
                name="create_event_handler",
                description="Create an event handler for incoming data",
                parameters={
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string", "description": "Event type to handle"},
                        "source_system": {"type": "string", "description": "Source system"},
                        "handler_logic": {"type": "string", "description": "Handler logic description"},
                        "target_entity": {"type": "string", "description": "Target analytics entity"}
                    },
                    "required": ["event_type", "source_system"]
                }
            ),
            ToolDefinition(
                name="test_connection",
                description="Test a connection configuration",
                parameters={
                    "type": "object",
                    "properties": {
                        "connection_id": {"type": "string", "description": "Connection ID to test"},
                        "test_type": {"type": "string", "enum": ["auth", "read", "write", "full"], "description": "Type of test"}
                    },
                    "required": ["connection_id"]
                }
            ),
            ToolDefinition(
                name="generate_connection_report",
                description="Generate connection status report",
                parameters={
                    "type": "object",
                    "properties": {
                        "connection_ids": {"type": "array", "items": {"type": "string"}, "description": "Connection IDs to report on"},
                        "include_metrics": {"type": "boolean", "description": "Include performance metrics"}
                    },
                    "required": []
                }
            ),
            # Collaboration tools
            ToolDefinition(
                name="request_mapping_assistance",
                description="Request Mapping Specialist to help with field mappings",
                parameters={
                    "type": "object",
                    "properties": {
                        "connection_id": {"type": "string", "description": "Connection ID"},
                        "source_entity": {"type": "string", "description": "Source entity"},
                        "target_entity": {"type": "string", "description": "Target entity"}
                    },
                    "required": ["connection_id", "source_entity"]
                }
            ),
            ToolDefinition(
                name="request_custom_development",
                description="Request Developer to create custom integration code",
                parameters={
                    "type": "object",
                    "properties": {
                        "integration_type": {"type": "string", "description": "Type of integration needed"},
                        "requirements": {"type": "array", "items": {"type": "string"}, "description": "Development requirements"},
                        "priority": {"type": "string", "enum": ["high", "medium", "low"], "description": "Priority"}
                    },
                    "required": ["integration_type", "requirements"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_target_system": self._analyze_target_system,
            "design_connection": self._design_connection,
            "generate_api_wrapper": self._generate_api_wrapper,
            "configure_connector": self._configure_connector,
            "setup_webhook_receiver": self._setup_webhook_receiver,
            "create_event_handler": self._create_event_handler,
            "test_connection": self._test_connection,
            "generate_connection_report": self._generate_connection_report,
            "request_mapping_assistance": self._request_mapping_assistance,
            "request_custom_development": self._request_custom_development
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.client_name:
            parts.append(f"Client: {context.client_name}")
        if "connections" in context.artifacts:
            parts.append(f"Connections: {len(context.artifacts['connections'])}")
        if "api_wrappers" in context.artifacts:
            parts.append(f"API Wrappers: {len(context.artifacts['api_wrappers'])}")
        return " | ".join(parts) if parts else "No connection context"
    
    async def _analyze_target_system(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        # System-specific integration options
        system_capabilities = {
            "salesforce": {"apis": ["REST", "Bulk", "Streaming", "Metadata"], "auth": ["oauth2"], "events": True},
            "hubspot": {"apis": ["REST v3"], "auth": ["oauth2", "api_key"], "events": True},
            "quickbooks": {"apis": ["REST"], "auth": ["oauth2"], "events": True},
            "xero": {"apis": ["REST"], "auth": ["oauth2"], "events": True},
            "sap": {"apis": ["OData", "RFC", "IDoc"], "auth": ["basic", "oauth2"], "events": False},
            "netsuite": {"apis": ["SuiteTalk", "RESTlet"], "auth": ["oauth2", "token"], "events": True},
        }
        
        system_name = tool_input.get("system_name", "").lower()
        capabilities = system_capabilities.get(system_name, {"apis": ["REST"], "auth": ["api_key"], "events": False})
        
        analysis = {
            "id": f"SYS-{str(uuid.uuid4())[:8].upper()}",
            "system_type": tool_input.get("system_type", ""),
            "system_name": tool_input.get("system_name", ""),
            "integration_requirements": tool_input.get("integration_requirements", []),
            "available_apis": capabilities.get("apis", []),
            "auth_methods": capabilities.get("auth", []),
            "supports_events": capabilities.get("events", False),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        if "system_analyses" not in context.artifacts:
            context.artifacts["system_analyses"] = []
        context.artifacts["system_analyses"].append(analysis)
        
        return {"success": True, "analysis": analysis}
    
    async def _design_connection(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        design = {
            "id": f"CONN-{str(uuid.uuid4())[:8].upper()}",
            "source_system": tool_input.get("source_system", ""),
            "target_system": tool_input.get("target_system", "analytics_engine"),
            "connection_type": tool_input.get("connection_type", "rest_api"),
            "auth_method": tool_input.get("auth_method", "oauth2"),
            "sync_pattern": tool_input.get("sync_pattern", "near_real_time"),
            "status": "designed",
            "designed_at": datetime.utcnow().isoformat()
        }
        
        if "connections" not in context.artifacts:
            context.artifacts["connections"] = []
        context.artifacts["connections"].append(design)
        
        return {"success": True, "connection_design": design}
    
    async def _generate_api_wrapper(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        wrapper = {
            "id": f"API-{str(uuid.uuid4())[:8].upper()}",
            "system_name": tool_input.get("system_name", ""),
            "api_version": tool_input.get("api_version", "v1"),
            "endpoints": tool_input.get("endpoints", []),
            "language": tool_input.get("language", "python"),
            "status": "generated",
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if "api_wrappers" not in context.artifacts:
            context.artifacts["api_wrappers"] = []
        context.artifacts["api_wrappers"].append(wrapper)
        
        return {"success": True, "api_wrapper": wrapper}
    
    async def _configure_connector(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        config = {
            "id": f"CFG-{str(uuid.uuid4())[:8].upper()}",
            "connector_type": tool_input.get("connector_type", ""),
            "connection_name": tool_input.get("connection_name", ""),
            "credentials": tool_input.get("credentials", {}),
            "sync_config": tool_input.get("sync_config", {}),
            "entities": tool_input.get("entities", []),
            "status": "configured",
            "configured_at": datetime.utcnow().isoformat()
        }
        
        if "connector_configs" not in context.artifacts:
            context.artifacts["connector_configs"] = []
        context.artifacts["connector_configs"].append(config)
        
        return {"success": True, "connector_config": config}
    
    async def _setup_webhook_receiver(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        webhook = {
            "id": f"WH-{str(uuid.uuid4())[:8].upper()}",
            "source_system": tool_input.get("source_system", ""),
            "event_types": tool_input.get("event_types", []),
            "endpoint_path": tool_input.get("endpoint_path", f"/webhooks/{tool_input.get('source_system', 'unknown')}"),
            "verification_method": tool_input.get("verification_method", "hmac"),
            "status": "configured",
            "configured_at": datetime.utcnow().isoformat()
        }
        
        if "webhook_receivers" not in context.artifacts:
            context.artifacts["webhook_receivers"] = []
        context.artifacts["webhook_receivers"].append(webhook)
        
        return {"success": True, "webhook_receiver": webhook}
    
    async def _create_event_handler(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        handler = {
            "id": f"EVT-{str(uuid.uuid4())[:8].upper()}",
            "event_type": tool_input.get("event_type", ""),
            "source_system": tool_input.get("source_system", ""),
            "handler_logic": tool_input.get("handler_logic", ""),
            "target_entity": tool_input.get("target_entity", ""),
            "status": "created",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "event_handlers" not in context.artifacts:
            context.artifacts["event_handlers"] = []
        context.artifacts["event_handlers"].append(handler)
        
        return {"success": True, "event_handler": handler}
    
    async def _test_connection(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        test_result = {
            "id": f"TEST-{str(uuid.uuid4())[:8].upper()}",
            "connection_id": tool_input.get("connection_id", ""),
            "test_type": tool_input.get("test_type", "auth"),
            "success": True,  # Would be actual test result
            "latency_ms": 150,  # Would be measured
            "tested_at": datetime.utcnow().isoformat()
        }
        
        if "connection_tests" not in context.artifacts:
            context.artifacts["connection_tests"] = []
        context.artifacts["connection_tests"].append(test_result)
        
        return {"success": True, "test_result": test_result}
    
    async def _generate_connection_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        connections = context.artifacts.get("connections", [])
        
        report = {
            "id": f"CONN-RPT-{str(uuid.uuid4())[:8].upper()}",
            "connection_ids": tool_input.get("connection_ids", [c["id"] for c in connections]),
            "total_connections": len(connections),
            "active_connections": len([c for c in connections if c.get("status") != "inactive"]),
            "include_metrics": tool_input.get("include_metrics", False),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["connection_report"] = report
        return {"success": True, "report": report}
    
    async def _request_mapping_assistance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"MAP-ASSIST-{str(uuid.uuid4())[:8].upper()}",
            "connection_id": tool_input.get("connection_id", ""),
            "source_entity": tool_input.get("source_entity", ""),
            "target_entity": tool_input.get("target_entity", ""),
            "status": "pending_mapping_specialist",
            "collaboration_type": "connection_specialist_to_mapping_specialist"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}
    
    async def _request_custom_development(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"DEV-REQ-{str(uuid.uuid4())[:8].upper()}",
            "integration_type": tool_input.get("integration_type", ""),
            "requirements": tool_input.get("requirements", []),
            "priority": tool_input.get("priority", "medium"),
            "status": "pending_developer",
            "collaboration_type": "connection_specialist_to_developer"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}


class DocumentAnalyzerAgent(BaseAgent):
    """
    Document Analyzer Agent - Analyzes documentation provided by interviewees.
    
    Extracts business entities, processes, KPIs, relationships, and requirements
    from various document types to accelerate the analytics model design process.
    """
    
    SYSTEM_PROMPT = """You are an expert Document Analyzer specializing in extracting 
structured business intelligence from unstructured documentation. Your role is to analyze 
documents provided by interviewees and decompose them into actionable insights that feed 
into the analytics model design.

## Document Types You Analyze

1. **Business Documents**
   - Business plans and strategy documents
   - Annual reports and investor presentations
   - Organizational charts and process maps
   - Policy and procedure manuals

2. **Technical Documents**
   - System architecture diagrams
   - API documentation
   - Database schemas and ERDs
   - Integration specifications

3. **Data Documents**
   - Data dictionaries
   - Report specifications
   - Dashboard mockups
   - KPI definitions

4. **Operational Documents**
   - Process flow diagrams
   - Standard operating procedures (SOPs)
   - Workflow documentation
   - Requirements specifications

## Extraction Capabilities

For each document, you extract:
- **Entities**: Business objects, data entities, actors
- **Processes**: Business processes, workflows, procedures
- **Metrics/KPIs**: Performance indicators, success measures
- **Relationships**: Entity relationships, process dependencies
- **Requirements**: Functional and non-functional requirements
- **Terminology**: Domain-specific terms for ubiquitous language

## Analysis Approach

1. **Document Classification**: Identify document type and purpose
2. **Content Extraction**: Extract text, tables, diagrams
3. **Entity Recognition**: Identify business entities and concepts
4. **Relationship Mapping**: Map connections between entities
5. **KPI Identification**: Extract metrics and success measures
6. **Gap Analysis**: Identify missing information for model design
7. **Synthesis**: Consolidate findings into structured output

## Integration with Model Design

Your extracted findings are used by:
- **Architect Agent**: For bounded context and entity design
- **Business Analyst Agent**: For KPI identification
- **Data Analyst Agent**: For metric design
- **Mapping Specialist Agent**: For source-to-target mapping

Always provide confidence scores for extracted information and flag ambiguities 
that require clarification from the interviewee."""

    def __init__(self, config: Optional[AgentConfig] = None):
        if config is None:
            config = AgentConfig(
                role=AgentRole.DOCUMENT_ANALYZER,
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                temperature=0.3
            )
        super().__init__(config)
        self._register_tools()
    
    def _get_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_document",
                description="Analyze a document to extract structured business intelligence",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Unique identifier for the document"
                        },
                        "document_name": {
                            "type": "string",
                            "description": "Name of the document"
                        },
                        "document_type": {
                            "type": "string",
                            "enum": ["business_plan", "technical_spec", "data_dictionary", 
                                     "process_map", "requirements", "report_spec", "api_doc",
                                     "org_chart", "policy", "sop", "other"],
                            "description": "Type of document being analyzed"
                        },
                        "content": {
                            "type": "string",
                            "description": "Document content (text extracted from file)"
                        },
                        "source_system": {
                            "type": "string",
                            "description": "Source system the document relates to (if applicable)"
                        }
                    },
                    "required": ["document_id", "document_name", "document_type", "content"]
                }
            ),
            ToolDefinition(
                name="extract_entities",
                description="Extract business entities from analyzed document",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract entities from"
                        },
                        "entity_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Types of entities to extract (e.g., 'customer', 'product', 'order')"
                        },
                        "include_attributes": {
                            "type": "boolean",
                            "description": "Whether to extract entity attributes"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="extract_processes",
                description="Extract business processes and workflows from document",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract processes from"
                        },
                        "include_steps": {
                            "type": "boolean",
                            "description": "Whether to extract individual process steps"
                        },
                        "include_actors": {
                            "type": "boolean",
                            "description": "Whether to identify actors/roles in processes"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="extract_kpis",
                description="Extract KPIs and metrics from document",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract KPIs from"
                        },
                        "categorize": {
                            "type": "boolean",
                            "description": "Whether to categorize KPIs by type"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="extract_relationships",
                description="Extract entity relationships from document",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract relationships from"
                        },
                        "relationship_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Types of relationships to look for"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="extract_terminology",
                description="Extract domain-specific terminology for ubiquitous language",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract terminology from"
                        },
                        "include_definitions": {
                            "type": "boolean",
                            "description": "Whether to include term definitions"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="extract_data_sources",
                description="Extract data source information from technical documents",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to extract data sources from"
                        },
                        "include_schemas": {
                            "type": "boolean",
                            "description": "Whether to extract schema information"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="identify_gaps",
                description="Identify information gaps that need clarification",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID to analyze for gaps"
                        },
                        "target_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Areas to check for gaps (entities, processes, kpis, relationships)"
                        }
                    },
                    "required": ["document_id"]
                }
            ),
            ToolDefinition(
                name="generate_document_summary",
                description="Generate a comprehensive summary of document analysis",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Document IDs to include in summary"
                        },
                        "include_recommendations": {
                            "type": "boolean",
                            "description": "Whether to include recommendations for model design"
                        }
                    },
                    "required": ["document_ids"]
                }
            ),
            ToolDefinition(
                name="request_architect_review",
                description="Request Architect to review extracted entities for DDD design",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID with extracted entities"
                        },
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entity names to review"
                        },
                        "context": {
                            "type": "string",
                            "description": "Additional context for the architect"
                        }
                    },
                    "required": ["document_id", "entities"]
                }
            ),
            ToolDefinition(
                name="request_business_analyst_review",
                description="Request Business Analyst to review extracted KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "document_id": {
                            "type": "string",
                            "description": "Document ID with extracted KPIs"
                        },
                        "kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPI names to review"
                        },
                        "industry_context": {
                            "type": "string",
                            "description": "Industry context for KPI validation"
                        }
                    },
                    "required": ["document_id", "kpis"]
                }
            )
        ]
    
    def _register_tools(self):
        self._tool_handlers = {
            "analyze_document": self._analyze_document,
            "extract_entities": self._extract_entities,
            "extract_processes": self._extract_processes,
            "extract_kpis": self._extract_kpis,
            "extract_relationships": self._extract_relationships,
            "extract_terminology": self._extract_terminology,
            "extract_data_sources": self._extract_data_sources,
            "identify_gaps": self._identify_gaps,
            "generate_document_summary": self._generate_document_summary,
            "request_architect_review": self._request_architect_review,
            "request_business_analyst_review": self._request_business_analyst_review
        }
    
    def get_context_summary(self, context: AgentContext) -> str:
        analyzed_docs = context.artifacts.get("analyzed_documents", [])
        extracted_entities = context.artifacts.get("extracted_entities", [])
        extracted_kpis = context.artifacts.get("extracted_kpis", [])
        
        return f"""Document Analysis Context:
- Analyzed Documents: {len(analyzed_docs)}
- Extracted Entities: {len(extracted_entities)}
- Extracted KPIs: {len(extracted_kpis)}
- Documents: {', '.join([d.get('document_name', 'Unknown') for d in analyzed_docs[:5]])}"""
    
    async def _analyze_document(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        document = {
            "id": tool_input.get("document_id", f"DOC-{str(uuid.uuid4())[:8].upper()}"),
            "document_name": tool_input.get("document_name", ""),
            "document_type": tool_input.get("document_type", "other"),
            "source_system": tool_input.get("source_system"),
            "content_length": len(tool_input.get("content", "")),
            "analysis_status": "analyzed",
            "analyzed_at": datetime.utcnow().isoformat(),
            "extraction_summary": {
                "entities_found": 0,
                "processes_found": 0,
                "kpis_found": 0,
                "relationships_found": 0,
                "terminology_terms": 0
            },
            "confidence_score": 0.85
        }
        
        if "analyzed_documents" not in context.artifacts:
            context.artifacts["analyzed_documents"] = []
        context.artifacts["analyzed_documents"].append(document)
        
        if "document_contents" not in context.artifacts:
            context.artifacts["document_contents"] = {}
        context.artifacts["document_contents"][document["id"]] = tool_input.get("content", "")
        
        return {"success": True, "document": document}
    
    async def _extract_entities(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        document_id = tool_input.get("document_id", "")
        entity_types = tool_input.get("entity_types", [])
        include_attributes = tool_input.get("include_attributes", True)
        
        extraction = {
            "id": f"ENT-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": document_id,
            "entity_types_requested": entity_types,
            "entities": [],
            "include_attributes": include_attributes,
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.80
        }
        
        if "extracted_entities" not in context.artifacts:
            context.artifacts["extracted_entities"] = []
        context.artifacts["extracted_entities"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _extract_processes(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        extraction = {
            "id": f"PROC-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "include_steps": tool_input.get("include_steps", True),
            "include_actors": tool_input.get("include_actors", True),
            "processes": [],
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.75
        }
        
        if "extracted_processes" not in context.artifacts:
            context.artifacts["extracted_processes"] = []
        context.artifacts["extracted_processes"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _extract_kpis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        extraction = {
            "id": f"KPI-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "categorize": tool_input.get("categorize", True),
            "kpis": [],
            "categories": [],
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.82
        }
        
        if "extracted_kpis" not in context.artifacts:
            context.artifacts["extracted_kpis"] = []
        context.artifacts["extracted_kpis"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _extract_relationships(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        extraction = {
            "id": f"REL-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "relationship_types": tool_input.get("relationship_types", []),
            "relationships": [],
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.78
        }
        
        if "extracted_relationships" not in context.artifacts:
            context.artifacts["extracted_relationships"] = []
        context.artifacts["extracted_relationships"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _extract_terminology(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        extraction = {
            "id": f"TERM-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "include_definitions": tool_input.get("include_definitions", True),
            "terms": [],
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.88
        }
        
        if "extracted_terminology" not in context.artifacts:
            context.artifacts["extracted_terminology"] = []
        context.artifacts["extracted_terminology"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _extract_data_sources(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        extraction = {
            "id": f"DS-EXT-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "include_schemas": tool_input.get("include_schemas", True),
            "data_sources": [],
            "extracted_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.85
        }
        
        if "extracted_data_sources" not in context.artifacts:
            context.artifacts["extracted_data_sources"] = []
        context.artifacts["extracted_data_sources"].append(extraction)
        
        return {"success": True, "extraction": extraction}
    
    async def _identify_gaps(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        target_areas = tool_input.get("target_areas", ["entities", "processes", "kpis", "relationships"])
        
        gap_analysis = {
            "id": f"GAP-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "target_areas": target_areas,
            "gaps": [],
            "clarification_questions": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        if "gap_analyses" not in context.artifacts:
            context.artifacts["gap_analyses"] = []
        context.artifacts["gap_analyses"].append(gap_analysis)
        
        return {"success": True, "gap_analysis": gap_analysis}
    
    async def _generate_document_summary(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        document_ids = tool_input.get("document_ids", [])
        
        summary = {
            "id": f"DOC-SUM-{str(uuid.uuid4())[:8].upper()}",
            "document_ids": document_ids,
            "total_documents": len(document_ids),
            "include_recommendations": tool_input.get("include_recommendations", True),
            "summary": {
                "total_entities": len(context.artifacts.get("extracted_entities", [])),
                "total_processes": len(context.artifacts.get("extracted_processes", [])),
                "total_kpis": len(context.artifacts.get("extracted_kpis", [])),
                "total_relationships": len(context.artifacts.get("extracted_relationships", [])),
                "total_terms": len(context.artifacts.get("extracted_terminology", []))
            },
            "recommendations": [],
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["document_summary"] = summary
        return {"success": True, "summary": summary}
    
    async def _request_architect_review(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"ARCH-REV-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "entities": tool_input.get("entities", []),
            "context": tool_input.get("context", ""),
            "status": "pending_architect",
            "collaboration_type": "document_analyzer_to_architect"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}
    
    async def _request_business_analyst_review(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        import uuid
        
        request = {
            "id": f"BA-REV-{str(uuid.uuid4())[:8].upper()}",
            "document_id": tool_input.get("document_id", ""),
            "kpis": tool_input.get("kpis", []),
            "industry_context": tool_input.get("industry_context", ""),
            "status": "pending_business_analyst",
            "collaboration_type": "document_analyzer_to_business_analyst"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}
