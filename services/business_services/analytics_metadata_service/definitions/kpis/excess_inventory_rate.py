"""
Excess Inventory Rate

The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.
"""

EXCESS_INVENTORY_RATE = {
    "code": "EXCESS_INVENTORY_RATE",
    "name": "Excess Inventory Rate",
    "description": "The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Excess Inventory Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.949625"},
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
                        32.51,
                        33.73,
                        31.78,
                        48.1,
                        33.04,
                        30.67,
                        34.29,
                        38.95,
                        33.18,
                        49.62,
                        48.97,
                        48.62
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.62,
                "unit": "%",
                "change": -0.35,
                "change_percent": -0.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 38.62,
                "min": 30.67,
                "max": 49.62,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.84,
                        "percentage": 22.3
                },
                {
                        "category": "Segment B",
                        "value": 10.28,
                        "percentage": 21.1
                },
                {
                        "category": "Segment C",
                        "value": 5.27,
                        "percentage": 10.8
                },
                {
                        "category": "Segment D",
                        "value": 2.34,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 19.89,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.977586",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Excess Inventory Rate"
        }
    },
}
