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
                        57.45,
                        65.36,
                        57.82,
                        66.87,
                        54.49,
                        56.88,
                        71.38,
                        64.87,
                        66.62,
                        63.64,
                        66.17,
                        69.07
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.07,
                "unit": "%",
                "change": 2.9,
                "change_percent": 4.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.38,
                "min": 54.49,
                "max": 71.38,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.03,
                        "percentage": 27.6
                },
                {
                        "category": "Segment B",
                        "value": 8.3,
                        "percentage": 12.0
                },
                {
                        "category": "Segment C",
                        "value": 9.47,
                        "percentage": 13.7
                },
                {
                        "category": "Segment D",
                        "value": 4.78,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 27.49,
                        "percentage": 39.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.508471",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Compliance Rate"
        }
    },
}
