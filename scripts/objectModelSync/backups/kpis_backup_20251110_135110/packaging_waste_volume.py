"""
Packaging Waste Volume

The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.
"""

PACKAGING_WASTE_VOLUME = {
    "code": "PACKAGING_WASTE_VOLUME",
    "name": "Packaging Waste Volume",
    "description": "The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.",
    "formula": "Total Waste Volume / Total Packaging Units",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Waste Volume to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.149325"},
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
                        524.57,
                        567.12,
                        655.79,
                        595.62,
                        607.74,
                        553.48,
                        541.12,
                        591.07,
                        632.5,
                        644.6,
                        562.44,
                        561.65
                ],
                "unit": "units"
        },
        "current": {
                "value": 561.65,
                "unit": "units",
                "change": -0.79,
                "change_percent": -0.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 586.48,
                "min": 524.57,
                "max": 655.79,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 147.45,
                        "percentage": 26.3
                },
                {
                        "category": "Category B",
                        "value": 135.01,
                        "percentage": 24.0
                },
                {
                        "category": "Category C",
                        "value": 83.93,
                        "percentage": 14.9
                },
                {
                        "category": "Category D",
                        "value": 45.52,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 149.74,
                        "percentage": 26.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.797041",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packaging Waste Volume"
        }
    },
}
