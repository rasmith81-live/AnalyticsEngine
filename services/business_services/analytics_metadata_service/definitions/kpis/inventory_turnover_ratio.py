"""
Inventory Turnover Ratio

The rate at which inventory is used and replaced over a certain period.
"""

INVENTORY_TURNOVER_RATIO = {
    "code": "INVENTORY_TURNOVER_RATIO",
    "name": "Inventory Turnover Ratio",
    "description": "The rate at which inventory is used and replaced over a certain period.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Turnover Ratio to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.988927"},
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
                        65.64,
                        57.65,
                        70.53,
                        74.77,
                        69.51,
                        62.82,
                        72.37,
                        61.32,
                        71.44,
                        67.2,
                        56.86,
                        65.57
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.57,
                "unit": "%",
                "change": 8.71,
                "change_percent": 15.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.31,
                "min": 56.86,
                "max": 74.77,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.91,
                        "percentage": 28.8
                },
                {
                        "category": "Segment B",
                        "value": 13.12,
                        "percentage": 20.0
                },
                {
                        "category": "Segment C",
                        "value": 7.24,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 2.93,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 23.37,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.074740",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Turnover Ratio"
        }
    },
}
