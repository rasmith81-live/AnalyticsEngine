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
                        47.9,
                        46.59,
                        54.05,
                        49.08,
                        40.6,
                        45.51,
                        40.82,
                        41.91,
                        42.24,
                        44.35,
                        51.42,
                        52.7
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.7,
                "unit": "%",
                "change": 1.28,
                "change_percent": 2.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 46.43,
                "min": 40.6,
                "max": 54.05,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 12.46,
                        "percentage": 23.6
                },
                {
                        "category": "Existing Customers",
                        "value": 12.95,
                        "percentage": 24.6
                },
                {
                        "category": "VIP Customers",
                        "value": 9.38,
                        "percentage": 17.8
                },
                {
                        "category": "At-Risk Customers",
                        "value": 3.06,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 14.85,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.516267",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Conversion Rate"
        }
    },
}
