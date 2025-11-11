"""
Freight Cost as a Percentage of Sales

The cost of transportation and logistics as a percentage of total sales, indicating the cost efficiency of logistics.
"""

FREIGHT_COST_AS_A_PERCENTAGE_OF_SALES = {
    "code": "FREIGHT_COST_AS_A_PERCENTAGE_OF_SALES",
    "name": "Freight Cost as a Percentage of Sales",
    "description": "The cost of transportation and logistics as a percentage of total sales, indicating the cost efficiency of logistics.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Freight Cost as a Percentage of Sales to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.962522"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        54.36,
                        54.94,
                        54.57,
                        54.71,
                        45.98,
                        38.08,
                        51.73,
                        52.14,
                        38.36,
                        55.2,
                        44.22,
                        46.06
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.06,
                "unit": "%",
                "change": 1.84,
                "change_percent": 4.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 49.2,
                "min": 38.08,
                "max": 55.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 7.39,
                        "percentage": 16.0
                },
                {
                        "category": "Channel Sales",
                        "value": 13.19,
                        "percentage": 28.6
                },
                {
                        "category": "Online Sales",
                        "value": 5.24,
                        "percentage": 11.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.4,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 14.84,
                        "percentage": 32.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.007735",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Freight Cost as a Percentage of Sales"
        }
    },
}
