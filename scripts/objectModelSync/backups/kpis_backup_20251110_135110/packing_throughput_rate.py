"""
Packing Throughput Rate

The number of units packed over a specific period, indicating the volume and efficiency of packing operations.
"""

PACKING_THROUGHPUT_RATE = {
    "code": "PACKING_THROUGHPUT_RATE",
    "name": "Packing Throughput Rate",
    "description": "The number of units packed over a specific period, indicating the volume and efficiency of packing operations.",
    "formula": "Total Orders Packed / Total Packing Time",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Throughput Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.176364"},
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
                        70.55,
                        71.67,
                        79.42,
                        67.42,
                        77.84,
                        74.85,
                        74.06,
                        70.02,
                        75.63,
                        77.67,
                        77.74,
                        79.03
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.03,
                "unit": "%",
                "change": 1.29,
                "change_percent": 1.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 74.66,
                "min": 67.42,
                "max": 79.42,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.35,
                        "percentage": 16.9
                },
                {
                        "category": "Category B",
                        "value": 20.85,
                        "percentage": 26.4
                },
                {
                        "category": "Category C",
                        "value": 7.65,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 10.46,
                        "percentage": 13.2
                },
                {
                        "category": "Other",
                        "value": 26.72,
                        "percentage": 33.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.842237",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Throughput Rate"
        }
    },
}
