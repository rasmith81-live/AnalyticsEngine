"""
Customer Retention Module

Focuses on maintaining and strengthening relationships with existing customers,
reducing churn, and maximizing customer lifetime value.
"""

from analytics_models import Module

CUSTOMER_RETENTION = Module(
    name="Customer Retention",
    code="CUSTOMER_RETENTION",
    description="Strategies and metrics for retaining existing customers and maximizing their lifetime value",
    is_active=True,
    display_order=3,
    metadata_={
        "value_chains": ["CUSTOMER_SUCCESS", "SALES_MGMT"],
        "industries": ["RETAIL", "MANUFACTURING", "TECHNOLOGY", "SERVICES", "SAAS"],
        "focus_areas": [
            "Churn Prevention & Reduction",
            "Customer Satisfaction & Loyalty",
            "Customer Health Monitoring",
            "Onboarding & Adoption",
            "Customer Support Excellence",
            "Lifetime Value Optimization",
            "Customer Engagement & Education"
        ]
    }
)
