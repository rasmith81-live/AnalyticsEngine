"""
Contract Renewal Rate

The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the
"""

CONTRACT_RENEWAL_RATE = {
    "code": "CONTRACT_RENEWAL_RATE",
    "name": "Contract Renewal Rate",
    "description": "The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
    "formula": "(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
    "calculation_formula": "(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Contract Renewal Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Contract", "Customer"], "last_validated": "2025-11-10T13:43:23.142994"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        40.63,
                        46.42,
                        43.45,
                        37.16,
                        34.67,
                        46.37,
                        36.08,
                        38.53,
                        42.83,
                        40.25,
                        49.37,
                        50.26
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.26,
                "unit": "%",
                "change": 0.89,
                "change_percent": 1.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 42.17,
                "min": 34.67,
                "max": 50.26,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.18,
                        "percentage": 26.2
                },
                {
                        "category": "Category B",
                        "value": 6.42,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 10.24,
                        "percentage": 20.4
                },
                {
                        "category": "Category D",
                        "value": 5.32,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 15.1,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.142994",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Contract Renewal Rate"
        }
    },
}
