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
                        72.69,
                        77.53,
                        87.03,
                        89.65,
                        80.32,
                        78.96,
                        80.89,
                        76.78,
                        77.84,
                        84.4,
                        79.42,
                        82.63
                ],
                "unit": "%"
        },
        "current": {
                "value": 82.63,
                "unit": "%",
                "change": 3.21,
                "change_percent": 4.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 80.68,
                "min": 72.69,
                "max": 89.65,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.62,
                        "percentage": 17.7
                },
                {
                        "category": "Category B",
                        "value": 19.74,
                        "percentage": 23.9
                },
                {
                        "category": "Category C",
                        "value": 7.4,
                        "percentage": 9.0
                },
                {
                        "category": "Category D",
                        "value": 8.78,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 32.09,
                        "percentage": 38.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.560690",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Invoice Error Rate"
        }
    },
}
