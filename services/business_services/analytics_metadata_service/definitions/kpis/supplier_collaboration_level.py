"""
Supplier Collaboration Level

The extent to which the buying organization works with suppliers to achieve mutual benefits.
"""

SUPPLIER_COLLABORATION_LEVEL = {
    "code": "SUPPLIER_COLLABORATION_LEVEL",
    "name": "Supplier Collaboration Level",
    "description": "The extent to which the buying organization works with suppliers to achieve mutual benefits.",
    "formula": "Qualitative Assessment Score based on Predefined Collaboration Criteria",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Collaboration Level to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.621727"},
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
                        48.86,
                        55.61,
                        42.52,
                        42.92,
                        41.41,
                        46.06,
                        37.42,
                        52.22,
                        55.57,
                        49.72,
                        39.76,
                        38.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 38.33,
                "unit": "%",
                "change": -1.43,
                "change_percent": -3.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 45.87,
                "min": 37.42,
                "max": 55.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 7.25,
                        "percentage": 18.9
                },
                {
                        "category": "Segment B",
                        "value": 8.19,
                        "percentage": 21.4
                },
                {
                        "category": "Segment C",
                        "value": 5.38,
                        "percentage": 14.0
                },
                {
                        "category": "Segment D",
                        "value": 2.43,
                        "percentage": 6.3
                },
                {
                        "category": "Other",
                        "value": 15.08,
                        "percentage": 39.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.508318",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Collaboration Level"
        }
    },
}
