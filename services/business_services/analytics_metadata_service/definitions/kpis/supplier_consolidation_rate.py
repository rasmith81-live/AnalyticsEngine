"""
Supplier Consolidation Rate

The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.
"""

SUPPLIER_CONSOLIDATION_RATE = {
    "code": "SUPPLIER_CONSOLIDATION_RATE",
    "name": "Supplier Consolidation Rate",
    "description": "The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Consolidation Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.627069"},
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
                        55.47,
                        43.01,
                        58.78,
                        40.69,
                        55.67,
                        55.69,
                        52.39,
                        55.13,
                        55.32,
                        52.15,
                        59.16,
                        51.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.08,
                "unit": "%",
                "change": -8.08,
                "change_percent": -13.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.88,
                "min": 40.69,
                "max": 59.16,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 8.1,
                        "percentage": 15.9
                },
                {
                        "category": "Segment B",
                        "value": 9.52,
                        "percentage": 18.6
                },
                {
                        "category": "Segment C",
                        "value": 6.98,
                        "percentage": 13.7
                },
                {
                        "category": "Segment D",
                        "value": 6.75,
                        "percentage": 13.2
                },
                {
                        "category": "Other",
                        "value": 19.73,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.525567",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Consolidation Rate"
        }
    },
}
