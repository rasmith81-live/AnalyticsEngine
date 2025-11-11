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
                        32196.92,
                        37371.31,
                        37855.6,
                        36183.47,
                        24303.63,
                        31186.92,
                        34647.08,
                        32629.93,
                        28956.49,
                        24808.11,
                        31583.98,
                        29634.63
                ],
                "unit": "$"
        },
        "current": {
                "value": 29634.63,
                "unit": "$",
                "change": -1949.35,
                "change_percent": -6.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 31779.84,
                "min": 24303.63,
                "max": 37855.6,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 7106.55,
                        "percentage": 24.0
                },
                {
                        "category": "Segment B",
                        "value": 4842.62,
                        "percentage": 16.3
                },
                {
                        "category": "Segment C",
                        "value": 3341.55,
                        "percentage": 11.3
                },
                {
                        "category": "Segment D",
                        "value": 4010.86,
                        "percentage": 13.5
                },
                {
                        "category": "Other",
                        "value": 10333.05,
                        "percentage": 34.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.198983",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Material Price Variance"
        }
    },
}
