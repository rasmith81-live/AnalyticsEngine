"""
Purchase History Object Model

Represents customer purchase history and patterns.
"""

PURCHASE_HISTORY = {
    "code": "PURCHASE_HISTORY",
    "name": "Purchase History",
    "description": "Customer purchase history and buying patterns",
    "table_schema": {"table_name": "purchase_history", "class_name": "Purchase History", "columns": [{"name": "history_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "total_purchases", "type": "String", "length": 255}, {"name": "total_value", "type": "Float"}, {"name": "average_purchase_value", "type": "Float"}, {"name": "purchase_frequency", "type": "String", "length": 255}, {"name": "last_purchase_date", "type": "DateTime", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_purchase_history_history_id", "columns": ["history_id"]}, {"name": "ix_purchase_history_customer_id", "columns": ["customer_id"]}, {"name": "ix_purchase_history_last_purchase_date", "columns": ["last_purchase_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "1" PurchaseHistory : has >
PurchaseHistory "1" -- "0..*" Purchase : contains >
Purchase "0..*" -- "1..*" Product : includes >
' Relationships to Related Objects
PurchaseHistory "1" -- "*" Contract : relates to
PurchaseHistory "1" -- "*" Customer : relates to
PurchaseHistory "1" -- "*" CustomerAdvocacyProgram : relates to
PurchaseHistory "1" -- "*" CustomerCohort : relates to
PurchaseHistory "1" -- "*" CustomerCommunity : relates to
PurchaseHistory "1" -- "*" CustomerEducation : relates to
PurchaseHistory "1" -- "*" CustomerFeedback : relates to
PurchaseHistory "1" -- "*" CustomerGoal : relates to
PurchaseHistory "1" -- "*" CustomerHealthRecord : relates to
PurchaseHistory "1" -- "*" CustomerJourney : relates to
PurchaseHistory "1" -- "*" CustomerOnboarding : relates to
PurchaseHistory "1" -- "*" CustomerSegment : relates to
PurchaseHistory "1" -- "*" CustomerSuccessManager : relates to
PurchaseHistory "1" -- "*" PerformanceBenchmark : relates to
PurchaseHistory "1" -- "*" PerformanceScorecard : relates to
PurchaseHistory "1" -- "*" ProductAdoption : relates to
PurchaseHistory "1" -- "*" ProductUsage : relates to
PurchaseHistory "1" -- "*" RenewalManagement : relates to
PurchaseHistory "1" -- "*" RevenueForecast : relates to
PurchaseHistory "1" -- "*" Sale : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"], "related_kpis": ["REPEAT_PURCHASE_RATE", "TIME_BETWEEN_PURCHASES", "UPSELLCROSS_SELL_CONVERSION_RATE"], "key_attributes": ["history_id", "customer_id", "total_purchases", "total_value", "average_purchase_value", "purchase_frequency", "last_purchase_date"], "related_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Performance Benchmark", "Performance Scorecard", "Product Adoption", "Product Usage", "Renewal Management", "Revenue Forecast", "Sale"]},
}
