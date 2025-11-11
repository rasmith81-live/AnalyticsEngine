"""
Fill Rate

The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.
"""

FILL_RATE = {
    "code": "FILL_RATE",
    "name": "Fill Rate",
    "description": "The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Fill Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Order", "Product"], "last_validated": "2025-11-10T13:49:32.952217"},
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
                        50.78,
                        51.78,
                        40.86,
                        51.43,
                        55.89,
                        54.52,
                        52.99,
                        40.01,
                        43.48,
                        38.27,
                        46.06,
                        56.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.89,
                "unit": "%",
                "change": 10.83,
                "change_percent": 23.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.58,
                "min": 38.27,
                "max": 56.89,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.44,
                        "percentage": 30.7
                },
                {
                        "category": "Segment B",
                        "value": 8.27,
                        "percentage": 14.5
                },
                {
                        "category": "Segment C",
                        "value": 10.88,
                        "percentage": 19.1
                },
                {
                        "category": "Segment D",
                        "value": 2.16,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 18.14,
                        "percentage": 31.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.983436",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Fill Rate"
        }
    },
}
