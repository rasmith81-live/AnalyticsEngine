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
                        59.91,
                        70.41,
                        66.89,
                        62.14,
                        73.49,
                        65.18,
                        69.97,
                        59.7,
                        76.57,
                        76.76,
                        69.56,
                        65.36
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.36,
                "unit": "%",
                "change": -4.2,
                "change_percent": -6.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 67.99,
                "min": 59.7,
                "max": 76.76,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.5,
                        "percentage": 23.7
                },
                {
                        "category": "Segment B",
                        "value": 14.18,
                        "percentage": 21.7
                },
                {
                        "category": "Segment C",
                        "value": 8.03,
                        "percentage": 12.3
                },
                {
                        "category": "Segment D",
                        "value": 7.79,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 19.86,
                        "percentage": 30.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.418937",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cargo Theft Rate"
        }
    },
}
