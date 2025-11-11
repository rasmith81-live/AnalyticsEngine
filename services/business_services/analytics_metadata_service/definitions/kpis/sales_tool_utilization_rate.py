"""
Sales Tool Utilization Rate

The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.
"""

SALES_TOOL_UTILIZATION_RATE = {
    "code": "SALES_TOOL_UTILIZATION_RATE",
    "name": "Sales Tool Utilization Rate",
    "description": "The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.",
    "formula": "(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
    "calculation_formula": "(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Tool Utilization Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.527394"},
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
                        48.03,
                        54.41,
                        52.2,
                        52.28,
                        52.46,
                        61.72,
                        61.17,
                        49.09,
                        55.79,
                        52.66,
                        65.54,
                        66.04
                ],
                "unit": "%"
        },
        "current": {
                "value": 66.04,
                "unit": "%",
                "change": 0.5,
                "change_percent": 0.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55.95,
                "min": 48.03,
                "max": 66.04,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.11,
                        "percentage": 18.3
                },
                {
                        "category": "Channel Sales",
                        "value": 13.86,
                        "percentage": 21.0
                },
                {
                        "category": "Online Sales",
                        "value": 12.88,
                        "percentage": 19.5
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.03,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 20.16,
                        "percentage": 30.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.275529",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Tool Utilization Rate"
        }
    },
}
