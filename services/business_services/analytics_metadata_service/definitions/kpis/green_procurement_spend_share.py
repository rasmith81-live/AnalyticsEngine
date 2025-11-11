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
                        927.86,
                        910.43,
                        943.21,
                        986.85,
                        909.91,
                        929.8,
                        963.9,
                        880.3,
                        971.84,
                        946.34,
                        923.82,
                        860.89
                ],
                "unit": "units"
        },
        "current": {
                "value": 860.89,
                "unit": "units",
                "change": -62.93,
                "change_percent": -6.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 929.6,
                "min": 860.89,
                "max": 986.85,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 189.36,
                        "percentage": 22.0
                },
                {
                        "category": "Segment B",
                        "value": 162.36,
                        "percentage": 18.9
                },
                {
                        "category": "Segment C",
                        "value": 91.79,
                        "percentage": 10.7
                },
                {
                        "category": "Segment D",
                        "value": 67.36,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 350.02,
                        "percentage": 40.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.013941",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Green Procurement Spend Share"
        }
    },
}
