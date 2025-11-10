"""
Lead Conversion Time KPI

The average time it takes to convert a lead into a sale, reflecting the team’s sales cycle efficiency.
"""

LEAD_CONVERSION_TIME = {
    "code": "LEAD_CONVERSION_TIME",
    "name": "Lead Conversion Time",
    "description": "The average time it takes to convert a lead into a sale, reflecting the team’s sales cycle efficiency.",
    "formula": "Total Time to Convert Leads / Number of Leads Converted",
    "calculation_formula": "Total Time to Convert Leads / Number of Leads Converted",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The average time it takes to convert a lead into a sale, reflecting the team’s sales cycle efficiency.",
    "expected_business_insights": "Highlights the efficiency of the sales process, showing opportunities to shorten the sales cycle.",
    "measurement_approach": "The average time it takes to convert a lead into a customer.",
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
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
}
