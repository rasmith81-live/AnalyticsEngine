"""
Cost Avoidance

The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.
"""

COST_AVOIDANCE = {
    "code": "COST_AVOIDANCE",
    "name": "Cost Avoidance",
    "description": "The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.",
    "formula": "Projected Cost without Procurement Intervention - Actual Cost Post-Intervention",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost Avoidance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.722526"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        63683.13,
                        72777.88,
                        76707.59,
                        64335.72,
                        71453.61,
                        69765.72,
                        67034.04,
                        66586.86,
                        78456.47,
                        73102.97,
                        73906.54,
                        68864.07
                ],
                "unit": "$"
        },
        "current": {
                "value": 68864.07,
                "unit": "$",
                "change": -5042.47,
                "change_percent": -6.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 70556.22,
                "min": 63683.13,
                "max": 78456.47,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18130.64,
                        "percentage": 26.3
                },
                {
                        "category": "Segment B",
                        "value": 15259.61,
                        "percentage": 22.2
                },
                {
                        "category": "Segment C",
                        "value": 6978.02,
                        "percentage": 10.1
                },
                {
                        "category": "Segment D",
                        "value": 6828.17,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 21667.63,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.520917",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost Avoidance"
        }
    },
}
