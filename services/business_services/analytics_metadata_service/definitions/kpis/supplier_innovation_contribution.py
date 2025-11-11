"""
Supplier Innovation Contribution

The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.
"""

SUPPLIER_INNOVATION_CONTRIBUTION = {
    "code": "SUPPLIER_INNOVATION_CONTRIBUTION",
    "name": "Supplier Innovation Contribution",
    "description": "The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Innovation Contribution to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "Supplier"], "last_validated": "2025-11-10T13:49:33.636951"},
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
                        900.09,
                        936.98,
                        860.13,
                        941.81,
                        917.78,
                        936.48,
                        892.64,
                        890.88,
                        910.04,
                        886.71,
                        892.69,
                        932.56
                ],
                "unit": "units"
        },
        "current": {
                "value": 932.56,
                "unit": "units",
                "change": 39.87,
                "change_percent": 4.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 908.23,
                "min": 860.13,
                "max": 941.81,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 227.24,
                        "percentage": 24.4
                },
                {
                        "category": "Segment B",
                        "value": 163.31,
                        "percentage": 17.5
                },
                {
                        "category": "Segment C",
                        "value": 101.05,
                        "percentage": 10.8
                },
                {
                        "category": "Segment D",
                        "value": 112.24,
                        "percentage": 12.0
                },
                {
                        "category": "Other",
                        "value": 328.72,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.558981",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Innovation Contribution"
        }
    },
}
