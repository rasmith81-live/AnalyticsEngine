"""
Transportation Cost per Unit Shipped

The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.
"""

TRANSPORTATION_COST_PER_UNIT_SHIPPED = {
    "code": "TRANSPORTATION_COST_PER_UNIT_SHIPPED",
    "name": "Transportation Cost per Unit Shipped",
    "description": "The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.",
    "formula": "Total Transportation Costs / Total Units Shipped",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Cost per Unit Shipped to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.755475"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        74108.69,
                        72801.23,
                        71838.45,
                        68633.88,
                        76517.33,
                        79492.23,
                        75812.62,
                        73236.14,
                        72160.86,
                        74911.85,
                        72080.01,
                        75161.1
                ],
                "unit": "$"
        },
        "current": {
                "value": 75161.1,
                "unit": "$",
                "change": 3081.09,
                "change_percent": 4.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 73896.2,
                "min": 68633.88,
                "max": 79492.23,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 25675.84,
                        "percentage": 34.2
                },
                {
                        "category": "Segment B",
                        "value": 11078.48,
                        "percentage": 14.7
                },
                {
                        "category": "Segment C",
                        "value": 9478.79,
                        "percentage": 12.6
                },
                {
                        "category": "Segment D",
                        "value": 4416.77,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 24511.22,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.881376",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Transportation Cost per Unit Shipped"
        }
    },
}
