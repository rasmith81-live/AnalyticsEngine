"""
Partner Retention Rate KPI

The percentage of channel partners that continue their relationship with the company over a given period, indicating partner satisfaction and stability in the channel network.
"""

from analytics_models import KPI

PARTNER_RETENTION_RATE = KPI(
    name="Partner Retention Rate",
    code="PARTNER_RETENTION_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The percentage of channel partners that continue their relationship with the company over a given period, indicating partner satisfaction and stability in the channel network.",
    kpi_definition="The percentage of channel partners that continue their relationship with the company over a given period, indicating partner satisfaction and stability in the channel network.",
    expected_business_insights="Highlights the effectiveness of partner engagement and support strategies in maintaining a stable partner base.",
    measurement_approach="Measures the percentage of channel partners who remain active over a given period.",
    
    # Formula
    formula="(Number of Partners at End of Period - Number of New Partners Acquired) / Number of Partners at Start of Period * 100",
    calculation_formula="(Number of Partners at End of Period - Number of New Partners Acquired) / Number of Partners at Start of Period * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing partner retention rate may indicate improved partner support and satisfaction with the company\'s products or services.
    * A decreasing rate could signal issues with communication, product quality, or changes in the competitive landscape.
    """,
    diagnostic_questions="""
    * What specific factors contribute to our channel partners\' decision to continue or discontinue their relationship with us?
    * How does our partner retention rate compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from channel partners to understand their needs and concerns, and take action based on their input.
    * Provide training and resources to help partners effectively sell and support the company\'s products or services.
    * Develop and maintain strong relationships with channel partners to build trust and loyalty.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of partner retention rate over time.
    * Pie charts to compare the distribution of retained and lost partners by region or product line.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining partner retention rate can lead to a loss of market share and revenue as partners seek out other companies to work with.
    * High partner turnover can indicate issues with the company\'s channel program, potentially leading to negative word-of-mouth and reputation damage.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track partner interactions and manage partner relationships effectively.
    * Partner portal platforms to provide partners with easy access to resources, training, and support.
    """,
    integration_points="""
    * Integrate partner retention rate data with sales performance metrics to understand the impact of partner stability on overall sales results.
    * Link partner retention rate with customer satisfaction data to identify potential correlations between partner stability and customer experience.
    """,
    change_impact_analysis="""
    * Improving partner retention can lead to increased sales and market share, but may also require investment in partner support and resources.
    * A declining partner retention rate can negatively impact customer satisfaction and brand reputation, affecting long-term business performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
