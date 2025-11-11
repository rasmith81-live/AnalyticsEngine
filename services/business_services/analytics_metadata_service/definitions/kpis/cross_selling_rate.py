"""
Cross-selling Rate

The percentage of customers who have been sold additional, complementary products or services.
"""

CROSS_SELLING_RATE = {
    "code": "CROSS_SELLING_RATE",
    "name": "Cross-selling Rate",
    "description": "The percentage of customers who have been sold additional, complementary products or services.",
    "formula": "(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cross-selling Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:49:32.790048"},
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
                        67.25,
                        60.96,
                        66.61,
                        68.09,
                        69.85,
                        60.68,
                        66.72,
                        63.39,
                        63.75,
                        59.32,
                        66.33,
                        72.0
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.0,
                "unit": "%",
                "change": 5.67,
                "change_percent": 8.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.41,
                "min": 59.32,
                "max": 72.0,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 24.66,
                        "percentage": 34.2
                },
                {
                        "category": "Existing Customers",
                        "value": 9.28,
                        "percentage": 12.9
                },
                {
                        "category": "VIP Customers",
                        "value": 8.39,
                        "percentage": 11.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.57,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 22.1,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.579880",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cross-selling Rate"
        }
    },
}
