"""
Packing Lead Time

The time taken from initiating packing operations to the completion of packing, critical for timely deliveries.
"""

PACKING_LEAD_TIME = {
    "code": "PACKING_LEAD_TIME",
    "name": "Packing Lead Time",
    "description": "The time taken from initiating packing operations to the completion of packing, critical for timely deliveries.",
    "formula": "Total Packing Time / Total Orders Packed",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Lead Time to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Lead", "Order"], "last_validated": "2025-11-10T13:49:33.164136"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        19.1,
                        16.5,
                        19.5,
                        16.1,
                        19.0,
                        19.8,
                        16.5,
                        16.2,
                        22.2,
                        19.6,
                        20.6,
                        17.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 17.3,
                "unit": "days",
                "change": -3.3,
                "change_percent": -16.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 18.53,
                "min": 16.1,
                "max": 22.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 3.4,
                        "percentage": 19.7
                },
                {
                        "category": "Segment B",
                        "value": 4.7,
                        "percentage": 27.2
                },
                {
                        "category": "Segment C",
                        "value": 2.96,
                        "percentage": 17.1
                },
                {
                        "category": "Segment D",
                        "value": 1.16,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 5.08,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.409975",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Lead Time"
        }
    },
}
