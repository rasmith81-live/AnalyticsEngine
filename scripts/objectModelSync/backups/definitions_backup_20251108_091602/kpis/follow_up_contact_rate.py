"""
Follow-up Contact Rate KPI

The frequency at which the sales team follows up with leads and prospects.
"""

from analytics_models import KPI

FOLLOW_UP_CONTACT_RATE = KPI(
    name="Follow-up Contact Rate",
    code="FOLLOW_UP_CONTACT_RATE",
    category="Inside Sales",
    
    # Core Definition
    description="The frequency at which the sales team follows up with leads and prospects.",
    kpi_definition="The frequency at which the sales team follows up with leads and prospects.",
    expected_business_insights="Reflects on the thoroughness of the sales process and the potential for improving lead nurturing.",
    measurement_approach="The percentage of leads that received a follow-up contact.",
    
    # Formula
    formula="(Number of Leads Followed Up / Total Number of Leads) * 100",
    calculation_formula="(Number of Leads Followed Up / Total Number of Leads) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing follow-up contact rate may indicate a proactive sales team or a growing number of leads and prospects.
    * A decreasing rate could signal a lack of follow-up processes or a decline in the quality of leads.
    """,
    diagnostic_questions="""
    * Are there specific leads or prospects that are consistently followed up with, and are there others that are often neglected?
    * How does our follow-up contact rate compare with industry benchmarks or with the performance of top-performing sales teams?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a structured follow-up schedule to ensure all leads and prospects are consistently contacted.
    * Utilize customer relationship management (CRM) software to automate and track follow-up activities.
    * Provide regular training and coaching to the sales team on effective follow-up techniques and best practices.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of follow-up contact rates over time.
    * Pie charts comparing follow-up contact rates for different sales representatives or territories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low follow-up contact rate can result in missed sales opportunities and decreased conversion rates.
    * An excessively high follow-up contact rate may lead to customer annoyance or perception of pushiness.
    """,
    tracking_tools="""
    * CRM systems such as Salesforce or HubSpot for tracking and managing follow-up activities.
    * Sales engagement platforms like Outreach or SalesLoft to automate and optimize follow-up processes.
    """,
    integration_points="""
    * Integrate follow-up contact rate data with lead generation systems to identify the most responsive lead sources.
    * Link follow-up contact rate with customer feedback systems to understand the impact of follow-up on customer satisfaction.
    """,
    change_impact_analysis="""
    * Improving the follow-up contact rate can lead to increased sales and revenue, but may also require additional resources and time from the sales team.
    * A declining follow-up contact rate can negatively impact the overall sales performance and the effectiveness of marketing efforts.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
