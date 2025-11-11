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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Lead", "Order"], "last_validated": "2025-11-10T13:43:23.822995"},
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
                        24.4,
                        31.1,
                        31.1,
                        30.9,
                        25.7,
                        27.0,
                        30.3,
                        29.6,
                        31.5,
                        27.1,
                        30.0,
                        30.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 30.5,
                "unit": "days",
                "change": 0.5,
                "change_percent": 1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 29.1,
                "min": 24.4,
                "max": 31.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.43,
                        "percentage": 30.9
                },
                {
                        "category": "Category B",
                        "value": 6.96,
                        "percentage": 22.8
                },
                {
                        "category": "Category C",
                        "value": 2.36,
                        "percentage": 7.7
                },
                {
                        "category": "Category D",
                        "value": 2.61,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 9.14,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.822995",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Lead Time"
        }
    },
}
