"""
Outbound Call Effectiveness KPI

The effectiveness of outbound sales calls measured by metrics such as conversion rate and average call duration.
"""

OUTBOUND_CALL_EFFECTIVENESS = {
    "code": "OUTBOUND_CALL_EFFECTIVENESS",
    "name": "Outbound Call Effectiveness",
    "description": "The effectiveness of outbound sales calls measured by metrics such as conversion rate and average call duration.",
    "formula": "Total Positive Outcomes from Calls / Total Number of Calls Made",
    "calculation_formula": "Total Positive Outcomes from Calls / Total Number of Calls Made",
    "category": "Sales Strategy",
    "is_active": True,
    "kpi_definition": "The effectiveness of outbound sales calls measured by metrics such as conversion rate and average call duration.",
    "expected_business_insights": "Provides insights into the productivity and success rate of outbound calling efforts.",
    "measurement_approach": "Measures results of outbound calls such as conversion rate, lead generation, or appointment setting.",
    "trend_analysis": """
    * An increasing outbound call conversion rate may indicate improved sales pitch effectiveness or better lead quality.
    * A decreasing average call duration could suggest more efficient communication or a decline in customer engagement.
    """,
    "diagnostic_questions": """
    * Are there specific customer segments that respond better to outbound calls?
    * How does our outbound call effectiveness compare with industry benchmarks or competitor performance?
    """,
    "actionable_tips": """
    * Provide targeted sales training to improve call quality and conversion rates.
    * Implement customer relationship management (CRM) systems to track and analyze call outcomes.
    * Regularly review and update call scripts to ensure relevance and effectiveness.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of conversion rates and call durations over time.
    * Pie charts to compare conversion rates across different sales representatives or teams.
    """,
    "risk_warnings": """
    * Low conversion rates may lead to wasted resources and demotivation among sales teams.
    * Long average call durations can indicate inefficiencies in the sales process or poor lead qualification.
    """,
    "tracking_tools": """
    * Call tracking and analytics software like CallRail or CallTrackingMetrics.
    * CRM systems with built-in call management features such as Salesforce or HubSpot.
    """,
    "integration_points": """
    * Integrate outbound call data with sales performance metrics to assess overall sales effectiveness.
    * Link call outcomes with customer data to personalize future outreach and improve conversion rates.
    """,
    "change_impact_analysis": """
    * Improving outbound call effectiveness can lead to increased sales revenue and customer acquisition.
    * However, overly aggressive outbound calling may negatively impact brand reputation and customer satisfaction.
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Appointment", "Call", "Deal", "Lead", "Lead Qualification", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
}
