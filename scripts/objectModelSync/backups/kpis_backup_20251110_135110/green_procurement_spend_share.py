"""
Green Procurement Spend Share

The share of total procurement spend that goes towards environmentally friendly products and services, as guided by ISO 20400.
"""

GREEN_PROCUREMENT_SPEND_SHARE = {
    "code": "GREEN_PROCUREMENT_SPEND_SHARE",
    "name": "Green Procurement Spend Share",
    "description": "The share of total procurement spend that goes towards environmentally friendly products and services, as guided by ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Green Procurement Spend Share to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:32.964618"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        912.21,
                        979.0,
                        935.36,
                        934.21,
                        1028.89,
                        1029.75,
                        966.43,
                        999.52,
                        940.12,
                        1011.75,
                        941.62,
                        1022.16
                ],
                "unit": "units"
        },
        "current": {
                "value": 1022.16,
                "unit": "units",
                "change": 80.54,
                "change_percent": 8.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 975.09,
                "min": 912.21,
                "max": 1029.75,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 299.6,
                        "percentage": 29.3
                },
                {
                        "category": "Category B",
                        "value": 121.6,
                        "percentage": 11.9
                },
                {
                        "category": "Category C",
                        "value": 114.92,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 85.0,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 401.04,
                        "percentage": 39.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.507141",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Green Procurement Spend Share"
        }
    },
}
