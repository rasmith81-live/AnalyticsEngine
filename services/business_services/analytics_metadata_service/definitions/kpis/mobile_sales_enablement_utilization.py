"""
Mobile Sales Enablement Utilization

The percentage of the sales team that uses mobile tools and applications to enable sales activities.
"""

MOBILE_SALES_ENABLEMENT_UTILIZATION = {
    "code": "MOBILE_SALES_ENABLEMENT_UTILIZATION",
    "name": "Mobile Sales Enablement Utilization",
    "description": "The percentage of the sales team that uses mobile tools and applications to enable sales activities.",
    "formula": "(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
    "calculation_formula": "(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Mobile Sales Enablement Utilization to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.062507"},
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
                        69.13,
                        59.63,
                        61.68,
                        65.13,
                        74.74,
                        60.54,
                        68.87,
                        65.86,
                        78.12,
                        65.03,
                        62.83,
                        74.34
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.34,
                "unit": "%",
                "change": 11.51,
                "change_percent": 18.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 67.16,
                "min": 59.63,
                "max": 78.12,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.66,
                        "percentage": 25.1
                },
                {
                        "category": "Channel Sales",
                        "value": 10.26,
                        "percentage": 13.8
                },
                {
                        "category": "Online Sales",
                        "value": 14.88,
                        "percentage": 20.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.3,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 26.24,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.219317",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Mobile Sales Enablement Utilization"
        }
    },
}
