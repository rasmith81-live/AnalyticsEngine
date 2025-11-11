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
                        315.66,
                        238.44,
                        289.77,
                        266.36,
                        337.38,
                        251.24,
                        373.0,
                        296.8,
                        334.18,
                        315.99,
                        369.8,
                        334.99
                ],
                "unit": "units"
        },
        "current": {
                "value": 334.99,
                "unit": "units",
                "change": -34.81,
                "change_percent": -9.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 310.3,
                "min": 238.44,
                "max": 373.0,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 60.87,
                        "percentage": 18.2
                },
                {
                        "category": "Segment B",
                        "value": 55.6,
                        "percentage": 16.6
                },
                {
                        "category": "Segment C",
                        "value": 37.93,
                        "percentage": 11.3
                },
                {
                        "category": "Segment D",
                        "value": 51.09,
                        "percentage": 15.3
                },
                {
                        "category": "Other",
                        "value": 129.5,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.593326",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Risk Assessment"
        }
    },
}
