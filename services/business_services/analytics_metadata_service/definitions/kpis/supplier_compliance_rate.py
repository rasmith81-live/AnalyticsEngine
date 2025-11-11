"""
Supplier Compliance Rate

The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.
"""

SUPPLIER_COMPLIANCE_RATE = {
    "code": "SUPPLIER_COMPLIANCE_RATE",
    "name": "Supplier Compliance Rate",
    "description": "The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Compliance Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.623352"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        52.99,
                        63.44,
                        48.08,
                        58.4,
                        60.4,
                        58.6,
                        52.49,
                        60.44,
                        63.64,
                        46.87,
                        62.81,
                        46.68
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.68,
                "unit": "%",
                "change": -16.13,
                "change_percent": -25.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.24,
                "min": 46.68,
                "max": 63.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.9,
                        "percentage": 34.1
                },
                {
                        "category": "Segment B",
                        "value": 8.49,
                        "percentage": 18.2
                },
                {
                        "category": "Segment C",
                        "value": 4.96,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 4.04,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 13.29,
                        "percentage": 28.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.512705",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Compliance Rate"
        }
    },
}
