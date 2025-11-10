"""
Co-Marketing Contribution KPI

The contribution of channel partners to joint marketing efforts and the effectiveness of those efforts in generating leads and sales.
"""

from analytics_models import KPI

CO_MARKETING_CONTRIBUTION = KPI(
    name="Co-Marketing Contribution",
    code="CO_MARKETING_CONTRIBUTION",
    category="Channel Sales",
    
    # Core Definition
    description="The contribution of channel partners to joint marketing efforts and the effectiveness of those efforts in generating leads and sales.",
    kpi_definition="The contribution of channel partners to joint marketing efforts and the effectiveness of those efforts in generating leads and sales.",
    expected_business_insights="Shows the return on investment of co-marketing initiatives and informs future marketing collaborations.",
    measurement_approach="Evaluates the effectiveness and contributions of joint marketing efforts with channel partners.",
    
    # Formula
    formula="Total Revenue from Co-Marketing Campaigns / Total Co-Marketing Investment",
    calculation_formula="Total Revenue from Co-Marketing Campaigns / Total Co-Marketing Investment",
    
    # Analysis
    trend_analysis="""
    * An increasing co-marketing contribution may indicate stronger collaboration with channel partners and more effective joint marketing efforts.
    * A decreasing co-marketing contribution could signal a lack of engagement from channel partners or ineffective marketing strategies.
    """,
    diagnostic_questions="""
    * Are there specific marketing activities that have shown better results in generating leads and sales?
    * How do our co-marketing efforts compare with industry benchmarks or with those of our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide training and resources to channel partners to improve their marketing capabilities.
    * Regularly review and optimize joint marketing strategies to ensure they are aligned with the needs and preferences of the target audience.
    * Establish clear goals and expectations for co-marketing efforts to ensure accountability and effectiveness.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of leads and sales generated from co-marketing activities over time.
    * Pie charts illustrating the distribution of leads and sales by channel partner or marketing activity.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low co-marketing contribution may result in missed opportunities for lead generation and sales growth.
    * Over-reliance on a few channel partners for co-marketing efforts can create vulnerability if those partners disengage or underperform.
    """,
    tracking_tools="""
    * Marketing automation platforms to streamline joint marketing campaigns and track their performance.
    * Collaboration tools for effective communication and resource sharing with channel partners.
    """,
    integration_points="""
    * Integrate co-marketing contribution data with CRM systems to track the impact on lead conversion and sales pipeline.
    * Link co-marketing efforts with sales performance metrics to assess the direct influence on revenue generation.
    """,
    change_impact_analysis="""
    * Improving co-marketing contribution can lead to increased brand visibility and market share, but may also require additional investment in resources and support for channel partners.
    * A decrease in co-marketing contribution may negatively impact overall sales performance and the strength of the channel partner relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Co-Marketing Campaign", "Customer", "Lead", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
