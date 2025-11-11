"""
Supplier Risk Assessment

The identification and evaluation of risks associated with a supplier
"""

SUPPLIER_RISK_ASSESSMENT = {
    "code": "SUPPLIER_RISK_ASSESSMENT",
    "name": "Supplier Risk Assessment",
    "description": "The identification and evaluation of risks associated with a supplier",
    "formula": "Qualitative Risk Score based on Predefined Risk Criteria",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Risk Assessment to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.649230"},
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
                        249.52,
                        310.34,
                        279.89,
                        255.77,
                        339.36,
                        358.81,
                        353.8,
                        299.86,
                        280.36,
                        255.41,
                        298.79,
                        286.85
                ],
                "unit": "units"
        },
        "current": {
                "value": 286.85,
                "unit": "units",
                "change": -11.94,
                "change_percent": -4.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 297.4,
                "min": 249.52,
                "max": 358.81,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 98.43,
                        "percentage": 34.3
                },
                {
                        "category": "Category B",
                        "value": 28.91,
                        "percentage": 10.1
                },
                {
                        "category": "Category C",
                        "value": 53.85,
                        "percentage": 18.8
                },
                {
                        "category": "Category D",
                        "value": 26.73,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 78.93,
                        "percentage": 27.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.884385",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Risk Assessment"
        }
    },
}
