"""
Sales Tool Utilization Rate KPI

Module: Business Development
"""

from analytics_models import KPI

SALES_TOOL_UTILIZATION_RATE = KPI(
    name="Sales Tool Utilization Rate",
    code="SALES_TOOL_UTILIZATION_RATE",
    description="The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.",
    
    # Definition & Context
    kpi_definition="The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.",
    expected_business_insights="Indicates how effectively the sales team is adopting and integrating sales tools into their workflows.",
    measurement_approach="Tracks the usage rate of designated sales tools by the sales team.",
    
    # Calculation
    formula="(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
    
    # Analysis
    trend_analysis="An increasing sales tool utilization rate may indicate better training and onboarding of the sales team, leading to improved adoption of new tools. A decreasing rate could signal resistance to change or a lack of perceived value in the tools provided, requiring a reevaluation of the tools' effectiveness.",
    diagnostic_questions=['Are there specific sales tools that are consistently underutilized, and if so, why?', 'How does the sales team perceive the usefulness of the tools provided, and what barriers exist to their full utilization?'],
    actionable_steps={
        "operational": ['Regularly gather feedback from the sales team to understand their needs and challenges with the current sales tools, and make adjustments accordingly.'],
        "strategic": ['Provide ongoing training and support to ensure the sales team is proficient in using the tools and understands their benefits.', 'Consider incentivizing the use of sales tools through recognition or rewards for those who demonstrate effective utilization.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend in sales tool utilization rate over time.', 'Pie charts illustrating the distribution of tool usage across the sales team to identify any disparities.']
    ],
    risk_warnings=['A low sales tool utilization rate may result in missed sales opportunities and inefficiencies in the sales process.', 'Over-reliance on certain tools could lead to a lack of diversity in sales approaches and strategies.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Sales enablement platforms like HubSpot or Salesforce to track and analyze the usage of sales tools.', 'Collaboration tools such as Slack or Microsoft Teams to facilitate communication and knowledge sharing around the use of sales tools.'],
    integration_points=['Integrate sales tool utilization data with performance management systems to assess the impact of tool usage on individual and team performance.', 'Link utilization metrics with customer relationship management (CRM) systems to understand how tool usage correlates with customer interactions and outcomes.'],
    
    # Impact
    change_impact="Improving sales tool utilization can lead to more efficient sales processes and potentially higher conversion rates. However, pushing for increased utilization without addressing underlying issues may result in superficial improvements that do not translate to actual sales performance.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Product Usage", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
