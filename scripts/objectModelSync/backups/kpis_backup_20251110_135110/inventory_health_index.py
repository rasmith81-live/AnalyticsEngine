"""
Inventory Health Index

A composite measure assessing the health of inventory including age, turnover, and obsolescence.
"""

INVENTORY_HEALTH_INDEX = {
    "code": "INVENTORY_HEALTH_INDEX",
    "name": "Inventory Health Index",
    "description": "A composite measure assessing the health of inventory including age, turnover, and obsolescence.",
    "formula": "Sum of weighted inventory metrics / Total number of inventory metrics",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Health Index to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """

* What factors are influencing this metric?
* Are there any anomalies in the data?
    
    """,
    "actionable_tips": """

* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    """,
    "visualization_suggestions": """

* Line chart for time series analysis
* Bar chart for comparisons
    
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.982972"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        356,
                        345,
                        344,
                        311,
                        313,
                        315,
                        321,
                        350,
                        321,
                        321,
                        353,
                        324
                ],
                "unit": "count"
        },
        "current": {
                "value": 324,
                "unit": "count",
                "change": -29,
                "change_percent": -8.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 331.17,
                "min": 311,
                "max": 356,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 92.52,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 78.5,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 32.7,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 16.24,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 104.04,
                        "percentage": 32.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.545508",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Inventory Health Index"
        }
    },
}
