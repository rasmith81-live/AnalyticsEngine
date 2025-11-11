"""
Procurement Cycle Efficiency

The efficiency of the procurement process from requisition to payment.
"""

PROCUREMENT_CYCLE_EFFICIENCY = {
    "code": "PROCUREMENT_CYCLE_EFFICIENCY",
    "name": "Procurement Cycle Efficiency",
    "description": "The efficiency of the procurement process from requisition to payment.",
    "formula": "Total Time for All Procurement Cycles / Number of Procurement Cycles",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Cycle Efficiency to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Payment"], "last_validated": "2025-11-10T13:49:33.254098"},
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
                        282,
                        271,
                        266,
                        242,
                        271,
                        280,
                        257,
                        243,
                        253,
                        262,
                        261,
                        252
                ],
                "unit": "count"
        },
        "current": {
                "value": 252,
                "unit": "count",
                "change": -9,
                "change_percent": -3.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 261.67,
                "min": 242,
                "max": 282,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 51.36,
                        "percentage": 20.4
                },
                {
                        "category": "Segment B",
                        "value": 44.29,
                        "percentage": 17.6
                },
                {
                        "category": "Segment C",
                        "value": 37.63,
                        "percentage": 14.9
                },
                {
                        "category": "Segment D",
                        "value": 14.11,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 104.61,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.599753",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Procurement Cycle Efficiency"
        }
    },
}
