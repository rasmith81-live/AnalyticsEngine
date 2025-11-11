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
                        49329.41,
                        51836.74,
                        48362.91,
                        61893.7,
                        61364.74,
                        51911.43,
                        49869.39,
                        57628.06,
                        59309.72,
                        50670.85,
                        60383.1,
                        47598.79
                ],
                "unit": "$"
        },
        "current": {
                "value": 47598.79,
                "unit": "$",
                "change": -12784.31,
                "change_percent": -21.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 54179.9,
                "min": 47598.79,
                "max": 61893.7,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16256.76,
                        "percentage": 34.2
                },
                {
                        "category": "Segment B",
                        "value": 9106.21,
                        "percentage": 19.1
                },
                {
                        "category": "Segment C",
                        "value": 6715.04,
                        "percentage": 14.1
                },
                {
                        "category": "Segment D",
                        "value": 4126.19,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 11394.59,
                        "percentage": 23.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.389324",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Cost Variance"
        }
    },
}
