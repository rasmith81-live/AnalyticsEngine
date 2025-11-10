"""
Lead Qualification Rate KPI

The percentage of leads that are qualified and accepted as potential opportunities.
"""

from analytics_models import KPI

LEAD_QUALIFICATION_RATE = KPI(
    name="Lead Qualification Rate",
    code="LEAD_QUALIFICATION_RATE",
    category="Sales Operations",
    
    # Core Definition
    description="The percentage of leads that are qualified and accepted as potential opportunities.",
    kpi_definition="The percentage of leads that are qualified and accepted as potential opportunities.",
    expected_business_insights="Highlights the quality of leads and the effectiveness of lead scoring systems.",
    measurement_approach="Measures the percentage of leads that are considered qualified for the sales process.",
    
    # Formula
    formula="(Number of Qualified Leads / Total Number of Leads) * 100",
    calculation_formula="(Number of Qualified Leads / Total Number of Leads) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing lead qualification rate may indicate improved lead generation strategies or better alignment between marketing and sales teams.
    * A decreasing rate could signal issues with lead quality, ineffective qualification criteria, or misalignment between sales and marketing efforts.
    """,
    diagnostic_questions="""
    * Are there specific lead sources or channels that consistently produce higher quality leads?
    * How does our lead qualification rate compare with industry benchmarks or historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Refine lead qualification criteria to ensure only the most promising leads are accepted.
    * Implement lead nurturing strategies to improve the quality of leads before they enter the sales pipeline.
    * Provide ongoing training and support for sales representatives to enhance their lead qualification skills.
    """,
    visualization_suggestions="""
    * Line charts showing lead qualification rates over time to identify trends and seasonality.
    * Pie charts comparing the distribution of qualified and unqualified leads by source or channel.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A high lead qualification rate may lead to a smaller pool of potential opportunities, impacting overall sales performance.
    * An excessively low qualification rate can result in wasted resources and decreased sales productivity.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems like Salesforce or HubSpot for tracking and managing lead qualification processes.
    * Marketing automation platforms to score and prioritize leads based on their engagement and behavior.
    """,
    integration_points="""
    * Integrate lead qualification data with marketing analytics to understand the quality of leads generated from different campaigns and channels.
    * Link lead qualification with sales forecasting to assess the impact of qualified leads on future revenue projections.
    """,
    change_impact_analysis="""
    * Improving lead qualification can lead to higher conversion rates and sales efficiency, but may also require adjustments in marketing strategies and resource allocation.
    * A declining lead qualification rate can negatively impact sales performance and revenue generation, affecting overall business growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Lead Qualification", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
