"""
Outbound Orders Processed per Hour

The number of outbound orders processed per hour.
"""

OUTBOUND_ORDERS_PROCESSED_PER_HOUR = {
    "code": "OUTBOUND_ORDERS_PROCESSED_PER_HOUR",
    "name": "Outbound Orders Processed per Hour",
    "description": "The number of outbound orders processed per hour.",
    "formula": "Total Outbound Orders Processed / Total Hours Worked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Outbound Orders Processed per Hour to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.137826"},
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
                        976.1,
                        968.98,
                        1084.5,
                        1086.36,
                        1053.02,
                        1055.95,
                        1035.23,
                        986.17,
                        1077.24,
                        997.17,
                        1054.59,
                        963.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 963.06,
                "unit": "units",
                "change": -91.53,
                "change_percent": -8.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 1028.2,
                "min": 963.06,
                "max": 1086.36,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 305.45,
                        "percentage": 31.7
                },
                {
                        "category": "Category B",
                        "value": 229.55,
                        "percentage": 23.8
                },
                {
                        "category": "Category C",
                        "value": 110.18,
                        "percentage": 11.4
                },
                {
                        "category": "Category D",
                        "value": 75.88,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 242.0,
                        "percentage": 25.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.778002",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Outbound Orders Processed per Hour"
        }
    },
}
