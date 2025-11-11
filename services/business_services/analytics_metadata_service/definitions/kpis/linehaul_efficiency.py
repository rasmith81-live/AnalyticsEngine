"""
Linehaul Efficiency

The efficiency of transportation between two points excluding pickup and delivery operations.
"""

LINEHAUL_EFFICIENCY = {
    "code": "LINEHAUL_EFFICIENCY",
    "name": "Linehaul Efficiency",
    "description": "The efficiency of transportation between two points excluding pickup and delivery operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Linehaul Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.021081"},
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
                        528.32,
                        637.66,
                        573.87,
                        534.45,
                        560.19,
                        552.96,
                        571.36,
                        576.52,
                        621.83,
                        575.72,
                        609.18,
                        518.52
                ],
                "unit": "units"
        },
        "current": {
                "value": 518.52,
                "unit": "units",
                "change": -90.66,
                "change_percent": -14.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 571.72,
                "min": 518.52,
                "max": 637.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 94.7,
                        "percentage": 18.3
                },
                {
                        "category": "Segment B",
                        "value": 69.86,
                        "percentage": 13.5
                },
                {
                        "category": "Segment C",
                        "value": 74.41,
                        "percentage": 14.4
                },
                {
                        "category": "Segment D",
                        "value": 74.45,
                        "percentage": 14.4
                },
                {
                        "category": "Other",
                        "value": 205.1,
                        "percentage": 39.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.143539",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Linehaul Efficiency"
        }
    },
}
