"""
Packaging Damage Rate

The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.
"""

PACKAGING_DAMAGE_RATE = {
    "code": "PACKAGING_DAMAGE_RATE",
    "name": "Packaging Damage Rate",
    "description": "The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Damage Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.142301"},
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
                        75.58,
                        66.96,
                        72.32,
                        70.63,
                        71.08,
                        66.72,
                        75.79,
                        60.01,
                        69.61,
                        69.49,
                        77.08,
                        72.94
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.94,
                "unit": "%",
                "change": -4.14,
                "change_percent": -5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.68,
                "min": 60.01,
                "max": 77.08,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.84,
                        "percentage": 20.3
                },
                {
                        "category": "Category B",
                        "value": 20.16,
                        "percentage": 27.6
                },
                {
                        "category": "Category C",
                        "value": 11.54,
                        "percentage": 15.8
                },
                {
                        "category": "Category D",
                        "value": 3.89,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 22.51,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.785167",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Damage Rate"
        }
    },
}
