"""
Supplier Rationalization

The process of analyzing and streamlining the supplier base to reduce complexity and costs.
"""

SUPPLIER_RATIONALIZATION = {
    "code": "SUPPLIER_RATIONALIZATION",
    "name": "Supplier Rationalization",
    "description": "The process of analyzing and streamlining the supplier base to reduce complexity and costs.",
    "formula": "Qualitative Assessment Score based on Rationalization Criteria",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Rationalization to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.647268"},
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
                        50.8,
                        44.18,
                        41.3,
                        48.14,
                        51.12,
                        52.98,
                        45.87,
                        42.52,
                        43.51,
                        53.03,
                        38.79,
                        45.04
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.04,
                "unit": "%",
                "change": 6.25,
                "change_percent": 16.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 46.44,
                "min": 38.79,
                "max": 53.03,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.02,
                        "percentage": 31.1
                },
                {
                        "category": "Category B",
                        "value": 5.81,
                        "percentage": 12.9
                },
                {
                        "category": "Category C",
                        "value": 5.26,
                        "percentage": 11.7
                },
                {
                        "category": "Category D",
                        "value": 4.05,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 15.9,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.881734",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Rationalization"
        }
    },
}
