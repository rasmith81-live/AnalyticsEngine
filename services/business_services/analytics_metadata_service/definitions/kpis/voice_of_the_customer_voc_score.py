"""



"""

VOICE_OF_THE_CUSTOMER_VOC_SCORE = {
    "code": "VOICE_OF_THE_CUSTOMER_VOC_SCORE",
    "name": "",
    "description": "",
    "formula": "Sum of All Customer Feedback Scores / Number of Feedback Instances",
    "calculation_formula": "Sum of All Customer Feedback Scores / Number of Feedback Instances",
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
    "metadata_": {"modules": [], "required_objects": [], "last_validated": "2025-11-10T13:49:33.793817"},
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
                        218,
                        198,
                        232,
                        207,
                        223,
                        230,
                        206,
                        214,
                        227,
                        210,
                        240,
                        218
                ],
                "unit": "count"
        },
        "current": {
                "value": 218,
                "unit": "count",
                "change": -22,
                "change_percent": -9.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 218.58,
                "min": 198,
                "max": 240,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 45.07,
                        "percentage": 20.7
                },
                {
                        "category": "Existing Customers",
                        "value": 60.34,
                        "percentage": 27.7
                },
                {
                        "category": "VIP Customers",
                        "value": 29.96,
                        "percentage": 13.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 10.94,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 71.69,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.959883",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": ""
        }
    },
}
