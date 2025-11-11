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
                        79.68,
                        68.04,
                        79.72,
                        75.5,
                        75.97,
                        64.73,
                        78.25,
                        81.43,
                        69.88,
                        68.72,
                        69.62,
                        71.55
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.55,
                "unit": "%",
                "change": 1.93,
                "change_percent": 2.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73.59,
                "min": 64.73,
                "max": 81.43,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.71,
                        "percentage": 23.4
                },
                {
                        "category": "Category B",
                        "value": 11.89,
                        "percentage": 16.6
                },
                {
                        "category": "Category C",
                        "value": 7.91,
                        "percentage": 11.1
                },
                {
                        "category": "Category D",
                        "value": 7.36,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 27.68,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.978831",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sustainable Product Innovation Rate"
        }
    },
}
