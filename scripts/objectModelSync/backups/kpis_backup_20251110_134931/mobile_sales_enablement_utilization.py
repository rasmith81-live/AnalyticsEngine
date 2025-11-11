"""
Mobile Sales Enablement Utilization

The percentage of the sales team that uses mobile tools and applications to enable sales activities.
"""

MOBILE_SALES_ENABLEMENT_UTILIZATION = {
    "code": "MOBILE_SALES_ENABLEMENT_UTILIZATION",
    "name": "Mobile Sales Enablement Utilization",
    "description": "The percentage of the sales team that uses mobile tools and applications to enable sales activities.",
    "formula": "(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
    "calculation_formula": "(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Mobile Sales Enablement Utilization to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.665391"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        156.61,
                        256.16,
                        252.35,
                        196.59,
                        162.04,
                        255.38,
                        237.05,
                        263.34,
                        274.15,
                        204.82,
                        232.56,
                        245.88
                ],
                "unit": "units"
        },
        "current": {
                "value": 245.88,
                "unit": "units",
                "change": 13.32,
                "change_percent": 5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 228.08,
                "min": 156.61,
                "max": 274.15,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 38.66,
                        "percentage": 15.7
                },
                {
                        "category": "Category B",
                        "value": 32.37,
                        "percentage": 13.2
                },
                {
                        "category": "Category C",
                        "value": 34.66,
                        "percentage": 14.1
                },
                {
                        "category": "Category D",
                        "value": 26.31,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 113.88,
                        "percentage": 46.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.665391",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Mobile Sales Enablement Utilization"
        }
    },
}
