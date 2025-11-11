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
                        476,
                        504,
                        479,
                        490,
                        514,
                        517,
                        482,
                        469,
                        493,
                        511,
                        501,
                        481
                ],
                "unit": "count"
        },
        "current": {
                "value": 481,
                "unit": "count",
                "change": -20,
                "change_percent": -4.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 493.08,
                "min": 469,
                "max": 517,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 116.32,
                        "percentage": 24.2
                },
                {
                        "category": "Segment B",
                        "value": 70.98,
                        "percentage": 14.8
                },
                {
                        "category": "Segment C",
                        "value": 71.99,
                        "percentage": 15.0
                },
                {
                        "category": "Segment D",
                        "value": 48.56,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 173.15,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.710812",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Putaway Time"
        }
    },
}
