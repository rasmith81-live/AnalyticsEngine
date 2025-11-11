"""
Sales Cycle Length

The length of time it takes for a lead to become a customer.
"""

SALES_CYCLE_LENGTH = {
    "code": "SALES_CYCLE_LENGTH",
    "name": "Sales Cycle Length",
    "description": "The length of time it takes for a lead to become a customer.",
    "formula": "Average Time from First Contact to Deal Closure",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Cycle Length to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Deal", "Lead"], "last_validated": "2025-11-10T13:49:33.404734"},
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
                        27.1,
                        29.4,
                        24.3,
                        26.2,
                        23.4,
                        30.7,
                        23.1,
                        25.5,
                        29.0,
                        30.3,
                        27.5,
                        29.9
                ],
                "unit": "days"
        },
        "current": {
                "value": 29.9,
                "unit": "days",
                "change": 2.4,
                "change_percent": 8.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 27.2,
                "min": 23.1,
                "max": 30.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 8.36,
                        "percentage": 28.0
                },
                {
                        "category": "Channel Sales",
                        "value": 7.3,
                        "percentage": 24.4
                },
                {
                        "category": "Online Sales",
                        "value": 2.94,
                        "percentage": 9.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.07,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 8.23,
                        "percentage": 27.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.937924",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Cycle Length"
        }
    },
}
