"""
Upselling Rate

The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.
"""

UPSELLING_RATE = {
    "code": "UPSELLING_RATE",
    "name": "Upselling Rate",
    "description": "The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.",
    "formula": "(Number of Customers Who Purchased Additional Services or Products / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Who Purchased Additional Services or Products / Total Number of Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Upselling Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:49:33.772531"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        61.93,
                        64.77,
                        55.86,
                        64.99,
                        50.26,
                        61.94,
                        50.51,
                        53.22,
                        61.02,
                        55.83,
                        62.88,
                        62.5
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.5,
                "unit": "%",
                "change": -0.38,
                "change_percent": -0.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 58.81,
                "min": 50.26,
                "max": 64.99,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.71,
                        "percentage": 15.5
                },
                {
                        "category": "Category B",
                        "value": 10.69,
                        "percentage": 17.1
                },
                {
                        "category": "Category C",
                        "value": 7.55,
                        "percentage": 12.1
                },
                {
                        "category": "Category D",
                        "value": 4.97,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 29.58,
                        "percentage": 47.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.190066",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upselling Rate"
        }
    },
}
