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
                        280,
                        281,
                        275,
                        317,
                        310,
                        311,
                        300,
                        274,
                        317,
                        321,
                        295,
                        295
                ],
                "unit": "count"
        },
        "current": {
                "value": 295,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 298.0,
                "min": 274,
                "max": 321,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 54.68,
                        "percentage": 18.5
                },
                {
                        "category": "Category B",
                        "value": 39.21,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 64.13,
                        "percentage": 21.7
                },
                {
                        "category": "Category D",
                        "value": 16.52,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 120.46,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.951571",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Procurement Cycle Efficiency"
        }
    },
}
