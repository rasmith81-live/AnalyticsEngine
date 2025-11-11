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
                        44.82,
                        35.41,
                        41.26,
                        34.59,
                        35.76,
                        44.53,
                        37.02,
                        45.21,
                        43.02,
                        35.56,
                        38.3,
                        43.51
                ],
                "unit": "%"
        },
        "current": {
                "value": 43.51,
                "unit": "%",
                "change": 5.21,
                "change_percent": 13.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 39.92,
                "min": 34.59,
                "max": 45.21,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.49,
                        "percentage": 24.1
                },
                {
                        "category": "Category B",
                        "value": 10.84,
                        "percentage": 24.9
                },
                {
                        "category": "Category C",
                        "value": 5.47,
                        "percentage": 12.6
                },
                {
                        "category": "Category D",
                        "value": 3.19,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 13.52,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.262393",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Warehouse Safety Incidents Rate"
        }
    },
}
