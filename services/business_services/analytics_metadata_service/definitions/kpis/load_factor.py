"""
Load Factor

The percentage of a transport vehicle’s available capacity that is being used.
"""

LOAD_FACTOR = {
    "code": "LOAD_FACTOR",
    "name": "Load Factor",
    "description": "The percentage of a transport vehicle\u2019s available capacity that is being used.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Load Factor to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:33.022325"},
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
                        932.07,
                        872.88,
                        857.44,
                        891.44,
                        879.5,
                        855.28,
                        890.07,
                        798.89,
                        867.16,
                        814.81,
                        802.61,
                        889.76
                ],
                "unit": "units"
        },
        "current": {
                "value": 889.76,
                "unit": "units",
                "change": 87.15,
                "change_percent": 10.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 862.66,
                "min": 798.89,
                "max": 932.07,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 135.86,
                        "percentage": 15.3
                },
                {
                        "category": "Segment B",
                        "value": 204.44,
                        "percentage": 23.0
                },
                {
                        "category": "Segment C",
                        "value": 102.28,
                        "percentage": 11.5
                },
                {
                        "category": "Segment D",
                        "value": 78.11,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 369.07,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.150838",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Load Factor"
        }
    },
}
