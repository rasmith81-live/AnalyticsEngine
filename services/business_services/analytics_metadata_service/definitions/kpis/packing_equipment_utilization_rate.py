"""
Packing Equipment Utilization Rate

The percentage of time that packing equipment is actively used compared to available operational time, indicating equipment efficiency.
"""

PACKING_EQUIPMENT_UTILIZATION_RATE = {
    "code": "PACKING_EQUIPMENT_UTILIZATION_RATE",
    "name": "Packing Equipment Utilization Rate",
    "description": "The percentage of time that packing equipment is actively used compared to available operational time, indicating equipment efficiency.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Equipment Utilization Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.155164"},
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
                        54.04,
                        40.21,
                        45.25,
                        50.43,
                        56.37,
                        46.69,
                        49.28,
                        54.9,
                        55.01,
                        39.35,
                        42.21,
                        49.76
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.76,
                "unit": "%",
                "change": 7.55,
                "change_percent": 17.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 48.62,
                "min": 39.35,
                "max": 56.37,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 7.81,
                        "percentage": 15.7
                },
                {
                        "category": "Segment B",
                        "value": 11.08,
                        "percentage": 22.3
                },
                {
                        "category": "Segment C",
                        "value": 8.63,
                        "percentage": 17.3
                },
                {
                        "category": "Segment D",
                        "value": 5.47,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 16.77,
                        "percentage": 33.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.393441",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Equipment Utilization Rate"
        }
    },
}
