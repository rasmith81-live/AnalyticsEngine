"""Service for instantiating Pydantic models from database data."""

from typing import Dict, Any, Type, TypeVar, Optional
from pydantic import BaseModel

# Import ontology models from local module
from ..ontology_models import (
    NodeDefinition,
    EdgeDefinition,
    ProcessDefinition,
    EntityDefinition,
    MetricDefinition,
    ValueChainPatternDefinition,
    ValueSetDefinition,
    CodeSystemDefinition,
    ConstraintDefinition,
    DesignPolicyDefinition,
    InterviewSessionDefinition,
    UtteranceDefinition,
    BusinessIntentDefinition,
    PatternMatchDefinition,
    DesignSuggestionDefinition,
    CompanyValueChainModelDefinition,
    ActorDefinition,
    BeneficiaryDefinition,
    ClientDefinition,
    RoleDefinition,
    PermissionDefinition,
    ModulePermissionDefinition,
    EntityPermissionDefinition,
    MetricPermissionDefinition,
    AttributePermissionDefinition,
    RowLevelSecurityDefinition,
    CountryDefinition,
    RegionDefinition,
    MetropolitanAreaDefinition,
    NAICSIndustryDefinition,
    CompanyDefinition,
    BusinessProcessDefinition,
    StrategicObjectiveDefinition,
    BenchmarkDefinition,
    AnalyticsStrategyDefinition,
    DataSourceDefinition,
    DataProductDefinition,
    AnalyticsUseCaseDefinition,
    DimensionDefinition,
    MetricCategoryDefinition,
    DataQualityRuleDefinition,
    ExternalEventDefinition,
)

T = TypeVar('T', bound=NodeDefinition)


class MetadataInstantiationService:
    """Instantiates Pydantic models from database JSONB data.
    
    Provides bidirectional conversion:
    - JSONB dict → Pydantic model (for reads)
    - Pydantic model → JSONB dict (for writes)
    """
    
    # Map kind → Pydantic class
    KIND_TO_CLASS: Dict[str, Type[NodeDefinition]] = {
        "entity_definition": EntityDefinition,
        "process_definition": ProcessDefinition,
        "metric_definition": MetricDefinition,
        "value_chain_pattern_definition": ValueChainPatternDefinition,
        "edge_definition": EdgeDefinition,
        "relationship_definition": EdgeDefinition,  # Backward compatibility
        "value_set_definition": ValueSetDefinition,
        "code_system_definition": CodeSystemDefinition,
        "constraint_definition": ConstraintDefinition,
        "design_policy_definition": DesignPolicyDefinition,
        "interview_session_definition": InterviewSessionDefinition,
        "utterance_definition": UtteranceDefinition,
        "business_intent_definition": BusinessIntentDefinition,
        "pattern_match_definition": PatternMatchDefinition,
        "design_suggestion_definition": DesignSuggestionDefinition,
        "company_value_chain_model_definition": CompanyValueChainModelDefinition,
        # Business ontology classes
        "actor_definition": ActorDefinition,
        "beneficiary_definition": BeneficiaryDefinition,
        "company_definition": CompanyDefinition,
        "business_process_definition": BusinessProcessDefinition,
        "strategic_objective_definition": StrategicObjectiveDefinition,
        "benchmark_definition": BenchmarkDefinition,
        # Authorization / Access Control classes
        "client_definition": ClientDefinition,
        "role_definition": RoleDefinition,
        "permission_definition": PermissionDefinition,
        "module_permission_definition": ModulePermissionDefinition,
        "entity_permission_definition": EntityPermissionDefinition,
        "metric_permission_definition": MetricPermissionDefinition,
        "attribute_permission_definition": AttributePermissionDefinition,
        "row_level_security_definition": RowLevelSecurityDefinition,
        # Geographic & Industry Classification classes
        "country_definition": CountryDefinition,
        "region_definition": RegionDefinition,
        "metropolitan_area_definition": MetropolitanAreaDefinition,
        "naics_industry_definition": NAICSIndustryDefinition,
        # Analytics Strategy & Data Management classes
        "analytics_strategy_definition": AnalyticsStrategyDefinition,
        "data_source_definition": DataSourceDefinition,
        "data_product_definition": DataProductDefinition,
        "analytics_use_case_definition": AnalyticsUseCaseDefinition,
        "dimension_definition": DimensionDefinition,
        "metric_category_definition": MetricCategoryDefinition,
        "data_quality_rule_definition": DataQualityRuleDefinition,
        "external_event_definition": ExternalEventDefinition,
    }
    
    def instantiate(
        self,
        kind: str,
        data: Dict[str, Any]
    ) -> NodeDefinition:
        """Instantiate Pydantic model from JSONB data.
        
        Args:
            kind: Type of definition (e.g., "entity_definition")
            data: JSONB data from database
            
        Returns:
            Instantiated Pydantic model
            
        Raises:
            ValueError: If kind is unknown
            ValidationError: If data doesn't match schema
        """
        model_class = self.KIND_TO_CLASS.get(kind)
        if not model_class:
            raise ValueError(f"Unknown kind: {kind}. Valid kinds: {list(self.KIND_TO_CLASS.keys())}")
        
        # Pydantic v2 validation
        return model_class.model_validate(data)
    
    def serialize(
        self,
        definition: NodeDefinition
    ) -> Dict[str, Any]:
        """Serialize Pydantic model to JSONB-ready dict.
        
        Args:
            definition: Pydantic model instance
            
        Returns:
            Dict ready for JSONB storage
        """
        return definition.model_dump(mode='json', exclude_none=False)
    
    def get_kind_from_model(self, definition: NodeDefinition) -> str:
        """Extract kind from Pydantic model.
        
        Args:
            definition: Pydantic model instance
            
        Returns:
            Kind string (e.g., "entity_definition")
        """
        return definition.kind
    
    def get_code_from_model(self, definition: NodeDefinition) -> Optional[str]:
        """Extract code from Pydantic model if it has one.
        
        Args:
            definition: Pydantic model instance
            
        Returns:
            Code string or None
        """
        return getattr(definition, 'code', None)
    
    def get_name_from_model(self, definition: NodeDefinition) -> str:
        """Extract name from Pydantic model.
        
        Args:
            definition: Pydantic model instance
            
        Returns:
            Name string
        """
        return definition.name
    
    def validate_kind(self, kind: str) -> bool:
        """Check if kind is valid.
        
        Args:
            kind: Kind string to validate
            
        Returns:
            True if valid, False otherwise
        """
        return kind in self.KIND_TO_CLASS
    
    def get_all_kinds(self) -> list[str]:
        """Get list of all valid kinds.
        
        Returns:
            List of kind strings
        """
        return list(self.KIND_TO_CLASS.keys())
