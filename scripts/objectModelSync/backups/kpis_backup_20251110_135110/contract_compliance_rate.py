"""
Contract Compliance Rate

The percentage of orders placed that are in compliance with the terms of the company
"""

CONTRACT_COMPLIANCE_RATE = {
    "code": "CONTRACT_COMPLIANCE_RATE",
    "name": "Contract Compliance Rate",
    "description": "The percentage of orders placed that are in compliance with the terms of the company",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Contract Compliance Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Contract", "Order", "Supplier"], "last_validated": "2025-11-10T13:49:32.713259"},
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
                        65.44,
                        73.02,
                        64.5,
                        73.17,
                        67.17,
                        72.09,
                        68.94,
                        63.8,
                        55.62,
                        68.26,
                        56.99,
                        62.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.31,
                "unit": "%",
                "change": 5.32,
                "change_percent": 9.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 65.94,
                "min": 55.62,
                "max": 73.17,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.21,
                        "percentage": 32.4
                },
                {
                        "category": "Category B",
                        "value": 9.45,
                        "percentage": 15.2
                },
                {
                        "category": "Category C",
                        "value": 10.76,
                        "percentage": 17.3
                },
                {
                        "category": "Category D",
                        "value": 6.49,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 15.4,
                        "percentage": 24.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.142199",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Compliance Rate"
        }
    },
}
