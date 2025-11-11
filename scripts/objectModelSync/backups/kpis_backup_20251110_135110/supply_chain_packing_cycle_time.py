"""
Supply Chain Packing Cycle Time

The total time from order placement to packing completion in the supply chain, providing a measure of packing speed and responsiveness.
"""

SUPPLY_CHAIN_PACKING_CYCLE_TIME = {
    "code": "SUPPLY_CHAIN_PACKING_CYCLE_TIME",
    "name": "Supply Chain Packing Cycle Time",
    "description": "The total time from order placement to packing completion in the supply chain, providing a measure of packing speed and responsiveness.",
    "formula": "Total Packing Cycle Time / Total Orders Packed",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Packing Cycle Time to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.662931"},
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
                        18.8,
                        19.6,
                        18.3,
                        14.2,
                        16.4,
                        16.7,
                        14.1,
                        18.1,
                        20.2,
                        20.5,
                        16.2,
                        15.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 15.3,
                "unit": "days",
                "change": -0.9,
                "change_percent": -5.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 17.37,
                "min": 14.1,
                "max": 20.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 4.93,
                        "percentage": 32.2
                },
                {
                        "category": "Category B",
                        "value": 3.08,
                        "percentage": 20.1
                },
                {
                        "category": "Category C",
                        "value": 1.78,
                        "percentage": 11.6
                },
                {
                        "category": "Category D",
                        "value": 0.87,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 4.64,
                        "percentage": 30.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.906840",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supply Chain Packing Cycle Time"
        }
    },
}
