"""
Rate of Follow-Up Contact KPI

The frequency at which sales representatives follow up with leads.
"""

from analytics_models import KPI

RATE_OF_FOLLOW_UP_CONTACT = KPI(
    name="Rate of Follow-Up Contact",
    code="RATE_OF_FOLLOW_UP_CONTACT",
    category="Sales Operations",
    
    # Core Definition
    description="The frequency at which sales representatives follow up with leads.",
    kpi_definition="The frequency at which sales representatives follow up with leads.",
    expected_business_insights="Indicates the level of customer service and persistence in the sales process.",
    measurement_approach="Measures the frequency of follow-up contacts with leads or customers.",
    
    # Formula
    formula="Total Number of Follow-Up Contacts / Total Number of Leads or Customers",
    calculation_formula="Total Number of Follow-Up Contacts / Total Number of Leads or Customers",
    
    # Analysis
    trend_analysis="""
    * An increasing rate of follow-up contact may indicate a proactive sales team or a higher volume of leads.
    * A decreasing rate could signal sales team burnout, lack of lead generation, or ineffective follow-up strategies.
    """,
    diagnostic_questions="""
    * Are there specific leads or lead sources that are being consistently followed up with?
    * How does our follow-up contact rate compare with industry benchmarks or with different sales representatives?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a lead scoring system to prioritize follow-up efforts on the most promising leads.
    * Provide sales representatives with training on effective follow-up techniques and time management.
    * Utilize customer relationship management (CRM) software to automate and track follow-up activities.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of follow-up contact rate over time.
    * Pie charts comparing follow-up contact rates between different sales representatives or lead sources.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low follow-up contact rate can result in missed sales opportunities and decreased conversion rates.
    * An excessively high follow-up contact rate may lead to customer annoyance or disengagement.
    """,
    tracking_tools="""
    * CRM systems such as Salesforce or HubSpot for tracking and managing follow-up activities.
    * Sales engagement platforms like Outreach or SalesLoft for automating and optimizing follow-up processes.
    """,
    integration_points="""
    * Integrate follow-up contact data with lead generation systems to understand the quality of leads being followed up with.
    * Link follow-up contact metrics with sales performance evaluations to assess the impact on overall sales effectiveness.
    """,
    change_impact_analysis="""
    * Improving the follow-up contact rate can lead to increased sales conversion and revenue generation.
    * However, excessive follow-up efforts without proper targeting can strain customer relationships and harm brand reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
