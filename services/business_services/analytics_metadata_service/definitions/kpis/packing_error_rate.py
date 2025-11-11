"""
Packing Error Rate

The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.
"""

PACKING_ERROR_RATE = {
    "code": "PACKING_ERROR_RATE",
    "name": "Packing Error Rate",
    "description": "The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Error Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:49:33.156752"},
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
                        56.4,
                        43.86,
                        45.64,
                        44.82,
                        44.56,
                        54.05,
                        49.25,
                        55.3,
                        56.15,
                        50.5,
                        55.21,
                        55.78
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.78,
                "unit": "%",
                "change": 0.57,
                "change_percent": 1.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 50.96,
                "min": 43.86,
                "max": 56.4,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.93,
                        "percentage": 19.6
                },
                {
                        "category": "Segment B",
                        "value": 14.94,
                        "percentage": 26.8
                },
                {
                        "category": "Segment C",
                        "value": 8.72,
                        "percentage": 15.6
                },
                {
                        "category": "Segment D",
                        "value": 5.79,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 15.4,
                        "percentage": 27.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.397758",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Error Rate"
        }
    },
}
