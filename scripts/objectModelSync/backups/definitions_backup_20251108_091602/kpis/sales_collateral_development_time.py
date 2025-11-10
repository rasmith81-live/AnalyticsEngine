"""
Sales Collateral Development Time KPI

The average time taken to develop new sales collateral or tools for the sales team.
"""

from analytics_models import KPI

SALES_COLLATERAL_DEVELOPMENT_TIME = KPI(
    name="Sales Collateral Development Time",
    code="SALES_COLLATERAL_DEVELOPMENT_TIME",
    category="Sales Enablement",
    
    # Core Definition
    description="The average time taken to develop new sales collateral or tools for the sales team.",
    kpi_definition="The average time taken to develop new sales collateral or tools for the sales team.",
    expected_business_insights="Indicates the efficiency of content creation processes and the agility of the marketing or sales enablement team.",
    measurement_approach="Measures the average time taken to create new sales collateral.",
    
    # Formula
    formula="Average Time to Produce New Sales Material",
    calculation_formula="Average Time to Produce New Sales Material",
    
    # Analysis
    trend_analysis="""
    * Development time may decrease as sales teams become more familiar with the collateral creation process and tools.
    * An increasing development time could indicate a need for more resources or a lack of efficiency in the creation process.
    """,
    diagnostic_questions="""
    * Are there specific types of collateral that consistently take longer to develop?
    * How does the development time for new collateral compare to the impact it has on sales performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in training and tools that can streamline the collateral development process.
    * Regularly gather feedback from the sales team to understand their specific needs for collateral and how it can be improved.
    * Consider outsourcing certain collateral development tasks to specialized agencies or freelancers to speed up the process.
    """,
    visualization_suggestions="""
    * Line charts showing the average development time over different quarters or years to identify long-term trends.
    * Stacked bar charts comparing development time for different types of collateral to pinpoint areas that require more attention.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Extended development time may lead to sales teams using outdated or ineffective collateral, impacting their performance.
    * Rapidly increasing development time could indicate a bottleneck in the creation process that needs to be addressed to avoid delays.
    """,
    tracking_tools="""
    * Project management software like Asana or Trello to track and manage the development of sales collateral.
    * Content creation tools such as Canva or Adobe Creative Cloud to streamline the design and creation process.
    """,
    integration_points="""
    * Integrate development time tracking with CRM systems to understand the impact of new collateral on sales activities and performance.
    * Link collateral development with marketing automation platforms to ensure alignment in messaging and branding.
    """,
    change_impact_analysis="""
    * Reducing development time can lead to more agile and responsive sales teams, potentially improving overall sales performance.
    * However, rushing the development process may compromise the quality and effectiveness of the collateral, impacting its impact on potential customers.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
