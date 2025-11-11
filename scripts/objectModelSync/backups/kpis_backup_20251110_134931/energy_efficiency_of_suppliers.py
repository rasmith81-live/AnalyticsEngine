"""
Energy Efficiency of Suppliers

The average level of energy efficiency among suppliers, reflecting adherence to ISO 20400
"""

ENERGY_EFFICIENCY_OF_SUPPLIERS = {
    "code": "ENERGY_EFFICIENCY_OF_SUPPLIERS",
    "name": "Energy Efficiency of Suppliers",
    "description": "The average level of energy efficiency among suppliers, reflecting adherence to ISO 20400",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Energy Efficiency of Suppliers to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:23.470212"},
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
                        770.08,
                        748.76,
                        831.5,
                        830.69,
                        848.72,
                        791.7,
                        793.31,
                        856.06,
                        845.5,
                        753.04,
                        821.88,
                        744.64
                ],
                "unit": "units"
        },
        "current": {
                "value": 744.64,
                "unit": "units",
                "change": -77.24,
                "change_percent": -9.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 802.99,
                "min": 744.64,
                "max": 856.06,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 166.13,
                        "percentage": 22.3
                },
                {
                        "category": "Category B",
                        "value": 119.7,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 123.0,
                        "percentage": 16.5
                },
                {
                        "category": "Category D",
                        "value": 74.34,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 261.47,
                        "percentage": 35.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.470212",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Energy Efficiency of Suppliers"
        }
    },
}
