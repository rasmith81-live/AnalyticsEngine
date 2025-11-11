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
                        44.35,
                        39.06,
                        48.52,
                        52.23,
                        38.45,
                        36.73,
                        39.69,
                        40.22,
                        38.05,
                        52.38,
                        43.85,
                        49.24
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.24,
                "unit": "%",
                "change": 5.39,
                "change_percent": 12.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 43.56,
                "min": 36.73,
                "max": 52.38,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.18,
                        "percentage": 32.9
                },
                {
                        "category": "Category B",
                        "value": 8.38,
                        "percentage": 17.0
                },
                {
                        "category": "Category C",
                        "value": 6.29,
                        "percentage": 12.8
                },
                {
                        "category": "Category D",
                        "value": 1.93,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 16.46,
                        "percentage": 33.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.265144",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Warehouse Utilization Rate"
        }
    },
}
