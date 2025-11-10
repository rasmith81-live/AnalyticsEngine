"""
Number of Qualified Leads KPI

The total number of leads that meet certain predefined criteria and are considered likely to become customers.
"""

from analytics_models import KPI

NUMBER_OF_QUALIFIED_LEADS = KPI(
    name="Number of Qualified Leads",
    code="NUMBER_OF_QUALIFIED_LEADS",
    category="Outside Sales",
    
    # Core Definition
    description="The total number of leads that meet certain predefined criteria and are considered likely to become customers.",
    kpi_definition="The total number of leads that meet certain predefined criteria and are considered likely to become customers.",
    expected_business_insights="Offers insight into the effectiveness of lead generation and qualification processes, impacting the efficiency of the sales funnel.",
    measurement_approach="Measures the total number of leads that meet specific qualification criteria.",
    
    # Formula
    formula="Sum of all Qualified Leads",
    calculation_formula="Sum of all Qualified Leads",
    
    # Analysis
    trend_analysis="""
    * An increasing number of qualified leads may indicate improved marketing strategies or increased demand for the product or service.
    * A decreasing number of qualified leads could signal a need for reevaluation of lead generation tactics or a decline in market interest.
    """,
    diagnostic_questions="""
    * What specific criteria are being used to qualify leads, and are they still relevant to the target customer base?
    * How do the conversion rates from qualified leads to customers compare to historical data or industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update the criteria for qualified leads to ensure they align with the changing market and customer needs.
    * Implement lead nurturing strategies to further qualify and engage potential customers before passing them to the sales team.
    * Provide ongoing training and support to the sales team to effectively convert qualified leads into customers.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of qualified leads over time.
    * Pie charts to visualize the distribution of qualified leads by source or criteria.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low number of qualified leads may lead to missed sales opportunities and revenue growth.
    * Overly strict criteria for qualified leads could result in a limited pool of potential customers and hinder business expansion.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage qualified leads throughout the sales process.
    * Marketing automation tools to streamline lead qualification and nurturing processes.
    """,
    integration_points="""
    * Integrate qualified lead data with sales performance metrics to analyze the effectiveness of lead qualification in driving actual sales.
    * Link qualified lead information with customer relationship management systems to ensure a seamless transition from marketing to sales activities.
    """,
    change_impact_analysis="""
    * An increase in the number of qualified leads can positively impact sales revenue and market share.
    * However, a decrease in qualified leads may require adjustments in marketing and sales strategies to maintain business growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lead", "Lead Qualification", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
