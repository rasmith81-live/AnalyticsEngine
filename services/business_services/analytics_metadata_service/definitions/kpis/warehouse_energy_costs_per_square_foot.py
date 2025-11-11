"""
Warehouse Energy Costs per Square Foot

The cost of energy consumption per square foot of warehouse space.
"""

WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT = {
    "code": "WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT",
    "name": "Warehouse Energy Costs per Square Foot",
    "description": "The cost of energy consumption per square foot of warehouse space.",
    "formula": "Total Energy Costs / Total Square Footage of Warehouse",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Energy Costs per Square Foot to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:49:33.800370"},
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
                        26776.26,
                        25369.12,
                        28861.99,
                        20617.99,
                        34534.12,
                        33230.27,
                        26951.42,
                        21696.76,
                        25206.23,
                        29281.51,
                        23617.28,
                        34328.8
                ],
                "unit": "$"
        },
        "current": {
                "value": 34328.8,
                "unit": "$",
                "change": 10711.52,
                "change_percent": 45.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 27539.31,
                "min": 20617.99,
                "max": 34534.12,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11467.77,
                        "percentage": 33.4
                },
                {
                        "category": "Segment B",
                        "value": 5893.33,
                        "percentage": 17.2
                },
                {
                        "category": "Segment C",
                        "value": 4782.01,
                        "percentage": 13.9
                },
                {
                        "category": "Segment D",
                        "value": 2502.63,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 9683.06,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.971001",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Warehouse Energy Costs per Square Foot"
        }
    },
}
