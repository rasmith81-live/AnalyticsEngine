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
                        66.88,
                        69.14,
                        76.44,
                        58.9,
                        76.0,
                        64.55,
                        64.63,
                        73.72,
                        61.6,
                        69.97,
                        75.72,
                        74.0
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.0,
                "unit": "%",
                "change": -1.72,
                "change_percent": -2.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.3,
                "min": 58.9,
                "max": 76.44,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.89,
                        "percentage": 18.8
                },
                {
                        "category": "Segment B",
                        "value": 18.84,
                        "percentage": 25.5
                },
                {
                        "category": "Segment C",
                        "value": 9.78,
                        "percentage": 13.2
                },
                {
                        "category": "Segment D",
                        "value": 5.71,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 25.78,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.498104",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Competitive Win Rate"
        }
    },
}
