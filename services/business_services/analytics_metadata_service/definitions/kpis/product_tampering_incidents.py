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
                        84,
                        116,
                        110,
                        107,
                        106,
                        86,
                        118,
                        117,
                        116,
                        108,
                        105,
                        131
                ],
                "unit": "count"
        },
        "current": {
                "value": 131,
                "unit": "count",
                "change": 26,
                "change_percent": 24.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 108.67,
                "min": 84,
                "max": 131,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 36.83,
                        "percentage": 28.1
                },
                {
                        "category": "Product Line B",
                        "value": 27.18,
                        "percentage": 20.7
                },
                {
                        "category": "Product Line C",
                        "value": 17.36,
                        "percentage": 13.3
                },
                {
                        "category": "Services",
                        "value": 11.26,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 38.37,
                        "percentage": 29.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.652170",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Product Tampering Incidents"
        }
    },
}
