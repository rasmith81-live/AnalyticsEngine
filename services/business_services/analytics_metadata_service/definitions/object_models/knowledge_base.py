"""
Knowledge Base Object Model

Represents knowledge base for customer self-service and education.
"""

KNOWLEDGE_BASE = {
    "code": "KNOWLEDGE_BASE",
    "name": "Knowledge Base",
    "description": "Knowledge base for customer self-service and education",
    "table_schema": {"table_name": "knowledge_base", "class_name": "Knowledge Base", "columns": [{"name": "kb_id", "type": "Integer", "index": True}, {"name": "article_count", "type": "Integer"}, {"name": "utilization_rate", "type": "Float"}, {"name": "search_count", "type": "Integer"}, {"name": "self_service_success_rate", "type": "Float"}, {"name": "article_views", "type": "String", "length": 255}, {"name": "helpful_votes", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_knowledge_base_kb_id", "columns": ["kb_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
KnowledgeBase "1" -- "0..*" Article : contains >
Customer "0..*" -- "0..*" Article : accesses >
KnowledgeBase "1" -- "0..*" SearchQuery : receives >
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
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["KNOWLEDGE_BASE_UTILIZATION_RATE", "CUSTOMER_SELF_SERVICE_SUCCESS_RATE", "CUSTOMER_KNOWLEDGE_RETENTION_RATE"], "key_attributes": ["kb_id", "article_count", "utilization_rate", "search_count", "self_service_success_rate", "article_views", "helpful_votes"], "related_objects": ["Account", "Account Penetration", "Appointment", "Assessment", "Certification", "Channel Deal", "Competitive Analysis", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Lead Qualification", "Lost Sale", "Market Segment", "Meeting", "Opportunity", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard"]},
}
