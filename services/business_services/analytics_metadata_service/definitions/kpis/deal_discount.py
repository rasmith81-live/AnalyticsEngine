"""
Average Deal Discount

The average percentage discount applied to deals, which can reflect the sales team
"""

DEAL_DISCOUNT = {
    "code": "DEAL_DISCOUNT",
    "name": "Average Deal Discount",
    "description": "The average percentage discount applied to deals, which can reflect the sales team",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Deal Discount to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:32.910015"},
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
                        832.34,
                        843.31,
                        753.75,
                        722.69,
                        710.95,
                        789.43,
                        720.47,
                        763.8,
                        809.98,
                        831.76,
                        710.41,
                        776.3
                ],
                "unit": "units"
        },
        "current": {
                "value": 776.3,
                "unit": "units",
                "change": 65.89,
                "change_percent": 9.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 772.1,
                "min": 710.41,
                "max": 843.31,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 250.81,
                        "percentage": 32.3
                },
                {
                        "category": "Segment B",
                        "value": 164.32,
                        "percentage": 21.2
                },
                {
                        "category": "Segment C",
                        "value": 96.67,
                        "percentage": 12.5
                },
                {
                        "category": "Segment D",
                        "value": 58.36,
                        "percentage": 7.5
                },
                {
                        "category": "Other",
                        "value": 206.14,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.877093",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Deal Discount"
        }
    },
}
