"""
Average Sales Pitch Length KPI

Module: Business Development
"""

AVERAGE_SALES_PITCH_LENGTH = {
    "code": "AVERAGE_SALES_PITCH_LENGTH",
    "name": "Average Sales Pitch Length",
    "description": "The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    "formula": "Total Duration of All Sales Pitches / Number of Sales Pitches",
    "category": "Business Development",
    "is_active": True,
    "kpi_definition": "The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    "expected_business_insights": "Provides insights into the efficiency of the sales process and potential customer engagement levels.",
    "measurement_approach": "Considers the average duration of sales presentations or meetings.",
    "trend_analysis": "Increasing average sales pitch length may indicate a more detailed and comprehensive approach to presenting products or services. A decreasing average pitch length could suggest a more concise and efficient communication style, but it may also lead to overlooking important details.",
    "diagnostic_questions": ["Are there specific products or services that require longer pitches to effectively convey their value?", "How does the average pitch length correlate with the success rate of closing deals?"],
    "actionable_steps": {"operational": ["Provide sales training to ensure that pitches are informative but also engaging and concise."], "strategic": ["Utilize technology such as presentation software to create visually appealing and impactful pitches without unnecessary length.", "Regularly review and refine the pitch content to focus on key value propositions and address customer pain points efficiently."]},
    "risk_warnings": ["Excessively long pitches may lead to customer disengagement and loss of interest.", "Overly short pitches might result in insufficient information being conveyed, leading to missed sales opportunities."],
    "suggested_tracking_tools": ["Customer relationship management (CRM) software to track the length of pitches and their outcomes.", "Video recording tools to analyze and improve the delivery and content of sales pitches."],
    "integration_points": ["Integrate pitch length data with customer feedback and conversion rates to understand the impact of pitch duration on sales performance.", "Link pitch length analysis with sales training programs to tailor coaching and development efforts based on the findings."],
    "change_impact": "Shorter, more effective pitches can lead to higher sales conversion rates and improved customer satisfaction. However, a significant reduction in pitch length may also raise concerns about the depth of product knowledge and understanding conveyed to customers.",
    "metadata_": {"modules": ["BUS_DEV"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Prospect Engagement", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["BUS_DEV"],
    "module_code": "BUS_DEV",
}
