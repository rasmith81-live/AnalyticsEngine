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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:32.944883"},
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
                        622.85,
                        605.02,
                        679.56,
                        615.96,
                        631.77,
                        565.09,
                        589.11,
                        633.43,
                        626.04,
                        611.73,
                        664.66,
                        622.96
                ],
                "unit": "units"
        },
        "current": {
                "value": 622.96,
                "unit": "units",
                "change": -41.7,
                "change_percent": -6.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 622.35,
                "min": 565.09,
                "max": 679.56,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 207.73,
                        "percentage": 33.3
                },
                {
                        "category": "Segment B",
                        "value": 68.3,
                        "percentage": 11.0
                },
                {
                        "category": "Segment C",
                        "value": 99.72,
                        "percentage": 16.0
                },
                {
                        "category": "Segment D",
                        "value": 60.0,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 187.21,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.964548",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Energy Efficiency of Suppliers"
        }
    },
}
