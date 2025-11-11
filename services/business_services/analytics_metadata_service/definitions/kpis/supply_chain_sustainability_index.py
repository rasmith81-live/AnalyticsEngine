"""
Supply Chain Sustainability Index

A composite metric that evaluates the environmental and social performance of the supply chain operations.
"""

SUPPLY_CHAIN_SUSTAINABILITY_INDEX = {
    "code": "SUPPLY_CHAIN_SUSTAINABILITY_INDEX",
    "name": "Supply Chain Sustainability Index",
    "description": "A composite metric that evaluates the environmental and social performance of the supply chain operations.",
    "formula": "Sustainability Score based on predefined criteria",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Sustainability Index to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.682000"},
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
                        63.0,
                        71.9,
                        68.6,
                        70.4,
                        71.8,
                        63.0,
                        62.4,
                        67.2,
                        71.4,
                        61.9,
                        73.5,
                        72.2
                ],
                "unit": "score"
        },
        "current": {
                "value": 72.2,
                "unit": "score",
                "change": -1.3,
                "change_percent": -1.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.11,
                "min": 61.9,
                "max": 73.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 23.27,
                        "percentage": 32.2
                },
                {
                        "category": "Segment B",
                        "value": 16.64,
                        "percentage": 23.0
                },
                {
                        "category": "Segment C",
                        "value": 11.07,
                        "percentage": 15.3
                },
                {
                        "category": "Segment D",
                        "value": 6.01,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 15.21,
                        "percentage": 21.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.681472",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Sustainability Index"
        }
    },
}
