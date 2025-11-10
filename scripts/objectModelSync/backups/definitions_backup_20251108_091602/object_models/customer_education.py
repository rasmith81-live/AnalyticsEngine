"""
Customer Education Object Model

Represents customer education content and engagement.
"""

from analytics_models import ObjectModel

CUSTOMER_EDUCATION = ObjectModel(
    name="Customer Education",
    code="CUSTOMER_EDUCATION",
    description="Customer education content and engagement tracking",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerEducation {
}

class Customer {
}

class EducationContent {
}

class EngagementRecord {
}

' Relationships
CustomerEducation "1" -- "0..*" EducationContent : contains >
Customer "0..*" -- "0..*" EducationContent : consumes >
Customer "1" -- "0..*" EngagementRecord : has >
EngagementRecord "0..*" -- "1" EducationContent : for >

@enduml

' Relationships to Related Objects
CustomerEducation "1" -- "*" Account : relates to
CustomerEducation "1" -- "*" AccountPenetration : relates to
CustomerEducation "1" -- "*" AccountPlan : relates to
CustomerEducation "1" -- "*" AccountRisk : relates to
CustomerEducation "1" -- "*" Call : relates to
CustomerEducation "1" -- "*" ChannelConflict : relates to
CustomerEducation "1" -- "*" ChannelDeal : relates to
CustomerEducation "1" -- "*" ChannelMarket : relates to
CustomerEducation "1" -- "*" ChannelPartner : relates to
CustomerEducation "1" -- "*" ChurnEvent : relates to
CustomerEducation "1" -- "*" CompetitiveAnalysis : relates to
CustomerEducation "1" -- "*" Contract : relates to
CustomerEducation "1" -- "*" Customer : relates to
CustomerEducation "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerEducation "1" -- "*" CustomerCohort : relates to
CustomerEducation "1" -- "*" CustomerCommunity : relates to
CustomerEducation "1" -- "*" CustomerFeedback : relates to
CustomerEducation "1" -- "*" CustomerGoal : relates to
CustomerEducation "1" -- "*" CustomerHealthRecord : relates to
CustomerEducation "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_EDUCATION_ENGAGEMENT_RATE"
        ],
        "key_attributes": [
            "education_id",
            "content_type",
            "topic",
            "engagement_rate",
            "completion_rate",
            "customer_count",
            "effectiveness_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
