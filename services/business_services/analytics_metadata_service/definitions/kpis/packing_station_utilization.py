"""
Packing Station Utilization

The percentage of packing stations that are actively in use, reflecting the operational efficiency of packing facilities.
"""

PACKING_STATION_UTILIZATION = {
    "code": "PACKING_STATION_UTILIZATION",
    "name": "Packing Station Utilization",
    "description": "The percentage of packing stations that are actively in use, reflecting the operational efficiency of packing facilities.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Station Utilization to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.175127"},
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
                        355.42,
                        254.46,
                        273.06,
                        332.85,
                        254.87,
                        264.41,
                        236.97,
                        373.86,
                        325.5,
                        294.03,
                        297.4,
                        230.49
                ],
                "unit": "units"
        },
        "current": {
                "value": 230.49,
                "unit": "units",
                "change": -66.91,
                "change_percent": -22.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 291.11,
                "min": 230.49,
                "max": 373.86,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 77.18,
                        "percentage": 33.5
                },
                {
                        "category": "Segment B",
                        "value": 23.18,
                        "percentage": 10.1
                },
                {
                        "category": "Segment C",
                        "value": 35.12,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 25.85,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 69.16,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.433235",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Station Utilization"
        }
    },
}
