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
                        819.84,
                        768.42,
                        758.76,
                        753.98,
                        820.15,
                        832.92,
                        704.02,
                        742.2,
                        724.96,
                        710.82,
                        737.17,
                        831.02
                ],
                "unit": "units"
        },
        "current": {
                "value": 831.02,
                "unit": "units",
                "change": 93.85,
                "change_percent": 12.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 767.02,
                "min": 704.02,
                "max": 832.92,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 127.3,
                        "percentage": 15.3
                },
                {
                        "category": "Category B",
                        "value": 106.9,
                        "percentage": 12.9
                },
                {
                        "category": "Category C",
                        "value": 187.44,
                        "percentage": 22.6
                },
                {
                        "category": "Category D",
                        "value": 89.34,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 320.04,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.903798",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Flexibility"
        }
    },
}
