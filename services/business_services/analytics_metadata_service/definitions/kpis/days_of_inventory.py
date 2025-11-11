"""
Days of Inventory

How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.
"""

DAYS_OF_INVENTORY = {
    "code": "DAYS_OF_INVENTORY",
    "name": "Days of Inventory",
    "description": "How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Days of Inventory to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.900102"},
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
                        10.7,
                        10.3,
                        9.0,
                        9.4,
                        10.8,
                        10.5,
                        9.9,
                        12.4,
                        6.2,
                        8.1,
                        7.3,
                        7.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 7.0,
                "unit": "days",
                "change": -0.3,
                "change_percent": -4.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 9.3,
                "min": 6.2,
                "max": 12.4,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 1.06,
                        "percentage": 15.1
                },
                {
                        "category": "Segment B",
                        "value": 1.07,
                        "percentage": 15.3
                },
                {
                        "category": "Segment C",
                        "value": 1.3,
                        "percentage": 18.6
                },
                {
                        "category": "Segment D",
                        "value": 0.39,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 3.18,
                        "percentage": 45.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.867230",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Days of Inventory"
        }
    },
}
