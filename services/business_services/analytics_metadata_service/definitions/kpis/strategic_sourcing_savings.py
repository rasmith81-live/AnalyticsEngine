"""
Strategic Sourcing Savings

The cost savings achieved through the strategic sourcing process by optimizing supplier selection and procurement practices.
"""

STRATEGIC_SOURCING_SAVINGS = {
    "code": "STRATEGIC_SOURCING_SAVINGS",
    "name": "Strategic Sourcing Savings",
    "description": "The cost savings achieved through the strategic sourcing process by optimizing supplier selection and procurement practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Sourcing Savings to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.612630"},
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
                        59.76,
                        53.29,
                        44.6,
                        45.72,
                        51.58,
                        54.86,
                        60.18,
                        44.07,
                        55.54,
                        57.4,
                        57.62,
                        58.65
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.65,
                "unit": "%",
                "change": 1.03,
                "change_percent": 1.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 53.61,
                "min": 44.07,
                "max": 60.18,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.66,
                        "percentage": 26.7
                },
                {
                        "category": "Segment B",
                        "value": 14.45,
                        "percentage": 24.6
                },
                {
                        "category": "Segment C",
                        "value": 5.76,
                        "percentage": 9.8
                },
                {
                        "category": "Segment D",
                        "value": 5.09,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 17.69,
                        "percentage": 30.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.484577",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Sourcing Savings"
        }
    },
}
