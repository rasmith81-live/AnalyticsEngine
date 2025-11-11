"""
Supply Chain Redundancy Level

The level of redundancy built into the supply chain to ensure continuity in the event of a disruption or security breach.
"""

SUPPLY_CHAIN_REDUNDANCY_LEVEL = {
    "code": "SUPPLY_CHAIN_REDUNDANCY_LEVEL",
    "name": "Supply Chain Redundancy Level",
    "description": "The level of redundancy built into the supply chain to ensure continuity in the event of a disruption or security breach.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Redundancy Level to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.667199"},
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
                        610.37,
                        604.05,
                        540.99,
                        549.36,
                        591.74,
                        541.85,
                        602.87,
                        640.05,
                        647.98,
                        518.62,
                        601.44,
                        589.36
                ],
                "unit": "units"
        },
        "current": {
                "value": 589.36,
                "unit": "units",
                "change": -12.08,
                "change_percent": -2.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 586.56,
                "min": 518.62,
                "max": 647.98,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 181.99,
                        "percentage": 30.9
                },
                {
                        "category": "Segment B",
                        "value": 85.38,
                        "percentage": 14.5
                },
                {
                        "category": "Segment C",
                        "value": 50.2,
                        "percentage": 8.5
                },
                {
                        "category": "Segment D",
                        "value": 35.24,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 236.55,
                        "percentage": 40.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.633447",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Redundancy Level"
        }
    },
}
