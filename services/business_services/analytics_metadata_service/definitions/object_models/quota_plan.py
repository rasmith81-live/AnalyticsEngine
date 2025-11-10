"""
Quota Plan Object Model

Represents sales quota plans and attainment tracking.
"""

QUOTA_PLAN = {
    "code": "QUOTA_PLAN",
    "name": "Quota Plan",
    "description": "Sales quota plans and attainment tracking",
    "table_schema": {"table_name": "quota_plan", "class_name": "Quota Plan", "columns": [{"name": "plan_id", "type": "Integer", "index": True}, {"name": "rep_id", "type": "Integer", "index": True}, {"name": "period", "type": "String", "length": 255}, {"name": "quota_amount", "type": "Float"}, {"name": "attainment_percentage", "type": "Float"}, {"name": "compensation", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_quota_plan_plan_id", "columns": ["plan_id"]}, {"name": "ix_quota_plan_rep_id", "columns": ["rep_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesOperationsTeam "1" -- "0..*" QuotaPlan : creates >
QuotaPlan "1" -- "1" SalesRepresentative : assigned to >
QuotaPlan "1" -- "1" Compensation : drives >
' Relationships to Related Objects
QuotaPlan "1" -- "*" AccountPlan : relates to
QuotaPlan "1" -- "*" CompetitiveAnalysis : relates to
QuotaPlan "1" -- "*" Deal : relates to
QuotaPlan "1" -- "*" KnowledgeBase : relates to
QuotaPlan "1" -- "*" Meeting : relates to
QuotaPlan "1" -- "*" Opportunity : relates to
QuotaPlan "1" -- "*" PartnerTraining : relates to
QuotaPlan "1" -- "*" PerformanceBenchmark : relates to
QuotaPlan "1" -- "*" PerformanceScorecard : relates to
QuotaPlan "1" -- "*" ProductAdoption : relates to
QuotaPlan "1" -- "*" ProductUsage : relates to
QuotaPlan "1" -- "*" SalesPipeline : relates to
QuotaPlan "1" -- "*" SupportTicket : relates to
QuotaPlan "1" -- "*" TerritoryAssignment : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["QUOTA_ATTAINMENT_RATE", "REVENUE_PER_SALES_REPRESENTATIVE"], "key_attributes": ["plan_id", "rep_id", "period", "quota_amount", "attainment_percentage", "compensation"], "related_objects": ["Account Plan", "Competitive Analysis", "Deal", "Knowledge Base", "Meeting", "Opportunity", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Product Adoption", "Product Usage", "Sales Pipeline", "Support Ticket", "Territory Assignment"]},
}
