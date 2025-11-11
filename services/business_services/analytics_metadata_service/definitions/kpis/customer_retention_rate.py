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
                        73.44,
                        64.45,
                        73.36,
                        79.19,
                        78.96,
                        77.01,
                        82.15,
                        68.78,
                        70.43,
                        71.78,
                        80.51,
                        69.06
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.06,
                "unit": "%",
                "change": -11.45,
                "change_percent": -14.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.09,
                "min": 64.45,
                "max": 82.15,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 20.9,
                        "percentage": 30.3
                },
                {
                        "category": "Existing Customers",
                        "value": 12.07,
                        "percentage": 17.5
                },
                {
                        "category": "VIP Customers",
                        "value": 10.18,
                        "percentage": 14.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.14,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 22.77,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.784560",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Customer Retention Rate"
        }
    },
}
