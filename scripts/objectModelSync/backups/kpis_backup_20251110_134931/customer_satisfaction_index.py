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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.349397"},
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
                        66.2,
                        70.9,
                        75.0,
                        64.4,
                        73.8,
                        68.8,
                        72.4,
                        65.6,
                        72.9,
                        66.3,
                        70.7,
                        64.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 64.6,
                "unit": "score",
                "change": -6.1,
                "change_percent": -8.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.3,
                "min": 64.4,
                "max": 75.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.46,
                        "percentage": 17.7
                },
                {
                        "category": "Category B",
                        "value": 11.18,
                        "percentage": 17.3
                },
                {
                        "category": "Category C",
                        "value": 11.04,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 9.02,
                        "percentage": 14.0
                },
                {
                        "category": "Other",
                        "value": 21.9,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.349397",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Customer Satisfaction Index"
        }
    },
}
