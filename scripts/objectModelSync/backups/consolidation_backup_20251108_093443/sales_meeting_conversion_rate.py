"""
Sales Meeting Conversion Rate KPI

The percentage of sales meetings that result in a further action or advance in the sales process.
"""

from analytics_models import KPI

SALES_MEETING_CONVERSION_RATE = KPI(
    name="Sales Meeting Conversion Rate",
    code="SALES_MEETING_CONVERSION_RATE",
    category="Key Account Management",
    
    # Core Definition
    description="The percentage of sales meetings that result in a further action or advance in the sales process.",
    kpi_definition="The percentage of sales meetings that result in a further action or advance in the sales process.",
    expected_business_insights="Provides insight into the effectiveness of sales presentations and the quality of prospect interactions.",
    measurement_approach="Measures the percentage of sales meetings that result in a sale.",
    
    # Formula
    formula="(Number of Sales / Total Number of Sales Meetings) * 100",
    calculation_formula="(Number of Sales / Total Number of Sales Meetings) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales meeting conversion rate may indicate improved sales strategies or better-qualified leads.
    * A decreasing rate could signal issues with the sales process, product offering, or market demand.
    """,
    diagnostic_questions="""
    * What are the common characteristics of sales meetings that result in further action?
    * Are there specific stages in the sales process where the conversion rate tends to drop?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and resources to improve the effectiveness of sales meetings.
    * Regularly review and update the sales process to address any identified bottlenecks or inefficiencies.
    * Implement lead scoring to prioritize high-quality leads for sales meetings.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales meeting conversion rates over time.
    * Pie charts to compare conversion rates across different sales representatives or territories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low conversion rate may lead to missed revenue targets and decreased morale among the sales team.
    * A sudden drop in conversion rate could indicate external factors affecting the market or customer behavior.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze the outcomes of sales meetings.
    * Sales enablement platforms to provide sales representatives with the necessary tools and content for effective meetings.
    """,
    integration_points="""
    * Integrate sales meeting data with customer feedback and satisfaction metrics to gain a comprehensive view of the sales process.
    * Link sales meeting outcomes with inventory and production systems to ensure seamless fulfillment of orders resulting from successful meetings.
    """,
    change_impact_analysis="""
    * Improving the sales meeting conversion rate can lead to increased revenue and customer acquisition.
    * However, changes in the conversion rate may also impact sales forecasting and resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "KEY_ACCOUNT_MANAGEMENT", "SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07"
        "replaces": ["SALES_MEETING_CONVERSION_RATIO"],
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Lead", "Lost Sale", "Meeting", "Opportunity", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
