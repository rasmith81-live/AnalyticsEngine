"""
Inventory Carrying Cost

The total cost of holding inventory including storage, insurance, and taxes.
"""

INVENTORY_CARRYING_COST = {
    "code": "INVENTORY_CARRYING_COST",
    "name": "Inventory Carrying Cost",
    "description": "The total cost of holding inventory including storage, insurance, and taxes.",
    "formula": "Sum of All Inventory-Related Costs / Total Value of Inventory",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Carrying Cost to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.979047"},
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
                        40233.92,
                        39354.27,
                        27566.7,
                        33274.84,
                        38737.44,
                        30747.55,
                        38534.49,
                        28496.85,
                        39942.78,
                        27880.71,
                        28037.25,
                        32691.81
                ],
                "unit": "$"
        },
        "current": {
                "value": 32691.81,
                "unit": "$",
                "change": 4654.56,
                "change_percent": 16.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 33791.55,
                "min": 27566.7,
                "max": 40233.92,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11025.03,
                        "percentage": 33.7
                },
                {
                        "category": "Segment B",
                        "value": 4466.76,
                        "percentage": 13.7
                },
                {
                        "category": "Segment C",
                        "value": 2583.27,
                        "percentage": 7.9
                },
                {
                        "category": "Segment D",
                        "value": 4195.72,
                        "percentage": 12.8
                },
                {
                        "category": "Other",
                        "value": 10421.03,
                        "percentage": 31.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.054240",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Inventory Carrying Cost"
        }
    },
}
