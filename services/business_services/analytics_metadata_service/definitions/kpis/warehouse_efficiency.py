"""
Average Warehouse Efficiency

The overall efficiency of warehouse operations based on output over input.
"""

WAREHOUSE_EFFICIENCY = {
    "code": "WAREHOUSE_EFFICIENCY",
    "name": "Average Warehouse Efficiency",
    "description": "The overall efficiency of warehouse operations based on output over input.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Warehouse Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Order", "Warehouse"], "last_validated": "2025-11-10T13:49:33.797103"},
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
                        604.16,
                        580.42,
                        537.2,
                        484.78,
                        551.61,
                        534.54,
                        604.06,
                        542.66,
                        504.14,
                        476.15,
                        613.66,
                        611.3
                ],
                "unit": "units"
        },
        "current": {
                "value": 611.3,
                "unit": "units",
                "change": -2.36,
                "change_percent": -0.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 553.72,
                "min": 476.15,
                "max": 613.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 197.58,
                        "percentage": 32.3
                },
                {
                        "category": "Segment B",
                        "value": 62.12,
                        "percentage": 10.2
                },
                {
                        "category": "Segment C",
                        "value": 67.59,
                        "percentage": 11.1
                },
                {
                        "category": "Segment D",
                        "value": 41.26,
                        "percentage": 6.7
                },
                {
                        "category": "Other",
                        "value": 242.75,
                        "percentage": 39.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.968388",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Warehouse Efficiency"
        }
    },
}
