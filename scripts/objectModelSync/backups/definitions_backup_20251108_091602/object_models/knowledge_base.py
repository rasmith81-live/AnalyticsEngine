"""
Knowledge Base Object Model

Represents knowledge base for customer self-service and education.
"""

from analytics_models import ObjectModel

KNOWLEDGE_BASE = ObjectModel(
    name="Knowledge Base",
    code="KNOWLEDGE_BASE",
    description="Knowledge base for customer self-service and education",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class KnowledgeBase {
}

class Article {
}

class Customer {
}

class SearchQuery {
}

' Relationships
KnowledgeBase "1" -- "0..*" Article : contains >
Customer "0..*" -- "0..*" Article : accesses >
KnowledgeBase "1" -- "0..*" SearchQuery : receives >

@enduml

' Relationships to Related Objects
KnowledgeBase "1" -- "*" Account : relates to
KnowledgeBase "1" -- "*" AccountPenetration : relates to
KnowledgeBase "1" -- "*" Appointment : relates to
KnowledgeBase "1" -- "*" Assessment : relates to
KnowledgeBase "1" -- "*" Certification : relates to
KnowledgeBase "1" -- "*" ChannelDeal : relates to
KnowledgeBase "1" -- "*" CompetitiveAnalysis : relates to
KnowledgeBase "1" -- "*" Deal : relates to
KnowledgeBase "1" -- "*" EnablementFeedback : relates to
KnowledgeBase "1" -- "*" EnablementPlatform : relates to
KnowledgeBase "1" -- "*" Lead : relates to
KnowledgeBase "1" -- "*" LeadQualification : relates to
KnowledgeBase "1" -- "*" LostSale : relates to
KnowledgeBase "1" -- "*" MarketSegment : relates to
KnowledgeBase "1" -- "*" Meeting : relates to
KnowledgeBase "1" -- "*" Opportunity : relates to
KnowledgeBase "1" -- "*" PartnerPerformanceScorecard : relates to
KnowledgeBase "1" -- "*" PartnerTraining : relates to
KnowledgeBase "1" -- "*" PerformanceBenchmark : relates to
KnowledgeBase "1" -- "*" PerformanceScorecard : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "KNOWLEDGE_BASE_UTILIZATION_RATE",
            "CUSTOMER_SELF_SERVICE_SUCCESS_RATE",
            "CUSTOMER_KNOWLEDGE_RETENTION_RATE"
        ],
        "key_attributes": [
            "kb_id",
            "article_count",
            "utilization_rate",
            "search_count",
            "self_service_success_rate",
            "article_views",
            "helpful_votes"
        ],
        "related_objects": ["Account", "Account Penetration", "Appointment", "Assessment", "Certification", "Channel Deal", "Competitive Analysis", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Lead Qualification", "Lost Sale", "Market Segment", "Meeting", "Opportunity", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard"]}
)
