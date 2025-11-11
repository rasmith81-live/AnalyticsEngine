"""
Packaging Sustainability Score

A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.
"""

PACKAGING_SUSTAINABILITY_SCORE = {
    "code": "PACKAGING_SUSTAINABILITY_SCORE",
    "name": "Packaging Sustainability Score",
    "description": "A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Sustainability Score to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.147826"},
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
                        81.2,
                        83.6,
                        81.5,
                        85.2,
                        84.5,
                        85.7,
                        82.3,
                        81.4,
                        75.7,
                        79.5,
                        84.3,
                        74.9
                ],
                "unit": "score"
        },
        "current": {
                "value": 74.9,
                "unit": "score",
                "change": -9.4,
                "change_percent": -11.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 81.65,
                "min": 74.9,
                "max": 85.7,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 23.78,
                        "percentage": 31.7
                },
                {
                        "category": "Segment B",
                        "value": 14.41,
                        "percentage": 19.2
                },
                {
                        "category": "Segment C",
                        "value": 7.94,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 4.28,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 24.49,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.380591",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Packaging Sustainability Score"
        }
    },
}
