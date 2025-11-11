"""
Counterfeit Product Rate

The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.
"""

COUNTERFEIT_PRODUCT_RATE = {
    "code": "COUNTERFEIT_PRODUCT_RATE",
    "name": "Counterfeit Product Rate",
    "description": "The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Counterfeit Product Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:32.737632"},
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
                        33.33,
                        33.1,
                        40.11,
                        43.21,
                        52.48,
                        43.59,
                        43.21,
                        33.04,
                        43.4,
                        38.11,
                        43.43,
                        48.76
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.76,
                "unit": "%",
                "change": 5.33,
                "change_percent": 12.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 41.31,
                "min": 33.04,
                "max": 52.48,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 10.16,
                        "percentage": 20.8
                },
                {
                        "category": "Product Line B",
                        "value": 6.59,
                        "percentage": 13.5
                },
                {
                        "category": "Product Line C",
                        "value": 8.91,
                        "percentage": 18.3
                },
                {
                        "category": "Services",
                        "value": 5.51,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 17.59,
                        "percentage": 36.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.564020",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Counterfeit Product Rate"
        }
    },
}
