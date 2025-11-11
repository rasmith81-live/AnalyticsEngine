"""
Carbon Footprint of Procurement

The total greenhouse gas emissions associated with procurement activities, aiming to measure and reduce the carbon footprint as per ISO 20400 guidance.
"""

CARBON_FOOTPRINT_OF_PROCUREMENT = {
    "code": "CARBON_FOOTPRINT_OF_PROCUREMENT",
    "name": "Carbon Footprint of Procurement",
    "description": "The total greenhouse gas emissions associated with procurement activities, aiming to measure and reduce the carbon footprint as per ISO 20400 guidance.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Carbon Footprint of Procurement to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.670304"},
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
                        851.94,
                        941.31,
                        797.03,
                        822.1,
                        908.32,
                        859.71,
                        919.2,
                        832.02,
                        844.63,
                        863.51,
                        835.09,
                        825.21
                ],
                "unit": "units"
        },
        "current": {
                "value": 825.21,
                "unit": "units",
                "change": -9.88,
                "change_percent": -1.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 858.34,
                "min": 797.03,
                "max": 941.31,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 245.43,
                        "percentage": 29.7
                },
                {
                        "category": "Segment B",
                        "value": 181.16,
                        "percentage": 22.0
                },
                {
                        "category": "Segment C",
                        "value": 112.2,
                        "percentage": 13.6
                },
                {
                        "category": "Segment D",
                        "value": 64.61,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 221.81,
                        "percentage": 26.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.417378",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Carbon Footprint of Procurement"
        }
    },
}
