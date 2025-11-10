"""
Sales Qualified Lead (SQL) Conversion Rate KPI

The percentage of sales qualified leads that convert into opportunities or sales.
"""

from analytics_models import KPI

SALES_QUALIFIED_LEAD_SQL_CONVERSION_RATE = KPI(
    name="Sales Qualified Lead (SQL) Conversion Rate",
    code="SALES_QUALIFIED_LEAD_SQL_CONVERSION_RATE",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of sales qualified leads that convert into opportunities or sales.",
    kpi_definition="The percentage of sales qualified leads that convert into opportunities or sales.",
    expected_business_insights="Helps in understanding the effectiveness of the lead qualification process and sales follow-up strategies, indicating whether the sales funnel is healthy and efficient.",
    measurement_approach="Measures the percentage of SQLs that turn into confirmed sales or opportunities, indicating how well leads are qualified and followed up on by the sales team.",
    
    # Formula
    formula="(Number of SQLs that Convert to Sales or Opportunities / Total Number of SQLs) * 100",
    calculation_formula="(Number of SQLs that Convert to Sales or Opportunities / Total Number of SQLs) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing SQL conversion rate may indicate improved lead qualification processes or a higher demand for the product or service.
    * A decreasing rate could signal issues with lead quality, sales follow-up, or changes in market conditions.
    """,
    diagnostic_questions="""
    * Are there specific criteria used to qualify leads as sales qualified? Are these criteria still relevant and effective?
    * What is the follow-up process for sales qualified leads? Are there any bottlenecks or gaps in the process?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update the criteria for sales qualified leads to ensure they align with the ideal customer profile and current market conditions.
    * Provide ongoing training and support for sales representatives to improve their ability to convert sales qualified leads into opportunities or sales.
    * Implement lead nurturing strategies to maintain engagement with sales qualified leads that are not yet ready to make a purchase.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the conversion rates at each stage of the sales process.
    * Line graphs to track the trend of SQL conversion rates over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low SQL conversion rate can lead to wasted resources and decreased sales effectiveness.
    * A high SQL conversion rate without corresponding sales growth may indicate issues with lead quality or sales tactics.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage sales qualified leads and their interactions with the sales team.
    * Sales enablement platforms to provide sales representatives with the tools and content they need to effectively engage and convert leads.
    """,
    integration_points="""
    * Integrate the SQL conversion rate with marketing automation platforms to align lead generation efforts with the sales qualification process.
    * Connect the SQL conversion rate with revenue and pipeline metrics to understand the impact of lead quality on overall sales performance.
    """,
    change_impact_analysis="""
    * Improving the SQL conversion rate can lead to more efficient use of sales resources and increased revenue generation.
    * However, a significant increase in the SQL conversion rate may require adjustments in sales capacity and resources to handle the higher volume of opportunities or sales.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
