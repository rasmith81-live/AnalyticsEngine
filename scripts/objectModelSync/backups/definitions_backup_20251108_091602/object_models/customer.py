"""
Customer Object Model

Represents customers who have completed purchases.
"""

from analytics_models import ObjectModel

CUSTOMER = ObjectModel(
    name="Customer",
    code="CUSTOMER",
    description="Organizations or individuals who have purchased products/services",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Customer {
}

' Business Development & Sales
class Account {
}

class Sale {
}

class Opportunity {
}

class Deal {
}

' Channel Sales
class ChannelPartner {
}

class ChannelDeal {
}

' Customer Retention & Success
class Subscription {
}

class Contract {
}

class CustomerOnboarding {
}

class CustomerHealthRecord {
}

class CustomerFeedback {
}

class LoyaltyProgram {
}

class ChurnEvent {
}

class QuarterlyBusinessReview {
}

' Customer Success Specific
class CustomerSuccessManager {
}

class ProductAdoption {
}

class CustomerGoal {
}

class RenewalManagement {
}

class ExpansionOpportunity {
}

' Key Account Management
class KeyAccount {
}

class KeyAccountManager {
}

class AccountPlan {
}

class Stakeholder {
}

' Shared
class Purchase {
}

class Referral {
}

class SupportTicket {
}

class Product {
}

' Relationships - Business Development
Account "1" -- "0..1" Customer : becomes >
Sale "1" -- "1" Customer : creates >
Opportunity "0..*" -- "0..1" Customer : for >
Deal "1" -- "0..1" Customer : results in >

' Relationships - Channel Sales
ChannelPartner "1" -- "0..*" Customer : acquires >
ChannelDeal "1" -- "1" Customer : for >

' Relationships - Customer Retention
Customer "1" -- "0..*" Subscription : has >
Customer "1" -- "0..*" Contract : has >
Customer "1" -- "1" CustomerOnboarding : completes >
Customer "1" -- "0..*" CustomerHealthRecord : tracked by >
Customer "1" -- "0..*" CustomerFeedback : provides >
Customer "0..*" -- "0..*" LoyaltyProgram : participates in >
Customer "1" -- "0..1" ChurnEvent : may experience >
Customer "1" -- "0..*" QuarterlyBusinessReview : attends >

' Relationships - Customer Success
Customer "0..*" -- "1" CustomerSuccessManager : managed by >
Customer "1" -- "0..*" ProductAdoption : has >
Customer "1" -- "0..*" CustomerGoal : sets >
Customer "1" -- "0..*" RenewalManagement : has >
Customer "1" -- "0..*" ExpansionOpportunity : has >

' Relationships - Key Account Management
Customer "0..1" -- "0..1" KeyAccount : may be >
KeyAccount "0..*" -- "1" KeyAccountManager : managed by >
KeyAccount "1" -- "1" AccountPlan : has >
KeyAccount "1" -- "1..*" Stakeholder : has >

' Relationships - Outside Sales
FieldVisit "0..*" -- "0..1" Customer : with >

' Relationships - Shared
Customer "1" -- "1..*" Purchase : makes >
Customer "1" -- "0..*" Referral : generates >
Customer "1" -- "0..*" SupportTicket : creates >
Customer "0..*" -- "0..*" Product : uses >

@enduml

' Related Objects

class Assessment {
}

class Call {
}

class CoachingSession {
}

class Goal {
}

class Lead {
}

class Meeting {
}

class PerformanceScorecard {
}

class Proposal {
}

class RevenueForecast {
}

' Relationships to Related Objects
Customer "1" -- "*" Account : relates to
Customer "1" -- "*" Assessment : relates to
Customer "1" -- "*" Call : relates to
Customer "1" -- "*" ChannelPartner : relates to
Customer "1" -- "*" CoachingSession : relates to
Customer "1" -- "*" Contract : relates to
Customer "1" -- "*" Deal : relates to
Customer "1" -- "*" Goal : relates to
Customer "1" -- "*" Lead : relates to
Customer "1" -- "*" Meeting : relates to
Customer "1" -- "*" Opportunity : relates to
Customer "1" -- "*" PerformanceScorecard : relates to
Customer "1" -- "*" Product : relates to
Customer "1" -- "*" Proposal : relates to
Customer "1" -- "*" RevenueForecast : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "OUTSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT"],
        "related_kpis": [
            "CUSTOMER_ACQUISITION_COST_CAC",
            "CUSTOMER_LIFETIME_VALUE_CLV",
            "CUSTOMER_RETENTION_RATE",
            "CUSTOMER_SATISFACTION_INDEX",
            "CHURN_RATE",
            "REPEAT_PURCHASE_RATE",
            "CUSTOMER_ENGAGEMENT_LEVEL",
            "CUSTOMER_EFFORT_SCORE_CES",
            "CUSTOMER_ONBOARDING_EFFICACY",
            "VOICE_OF_THE_CUSTOMER_VOC_SCORE"
        ],
        "key_attributes": [
            "customer_name",
            "customer_type",
            "acquisition_date",
            "lifetime_value",
            "satisfaction_score",
            "health_score",
            "churn_risk",
            "last_purchase_date",
            "total_purchases"
        ],
        "related_objects": ["Account", "Assessment", "Call", "Channel Partner", "Coaching Session", "Contract", "Deal", "Goal", "Lead", "Meeting", "Opportunity", "Performance Scorecard", "Product", "Proposal", "Revenue Forecast"]}
)
