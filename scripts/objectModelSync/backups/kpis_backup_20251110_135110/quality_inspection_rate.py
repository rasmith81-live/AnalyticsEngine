"""
Quality Inspection Rate

The percentage of incoming goods that undergo quality inspection.
"""

QUALITY_INSPECTION_RATE = {
    "code": "QUALITY_INSPECTION_RATE",
    "name": "Quality Inspection Rate",
    "description": "The percentage of incoming goods that undergo quality inspection.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Quality Inspection Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Product", "QualityMetric"], "last_validated": "2025-11-10T13:49:33.307859"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        62.47,
                        65.08,
                        75.13,
                        71.02,
                        76.45,
                        61.3,
                        75.88,
                        67.8,
                        74.44,
                        75.64,
                        75.44,
                        68.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.96,
                "unit": "%",
                "change": -6.48,
                "change_percent": -8.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 70.8,
                "min": 61.3,
                "max": 76.45,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.27,
                        "percentage": 23.6
                },
                {
                        "category": "Category B",
                        "value": 12.99,
                        "percentage": 18.8
                },
                {
                        "category": "Category C",
                        "value": 12.84,
                        "percentage": 18.6
                },
                {
                        "category": "Category D",
                        "value": 8.0,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 18.86,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.026867",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Quality Inspection Rate"
        }
    },
}
