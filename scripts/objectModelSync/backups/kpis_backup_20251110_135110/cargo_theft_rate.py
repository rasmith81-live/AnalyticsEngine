"""
Cargo Theft Rate

The frequency of cargo theft incidents per total shipments, illustrating the level of security threats faced by the supply chain.
"""

CARGO_THEFT_RATE = {
    "code": "CARGO_THEFT_RATE",
    "name": "Cargo Theft Rate",
    "description": "The frequency of cargo theft incidents per total shipments, illustrating the level of security threats faced by the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cargo Theft Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.673409"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        39.8,
                        54.52,
                        57.0,
                        52.95,
                        49.21,
                        56.87,
                        47.39,
                        55.53,
                        54.64,
                        38.98,
                        55.24,
                        45.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.71,
                "unit": "%",
                "change": -9.53,
                "change_percent": -17.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 50.65,
                "min": 38.98,
                "max": 57.0,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.02,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 10.7,
                        "percentage": 23.4
                },
                {
                        "category": "Category C",
                        "value": 7.24,
                        "percentage": 15.8
                },
                {
                        "category": "Category D",
                        "value": 1.52,
                        "percentage": 3.3
                },
                {
                        "category": "Other",
                        "value": 13.23,
                        "percentage": 28.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.070978",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cargo Theft Rate"
        }
    },
}
