"""
Fleet Utilization Rate

The percentage of time a fleet is used compared to its availability for use.
"""

FLEET_UTILIZATION_RATE = {
    "code": "FLEET_UTILIZATION_RATE",
    "name": "Fleet Utilization Rate",
    "description": "The percentage of time a fleet is used compared to its availability for use.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Fleet Utilization Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.957758"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        35.89,
                        52.57,
                        50.0,
                        37.26,
                        49.61,
                        50.72,
                        45.45,
                        54.51,
                        54.14,
                        46.66,
                        34.94,
                        36.2
                ],
                "unit": "%"
        },
        "current": {
                "value": 36.2,
                "unit": "%",
                "change": 1.26,
                "change_percent": 3.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 45.66,
                "min": 34.94,
                "max": 54.51,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.13,
                        "percentage": 25.2
                },
                {
                        "category": "Segment B",
                        "value": 5.11,
                        "percentage": 14.1
                },
                {
                        "category": "Segment C",
                        "value": 6.73,
                        "percentage": 18.6
                },
                {
                        "category": "Segment D",
                        "value": 1.99,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 13.24,
                        "percentage": 36.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.992276",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Fleet Utilization Rate"
        }
    },
}
