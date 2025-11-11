"""
Procurement ROI

The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.
"""

PROCUREMENT_ROI = {
    "code": "PROCUREMENT_ROI",
    "name": "Procurement ROI",
    "description": "The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement ROI to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Return"], "last_validated": "2025-11-10T13:49:33.258592"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        604.18,
                        609.56,
                        583.1,
                        593.47,
                        639.66,
                        591.93,
                        576.5,
                        609.16,
                        589.94,
                        665.36,
                        587.49,
                        548.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 548.06,
                "unit": "units",
                "change": -39.43,
                "change_percent": -6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 599.87,
                "min": 548.06,
                "max": 665.36,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 184.34,
                        "percentage": 33.6
                },
                {
                        "category": "Segment B",
                        "value": 114.11,
                        "percentage": 20.8
                },
                {
                        "category": "Segment C",
                        "value": 44.34,
                        "percentage": 8.1
                },
                {
                        "category": "Segment D",
                        "value": 46.3,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 158.97,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.610802",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Procurement ROI"
        }
    },
}
