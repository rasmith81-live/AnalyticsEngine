"""
Lead-to-Opportunity Conversion Rate

The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.
"""

LEAD_TO_OPPORTUNITY_CONVERSION_RATE = {
    "code": "LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
    "name": "Lead-to-Opportunity Conversion Rate",
    "description": "The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.",
    "formula": "(Number of Leads Converted to Opportunities / Total Number of Leads) * 100",
    "calculation_formula": "(Number of Leads Converted to Opportunities / Total Number of Leads) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead-to-Opportunity Conversion Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.019008"},
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
                        54.48,
                        69.7,
                        62.99,
                        70.96,
                        61.01,
                        60.18,
                        53.84,
                        68.25,
                        53.97,
                        66.78,
                        65.88,
                        59.36
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.36,
                "unit": "%",
                "change": -6.52,
                "change_percent": -9.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 62.28,
                "min": 53.84,
                "max": 70.96,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.95,
                        "percentage": 20.1
                },
                {
                        "category": "Category B",
                        "value": 14.39,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 5.89,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 2.85,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 24.28,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.602219",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead-to-Opportunity Conversion Rate"
        }
    },
}
