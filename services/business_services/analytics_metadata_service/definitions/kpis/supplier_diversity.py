"""
Supplier Diversity

The diversity of the company
"""

SUPPLIER_DIVERSITY = {
    "code": "SUPPLIER_DIVERSITY",
    "name": "Supplier Diversity",
    "description": "The diversity of the company",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Diversity to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.630668"},
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
                        505.03,
                        505.81,
                        542.88,
                        531.22,
                        418.7,
                        563.72,
                        527.98,
                        454.86,
                        482.66,
                        541.2,
                        461.17,
                        499.15
                ],
                "unit": "units"
        },
        "current": {
                "value": 499.15,
                "unit": "units",
                "change": 37.98,
                "change_percent": 8.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 502.86,
                "min": 418.7,
                "max": 563.72,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 143.75,
                        "percentage": 28.8
                },
                {
                        "category": "Segment B",
                        "value": 109.31,
                        "percentage": 21.9
                },
                {
                        "category": "Segment C",
                        "value": 40.21,
                        "percentage": 8.1
                },
                {
                        "category": "Segment D",
                        "value": 23.55,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 182.33,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.535548",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Diversity"
        }
    },
}
