"""
Stock-out Rate

The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.
"""

STOCK_OUT_RATE = {
    "code": "STOCK_OUT_RATE",
    "name": "Stock-out Rate",
    "description": "The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stock-out Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Inventory", "Order", "Product", "Supplier"], "last_validated": "2025-11-10T13:49:33.589060"},
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
                        54.72,
                        64.77,
                        73.78,
                        54.56,
                        56.22,
                        72.47,
                        57.76,
                        67.94,
                        67.14,
                        70.46,
                        66.94,
                        69.75
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.75,
                "unit": "%",
                "change": 2.81,
                "change_percent": 4.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 64.71,
                "min": 54.56,
                "max": 73.78,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.34,
                        "percentage": 19.1
                },
                {
                        "category": "Segment B",
                        "value": 12.36,
                        "percentage": 17.7
                },
                {
                        "category": "Segment C",
                        "value": 7.89,
                        "percentage": 11.3
                },
                {
                        "category": "Segment D",
                        "value": 5.24,
                        "percentage": 7.5
                },
                {
                        "category": "Other",
                        "value": 30.92,
                        "percentage": 44.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.426048",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Stock-out Rate"
        }
    },
}
