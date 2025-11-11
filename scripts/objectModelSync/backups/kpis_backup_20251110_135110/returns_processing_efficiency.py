"""
Returns Processing Efficiency

The effectiveness of handling and processing returned items.
"""

RETURNS_PROCESSING_EFFICIENCY = {
    "code": "RETURNS_PROCESSING_EFFICIENCY",
    "name": "Returns Processing Efficiency",
    "description": "The effectiveness of handling and processing returned items.",
    "formula": "Total Time Taken for Processing Returns / Total Number of Returned Items",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Returns Processing Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Product", "Return"], "last_validated": "2025-11-10T13:49:33.355150"},
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
                        130,
                        154,
                        176,
                        178,
                        180,
                        133,
                        140,
                        166,
                        178,
                        158,
                        151,
                        179
                ],
                "unit": "count"
        },
        "current": {
                "value": 179,
                "unit": "count",
                "change": 28,
                "change_percent": 18.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 160.25,
                "min": 130,
                "max": 180,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 56.78,
                        "percentage": 31.7
                },
                {
                        "category": "Category B",
                        "value": 36.83,
                        "percentage": 20.6
                },
                {
                        "category": "Category C",
                        "value": 18.68,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 11.74,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 54.97,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.105857",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Returns Processing Efficiency"
        }
    },
}
