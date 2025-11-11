"""
Percentage of Recycled or Green Products Purchased

The proportion of total purchases that are made up of environmentally friendly or sustainable products.
"""

PERCENTAGE_OF_RECYCLED_OR_GREEN_PRODUCTS_PURCHASED = {
    "code": "PERCENTAGE_OF_RECYCLED_OR_GREEN_PRODUCTS_PURCHASED",
    "name": "Percentage of Recycled or Green Products Purchased",
    "description": "The proportion of total purchases that are made up of environmentally friendly or sustainable products.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Percentage of Recycled or Green Products Purchased to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.229762"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        63.24,
                        62.57,
                        59.83,
                        55.96,
                        57.8,
                        51.76,
                        57.23,
                        60.51,
                        65.37,
                        70.85,
                        67.98,
                        64.79
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.79,
                "unit": "%",
                "change": -3.19,
                "change_percent": -4.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 61.49,
                "min": 51.76,
                "max": 70.85,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 10.7,
                        "percentage": 16.5
                },
                {
                        "category": "Product Line B",
                        "value": 13.23,
                        "percentage": 20.4
                },
                {
                        "category": "Product Line C",
                        "value": 10.34,
                        "percentage": 16.0
                },
                {
                        "category": "Services",
                        "value": 6.64,
                        "percentage": 10.2
                },
                {
                        "category": "Other",
                        "value": 23.88,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.545354",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Percentage of Recycled or Green Products Purchased"
        }
    },
}
