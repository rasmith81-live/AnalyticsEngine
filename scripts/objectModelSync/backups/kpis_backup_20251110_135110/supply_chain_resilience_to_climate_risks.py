"""
Supply Chain Resilience to Climate Risks

A measure of the supply chain
"""

SUPPLY_CHAIN_RESILIENCE_TO_CLIMATE_RISKS = {
    "code": "SUPPLY_CHAIN_RESILIENCE_TO_CLIMATE_RISKS",
    "name": "Supply Chain Resilience to Climate Risks",
    "description": "A measure of the supply chain",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Resilience to Climate Risks to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.670389"},
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
                        753.72,
                        717.91,
                        712.68,
                        789.41,
                        773.8,
                        689.21,
                        681.42,
                        712.21,
                        781.16,
                        767.79,
                        721.29,
                        749.59
                ],
                "unit": "units"
        },
        "current": {
                "value": 749.59,
                "unit": "units",
                "change": 28.3,
                "change_percent": 3.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 737.52,
                "min": 681.42,
                "max": 789.41,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 231.32,
                        "percentage": 30.9
                },
                {
                        "category": "Category B",
                        "value": 83.03,
                        "percentage": 11.1
                },
                {
                        "category": "Category C",
                        "value": 128.04,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 74.15,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 233.05,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.919442",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Resilience to Climate Risks"
        }
    },
}
