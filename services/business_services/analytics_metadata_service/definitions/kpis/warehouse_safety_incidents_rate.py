"""
Warehouse Safety Incidents Rate

The number of safety incidents recorded in a warehouse per time unit.
"""

WAREHOUSE_SAFETY_INCIDENTS_RATE = {
    "code": "WAREHOUSE_SAFETY_INCIDENTS_RATE",
    "name": "Warehouse Safety Incidents Rate",
    "description": "The number of safety incidents recorded in a warehouse per time unit.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Safety Incidents Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:49:33.805633"},
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
                        46.06,
                        46.45,
                        46.29,
                        52.93,
                        63.27,
                        61.93,
                        54.32,
                        46.94,
                        65.15,
                        61.16,
                        64.79,
                        60.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 60.89,
                "unit": "%",
                "change": -3.9,
                "change_percent": -6.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55.85,
                "min": 46.06,
                "max": 65.15,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.04,
                        "percentage": 26.3
                },
                {
                        "category": "Segment B",
                        "value": 10.44,
                        "percentage": 17.1
                },
                {
                        "category": "Segment C",
                        "value": 6.77,
                        "percentage": 11.1
                },
                {
                        "category": "Segment D",
                        "value": 7.41,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 20.23,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.982336",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Warehouse Safety Incidents Rate"
        }
    },
}
