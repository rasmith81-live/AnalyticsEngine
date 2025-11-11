"""
Sales Tool Utilization Rate

The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.
"""

SALES_TOOL_UTILIZATION_RATE = {
    "code": "SALES_TOOL_UTILIZATION_RATE",
    "name": "Sales Tool Utilization Rate",
    "description": "The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.",
    "formula": "(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
    "calculation_formula": "(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Tool Utilization Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.670729"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        54.06,
                        50.57,
                        48.95,
                        45.49,
                        61.1,
                        47.41,
                        59.24,
                        44.79,
                        45.61,
                        54.89,
                        44.27,
                        61.1
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.1,
                "unit": "%",
                "change": 16.83,
                "change_percent": 38.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 51.46,
                "min": 44.27,
                "max": 61.1,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.91,
                        "percentage": 21.1
                },
                {
                        "category": "Category B",
                        "value": 15.28,
                        "percentage": 25.0
                },
                {
                        "category": "Category C",
                        "value": 7.51,
                        "percentage": 12.3
                },
                {
                        "category": "Category D",
                        "value": 7.02,
                        "percentage": 11.5
                },
                {
                        "category": "Other",
                        "value": 18.38,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.670729",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Tool Utilization Rate"
        }
    },
}
