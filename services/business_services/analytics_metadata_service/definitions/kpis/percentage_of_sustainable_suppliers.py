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
                        77.03,
                        71.04,
                        76.06,
                        69.98,
                        77.12,
                        73.54,
                        78.11,
                        74.79,
                        70.43,
                        69.25,
                        72.47,
                        68.91
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.91,
                "unit": "%",
                "change": -3.56,
                "change_percent": -4.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73.23,
                "min": 68.91,
                "max": 78.11,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.37,
                        "percentage": 15.0
                },
                {
                        "category": "Segment B",
                        "value": 11.73,
                        "percentage": 17.0
                },
                {
                        "category": "Segment C",
                        "value": 15.45,
                        "percentage": 22.4
                },
                {
                        "category": "Segment D",
                        "value": 6.01,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 25.35,
                        "percentage": 36.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.549005",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Percentage of Sustainable Suppliers"
        }
    },
}
