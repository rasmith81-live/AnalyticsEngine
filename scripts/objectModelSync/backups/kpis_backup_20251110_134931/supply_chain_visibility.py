"""
Supply Chain Visibility

The degree to which stakeholders can access real-time data and track products throughout the supply chain, improving decision-making and responsiveness.
"""

SUPPLY_CHAIN_VISIBILITY = {
    "code": "SUPPLY_CHAIN_VISIBILITY",
    "name": "Supply Chain Visibility",
    "description": "The degree to which stakeholders can access real-time data and track products throughout the supply chain, improving decision-making and responsiveness.",
    "formula": "Visibility Score based on traceability and transparency criteria",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Visibility to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.954043"},
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
                        801.84,
                        939.6,
                        883.46,
                        794.54,
                        922.02,
                        887.04,
                        876.32,
                        874.33,
                        896.05,
                        796.49,
                        881.06,
                        830.9
                ],
                "unit": "units"
        },
        "current": {
                "value": 830.9,
                "unit": "units",
                "change": -50.16,
                "change_percent": -5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 865.3,
                "min": 794.54,
                "max": 939.6,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 179.92,
                        "percentage": 21.7
                },
                {
                        "category": "Category B",
                        "value": 195.23,
                        "percentage": 23.5
                },
                {
                        "category": "Category C",
                        "value": 156.75,
                        "percentage": 18.9
                },
                {
                        "category": "Category D",
                        "value": 71.8,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 227.2,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.954043",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Visibility"
        }
    },
}
