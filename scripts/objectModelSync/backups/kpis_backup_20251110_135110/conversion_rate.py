"""
Conversion Rate

The percentage of leads that convert into paying customers.
"""

CONVERSION_RATE = {
    "code": "CONVERSION_RATE",
    "name": "Conversion Rate",
    "description": "The percentage of leads that convert into paying customers.",
    "formula": "(Number of New Customers / Number of Leads) * 100",
    "calculation_formula": "(Number of New Customers / Number of Leads) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Conversion Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Lead"], "last_validated": "2025-11-10T13:49:32.720062"},
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
                        67.63,
                        74.84,
                        68.17,
                        69.76,
                        60.76,
                        74.15,
                        63.31,
                        79.21,
                        69.22,
                        70.01,
                        74.69,
                        65.73
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.73,
                "unit": "%",
                "change": -8.96,
                "change_percent": -12.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.79,
                "min": 60.76,
                "max": 79.21,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.15,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 10.48,
                        "percentage": 15.9
                },
                {
                        "category": "Category C",
                        "value": 8.94,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 9.72,
                        "percentage": 14.8
                },
                {
                        "category": "Other",
                        "value": 24.44,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.149750",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Conversion Rate"
        }
    },
}
