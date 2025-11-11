"""
Environmental Impact of Packaging

A measure of the environmental footprint of packaging materials, assessing sustainability practices in the supply chain.
"""

ENVIRONMENTAL_IMPACT_OF_PACKAGING = {
    "code": "ENVIRONMENTAL_IMPACT_OF_PACKAGING",
    "name": "Environmental Impact of Packaging",
    "description": "A measure of the environmental footprint of packaging materials, assessing sustainability practices in the supply chain.",
    "formula": "Total Environmental Impact Score / Total Packaging Units",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Environmental Impact of Packaging to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.945983"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        583.56,
                        638.26,
                        627.04,
                        585.77,
                        667.62,
                        641.25,
                        588.38,
                        705.17,
                        679.98,
                        652.65,
                        684.84,
                        615.05
                ],
                "unit": "units"
        },
        "current": {
                "value": 615.05,
                "unit": "units",
                "change": -69.79,
                "change_percent": -10.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 639.13,
                "min": 583.56,
                "max": 705.17,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 177.38,
                        "percentage": 28.8
                },
                {
                        "category": "Category B",
                        "value": 81.88,
                        "percentage": 13.3
                },
                {
                        "category": "Category C",
                        "value": 97.16,
                        "percentage": 15.8
                },
                {
                        "category": "Category D",
                        "value": 39.64,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 218.99,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.472845",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Environmental Impact of Packaging"
        }
    },
}
