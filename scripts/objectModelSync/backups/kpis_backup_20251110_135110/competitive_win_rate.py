"""
Competitive Win Rate

The percentage of deals won against competitors, indicating the sales team
"""

COMPETITIVE_WIN_RATE = {
    "code": "COMPETITIVE_WIN_RATE",
    "name": "Competitive Win Rate",
    "description": "The percentage of deals won against competitors, indicating the sales team",
    "formula": "(Number of Deals Won Against Competitors / Total Number of Competitive Deals) * 100",
    "calculation_formula": "(Number of Deals Won Against Competitors / Total Number of Competitive Deals) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Competitive Win Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:32.709100"},
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
                        55.71,
                        56.76,
                        56.54,
                        60.01,
                        72.04,
                        74.24,
                        73.08,
                        62.69,
                        58.27,
                        67.48,
                        57.1,
                        56.07
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.07,
                "unit": "%",
                "change": -1.03,
                "change_percent": -1.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 62.5,
                "min": 55.71,
                "max": 74.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.72,
                        "percentage": 17.3
                },
                {
                        "category": "Category B",
                        "value": 13.29,
                        "percentage": 23.7
                },
                {
                        "category": "Category C",
                        "value": 6.09,
                        "percentage": 10.9
                },
                {
                        "category": "Category D",
                        "value": 5.93,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 21.04,
                        "percentage": 37.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.133772",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Competitive Win Rate"
        }
    },
}
