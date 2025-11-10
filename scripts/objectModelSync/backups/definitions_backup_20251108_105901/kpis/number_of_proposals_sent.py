"""
Number of Proposals Sent KPI

The total number of sales proposals or quotes sent to potential customers.
"""

from analytics_models import KPI

NUMBER_OF_PROPOSALS_SENT = KPI(
    name="Number of Proposals Sent",
    code="NUMBER_OF_PROPOSALS_SENT",
    category="Sales Development",
    
    # Core Definition
    description="The total number of sales proposals or quotes sent to potential customers.",
    kpi_definition="The total number of sales proposals or quotes sent to potential customers.",
    expected_business_insights="Indicates the level of sales activity and potential upcoming business.",
    measurement_approach="Measures the number of sales proposals sent to potential or existing customers.",
    
    # Formula
    formula="Total Number of Sales Proposals Issued",
    calculation_formula="Total Number of Sales Proposals Issued",
    
    # Analysis
    trend_analysis="""
    * An increasing number of proposals sent may indicate a proactive sales team or a growing customer base.
    * A decreasing number could signal a lack of lead generation or a shift in sales strategy towards more targeted prospects.
    """,
    diagnostic_questions="""
    * Are there specific sales channels or regions that are driving the majority of proposal requests?
    * How does the conversion rate from proposals to sales compare to historical data or industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement a CRM system to better track and manage proposal requests and follow-ups.
    * Provide sales training on effective proposal writing and presentation techniques.
    * Regularly review and update proposal templates to ensure they align with the latest product or service offerings.
    """,
    visualization_suggestions="""
    * Line charts showing the monthly or quarterly trend in the number of proposals sent.
    * Pie charts to compare the distribution of proposals across different product lines or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A high number of proposals sent without corresponding sales could indicate a problem with the quality of leads or the effectiveness of the sales team.
    * A low number of proposals may lead to missed opportunities and stagnant sales growth.
    """,
    tracking_tools="""
    * Proposal management software like PandaDoc or Qwilr for creating, sending, and tracking proposals.
    * Data analytics tools to identify patterns in proposal requests and optimize sales strategies.
    """,
    integration_points="""
    * Integrate proposal tracking with the CRM system to streamline lead management and follow-up processes.
    * Link proposal data with marketing automation platforms to align sales and marketing efforts for better lead generation.
    """,
    change_impact_analysis="""
    * An increase in the number of proposals sent may lead to higher workload for the sales team and a need for more efficient processes.
    * A decrease in proposals could impact revenue and market share if not addressed with targeted marketing and sales efforts.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
