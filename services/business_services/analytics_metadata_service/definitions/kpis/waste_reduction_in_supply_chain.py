"""
Waste Reduction in Supply Chain

The percentage reduction of waste generated throughout the supply chain, aligning with ISO 20400
"""

WASTE_REDUCTION_IN_SUPPLY_CHAIN = {
    "code": "WASTE_REDUCTION_IN_SUPPLY_CHAIN",
    "name": "Waste Reduction in Supply Chain",
    "description": "The percentage reduction of waste generated throughout the supply chain, aligning with ISO 20400",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Waste Reduction in Supply Chain to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.808405"},
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
                        181.39,
                        230.79,
                        291.5,
                        230.21,
                        194.8,
                        274.78,
                        246.29,
                        219.88,
                        260.7,
                        263.67,
                        242.06,
                        252.39
                ],
                "unit": "units"
        },
        "current": {
                "value": 252.39,
                "unit": "units",
                "change": 10.33,
                "change_percent": 4.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 240.7,
                "min": 181.39,
                "max": 291.5,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 45.58,
                        "percentage": 18.1
                },
                {
                        "category": "Segment B",
                        "value": 70.0,
                        "percentage": 27.7
                },
                {
                        "category": "Segment C",
                        "value": 47.77,
                        "percentage": 18.9
                },
                {
                        "category": "Segment D",
                        "value": 24.3,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 64.74,
                        "percentage": 25.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.989194",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Waste Reduction in Supply Chain"
        }
    },
}
