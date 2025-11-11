"""
Cost Savings

The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.
"""

COST_SAVINGS = {
    "code": "COST_SAVINGS",
    "name": "Cost Savings",
    "description": "The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.",
    "formula": "Baseline Spend - Current Spend",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost Savings to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.735508"},
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
                        100020.94,
                        94762.7,
                        100651.4,
                        105034.54,
                        92878.16,
                        94908.07,
                        99802.11,
                        95762.55,
                        101914.24,
                        104957.76,
                        105326.53,
                        105032.54
                ],
                "unit": "$"
        },
        "current": {
                "value": 105032.54,
                "unit": "$",
                "change": -293.99,
                "change_percent": -0.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 100087.63,
                "min": 92878.16,
                "max": 105326.53,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22713.03,
                        "percentage": 21.6
                },
                {
                        "category": "Segment B",
                        "value": 19878.96,
                        "percentage": 18.9
                },
                {
                        "category": "Segment C",
                        "value": 11501.15,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 10620.9,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 40318.5,
                        "percentage": 38.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.557117",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost Savings"
        }
    },
}
