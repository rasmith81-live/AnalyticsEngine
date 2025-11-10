"""
Product Object Model

Represents products or services being sold.
"""

from analytics_models import ObjectModel

PRODUCT = ObjectModel(
    name="Product",
    code="PRODUCT",
    description="Products or services offered by the company",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "product",
        "class_name": "Product",
        "columns": [
            {
                "name": "product_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "product_code",
                "type": "String",
                "length": 255
            },
            {
                "name": "category",
                "type": "String",
                "length": 255
            },
            {
                "name": "base_price",
                "type": "String",
                "length": 255
            },
            {
                "name": "cost",
                "type": "String",
                "length": 255
            },
            {
                "name": "margin",
                "type": "String",
                "length": 255
            },
            {
                "name": "is_active",
                "type": "Boolean",
                "default": "False"
            },
            {
                "name": "return_rate",
                "type": "Float"
            },
            {
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            },
            {
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            }
        ],
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Sales Entities
' Customer Entities
' Customer Success & Retention
' Key Account Management
' Shared
' Relationships - Sales
Product "1..*" -- "0..*" Deal : included in >
Product "1..*" -- "0..*" Sale : sold in >
Product "1..*" -- "0..*" Opportunity : featured in >
Product "1..*" -- "0..*" ChannelDeal : sold through >
Product "1..*" -- "0..*" Demo : demonstrated in >
' Relationships - Customer
Product "0..*" -- "0..*" Customer : used by >
Product "1..*" -- "0..*" Subscription : included in >
Product "1..*" -- "0..*" Contract : covered by >
' Relationships - Usage & Adoption
Product "1" -- "0..*" ProductUsage : tracked by >
Product "1" -- "0..*" ProductAdoption : adopted through >
Product "0..*" -- "0..*" CustomerEducation : taught in >
' Relationships - Key Account Management
Product "0..*" -- "0..*" AccountPenetration : measured in >
Product "0..*" -- "0..*" AccountPlan : included in >
' Relationships - Shared
Product "1" -- "0..*" ProductReturn : subject of >
Product "1" -- "1..*" Pricing : has >
' Related Objects
' Relationships to Related Objects
Product "1" -- "*" Account : relates to
Product "1" -- "*" Appointment : relates to
Product "1" -- "*" Benchmark : relates to
Product "1" -- "*" Certification : relates to
Product "1" -- "*" ChannelPartner : relates to
Product "1" -- "*" CoachingSession : relates to
Product "1" -- "*" Contract : relates to
Product "1" -- "*" Customer : relates to
Product "1" -- "*" Deal : relates to
Product "1" -- "*" Demo : relates to
Product "1" -- "*" Goal : relates to
Product "1" -- "*" Lead : relates to
Product "1" -- "*" Opportunity : relates to
Product "1" -- "*" Sale : relates to
Product "1" -- "*" SalesContent : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "INVENTORY_MGMT"],
        "related_kpis": [
            "PRODUCT_RETURN_RATE",
            "UPSELLING_RATE",
            "CROSS_SELLING_RATE"
        ],
        "key_attributes": [
            "product_name",
            "product_code",
            "category",
            "base_price",
            "cost",
            "margin",
            "is_active",
            "return_rate"
        ],
        "related_objects": ["Account", "Appointment", "Benchmark", "Certification", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Goal", "Lead", "Opportunity", "Sale", "Sales Content"]}

)
