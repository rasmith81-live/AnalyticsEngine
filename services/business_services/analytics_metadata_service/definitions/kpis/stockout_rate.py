"""
Stockout Rate


"""

STOCKOUT_RATE = {
    "code": "STOCKOUT_RATE",
    "name": "Stockout Rate",
    "description": "",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "General",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stockout Rate to be added.",
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
    "metadata_": {"modules": [], "required_objects": [], "last_validated": "2025-11-10T13:49:33.594807"},
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
                        41.09,
                        43.71,
                        50.7,
                        56.4,
                        57.56,
                        57.71,
                        57.24,
                        60.87,
                        46.37,
                        53.32,
                        44.82,
                        48.09
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.09,
                "unit": "%",
                "change": 3.27,
                "change_percent": 7.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 51.49,
                "min": 41.09,
                "max": 60.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.25,
                        "percentage": 21.3
                },
                {
                        "category": "Segment B",
                        "value": 8.26,
                        "percentage": 17.2
                },
                {
                        "category": "Segment C",
                        "value": 8.15,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 4.48,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 16.95,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.445349",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Stockout Rate"
        }
    },
}
