"""
Percentage of Sustainable Suppliers

The proportion of suppliers that meet the organization
"""

PERCENTAGE_OF_SUSTAINABLE_SUPPLIERS = {
    "code": "PERCENTAGE_OF_SUSTAINABLE_SUPPLIERS",
    "name": "Percentage of Sustainable Suppliers",
    "description": "The proportion of suppliers that meet the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Percentage of Sustainable Suppliers to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.231314"},
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
                        72.62,
                        62.86,
                        61.49,
                        65.45,
                        62.18,
                        70.51,
                        64.98,
                        67.79,
                        59.87,
                        65.03,
                        74.41,
                        55.61
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.61,
                "unit": "%",
                "change": -18.8,
                "change_percent": -25.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.23,
                "min": 55.61,
                "max": 74.41,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.43,
                        "percentage": 33.1
                },
                {
                        "category": "Category B",
                        "value": 11.77,
                        "percentage": 21.2
                },
                {
                        "category": "Category C",
                        "value": 4.87,
                        "percentage": 8.8
                },
                {
                        "category": "Category D",
                        "value": 3.3,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 17.24,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.923961",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Percentage of Sustainable Suppliers"
        }
    },
}
