"""
Packaging Compliance Rate

The percentage of packages that meet regulatory and safety standards, ensuring compliance with industry regulations.
"""

PACKAGING_COMPLIANCE_RATE = {
    "code": "PACKAGING_COMPLIANCE_RATE",
    "name": "Packaging Compliance Rate",
    "description": "The percentage of packages that meet regulatory and safety standards, ensuring compliance with industry regulations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Compliance Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.141234"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        41.54,
                        53.64,
                        46.32,
                        49.77,
                        48.75,
                        44.43,
                        42.19,
                        52.06,
                        57.66,
                        41.61,
                        46.12,
                        52.01
                ],
                "unit": "%"
        },
        "current": {
                "value": 52.01,
                "unit": "%",
                "change": 5.89,
                "change_percent": 12.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.01,
                "min": 41.54,
                "max": 57.66,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 15.8,
                        "percentage": 30.4
                },
                {
                        "category": "Segment B",
                        "value": 11.99,
                        "percentage": 23.1
                },
                {
                        "category": "Segment C",
                        "value": 6.77,
                        "percentage": 13.0
                },
                {
                        "category": "Segment D",
                        "value": 2.24,
                        "percentage": 4.3
                },
                {
                        "category": "Other",
                        "value": 15.21,
                        "percentage": 29.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.363312",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Compliance Rate"
        }
    },
}
