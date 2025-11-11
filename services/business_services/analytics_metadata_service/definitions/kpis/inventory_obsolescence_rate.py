"""
Inventory Obsolescence Rate

The percentage of inventory that becomes obsolete before it is sold or used, reflecting product lifecycle management effectiveness.
"""

INVENTORY_OBSOLESCENCE_RATE = {
    "code": "INVENTORY_OBSOLESCENCE_RATE",
    "name": "Inventory Obsolescence Rate",
    "description": "The percentage of inventory that becomes obsolete before it is sold or used, reflecting product lifecycle management effectiveness.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Obsolescence Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:49:32.982972"},
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
                        79.57,
                        79.3,
                        68.53,
                        75.67,
                        74.21,
                        67.42,
                        75.25,
                        84.81,
                        79.98,
                        75.14,
                        67.62,
                        69.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.41,
                "unit": "%",
                "change": 1.79,
                "change_percent": 2.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 74.74,
                "min": 67.42,
                "max": 84.81,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.33,
                        "percentage": 23.5
                },
                {
                        "category": "Segment B",
                        "value": 15.28,
                        "percentage": 22.0
                },
                {
                        "category": "Segment C",
                        "value": 8.94,
                        "percentage": 12.9
                },
                {
                        "category": "Segment D",
                        "value": 6.39,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 22.47,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.065055",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Obsolescence Rate"
        }
    },
}
