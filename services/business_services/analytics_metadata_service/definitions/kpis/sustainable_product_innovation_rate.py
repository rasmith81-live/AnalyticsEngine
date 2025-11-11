"""
Sustainable Product Innovation Rate

The rate at which new products or services are developed that meet sustainability criteria outlined in ISO 20400.
"""

SUSTAINABLE_PRODUCT_INNOVATION_RATE = {
    "code": "SUSTAINABLE_PRODUCT_INNOVATION_RATE",
    "name": "Sustainable Product Innovation Rate",
    "description": "The rate at which new products or services are developed that meet sustainability criteria outlined in ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sustainable Product Innovation Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:33.698735"},
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
                        56.21,
                        57.71,
                        51.68,
                        59.33,
                        68.06,
                        67.55,
                        65.6,
                        55.2,
                        54.3,
                        62.65,
                        59.54,
                        55.13
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.13,
                "unit": "%",
                "change": -4.41,
                "change_percent": -7.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 59.41,
                "min": 51.68,
                "max": 68.06,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 14.04,
                        "percentage": 25.5
                },
                {
                        "category": "Product Line B",
                        "value": 8.07,
                        "percentage": 14.6
                },
                {
                        "category": "Product Line C",
                        "value": 9.22,
                        "percentage": 16.7
                },
                {
                        "category": "Services",
                        "value": 5.55,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 18.25,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.727798",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sustainable Product Innovation Rate"
        }
    },
}
