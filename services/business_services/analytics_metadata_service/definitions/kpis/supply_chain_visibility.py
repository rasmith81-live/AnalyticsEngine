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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.687100"},
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
                        705.46,
                        654.86,
                        620.21,
                        700.85,
                        610.26,
                        652.52,
                        674.67,
                        629.2,
                        600.8,
                        614.98,
                        636.62,
                        731.47
                ],
                "unit": "units"
        },
        "current": {
                "value": 731.47,
                "unit": "units",
                "change": 94.85,
                "change_percent": 14.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 652.66,
                "min": 600.8,
                "max": 731.47,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 142.2,
                        "percentage": 19.4
                },
                {
                        "category": "Segment B",
                        "value": 123.69,
                        "percentage": 16.9
                },
                {
                        "category": "Segment C",
                        "value": 128.36,
                        "percentage": 17.5
                },
                {
                        "category": "Segment D",
                        "value": 58.7,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 278.52,
                        "percentage": 38.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.696096",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Visibility"
        }
    },
}
