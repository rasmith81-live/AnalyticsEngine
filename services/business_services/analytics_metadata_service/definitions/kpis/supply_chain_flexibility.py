"""
Supply Chain Flexibility

The ability of the supply chain to adapt to changes in demand, supply, and market conditions without significant performance degradation.
"""

SUPPLY_CHAIN_FLEXIBILITY = {
    "code": "SUPPLY_CHAIN_FLEXIBILITY",
    "name": "Supply Chain Flexibility",
    "description": "The ability of the supply chain to adapt to changes in demand, supply, and market conditions without significant performance degradation.",
    "formula": "Scored on a predetermined flexibility scale",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Flexibility to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.661357"},
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
                        687.2,
                        804.32,
                        681.91,
                        697.75,
                        789.19,
                        701.03,
                        779.52,
                        732.43,
                        773.07,
                        742.52,
                        732.34,
                        769.25
                ],
                "unit": "units"
        },
        "current": {
                "value": 769.25,
                "unit": "units",
                "change": 36.91,
                "change_percent": 5.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 740.88,
                "min": 681.91,
                "max": 804.32,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 120.44,
                        "percentage": 15.7
                },
                {
                        "category": "Segment B",
                        "value": 173.45,
                        "percentage": 22.5
                },
                {
                        "category": "Segment C",
                        "value": 72.23,
                        "percentage": 9.4
                },
                {
                        "category": "Segment D",
                        "value": 115.05,
                        "percentage": 15.0
                },
                {
                        "category": "Other",
                        "value": 288.08,
                        "percentage": 37.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.620132",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Flexibility"
        }
    },
}
