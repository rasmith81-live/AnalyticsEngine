"""
Inbound Orders Processed per Hour

The number of inbound orders processed per hour.
"""

INBOUND_ORDERS_PROCESSED_PER_HOUR = {
    "code": "INBOUND_ORDERS_PROCESSED_PER_HOUR",
    "name": "Inbound Orders Processed per Hour",
    "description": "The number of inbound orders processed per hour.",
    "formula": "Total Inbound Orders Processed / Total Hours Worked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inbound Orders Processed per Hour to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:32.971099"},
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
                        486.31,
                        401.3,
                        366.81,
                        485.64,
                        444.48,
                        396.71,
                        478.47,
                        457.88,
                        385.74,
                        417.46,
                        425.22,
                        395.43
                ],
                "unit": "units"
        },
        "current": {
                "value": 395.43,
                "unit": "units",
                "change": -29.79,
                "change_percent": -7.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 428.45,
                "min": 366.81,
                "max": 486.31,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 91.36,
                        "percentage": 23.1
                },
                {
                        "category": "Segment B",
                        "value": 79.44,
                        "percentage": 20.1
                },
                {
                        "category": "Segment C",
                        "value": 52.51,
                        "percentage": 13.3
                },
                {
                        "category": "Segment D",
                        "value": 45.24,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 126.88,
                        "percentage": 32.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.025202",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Inbound Orders Processed per Hour"
        }
    },
}
