"""
Supply Chain Carbon Footprint

The total amount of greenhouse gases produced directly or indirectly by supply chain activities, measured in carbon dioxide equivalent.
"""

SUPPLY_CHAIN_CARBON_FOOTPRINT = {
    "code": "SUPPLY_CHAIN_CARBON_FOOTPRINT",
    "name": "Supply Chain Carbon Footprint",
    "description": "The total amount of greenhouse gases produced directly or indirectly by supply chain activities, measured in carbon dioxide equivalent.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Carbon Footprint to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.657347"},
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
                        623.87,
                        577.76,
                        541.79,
                        515.81,
                        531.9,
                        596.73,
                        600.72,
                        547.05,
                        557.08,
                        562.06,
                        540.9,
                        625.57
                ],
                "unit": "units"
        },
        "current": {
                "value": 625.57,
                "unit": "units",
                "change": 84.67,
                "change_percent": 15.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 568.44,
                "min": 515.81,
                "max": 625.57,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 139.67,
                        "percentage": 22.3
                },
                {
                        "category": "Segment B",
                        "value": 103.27,
                        "percentage": 16.5
                },
                {
                        "category": "Segment C",
                        "value": 106.69,
                        "percentage": 17.1
                },
                {
                        "category": "Segment D",
                        "value": 60.28,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 215.66,
                        "percentage": 34.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.610822",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Carbon Footprint"
        }
    },
}
