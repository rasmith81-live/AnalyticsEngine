"""
Yield per Mile

The revenue or profit generated for each mile of transportation.
"""

YIELD_PER_MILE = {
    "code": "YIELD_PER_MILE",
    "name": "Yield per Mile",
    "description": "The revenue or profit generated for each mile of transportation.",
    "formula": "Total Revenue / Total Miles Driven",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Yield per Mile to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.828786"},
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
                        630.96,
                        636.77,
                        677.91,
                        664.8,
                        620.85,
                        558.2,
                        632.91,
                        621.52,
                        534.43,
                        664.06,
                        569.74,
                        656.52
                ],
                "unit": "units"
        },
        "current": {
                "value": 656.52,
                "unit": "units",
                "change": 86.78,
                "change_percent": 15.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 622.39,
                "min": 534.43,
                "max": 677.91,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 179.1,
                        "percentage": 27.3
                },
                {
                        "category": "Segment B",
                        "value": 102.63,
                        "percentage": 15.6
                },
                {
                        "category": "Segment C",
                        "value": 59.53,
                        "percentage": 9.1
                },
                {
                        "category": "Segment D",
                        "value": 93.65,
                        "percentage": 14.3
                },
                {
                        "category": "Other",
                        "value": 221.61,
                        "percentage": 33.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:14.021361",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Yield per Mile"
        }
    },
}
