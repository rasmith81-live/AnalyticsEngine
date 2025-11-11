"""
Lead Nurturing Success Rate

The percentage of leads that become opportunities as a result of lead nurturing efforts.
"""

LEAD_NURTURING_SUCCESS_RATE = {
    "code": "LEAD_NURTURING_SUCCESS_RATE",
    "name": "Lead Nurturing Success Rate",
    "description": "The percentage of leads that become opportunities as a result of lead nurturing efforts.",
    "formula": "(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
    "calculation_formula": "(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Nurturing Success Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.583155"},
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
                        32.76,
                        34.73,
                        49.54,
                        37.52,
                        50.04,
                        34.44,
                        48.68,
                        49.13,
                        43.01,
                        45.61,
                        36.83,
                        39.41
                ],
                "unit": "%"
        },
        "current": {
                "value": 39.41,
                "unit": "%",
                "change": 2.58,
                "change_percent": 7.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 41.81,
                "min": 32.76,
                "max": 50.04,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.44,
                        "percentage": 26.5
                },
                {
                        "category": "Category B",
                        "value": 4.97,
                        "percentage": 12.6
                },
                {
                        "category": "Category C",
                        "value": 7.76,
                        "percentage": 19.7
                },
                {
                        "category": "Category D",
                        "value": 2.92,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 13.32,
                        "percentage": 33.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.583155",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead Nurturing Success Rate"
        }
    },
}
