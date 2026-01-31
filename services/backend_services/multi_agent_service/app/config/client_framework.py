# =============================================================================
# Client Framework Configuration
# Industry-agnostic framework definitions loaded from client configuration
# =============================================================================
"""
Client-defined industry framework configuration.

This module provides the schema and loading mechanism for client-specific
value chain frameworks and industry configurations. The system is designed
to be completely industry-agnostic - all industry-specific knowledge
(SCOR, APQC, custom frameworks) comes from client configuration.

Usage:
    # Client defines their framework in metadata service
    framework = ClientFramework(
        code="retail_value_chain",
        name="Retail Value Chain",
        industry="Retail",
        modules=[
            ModuleDefinition(code="sourcing", name="Sourcing", ...),
            ModuleDefinition(code="fulfillment", name="Fulfillment", ...),
        ],
        kpi_templates=[...],
        relationships=[...]
    )
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class FrameworkType(str, Enum):
    """Types of industry frameworks supported."""
    SCOR = "scor"              # Supply Chain Operations Reference
    APQC = "apqc"              # APQC Process Classification Framework
    ITIL = "itil"              # IT Infrastructure Library
    COBIT = "cobit"            # Control Objectives for IT
    CUSTOM = "custom"          # Client-defined custom framework
    HYBRID = "hybrid"          # Combination of standard frameworks


class ModuleDefinition(BaseModel):
    """Definition of a value chain module."""
    code: str = Field(..., description="Unique module code")
    name: str = Field(..., description="Display name")
    description: str = Field(default="", description="Module description")
    parent_code: Optional[str] = Field(default=None, description="Parent module for hierarchy")
    sequence: int = Field(default=0, description="Display sequence in value chain")
    icon: Optional[str] = Field(default=None, description="UI icon identifier")
    color: Optional[str] = Field(default=None, description="UI color code")
    tags: List[str] = Field(default_factory=list, description="Categorization tags")


class KPITemplate(BaseModel):
    """Template for a KPI definition."""
    code: str = Field(..., description="Unique KPI code")
    name: str = Field(..., description="Display name")
    description: str = Field(default="", description="KPI description")
    formula: str = Field(..., description="Calculation formula")
    unit: str = Field(..., description="Unit of measure")
    module_code: str = Field(..., description="Associated value chain module")
    required_entities: List[str] = Field(default_factory=list, description="Required entity codes")
    aggregation_type: str = Field(default="sum", description="How to aggregate (sum, avg, count, etc.)")
    time_dimension: bool = Field(default=True, description="Whether KPI is time-based")
    benchmark_low: Optional[float] = Field(default=None, description="Industry benchmark low")
    benchmark_high: Optional[float] = Field(default=None, description="Industry benchmark high")
    tags: List[str] = Field(default_factory=list, description="Categorization tags")


class RelationshipDefinition(BaseModel):
    """Definition of a relationship between modules or entities."""
    source_code: str = Field(..., description="Source module/entity code")
    target_code: str = Field(..., description="Target module/entity code")
    relationship_type: str = Field(..., description="Type of relationship (flows_to, depends_on, etc.)")
    description: str = Field(default="", description="Relationship description")
    weight: float = Field(default=1.0, description="Relationship strength/weight")


class ClientFramework(BaseModel):
    """
    Complete client framework configuration.
    
    This is the master configuration that defines a client's
    industry-specific value chain, modules, KPIs, and relationships.
    """
    code: str = Field(..., description="Unique framework code")
    name: str = Field(..., description="Framework display name")
    description: str = Field(default="", description="Framework description")
    
    # Industry context (client-defined, not hardcoded)
    industry: str = Field(..., description="Client's industry")
    sub_industry: Optional[str] = Field(default=None, description="Sub-industry if applicable")
    
    # Framework type and optional base
    framework_type: FrameworkType = Field(default=FrameworkType.CUSTOM)
    base_framework: Optional[str] = Field(
        default=None, 
        description="Base framework this extends (e.g., 'scor_level1' if using SCOR)"
    )
    
    # Value chain structure
    modules: List[ModuleDefinition] = Field(
        default_factory=list,
        description="Value chain modules"
    )
    
    # KPI templates
    kpi_templates: List[KPITemplate] = Field(
        default_factory=list,
        description="KPI templates for this framework"
    )
    
    # Relationships
    relationships: List[RelationshipDefinition] = Field(
        default_factory=list,
        description="Relationships between modules"
    )
    
    # Metadata
    version: str = Field(default="1.0.0", description="Framework version")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: Optional[str] = Field(default=None, description="User who created")
    
    # Agent guidance
    agent_instructions: Dict[str, str] = Field(
        default_factory=dict,
        description="Role-specific instructions for agents working with this framework"
    )
    
    def get_module(self, code: str) -> Optional[ModuleDefinition]:
        """Get module by code."""
        for module in self.modules:
            if module.code == code:
                return module
        return None
    
    def get_kpis_for_module(self, module_code: str) -> List[KPITemplate]:
        """Get all KPI templates for a module."""
        return [kpi for kpi in self.kpi_templates if kpi.module_code == module_code]
    
    def get_module_hierarchy(self) -> Dict[str, List[ModuleDefinition]]:
        """Get modules organized by parent."""
        hierarchy = {"root": []}
        for module in self.modules:
            parent = module.parent_code or "root"
            if parent not in hierarchy:
                hierarchy[parent] = []
            hierarchy[parent].append(module)
        return hierarchy


class ClientConfiguration(BaseModel):
    """
    Complete client configuration including framework and settings.
    
    This is loaded from the database/metadata service for each client.
    """
    client_id: str = Field(..., description="Unique client identifier")
    client_name: str = Field(..., description="Client display name")
    
    # Primary framework
    framework: ClientFramework = Field(..., description="Client's value chain framework")
    
    # Additional frameworks (for multi-industry clients)
    additional_frameworks: List[ClientFramework] = Field(
        default_factory=list,
        description="Additional frameworks for different business units"
    )
    
    # Agent customization
    agent_preferences: Dict[str, Any] = Field(
        default_factory=dict,
        description="Client-specific agent behavior preferences"
    )
    
    # Data source mappings
    data_source_mappings: Dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of framework entities to client data sources"
    )
    
    # Active status
    is_active: bool = Field(default=True)
    
    def get_all_modules(self) -> List[ModuleDefinition]:
        """Get all modules across all frameworks."""
        modules = list(self.framework.modules)
        for fw in self.additional_frameworks:
            modules.extend(fw.modules)
        return modules
    
    def get_all_kpi_templates(self) -> List[KPITemplate]:
        """Get all KPI templates across all frameworks."""
        templates = list(self.framework.kpi_templates)
        for fw in self.additional_frameworks:
            templates.extend(fw.kpi_templates)
        return templates


# =============================================================================
# Framework Loader (integrates with metadata service)
# =============================================================================

class FrameworkLoader:
    """
    Loads client framework configuration from metadata service.
    
    This is the integration point between agents and client configuration.
    """
    
    def __init__(self, metadata_client=None):
        """
        Initialize with metadata client.
        
        Args:
            metadata_client: MetadataEventClient for loading from service
        """
        self.metadata_client = metadata_client
        self._cache: Dict[str, ClientConfiguration] = {}
    
    async def load_client_config(self, client_id: str) -> Optional[ClientConfiguration]:
        """
        Load client configuration from metadata service.
        
        Args:
            client_id: Client identifier
            
        Returns:
            ClientConfiguration if found, None otherwise
        """
        # Check cache first
        if client_id in self._cache:
            return self._cache[client_id]
        
        # Load from metadata service
        if self.metadata_client:
            try:
                config_data = await self.metadata_client.get_client_configuration(client_id)
                if config_data:
                    config = ClientConfiguration(**config_data)
                    self._cache[client_id] = config
                    return config
            except Exception:
                pass
        
        return None
    
    async def get_framework(self, client_id: str) -> Optional[ClientFramework]:
        """Get client's primary framework."""
        config = await self.load_client_config(client_id)
        return config.framework if config else None
    
    async def get_kpi_templates(
        self, 
        client_id: str, 
        module_code: Optional[str] = None
    ) -> List[KPITemplate]:
        """
        Get KPI templates for client, optionally filtered by module.
        
        Args:
            client_id: Client identifier
            module_code: Optional module filter
            
        Returns:
            List of KPI templates
        """
        config = await self.load_client_config(client_id)
        if not config:
            return []
        
        templates = config.get_all_kpi_templates()
        if module_code:
            templates = [t for t in templates if t.module_code == module_code]
        return templates
    
    async def get_agent_instructions(
        self, 
        client_id: str, 
        agent_role: str
    ) -> Optional[str]:
        """
        Get client-specific instructions for an agent role.
        
        Args:
            client_id: Client identifier
            agent_role: Agent role name
            
        Returns:
            Instructions string if defined, None otherwise
        """
        config = await self.load_client_config(client_id)
        if not config:
            return None
        
        return config.framework.agent_instructions.get(agent_role)
    
    def clear_cache(self, client_id: Optional[str] = None):
        """Clear cached configurations."""
        if client_id:
            self._cache.pop(client_id, None)
        else:
            self._cache.clear()
