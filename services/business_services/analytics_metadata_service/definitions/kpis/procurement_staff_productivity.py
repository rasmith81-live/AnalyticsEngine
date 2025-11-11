"""
Procurement Staff Productivity


"""

PROCUREMENT_STAFF_PRODUCTIVITY = {
    "code": "PROCUREMENT_STAFF_PRODUCTIVITY",
    "name": "Procurement Staff Productivity",
    "description": "",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "General",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Staff Productivity to be added.",
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
    "metadata_": {"modules": [], "required_objects": [], "last_validated": "2025-11-10T13:49:33.260223"},
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
                        981.04,
                        902.54,
                        910.22,
                        905.62,
                        1028.04,
                        1020.79,
                        911.14,
                        960.68,
                        974.54,
                        890.43,
                        902.95,
                        945.13
                ],
                "unit": "units"
        },
        "current": {
                "value": 945.13,
                "unit": "units",
                "change": 42.18,
                "change_percent": 4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 944.43,
                "min": 890.43,
                "max": 1028.04,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 187.98,
                        "percentage": 19.9
                },
                {
                        "category": "Product Line B",
                        "value": 135.01,
                        "percentage": 14.3
                },
                {
                        "category": "Product Line C",
                        "value": 125.91,
                        "percentage": 13.3
                },
                {
                        "category": "Services",
                        "value": 122.18,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 374.05,
                        "percentage": 39.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.615674",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Procurement Staff Productivity"
        }
    },
}
