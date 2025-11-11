"""
Demo-to-Closing Rate

The percentage of product or service demonstrations that result in a closed sale.
"""

DEMO_TO_CLOSING_RATE = {
    "code": "DEMO_TO_CLOSING_RATE",
    "name": "Demo-to-Closing Rate",
    "description": "The percentage of product or service demonstrations that result in a closed sale.",
    "formula": "(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
    "calculation_formula": "(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demo-to-Closing Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "Product"], "last_validated": "2025-11-10T13:49:32.926895"},
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
                        68.1,
                        58.37,
                        58.08,
                        58.91,
                        69.53,
                        69.37,
                        53.11,
                        67.84,
                        55.9,
                        62.65,
                        56.06,
                        57.74
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.74,
                "unit": "%",
                "change": 1.68,
                "change_percent": 3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 61.31,
                "min": 53.11,
                "max": 69.53,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.58,
                        "percentage": 30.4
                },
                {
                        "category": "Segment B",
                        "value": 6.1,
                        "percentage": 10.6
                },
                {
                        "category": "Segment C",
                        "value": 9.73,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 5.47,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 18.86,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.920349",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Demo-to-Closing Rate"
        }
    },
}
