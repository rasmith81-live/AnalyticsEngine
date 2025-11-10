"""
Key Account Management Module

Focuses on strategic management of high-value customer accounts,
building deep relationships, and maximizing account value and retention.
"""

from analytics_models import Module

KEY_ACCOUNT_MANAGEMENT = Module(
    name="Key Account Management",
    code="KEY_ACCOUNT_MANAGEMENT",
    description="Strategic management of high-value accounts to maximize lifetime value and retention",
    is_active=True,
    display_order=6,
    metadata_={
        "value_chains": ["SALES_MGMT", "CUSTOMER_SUCCESS"],
        "industries": ["B2B", "ENTERPRISE", "TECHNOLOGY", "MANUFACTURING", "SERVICES"],
        "focus_areas": [
            "Strategic Account Planning",
            "Executive Relationship Management",
            "Account Growth & Expansion",
            "Account Health & Risk Management",
            "Multi-Stakeholder Engagement",
            "Account Retention & Renewal",
            "Value Delivery & ROI Demonstration"
        ]
    }
)
