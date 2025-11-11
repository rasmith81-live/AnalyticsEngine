"""
Packing Cost Variance

The difference between projected and actual packing costs, important for budget management and cost control.
"""

PACKING_COST_VARIANCE = {
    "code": "PACKING_COST_VARIANCE",
    "name": "Packing Cost Variance",
    "description": "The difference between projected and actual packing costs, important for budget management and cost control.",
    "formula": "Actual Packing Costs - Budgeted Packing Costs",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Cost Variance to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.152519"},
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
                        28360.88,
                        29926.82,
                        38332.99,
                        24376.65,
                        29192.04,
                        35915.39,
                        36550.79,
                        30126.53,
                        26374.55,
                        24077.39,
                        25160.68,
                        25544.54
                ],
                "unit": "$"
        },
        "current": {
                "value": 25544.54,
                "unit": "$",
                "change": 383.86,
                "change_percent": 1.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 29494.94,
                "min": 24077.39,
                "max": 38332.99,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7805.42,
                        "percentage": 30.6
                },
                {
                        "category": "Category B",
                        "value": 3917.59,
                        "percentage": 15.3
                },
                {
                        "category": "Category C",
                        "value": 4585.39,
                        "percentage": 18.0
                },
                {
                        "category": "Category D",
                        "value": 1220.27,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 8015.87,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.802781",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Cost Variance"
        }
    },
}
