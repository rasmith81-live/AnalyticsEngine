"""
Perfect Order Rate

The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.
"""

PERFECT_ORDER_RATE = {
    "code": "PERFECT_ORDER_RATE",
    "name": "Perfect Order Rate",
    "description": "The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Perfect Order Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.233702"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        58.85,
                        55.54,
                        70.33,
                        58.05,
                        72.7,
                        72.24,
                        71.57,
                        73.7,
                        70.96,
                        54.41,
                        71.66,
                        69.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.41,
                "unit": "%",
                "change": -2.25,
                "change_percent": -3.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 66.62,
                "min": 54.41,
                "max": 73.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.63,
                        "percentage": 22.5
                },
                {
                        "category": "Segment B",
                        "value": 17.65,
                        "percentage": 25.4
                },
                {
                        "category": "Segment C",
                        "value": 9.82,
                        "percentage": 14.1
                },
                {
                        "category": "Segment D",
                        "value": 6.71,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 19.6,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.553517",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Perfect Order Rate"
        }
    },
}
