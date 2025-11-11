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
                        59.28,
                        55.92,
                        57.4,
                        61.59,
                        48.1,
                        48.73,
                        57.72,
                        62.25,
                        60.18,
                        52.19,
                        61.08,
                        54.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 54.16,
                "unit": "%",
                "change": -6.92,
                "change_percent": -11.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.55,
                "min": 48.1,
                "max": 62.25,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.79,
                        "percentage": 34.7
                },
                {
                        "category": "Category B",
                        "value": 11.98,
                        "percentage": 22.1
                },
                {
                        "category": "Category C",
                        "value": 4.22,
                        "percentage": 7.8
                },
                {
                        "category": "Category D",
                        "value": 3.84,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 15.33,
                        "percentage": 28.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.576286",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Land-and-Expand Success Rate"
        }
    },
}
