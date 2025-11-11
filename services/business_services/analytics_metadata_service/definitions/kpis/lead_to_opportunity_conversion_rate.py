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
                        67.49,
                        69.75,
                        73.39,
                        67.83,
                        77.03,
                        63.33,
                        61.28,
                        66.93,
                        66.88,
                        77.06,
                        63.55,
                        65.37
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.37,
                "unit": "%",
                "change": 1.82,
                "change_percent": 2.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.32,
                "min": 61.28,
                "max": 77.06,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.89,
                        "percentage": 33.5
                },
                {
                        "category": "Segment B",
                        "value": 9.25,
                        "percentage": 14.2
                },
                {
                        "category": "Segment C",
                        "value": 7.07,
                        "percentage": 10.8
                },
                {
                        "category": "Segment D",
                        "value": 6.14,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 21.02,
                        "percentage": 32.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.137527",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Lead-to-Opportunity Conversion Rate"
        }
    },
}
