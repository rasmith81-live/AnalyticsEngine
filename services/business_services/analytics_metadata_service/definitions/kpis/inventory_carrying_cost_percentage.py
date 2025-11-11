"""
Inventory Carrying Cost Percentage

The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.
"""

INVENTORY_CARRYING_COST_PERCENTAGE = {
    "code": "INVENTORY_CARRYING_COST_PERCENTAGE",
    "name": "Inventory Carrying Cost Percentage",
    "description": "The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Carrying Cost Percentage to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.982972"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        68.18,
                        80.81,
                        74.26,
                        77.77,
                        74.13,
                        66.03,
                        83.61,
                        72.45,
                        82.93,
                        75.37,
                        74.33,
                        67.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.33,
                "unit": "%",
                "change": -7.0,
                "change_percent": -9.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.77,
                "min": 66.03,
                "max": 83.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.48,
                        "percentage": 20.0
                },
                {
                        "category": "Segment B",
                        "value": 10.21,
                        "percentage": 15.2
                },
                {
                        "category": "Segment C",
                        "value": 8.17,
                        "percentage": 12.1
                },
                {
                        "category": "Segment D",
                        "value": 8.33,
                        "percentage": 12.4
                },
                {
                        "category": "Other",
                        "value": 27.14,
                        "percentage": 40.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.057749",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Carrying Cost Percentage"
        }
    },
}
