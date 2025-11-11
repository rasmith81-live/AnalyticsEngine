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
                        64.03,
                        67.52,
                        61.95,
                        61.2,
                        52.26,
                        67.61,
                        57.5,
                        62.48,
                        67.09,
                        53.88,
                        67.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.03,
                "unit": "%",
                "change": 13.15,
                "change_percent": 24.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.04,
                "min": 52.26,
                "max": 67.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 20.36,
                        "percentage": 30.4
                },
                {
                        "category": "Existing Customers",
                        "value": 9.81,
                        "percentage": 14.6
                },
                {
                        "category": "VIP Customers",
                        "value": 10.64,
                        "percentage": 15.9
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.59,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 22.63,
                        "percentage": 33.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.922068",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upselling Rate"
        }
    },
}
