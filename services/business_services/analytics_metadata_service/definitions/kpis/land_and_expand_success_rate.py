"""
Land-and-Expand Success Rate

The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.
"""

LAND_AND_EXPAND_SUCCESS_RATE = {
    "code": "LAND_AND_EXPAND_SUCCESS_RATE",
    "name": "Land-and-Expand Success Rate",
    "description": "The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.",
    "formula": "(Revenue from Upselling and Cross-Selling to Existing Customers / Total Revenue from Existing Customers) * 100",
    "calculation_formula": "(Revenue from Upselling and Cross-Selling to Existing Customers / Total Revenue from Existing Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Land-and-Expand Success Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Lead", "Product"], "last_validated": "2025-11-10T13:49:33.000198"},
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
                        57.06,
                        50.5,
                        43.63,
                        57.98,
                        50.84,
                        63.13,
                        47.55,
                        58.76,
                        51.93,
                        58.01,
                        46.99,
                        62.05
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.05,
                "unit": "%",
                "change": 15.06,
                "change_percent": 32.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 54.04,
                "min": 43.63,
                "max": 63.13,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 11.48,
                        "percentage": 18.5
                },
                {
                        "category": "Existing Customers",
                        "value": 13.96,
                        "percentage": 22.5
                },
                {
                        "category": "VIP Customers",
                        "value": 6.64,
                        "percentage": 10.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.58,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 25.39,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.097250",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Land-and-Expand Success Rate"
        }
    },
}
