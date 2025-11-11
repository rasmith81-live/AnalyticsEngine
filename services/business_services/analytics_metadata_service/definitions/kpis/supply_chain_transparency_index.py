"""
Supply Chain Transparency Index

A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.
"""

SUPPLY_CHAIN_TRANSPARENCY_INDEX = {
    "code": "SUPPLY_CHAIN_TRANSPARENCY_INDEX",
    "name": "Supply Chain Transparency Index",
    "description": "A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Transparency Index to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:33.685504"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        74.8,
                        74.4,
                        82.6,
                        71.9,
                        74.9,
                        74.2,
                        78.8,
                        77.9,
                        73.4,
                        71.9,
                        81.1,
                        81.8
                ],
                "unit": "score"
        },
        "current": {
                "value": 81.8,
                "unit": "score",
                "change": 0.7,
                "change_percent": 0.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 76.47,
                "min": 71.9,
                "max": 82.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 24.6,
                        "percentage": 30.1
                },
                {
                        "category": "Segment B",
                        "value": 12.02,
                        "percentage": 14.7
                },
                {
                        "category": "Segment C",
                        "value": 8.64,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 5.6,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 30.94,
                        "percentage": 37.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.691830",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Transparency Index"
        }
    },
}
