"""
Customs Clearance Efficiency

The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.
"""

CUSTOMS_CLEARANCE_EFFICIENCY = {
    "code": "CUSTOMS_CLEARANCE_EFFICIENCY",
    "name": "Customs Clearance Efficiency",
    "description": "The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.",
    "formula": "Sum of Customs Clearance Times / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customs Clearance Efficiency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.896379"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        378,
                        406,
                        419,
                        378,
                        411,
                        416,
                        398,
                        407,
                        391,
                        413,
                        404,
                        409
                ],
                "unit": "count"
        },
        "current": {
                "value": 409,
                "unit": "count",
                "change": 5,
                "change_percent": 1.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 402.5,
                "min": 378,
                "max": 419,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 123.24,
                        "percentage": 30.1
                },
                {
                        "category": "Segment B",
                        "value": 69.27,
                        "percentage": 16.9
                },
                {
                        "category": "Segment C",
                        "value": 33.94,
                        "percentage": 8.3
                },
                {
                        "category": "Segment D",
                        "value": 24.27,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 158.28,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.857414",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customs Clearance Efficiency"
        }
    },
}
