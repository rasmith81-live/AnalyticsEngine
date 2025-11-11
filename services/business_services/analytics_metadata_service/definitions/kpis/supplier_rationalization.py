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
                        50.59,
                        35.45,
                        40.25,
                        38.68,
                        51.26,
                        50.03,
                        53.33,
                        47.77,
                        45.72,
                        52.09,
                        51.07,
                        40.67
                ],
                "unit": "%"
        },
        "current": {
                "value": 40.67,
                "unit": "%",
                "change": -10.4,
                "change_percent": -20.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 46.41,
                "min": 35.45,
                "max": 53.33,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.12,
                        "percentage": 34.7
                },
                {
                        "category": "Segment B",
                        "value": 5.78,
                        "percentage": 14.2
                },
                {
                        "category": "Segment C",
                        "value": 3.26,
                        "percentage": 8.0
                },
                {
                        "category": "Segment D",
                        "value": 1.79,
                        "percentage": 4.4
                },
                {
                        "category": "Other",
                        "value": 15.72,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.588884",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Rationalization"
        }
    },
}
