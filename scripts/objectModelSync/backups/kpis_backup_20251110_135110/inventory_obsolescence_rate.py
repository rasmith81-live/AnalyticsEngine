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
                        58.45,
                        65.1,
                        62.67,
                        54.99,
                        63.19,
                        60.56,
                        59.17,
                        49.39,
                        45.58,
                        53.79,
                        54.18,
                        58.63
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.63,
                "unit": "%",
                "change": 4.45,
                "change_percent": 8.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 57.14,
                "min": 45.58,
                "max": 65.1,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.74,
                        "percentage": 20.0
                },
                {
                        "category": "Category B",
                        "value": 12.42,
                        "percentage": 21.2
                },
                {
                        "category": "Category C",
                        "value": 10.02,
                        "percentage": 17.1
                },
                {
                        "category": "Category D",
                        "value": 6.18,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 18.27,
                        "percentage": 31.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.548357",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Obsolescence Rate"
        }
    },
}
