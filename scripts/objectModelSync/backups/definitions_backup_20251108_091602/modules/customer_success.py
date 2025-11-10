"""
Customer Success Module

Focuses on ensuring customers achieve their desired outcomes while using the product or service,
driving adoption, engagement, and long-term value realization.
"""

from analytics_models import Module

CUSTOMER_SUCCESS = Module(
    name="Customer Success",
    code="CUSTOMER_SUCCESS",
    description="Proactive strategies to ensure customers achieve their goals and realize value from products/services",
    is_active=True,
    display_order=4,
    metadata_={
        "value_chains": ["CUSTOMER_SUCCESS"],
        "industries": ["SAAS", "TECHNOLOGY", "SERVICES", "B2B"],
        "focus_areas": [
            "Customer Onboarding & Adoption",
            "Customer Health Monitoring",
            "Proactive Engagement & Support",
            "Customer Education & Enablement",
            "Renewal & Expansion Management",
            "Customer Advocacy & Community",
            "CSM Team Performance",
            "Value Realization & Goal Achievement"
        ]
    }
)
