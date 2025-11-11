"""
Material Price Variance

The difference between the actual cost of materials and the standard cost, indicating how well costs are controlled.
"""

MATERIAL_PRICE_VARIANCE = {
    "code": "MATERIAL_PRICE_VARIANCE",
    "name": "Material Price Variance",
    "description": "The difference between the actual cost of materials and the standard cost, indicating how well costs are controlled.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Material Price Variance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.046963"},
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
                        97379.11,
                        96657.6,
                        104548.9,
                        92338.57,
                        99845.37,
                        102692.12,
                        96401.49,
                        105519.3,
                        92576.0,
                        92754.13,
                        95642.15,
                        96270.47
                ],
                "unit": "$"
        },
        "current": {
                "value": 96270.47,
                "unit": "$",
                "change": 628.32,
                "change_percent": 0.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 97718.77,
                "min": 92338.57,
                "max": 105519.3,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 32308.3,
                        "percentage": 33.6
                },
                {
                        "category": "Category B",
                        "value": 18017.16,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 14847.74,
                        "percentage": 15.4
                },
                {
                        "category": "Category D",
                        "value": 8253.48,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 22843.79,
                        "percentage": 23.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.646398",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Material Price Variance"
        }
    },
}
