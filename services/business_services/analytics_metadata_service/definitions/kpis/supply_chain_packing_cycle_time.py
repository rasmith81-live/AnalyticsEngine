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
                        11.5,
                        16.3,
                        16.8,
                        15.9,
                        18.1,
                        15.4,
                        13.7,
                        13.3,
                        16.4,
                        17.0,
                        18.2,
                        17.4
                ],
                "unit": "days"
        },
        "current": {
                "value": 17.4,
                "unit": "days",
                "change": -0.8,
                "change_percent": -4.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 15.83,
                "min": 11.5,
                "max": 18.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 5.25,
                        "percentage": 30.2
                },
                {
                        "category": "Segment B",
                        "value": 2.14,
                        "percentage": 12.3
                },
                {
                        "category": "Segment C",
                        "value": 3.22,
                        "percentage": 18.5
                },
                {
                        "category": "Segment D",
                        "value": 0.73,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 6.06,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.624804",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supply Chain Packing Cycle Time"
        }
    },
}
