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
                        66.76,
                        53.99,
                        65.71,
                        63.64,
                        56.37,
                        55.28,
                        56.08,
                        59.82,
                        72.88,
                        62.66,
                        67.78,
                        62.21
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.21,
                "unit": "%",
                "change": -5.57,
                "change_percent": -8.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 61.93,
                "min": 53.99,
                "max": 72.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.2,
                        "percentage": 26.0
                },
                {
                        "category": "Segment B",
                        "value": 13.05,
                        "percentage": 21.0
                },
                {
                        "category": "Segment C",
                        "value": 11.11,
                        "percentage": 17.9
                },
                {
                        "category": "Segment D",
                        "value": 5.47,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 16.38,
                        "percentage": 26.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.436441",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Throughput Rate"
        }
    },
}
