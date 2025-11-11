"""
Packing Process Cycle Efficiency

The ratio of value-added time to total packing cycle time, indicating the efficiency of packing processes.
"""

PACKING_PROCESS_CYCLE_EFFICIENCY = {
    "code": "PACKING_PROCESS_CYCLE_EFFICIENCY",
    "name": "Packing Process Cycle Efficiency",
    "description": "The ratio of value-added time to total packing cycle time, indicating the efficiency of packing processes.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Process Cycle Efficiency to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.167577"},
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
                        15.5,
                        14.7,
                        13.6,
                        11.4,
                        12.7,
                        15.1,
                        16.1,
                        11.6,
                        16.1,
                        14.0,
                        15.2,
                        10.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 10.3,
                "unit": "days",
                "change": -4.9,
                "change_percent": -32.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 13.86,
                "min": 10.3,
                "max": 16.1,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.04,
                        "percentage": 29.5
                },
                {
                        "category": "Category B",
                        "value": 2.04,
                        "percentage": 19.8
                },
                {
                        "category": "Category C",
                        "value": 1.48,
                        "percentage": 14.4
                },
                {
                        "category": "Category D",
                        "value": 0.59,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 3.15,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.828417",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Process Cycle Efficiency"
        }
    },
}
