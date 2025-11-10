"""
Average Lead Score KPI

Module: Business Development
"""

AVERAGE_LEAD_SCORE = {
    "code": "AVERAGE_LEAD_SCORE",
    "name": "Average Lead Score",
    "description": "The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
    "formula": "Sum of All Lead Scores / Total Number of Leads",
    "category": "Business Development",
    "is_active": True,
    "kpi_definition": "The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
    "expected_business_insights": "Helps prioritize sales efforts on high-quality leads likely to convert.",
    "measurement_approach": "Measures the average score assigned to leads based on their perceived quality or sales-readiness.",
    "trend_analysis": "An increasing average lead score may indicate that the business development team is effectively targeting higher quality leads. A decreasing average lead score could signal a decline in lead quality or a need for reassessment of lead scoring criteria.",
    "diagnostic_questions": ["What criteria are used to score leads, and are they still relevant and effective?", "How does the average lead score compare to conversion rates and actual sales, and are there discrepancies that need to be addressed?"],
    "actionable_steps": {"operational": ["Regularly review and update lead scoring criteria based on feedback from the sales team and actual conversion data."], "strategic": ["Provide additional training and resources to the business development team to improve lead qualification and nurturing processes.", "Implement lead scoring automation tools to ensure consistency and accuracy in the scoring process."]},
    "risk_warnings": ["A consistently low average lead score may lead to wasted resources and efforts on pursuing low-quality leads.", "An excessively high average lead score may indicate a narrow focus that misses potential opportunities in other segments."],
    "suggested_tracking_tools": ["Customer Relationship Management (CRM) software with lead scoring capabilities to track and manage lead quality.", "Marketing automation platforms to streamline lead nurturing and scoring processes."],
    "integration_points": ["Integrate lead scoring data with sales performance metrics to identify correlations and optimize lead quality.", "Link lead scoring with marketing campaign data to assess the effectiveness of different lead generation channels."],
    "change_impact": "Improving the average lead score can lead to more efficient use of sales resources and higher conversion rates. However, overly stringent lead scoring criteria may limit the pool of potential leads and impact overall sales volume.",
    "metadata_": {"modules": ["BUS_DEV", "SALES_DEVELOPMENT"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Lead", "Lead Qualification", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["BUS_DEV", "SALES_DEVELOPMENT"],
    "module_code": "BUS_DEV",
}
