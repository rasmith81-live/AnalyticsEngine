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
                        29.8,
                        29.1,
                        28.1,
                        27.9,
                        30.7,
                        23.5,
                        26.4,
                        28.4,
                        26.4,
                        30.0,
                        23.9,
                        26.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 26.1,
                "unit": "days",
                "change": 2.2,
                "change_percent": 9.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 27.53,
                "min": 23.5,
                "max": 30.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 8.37,
                        "percentage": 32.1
                },
                {
                        "category": "Segment B",
                        "value": 3.88,
                        "percentage": 14.9
                },
                {
                        "category": "Segment C",
                        "value": 2.8,
                        "percentage": 10.7
                },
                {
                        "category": "Segment D",
                        "value": 1.83,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 9.22,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.416861",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Process Cycle Efficiency"
        }
    },
}
