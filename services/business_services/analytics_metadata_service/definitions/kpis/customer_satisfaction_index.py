"""
Customer Satisfaction Index

A measure of how satisfied customers are with a company
"""

CUSTOMER_SATISFACTION_INDEX = {
    "code": "CUSTOMER_SATISFACTION_INDEX",
    "name": "Customer Satisfaction Index",
    "description": "A measure of how satisfied customers are with a company",
    "formula": "(Sum of Customer Satisfaction Scores / Number of Respondents) * 100",
    "calculation_formula": "(Sum of Customer Satisfaction Scores / Number of Respondents) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction Index to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.875757"},
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
                        68.69,
                        73.13,
                        63.2,
                        77.01,
                        82.01,
                        68.59,
                        76.63,
                        74.41,
                        69.98,
                        80.1,
                        63.01,
                        65.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.96,
                "unit": "%",
                "change": 2.95,
                "change_percent": 4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.89,
                "min": 63.01,
                "max": 82.01,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 20.61,
                        "percentage": 31.2
                },
                {
                        "category": "Existing Customers",
                        "value": 13.23,
                        "percentage": 20.1
                },
                {
                        "category": "VIP Customers",
                        "value": 6.32,
                        "percentage": 9.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 7.67,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 18.13,
                        "percentage": 27.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.788815",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Satisfaction Index"
        }
    },
}
