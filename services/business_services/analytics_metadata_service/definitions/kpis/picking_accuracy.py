"""
Picking Accuracy

The percentage of orders picked without errors from inventory.
"""

PICKING_ACCURACY = {
    "code": "PICKING_ACCURACY",
    "name": "Picking Accuracy",
    "description": "The percentage of orders picked without errors from inventory.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Picking Accuracy to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Order"], "last_validated": "2025-11-10T13:49:33.235292"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        357.14,
                        418.02,
                        326.28,
                        353.63,
                        327.16,
                        301.14,
                        413.45,
                        420.49,
                        396.62,
                        308.32,
                        415.14,
                        424.14
                ],
                "unit": "units"
        },
        "current": {
                "value": 424.14,
                "unit": "units",
                "change": 9.0,
                "change_percent": 2.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 371.79,
                "min": 301.14,
                "max": 424.14,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 108.74,
                        "percentage": 25.6
                },
                {
                        "category": "Segment B",
                        "value": 88.7,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 79.18,
                        "percentage": 18.7
                },
                {
                        "category": "Segment D",
                        "value": 28.27,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 119.25,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.558048",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Picking Accuracy"
        }
    },
}
