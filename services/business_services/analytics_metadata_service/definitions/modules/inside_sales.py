"""
Inside Sales Module

Focuses on remote sales activities conducted from an office or call center,
emphasizing phone, email, and digital communication to close deals efficiently.
"""

from analytics_models import Module

INSIDE_SALES = Module(
    name="Inside Sales",
    code="INSIDE_SALES",
    description="Remote sales operations using phone, email, and digital channels to efficiently close deals",
    is_active=True,
    display_order=5,
    metadata_={
        "value_chains": ["SALES_MGMT"],
        "industries": ["TECHNOLOGY", "SAAS", "B2B", "SERVICES"],
        "focus_areas": [
            "Call & Email Activity Management",
            "Lead Qualification & Conversion",
            "Sales Pipeline Management",
            "Remote Selling Effectiveness",
            "Sales Team Productivity",
            "Customer Acquisition Efficiency",
            "Deal Velocity & Conversion"
        ]
    }
)
