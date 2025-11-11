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
                        792.5,
                        654.54,
                        780.07,
                        691.8,
                        692.74,
                        678.44,
                        775.59,
                        689.22,
                        685.31,
                        661.17,
                        731.65,
                        749.92
                ],
                "unit": "units"
        },
        "current": {
                "value": 749.92,
                "unit": "units",
                "change": 18.27,
                "change_percent": 2.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 715.25,
                "min": 654.54,
                "max": 792.5,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 203.58,
                        "percentage": 27.1
                },
                {
                        "category": "Segment B",
                        "value": 133.94,
                        "percentage": 17.9
                },
                {
                        "category": "Segment C",
                        "value": 93.93,
                        "percentage": 12.5
                },
                {
                        "category": "Segment D",
                        "value": 36.15,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 282.32,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.352393",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Outbound Orders Processed per Hour"
        }
    },
}
