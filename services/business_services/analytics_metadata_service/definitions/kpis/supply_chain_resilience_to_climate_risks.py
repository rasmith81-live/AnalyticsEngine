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
                        969.47,
                        975.23,
                        1005.29,
                        993.12,
                        889.69,
                        945.63,
                        1011.27,
                        994.25,
                        924.05,
                        897.8,
                        964.03,
                        892.86
                ],
                "unit": "units"
        },
        "current": {
                "value": 892.86,
                "unit": "units",
                "change": -71.17,
                "change_percent": -7.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 955.22,
                "min": 889.69,
                "max": 1011.27,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 257.68,
                        "percentage": 28.9
                },
                {
                        "category": "Segment B",
                        "value": 101.97,
                        "percentage": 11.4
                },
                {
                        "category": "Segment C",
                        "value": 159.56,
                        "percentage": 17.9
                },
                {
                        "category": "Segment D",
                        "value": 107.05,
                        "percentage": 12.0
                },
                {
                        "category": "Other",
                        "value": 266.6,
                        "percentage": 29.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.643072",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Resilience to Climate Risks"
        }
    },
}
