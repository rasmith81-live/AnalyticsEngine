"""
Sales Training and Coaching Module

Focuses on developing sales team capabilities through training programs,
coaching sessions, skill development, and performance improvement.
"""

from analytics_models import Module

SALES_TRAINING_COACHING = Module(
    name="Sales Training and Coaching",
    code="SALES_TRAINING_COACHING",
    description="Developing sales team capabilities through training, coaching, and skill development",
    is_active=True,
    display_order=13,
    metadata_={
        "value_chains": ["SALES_MGMT", "TRAINING_DEV", "PERFORMANCE_MGMT"],
        "industries": ["ALL"],
        "focus_areas": [
            "Sales Training Programs",
            "Coaching & Mentoring",
            "Skill Development",
            "Performance Improvement",
            "Onboarding & Ramp-up",
            "Certification & Assessment",
            "Continuous Learning"
        ]
    }
)
