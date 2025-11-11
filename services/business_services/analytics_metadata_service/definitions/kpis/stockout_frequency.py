"""
Stockout Frequency

The frequency with which inventory items are out of stock.
"""

STOCKOUT_FREQUENCY = {
    "code": "STOCKOUT_FREQUENCY",
    "name": "Stockout Frequency",
    "description": "The frequency with which inventory items are out of stock.",
    "formula": "Total Number of Stockouts / Total Number of Inventory Checks",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stockout Frequency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:49:33.592767"},
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
                        162,
                        193,
                        193,
                        194,
                        163,
                        194,
                        185,
                        154,
                        150,
                        173,
                        167,
                        164
                ],
                "unit": "count"
        },
        "current": {
                "value": 164,
                "unit": "count",
                "change": -3,
                "change_percent": -1.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 174.33,
                "min": 150,
                "max": 194,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 29.54,
                        "percentage": 18.0
                },
                {
                        "category": "Segment B",
                        "value": 41.33,
                        "percentage": 25.2
                },
                {
                        "category": "Segment C",
                        "value": 17.93,
                        "percentage": 10.9
                },
                {
                        "category": "Segment D",
                        "value": 21.82,
                        "percentage": 13.3
                },
                {
                        "category": "Other",
                        "value": 53.38,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.434999",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Stockout Frequency"
        }
    },
}
