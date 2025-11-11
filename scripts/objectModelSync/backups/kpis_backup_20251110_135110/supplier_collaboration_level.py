"""
Supplier Collaboration Level

The extent to which the buying organization works with suppliers to achieve mutual benefits.
"""

SUPPLIER_COLLABORATION_LEVEL = {
    "code": "SUPPLIER_COLLABORATION_LEVEL",
    "name": "Supplier Collaboration Level",
    "description": "The extent to which the buying organization works with suppliers to achieve mutual benefits.",
    "formula": "Qualitative Assessment Score based on Predefined Collaboration Criteria",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Collaboration Level to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.621727"},
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
                        66.52,
                        65.7,
                        58.85,
                        65.5,
                        58.64,
                        61.7,
                        64.0,
                        53.24,
                        57.11,
                        65.89,
                        54.81,
                        64.93
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.93,
                "unit": "%",
                "change": 10.12,
                "change_percent": 18.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 61.41,
                "min": 53.24,
                "max": 66.52,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.97,
                        "percentage": 23.1
                },
                {
                        "category": "Category B",
                        "value": 8.31,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 10.07,
                        "percentage": 15.5
                },
                {
                        "category": "Category D",
                        "value": 5.58,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 26.0,
                        "percentage": 40.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.839947",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Collaboration Level"
        }
    },
}
