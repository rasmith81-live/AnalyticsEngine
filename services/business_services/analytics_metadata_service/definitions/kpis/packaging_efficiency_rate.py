"""
Packaging Efficiency Rate

The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.
"""

PACKAGING_EFFICIENCY_RATE = {
    "code": "PACKAGING_EFFICIENCY_RATE",
    "name": "Packaging Efficiency Rate",
    "description": "The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Efficiency Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.143364"},
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
                        62.68,
                        55.13,
                        44.18,
                        54.79,
                        61.77,
                        60.75,
                        49.63,
                        58.21,
                        57.14,
                        52.79,
                        48.5,
                        55.84
                ],
                "unit": "%"
        },
        "current": {
                "value": 55.84,
                "unit": "%",
                "change": 7.34,
                "change_percent": 15.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 55.12,
                "min": 44.18,
                "max": 62.68,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.73,
                        "percentage": 19.2
                },
                {
                        "category": "Segment B",
                        "value": 15.55,
                        "percentage": 27.8
                },
                {
                        "category": "Segment C",
                        "value": 6.99,
                        "percentage": 12.5
                },
                {
                        "category": "Segment D",
                        "value": 3.25,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 19.32,
                        "percentage": 34.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.371799",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Efficiency Rate"
        }
    },
}
