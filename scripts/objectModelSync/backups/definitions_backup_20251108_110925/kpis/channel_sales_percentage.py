"""
Channel Sales Percentage KPI

The percentage of total sales that come through various distribution channels (e.g., online, retail, direct).
"""

from analytics_models import KPI

CHANNEL_SALES_PERCENTAGE = KPI(
    name="Channel Sales Percentage",
    code="CHANNEL_SALES_PERCENTAGE",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of total sales that come through various distribution channels (e.g., online, retail, direct).",
    kpi_definition="The percentage of total sales that come through various distribution channels (e.g., online, retail, direct).",
    expected_business_insights="Identifies which channels are most effective or need improvement and guides resource allocation.",
    measurement_approach="Represents the percentage of total sales generated through each sales channel.",
    
    # Formula
    formula="(Total Sales per Channel / Total Sales) * 100",
    calculation_formula="(Total Sales per Channel / Total Sales) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing channel sales percentage may indicate successful expansion into new distribution channels or increased online sales.
    * Decreasing percentage could signal a shift in customer preferences towards other sales channels or a decline in retail sales.
    """,
    diagnostic_questions="""
    * Which distribution channels are driving the majority of our sales?
    * Are there specific products that perform better in certain channels?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in marketing and promotions for underperforming channels to drive sales.
    * Optimize inventory allocation based on channel performance to meet demand effectively.
    * Explore partnerships or collaborations to expand into new sales channels.
    """,
    visualization_suggestions="""
    * Stacked bar charts comparing sales percentage by different channels over time.
    * Line graphs showing the trend of each channel\'s sales percentage over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Relying too heavily on a single channel may expose the business to risks if that channel experiences issues.
    * Ignoring underperforming channels may lead to missed opportunities for sales growth.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track sales by channel and customer preferences.
    * Business intelligence tools to analyze sales data and identify channel performance trends.
    """,
    integration_points="""
    * Integrate sales channel data with inventory management systems to ensure adequate stock levels for each channel.
    * Link channel sales data with marketing platforms to align promotional efforts with channel performance.
    """,
    change_impact_analysis="""
    * Increasing channel sales percentage may lead to higher overall sales revenue but could also require additional resources for managing multiple channels.
    * Decreasing percentage in a specific channel may impact relationships with retail partners or online platforms.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
