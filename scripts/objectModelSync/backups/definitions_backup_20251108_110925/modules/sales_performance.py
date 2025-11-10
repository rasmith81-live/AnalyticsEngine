"""
Sales Performance Module

Focuses on measuring and analyzing sales team and individual performance
through metrics, benchmarks, and performance management.
"""

from analytics_models import Module

SALES_PERFORMANCE = Module(
    name="Sales Performance",
    code="SALES_PERFORMANCE",
    description="Measuring and analyzing sales team and individual performance",
    is_active=True,
    display_order=11,
    metadata_={
        "value_chains": ["SALES_MGMT", "PERFORMANCE_MGMT"],
        "industries": ["ALL"],
        "focus_areas": [
            "Individual Performance Metrics",
            "Team Performance Analytics",
            "Performance Benchmarking",
            "Productivity Measurement",
            "Performance Management",
            "Goal Achievement Tracking",
            "Performance Improvement"
        ]
    }
)
