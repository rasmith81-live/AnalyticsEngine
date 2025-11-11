"""
Invoice Error Rate

The percentage of invoices that contain errors, requiring additional time and resources to resolve.
"""

INVOICE_ERROR_RATE = {
    "code": "INVOICE_ERROR_RATE",
    "name": "Invoice Error Rate",
    "description": "The percentage of invoices that contain errors, requiring additional time and resources to resolve.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Invoice Error Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Invoice"], "last_validated": "2025-11-10T13:49:32.989685"},
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
                        63.58,
                        61.68,
                        76.21,
                        64.64,
                        74.02,
                        69.71,
                        71.38,
                        71.55,
                        72.05,
                        77.29,
                        74.12,
                        76.49
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.49,
                "unit": "%",
                "change": 2.37,
                "change_percent": 3.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 71.06,
                "min": 61.68,
                "max": 77.29,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 24.64,
                        "percentage": 32.2
                },
                {
                        "category": "Segment B",
                        "value": 9.29,
                        "percentage": 12.1
                },
                {
                        "category": "Segment C",
                        "value": 6.79,
                        "percentage": 8.9
                },
                {
                        "category": "Segment D",
                        "value": 3.92,
                        "percentage": 5.1
                },
                {
                        "category": "Other",
                        "value": 31.85,
                        "percentage": 41.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.077467",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Invoice Error Rate"
        }
    },
}
