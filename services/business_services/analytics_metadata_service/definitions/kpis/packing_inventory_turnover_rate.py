"""
Packing Inventory Turnover Rate

The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.
"""

PACKING_INVENTORY_TURNOVER_RATE = {
    "code": "PACKING_INVENTORY_TURNOVER_RATE",
    "name": "Packing Inventory Turnover Rate",
    "description": "The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.",
    "formula": "Total Packing Materials Used / Average Packing Inventory",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Inventory Turnover Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:33.161474"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        67.44,
                        76.22,
                        83.46,
                        64.59,
                        70.96,
                        66.66,
                        77.73,
                        71.86,
                        80.47,
                        80.8,
                        77.88,
                        82.16
                ],
                "unit": "%"
        },
        "current": {
                "value": 82.16,
                "unit": "%",
                "change": 4.28,
                "change_percent": 5.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 75.02,
                "min": 64.59,
                "max": 83.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 26.2,
                        "percentage": 31.9
                },
                {
                        "category": "Segment B",
                        "value": 12.87,
                        "percentage": 15.7
                },
                {
                        "category": "Segment C",
                        "value": 13.91,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 4.78,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 24.4,
                        "percentage": 29.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.405465",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Inventory Turnover Rate"
        }
    },
}
