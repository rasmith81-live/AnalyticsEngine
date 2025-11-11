"""
Lead Conversion Time

The average time it takes to convert a lead into a sale, reflecting the team’s sales cycle efficiency.
"""

LEAD_CONVERSION_TIME = {
    "code": "LEAD_CONVERSION_TIME",
    "name": "Lead Conversion Time",
    "description": "The average time it takes to convert a lead into a sale, reflecting the team\u2019s sales cycle efficiency.",
    "formula": "Total Time to Convert Leads / Number of Leads Converted",
    "calculation_formula": "Total Time to Convert Leads / Number of Leads Converted",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Conversion Time to be added.",
    "trend_analysis": """

    * An increasing lead conversion time may indicate inefficiencies in the sales process or a lack of qualified leads.
    * A decreasing lead conversion time can signal improved lead qualification, better sales tactics, or more effective follow-up.
    
    """,
    "diagnostic_questions": """

    * Are there specific stages in the sales cycle where leads tend to get stuck or delayed?
    * How does our lead conversion time compare with industry benchmarks or with our competitors?
    
    """,
    "actionable_tips": """

    * Implement lead scoring to prioritize high-quality leads and focus efforts on those most likely to convert.
    * Provide ongoing training and support for sales representatives to improve their closing techniques and objection handling.
    * Utilize customer relationship management (CRM) software to track lead interactions and identify areas for improvement in the sales process.
    
    """,
    "visualization_suggestions": """

    * Line charts showing lead conversion time over different time periods to identify trends and seasonality.
    * Funnel charts to visualize the drop-off points in the sales process and areas for improvement.
    
    """,
    "risk_warnings": """

    * Long lead conversion times can result in missed sales opportunities and revenue loss.
    * Rapidly decreasing lead conversion times may indicate a focus on quantity over quality, leading to potential customer dissatisfaction.
    
    """,
    "tracking_tools": """

    * Utilize sales analytics tools like Salesforce or HubSpot to track and analyze lead conversion times.
    * Implement marketing automation platforms to ensure leads are properly nurtured and engaged throughout the sales process.
    
    """,
    "integration_points": """

    * Integrate lead conversion time data with marketing campaign performance to understand the quality of leads generated from different sources.
    * Link lead conversion time with customer feedback systems to identify areas for improvement in the sales process based on customer experiences.
    
    """,
    "change_impact_analysis": """

    * Improving lead conversion time can increase sales revenue and customer acquisition, but may require additional resources for lead nurturing and follow-up.
    * Conversely, a prolonged lead conversion time can impact cash flow and overall sales team morale, affecting the organization's bottom line and employee retention.
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.580931"},
    "required_objects": [],
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
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
                        249,
                        256,
                        250,
                        244,
                        242,
                        247,
                        277,
                        266,
                        239,
                        234,
                        256,
                        263
                ],
                "unit": "count"
        },
        "current": {
                "value": 263,
                "unit": "count",
                "change": 7,
                "change_percent": 2.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 251.92,
                "min": 234,
                "max": 277,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 59.42,
                        "percentage": 22.6
                },
                {
                        "category": "Category B",
                        "value": 39.3,
                        "percentage": 14.9
                },
                {
                        "category": "Category C",
                        "value": 35.13,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 21.82,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 107.33,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.580931",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Lead Conversion Time"
        }
    },
}
