"""
Warehouse Utilization Rate

The percentage of warehouse capacity that is currently being used, indicating the effectiveness of space management.
"""

WAREHOUSE_UTILIZATION_RATE = {
    "code": "WAREHOUSE_UTILIZATION_RATE",
    "name": "Warehouse Utilization Rate",
    "description": "The percentage of warehouse capacity that is currently being used, indicating the effectiveness of space management.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Utilization Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:49:33.807276"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        75.75,
                        66.55,
                        64.61,
                        76.51,
                        63.07,
                        73.71,
                        63.01,
                        58.37,
                        77.36,
                        60.41,
                        65.72,
                        72.47
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.47,
                "unit": "%",
                "change": 6.75,
                "change_percent": 10.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.13,
                "min": 58.37,
                "max": 77.36,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.05,
                        "percentage": 23.5
                },
                {
                        "category": "Segment B",
                        "value": 9.07,
                        "percentage": 12.5
                },
                {
                        "category": "Segment C",
                        "value": 13.95,
                        "percentage": 19.2
                },
                {
                        "category": "Segment D",
                        "value": 4.53,
                        "percentage": 6.3
                },
                {
                        "category": "Other",
                        "value": 27.87,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.986020",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Warehouse Utilization Rate"
        }
    },
}
