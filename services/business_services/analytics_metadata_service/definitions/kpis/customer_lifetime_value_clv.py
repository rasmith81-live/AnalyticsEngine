"""



"""

CUSTOMER_LIFETIME_VALUE_CLV = {
    "code": "CUSTOMER_LIFETIME_VALUE_CLV",
    "name": "",
    "description": "",
    "formula": "(Annual Revenue per Customer * Customer Relationship in Years) - Initial Acquisition Cost",
    "calculation_formula": "(Annual Revenue per Customer * Customer Relationship in Years) - Initial Acquisition Cost",
    "category": "General",
    "is_active": True,
    "full_kpi_definition": "Complete definition for  to be added.",
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
    "metadata_": {"modules": [], "required_objects": [], "last_validated": "2025-11-10T13:49:32.846795"},
    "required_objects": [],
    "modules": [],
    "module_code": "GENERAL",
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
                        858.05,
                        869.57,
                        880.62,
                        869.49,
                        871.24,
                        902.91,
                        922.97,
                        939.72,
                        859.06,
                        836.84,
                        881.45,
                        857.65
                ],
                "unit": "units"
        },
        "current": {
                "value": 857.65,
                "unit": "units",
                "change": -23.8,
                "change_percent": -2.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 879.13,
                "min": 836.84,
                "max": 939.72,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 269.64,
                        "percentage": 31.4
                },
                {
                        "category": "Existing Customers",
                        "value": 119.35,
                        "percentage": 13.9
                },
                {
                        "category": "VIP Customers",
                        "value": 118.25,
                        "percentage": 13.8
                },
                {
                        "category": "At-Risk Customers",
                        "value": 92.65,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 257.76,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.718486",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": ""
        }
    },
}
