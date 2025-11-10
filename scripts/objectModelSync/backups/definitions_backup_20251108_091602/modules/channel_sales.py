"""
Channel Sales Module

Focuses on managing and optimizing sales through channel partners,
including partner recruitment, enablement, performance tracking, and relationship management.
"""

from analytics_models import Module

CHANNEL_SALES = Module(
    name="Channel Sales",
    code="CHANNEL_SALES",
    description="Management and optimization of sales through channel partners",
    is_active=True,
    display_order=2,
    metadata_={
        "value_chains": ["SALES_MGMT"],
        "industries": ["RETAIL", "MANUFACTURING", "TECHNOLOGY", "SERVICES"],
        "focus_areas": [
            "Partner Recruitment & Onboarding",
            "Partner Enablement & Training",
            "Partner Performance Management",
            "Channel Conflict Resolution",
            "Co-Marketing & Collaboration",
            "Partner Retention & Loyalty"
        ]
    }
)
