"""
Packaging Compliance Rate

The percentage of packages that meet regulatory and safety standards, ensuring compliance with industry regulations.
"""

PACKAGING_COMPLIANCE_RATE = {
    "code": "PACKAGING_COMPLIANCE_RATE",
    "name": "Packaging Compliance Rate",
    "description": "The percentage of packages that meet regulatory and safety standards, ensuring compliance with industry regulations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Compliance Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.141234"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        76.85,
                        71.99,
                        67.99,
                        79.39,
                        73.89,
                        81.86,
                        75.22,
                        73.27,
                        79.17,
                        76.94,
                        74.31,
                        69.25
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.25,
                "unit": "%",
                "change": -5.06,
                "change_percent": -6.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 75.01,
                "min": 67.99,
                "max": 81.86,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.84,
                        "percentage": 30.1
                },
                {
                        "category": "Category B",
                        "value": 8.24,
                        "percentage": 11.9
                },
                {
                        "category": "Category C",
                        "value": 13.25,
                        "percentage": 19.1
                },
                {
                        "category": "Category D",
                        "value": 4.98,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 21.94,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.782865",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Compliance Rate"
        }
    },
}
