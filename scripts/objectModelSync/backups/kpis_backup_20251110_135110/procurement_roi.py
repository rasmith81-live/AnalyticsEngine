"""
Procurement ROI

The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.
"""

PROCUREMENT_ROI = {
    "code": "PROCUREMENT_ROI",
    "name": "Procurement ROI",
    "description": "The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement ROI to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Return"], "last_validated": "2025-11-10T13:49:33.258592"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        156.13,
                        141.68,
                        171.14,
                        138.42,
                        168.53,
                        191.18,
                        143.86,
                        105.21,
                        137.75,
                        180.5,
                        167.22,
                        103.79
                ],
                "unit": "units"
        },
        "current": {
                "value": 103.79,
                "unit": "units",
                "change": -63.43,
                "change_percent": -37.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 150.45,
                "min": 103.79,
                "max": 191.18,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.34,
                        "percentage": 18.6
                },
                {
                        "category": "Category B",
                        "value": 17.32,
                        "percentage": 16.7
                },
                {
                        "category": "Category C",
                        "value": 22.37,
                        "percentage": 21.6
                },
                {
                        "category": "Category D",
                        "value": 10.79,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 33.97,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.958956",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Procurement ROI"
        }
    },
}
