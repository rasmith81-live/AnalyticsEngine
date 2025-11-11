"""
Vehicle Maintenance Costs per Mile

The cost incurred for maintaining a vehicle per mile driven.
"""

VEHICLE_MAINTENANCE_COSTS_PER_MILE = {
    "code": "VEHICLE_MAINTENANCE_COSTS_PER_MILE",
    "name": "Vehicle Maintenance Costs per Mile",
    "description": "The cost incurred for maintaining a vehicle per mile driven.",
    "formula": "Total Vehicle Maintenance Costs / Total Miles Driven",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Vehicle Maintenance Costs per Mile to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.779686"},
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
                        30337.2,
                        27733.84,
                        26866.17,
                        20233.38,
                        29853.24,
                        26266.21,
                        23251.51,
                        18331.43,
                        22921.44,
                        28133.82,
                        26798.69,
                        26067.42
                ],
                "unit": "$"
        },
        "current": {
                "value": 26067.42,
                "unit": "$",
                "change": -731.27,
                "change_percent": -2.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 25566.2,
                "min": 18331.43,
                "max": 30337.2,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 7226.74,
                        "percentage": 27.7
                },
                {
                        "category": "Segment B",
                        "value": 3100.93,
                        "percentage": 11.9
                },
                {
                        "category": "Segment C",
                        "value": 2409.14,
                        "percentage": 9.2
                },
                {
                        "category": "Segment D",
                        "value": 3463.46,
                        "percentage": 13.3
                },
                {
                        "category": "Other",
                        "value": 9867.15,
                        "percentage": 37.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.937641",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Vehicle Maintenance Costs per Mile"
        }
    },
}
