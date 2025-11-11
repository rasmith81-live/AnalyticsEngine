"""
Customer Retention Rate

The percentage of customers who remain with the company over a specified period, indicating the success of customer satisfaction and retention strategies.
"""

CUSTOMER_RETENTION_RATE = {
    "code": "CUSTOMER_RETENTION_RATE",
    "name": "Customer Retention Rate",
    "description": "The percentage of customers who remain with the company over a specified period, indicating the success of customer satisfaction and retention strategies.",
    "formula": "((Number of Customers at End of Period - Number of New Customers Acquired During Period) / Number of Customers at Start of Period) * 100",
    "calculation_formula": "((Number of Customers at End of Period - Number of New Customers Acquired During Period) / Number of Customers at Start of Period) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Retention Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:32.873046"},
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
                        50.71,
                        52.71,
                        59.22,
                        68.42,
                        69.17,
                        54.86,
                        64.47,
                        57.61,
                        66.3,
                        58.9,
                        57.71,
                        60.32
                ],
                "unit": "%"
        },
        "current": {
                "value": 60.32,
                "unit": "%",
                "change": 2.61,
                "change_percent": 4.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 60.03,
                "min": 50.71,
                "max": 69.17,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.42,
                        "percentage": 18.9
                },
                {
                        "category": "Category B",
                        "value": 7.93,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 10.49,
                        "percentage": 17.4
                },
                {
                        "category": "Category D",
                        "value": 3.97,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 26.51,
                        "percentage": 43.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.346269",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Retention Rate"
        }
    },
}
