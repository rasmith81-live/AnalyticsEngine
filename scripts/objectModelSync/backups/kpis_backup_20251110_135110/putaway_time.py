"""
Putaway Time

The time it takes to store goods in their designated location after receipt.
"""

PUTAWAY_TIME = {
    "code": "PUTAWAY_TIME",
    "name": "Putaway Time",
    "description": "The time it takes to store goods in their designated location after receipt.",
    "formula": "Total Time Taken for Putaway / Total Number of Items Putaway",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Putaway Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:33.303507"},
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
                        245,
                        231,
                        232,
                        244,
                        222,
                        232,
                        232,
                        229,
                        257,
                        233,
                        260,
                        250
                ],
                "unit": "count"
        },
        "current": {
                "value": 250,
                "unit": "count",
                "change": -10,
                "change_percent": -3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 238.92,
                "min": 222,
                "max": 260,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.36,
                        "percentage": 33.3
                },
                {
                        "category": "Category B",
                        "value": 41.84,
                        "percentage": 16.7
                },
                {
                        "category": "Category C",
                        "value": 33.54,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 9.87,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 81.39,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.019431",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Putaway Time"
        }
    },
}
