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
                        152.88,
                        113.07,
                        211.85,
                        234.53,
                        141.86,
                        236.57,
                        210.86,
                        153.42,
                        96.76,
                        159.58,
                        177.55,
                        210.7
                ],
                "unit": "units"
        },
        "current": {
                "value": 210.7,
                "unit": "units",
                "change": 33.15,
                "change_percent": 18.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 174.97,
                "min": 96.76,
                "max": 236.57,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 55.81,
                        "percentage": 26.5
                },
                {
                        "category": "Category B",
                        "value": 29.56,
                        "percentage": 14.0
                },
                {
                        "category": "Category C",
                        "value": 24.7,
                        "percentage": 11.7
                },
                {
                        "category": "Category D",
                        "value": 17.48,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 83.15,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.299452",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Yield per Mile"
        }
    },
}
