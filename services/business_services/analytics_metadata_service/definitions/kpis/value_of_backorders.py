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
                        33337.59,
                        39155.7,
                        37429.77,
                        41033.79,
                        32777.51,
                        30289.39,
                        31749.6,
                        31856.32,
                        39614.32,
                        33822.08,
                        37600.92,
                        33760.95
                ],
                "unit": "$"
        },
        "current": {
                "value": 33760.95,
                "unit": "$",
                "change": -3839.97,
                "change_percent": -10.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 35202.33,
                "min": 30289.39,
                "max": 41033.79,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 8512.16,
                        "percentage": 25.2
                },
                {
                        "category": "Product Line B",
                        "value": 8657.43,
                        "percentage": 25.6
                },
                {
                        "category": "Product Line C",
                        "value": 3088.03,
                        "percentage": 9.1
                },
                {
                        "category": "Services",
                        "value": 2460.11,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 11043.22,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.929155",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Value of Backorders"
        }
    },
}
