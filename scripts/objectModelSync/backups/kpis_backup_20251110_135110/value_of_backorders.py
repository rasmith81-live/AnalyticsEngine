"""
Value of Backorders

The monetary value of all backordered items.
"""

VALUE_OF_BACKORDERS = {
    "code": "VALUE_OF_BACKORDERS",
    "name": "Value of Backorders",
    "description": "The monetary value of all backordered items.",
    "formula": "Sum of Product Prices * Quantity Backordered",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Value of Backorders to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:49:33.776404"},
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
                        28991.27,
                        39180.52,
                        26861.52,
                        32183.61,
                        28834.67,
                        29142.46,
                        33855.06,
                        35122.07,
                        34684.46,
                        27108.73,
                        32318.79,
                        27866.82
                ],
                "unit": "$"
        },
        "current": {
                "value": 27866.82,
                "unit": "$",
                "change": -4451.97,
                "change_percent": -13.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 31345.83,
                "min": 26861.52,
                "max": 39180.52,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8863.02,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 4167.06,
                        "percentage": 15.0
                },
                {
                        "category": "Category C",
                        "value": 3768.92,
                        "percentage": 13.5
                },
                {
                        "category": "Category D",
                        "value": 2887.03,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 8180.79,
                        "percentage": 29.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.198139",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Value of Backorders"
        }
    },
}
