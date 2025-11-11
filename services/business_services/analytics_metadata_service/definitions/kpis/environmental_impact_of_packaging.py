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
                        452.16,
                        448.76,
                        491.66,
                        387.03,
                        443.15,
                        441.61,
                        409.28,
                        375.53,
                        444.69,
                        354.52,
                        429.79,
                        474.54
                ],
                "unit": "units"
        },
        "current": {
                "value": 474.54,
                "unit": "units",
                "change": 44.75,
                "change_percent": 10.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 429.39,
                "min": 354.52,
                "max": 491.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 87.47,
                        "percentage": 18.4
                },
                {
                        "category": "Segment B",
                        "value": 99.44,
                        "percentage": 21.0
                },
                {
                        "category": "Segment C",
                        "value": 66.84,
                        "percentage": 14.1
                },
                {
                        "category": "Segment D",
                        "value": 51.59,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 169.2,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.968122",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Environmental Impact of Packaging"
        }
    },
}
