"""
Sales Enablement Module

Focuses on equipping sales teams with content, tools, training, and processes
to improve sales effectiveness and productivity.
"""

from analytics_models import Module

SALES_ENABLEMENT = Module(
    name="Sales Enablement",
    code="SALES_ENABLEMENT",
    description="Equipping sales teams with content, tools, training, and processes for effectiveness",
    is_active=True,
    display_order=9,
    metadata_={
        "value_chains": ["SALES_MGMT", "TRAINING_DEV"],
        "industries": ["ALL"],
        "focus_areas": [
            "Sales Training & Development",
            "Content Management",
            "Sales Tools & Technology",
            "Sales Process Optimization",
            "Onboarding & Ramp Time",
            "Performance Enablement",
            "Sales Coaching"
        ]
    }
)
