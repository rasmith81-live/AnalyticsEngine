"""
Product Tampering Incidents

The number of product tampering incidents detected, which affects consumer safety and brand reputation.
"""

PRODUCT_TAMPERING_INCIDENTS = {
    "code": "PRODUCT_TAMPERING_INCIDENTS",
    "name": "Product Tampering Incidents",
    "description": "The number of product tampering incidents detected, which affects consumer safety and brand reputation.",
    "formula": "Total Number of Product Tampering Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Tampering Incidents to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:33.275109"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        460,
                        445,
                        489,
                        480,
                        457,
                        464,
                        483,
                        444,
                        464,
                        484,
                        482,
                        473
                ],
                "unit": "count"
        },
        "current": {
                "value": 473,
                "unit": "count",
                "change": -9,
                "change_percent": -1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 468.75,
                "min": 444,
                "max": 489,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 139.53,
                        "percentage": 29.5
                },
                {
                        "category": "Category B",
                        "value": 101.46,
                        "percentage": 21.5
                },
                {
                        "category": "Category C",
                        "value": 56.45,
                        "percentage": 11.9
                },
                {
                        "category": "Category D",
                        "value": 25.39,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 150.17,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.983197",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Tampering Incidents"
        }
    },
}
