"""
Order Packing Accuracy

The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.
"""

ORDER_PACKING_ACCURACY = {
    "code": "ORDER_PACKING_ACCURACY",
    "name": "Order Packing Accuracy",
    "description": "The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Packing Accuracy to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Order"], "last_validated": "2025-11-10T13:49:33.122343"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        570.48,
                        604.38,
                        645.34,
                        528.99,
                        644.27,
                        577.02,
                        549.08,
                        585.5,
                        599.0,
                        578.94,
                        626.35,
                        622.68
                ],
                "unit": "units"
        },
        "current": {
                "value": 622.68,
                "unit": "units",
                "change": -3.67,
                "change_percent": -0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 594.34,
                "min": 528.99,
                "max": 645.34,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 119.07,
                        "percentage": 19.1
                },
                {
                        "category": "Segment B",
                        "value": 168.11,
                        "percentage": 27.0
                },
                {
                        "category": "Segment C",
                        "value": 52.68,
                        "percentage": 8.5
                },
                {
                        "category": "Segment D",
                        "value": 69.73,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 213.09,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.318972",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Packing Accuracy"
        }
    },
}
