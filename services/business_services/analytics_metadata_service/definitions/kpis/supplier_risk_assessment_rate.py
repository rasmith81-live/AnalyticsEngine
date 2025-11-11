"""
Supplier Risk Assessment Rate

The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.
"""

SUPPLIER_RISK_ASSESSMENT_RATE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_RATE",
    "name": "Supplier Risk Assessment Rate",
    "description": "The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Risk Assessment Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.653769"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        50.01,
                        38.8,
                        46.74,
                        51.29,
                        36.4,
                        38.0,
                        39.68,
                        51.87,
                        39.71,
                        36.81,
                        33.89,
                        45.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.71,
                "unit": "%",
                "change": 11.82,
                "change_percent": 34.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 42.41,
                "min": 33.89,
                "max": 51.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.31,
                        "percentage": 20.4
                },
                {
                        "category": "Segment B",
                        "value": 10.95,
                        "percentage": 24.0
                },
                {
                        "category": "Segment C",
                        "value": 4.83,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 2.77,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 17.85,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.602079",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Risk Assessment Rate"
        }
    },
}
