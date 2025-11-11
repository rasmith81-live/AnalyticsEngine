"""
Maverick Spend

The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.
"""

MAVERICK_SPEND = {
    "code": "MAVERICK_SPEND",
    "name": "Maverick Spend",
    "description": "The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.",
    "formula": "Total Maverick Spend / Total Spend",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Maverick Spend to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Contract", "Supplier"], "last_validated": "2025-11-10T13:49:33.051548"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        542.86,
                        465.01,
                        581.38,
                        477.99,
                        515.32,
                        543.82,
                        519.38,
                        592.29,
                        570.49,
                        587.38,
                        494.94,
                        555.73
                ],
                "unit": "units"
        },
        "current": {
                "value": 555.73,
                "unit": "units",
                "change": 60.79,
                "change_percent": 12.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 537.22,
                "min": 465.01,
                "max": 592.29,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 167.79,
                        "percentage": 30.2
                },
                {
                        "category": "Segment B",
                        "value": 80.67,
                        "percentage": 14.5
                },
                {
                        "category": "Segment C",
                        "value": 105.58,
                        "percentage": 19.0
                },
                {
                        "category": "Segment D",
                        "value": 59.92,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 141.77,
                        "percentage": 25.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.204848",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Maverick Spend"
        }
    },
}
