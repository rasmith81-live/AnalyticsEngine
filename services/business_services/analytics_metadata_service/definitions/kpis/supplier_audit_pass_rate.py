"""
Supplier Audit Pass Rate

The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.
"""

SUPPLIER_AUDIT_PASS_RATE = {
    "code": "SUPPLIER_AUDIT_PASS_RATE",
    "name": "Supplier Audit Pass Rate",
    "description": "The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Audit Pass Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.614309"},
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
                        73.69,
                        74.76,
                        63.11,
                        74.63,
                        66.2,
                        71.16,
                        65.51,
                        71.99,
                        70.83,
                        73.23,
                        64.59,
                        71.12
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.12,
                "unit": "%",
                "change": 6.53,
                "change_percent": 10.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.07,
                "min": 63.11,
                "max": 74.76,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22.67,
                        "percentage": 31.9
                },
                {
                        "category": "Segment B",
                        "value": 15.56,
                        "percentage": 21.9
                },
                {
                        "category": "Segment C",
                        "value": 8.55,
                        "percentage": 12.0
                },
                {
                        "category": "Segment D",
                        "value": 3.15,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 21.19,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.489421",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Audit Pass Rate"
        }
    },
}
