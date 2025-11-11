"""
Packing Quality Control Rate

The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.
"""

PACKING_QUALITY_CONTROL_RATE = {
    "code": "PACKING_QUALITY_CONTROL_RATE",
    "name": "Packing Quality Control Rate",
    "description": "The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Quality Control Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Order", "Product", "QualityMetric"], "last_validated": "2025-11-10T13:49:33.170760"},
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
                        67.03,
                        79.84,
                        71.8,
                        65.89,
                        62.92,
                        69.18,
                        80.68,
                        77.59,
                        78.05,
                        65.7,
                        79.1,
                        62.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.08,
                "unit": "%",
                "change": -17.02,
                "change_percent": -21.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 71.66,
                "min": 62.08,
                "max": 80.68,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.25,
                        "percentage": 31.0
                },
                {
                        "category": "Segment B",
                        "value": 10.47,
                        "percentage": 16.9
                },
                {
                        "category": "Segment C",
                        "value": 9.78,
                        "percentage": 15.8
                },
                {
                        "category": "Segment D",
                        "value": 3.35,
                        "percentage": 5.4
                },
                {
                        "category": "Other",
                        "value": 19.23,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.423893",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Quality Control Rate"
        }
    },
}
