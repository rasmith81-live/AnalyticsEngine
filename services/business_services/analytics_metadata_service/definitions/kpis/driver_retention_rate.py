"""
Driver Retention Rate

The rate at which a company retains its drivers over a period.
"""

DRIVER_RETENTION_RATE = {
    "code": "DRIVER_RETENTION_RATE",
    "name": "Driver Retention Rate",
    "description": "The rate at which a company retains its drivers over a period.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Driver Retention Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.935239"},
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
                        36.49,
                        34.4,
                        38.91,
                        34.05,
                        31.45,
                        33.29,
                        45.55,
                        42.35,
                        48.83,
                        47.18,
                        35.31,
                        45.48
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.48,
                "unit": "%",
                "change": 10.17,
                "change_percent": 28.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 39.44,
                "min": 31.45,
                "max": 48.83,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.39,
                        "percentage": 29.4
                },
                {
                        "category": "Segment B",
                        "value": 5.12,
                        "percentage": 11.3
                },
                {
                        "category": "Segment C",
                        "value": 4.59,
                        "percentage": 10.1
                },
                {
                        "category": "Segment D",
                        "value": 6.12,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 16.26,
                        "percentage": 35.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.940432",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Driver Retention Rate"
        }
    },
}
