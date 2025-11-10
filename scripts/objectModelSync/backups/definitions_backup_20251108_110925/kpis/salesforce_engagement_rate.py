"""
Salesforce Engagement Rate KPI

Module: Business Development
"""

from analytics_models import KPI

SALESFORCE_ENGAGEMENT_RATE = KPI(
    name="Salesforce Engagement Rate",
    code="SALESFORCE_ENGAGEMENT_RATE",
    description="The level of active use of the salesforce automation tools by the sales team, reflecting on tool adoption and efficiency.",
    
    # Definition & Context
    kpi_definition="The level of active use of the salesforce automation tools by the sales team, reflecting on tool adoption and efficiency.",
    expected_business_insights="Indicates the adoption of Salesforce within sales processes and can correlate to data-driven decision making.",
    measurement_approach="Tracks the level of interaction and usage of the Salesforce CRM platform by sales representatives.",
    
    # Calculation
    formula="(Number of Active Users on Salesforce / Total Number of Sales Representatives) * 100",
    
    # Analysis
    trend_analysis="An increasing Salesforce Engagement Rate may indicate better adoption of the sales automation tools and improved efficiency in the sales process. A decreasing rate could signal a lack of training or support for the sales team, or a need for updates or improvements to the salesforce automation tools.",
    diagnostic_questions=['Are there specific features or functionalities within the salesforce automation tools that the sales team finds difficult to use or unnecessary?', 'How does the sales team perceive the effectiveness of the salesforce automation tools in helping them manage their sales activities?'],
    actionable_steps={
        "operational": ['Provide regular training and support for the sales team to ensure they are proficient in using the salesforce automation tools.'],
        "strategic": ['Solicit feedback from the sales team on the usability and effectiveness of the tools, and make necessary improvements based on their input.', 'Implement a rewards or recognition system for sales team members who actively and effectively use the salesforce automation tools.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of Salesforce Engagement Rate over time.', 'Pie charts comparing the adoption rates of different salesforce automation tools within the sales team.']
    ],
    risk_warnings=['A low Salesforce Engagement Rate may lead to underutilization of the salesforce automation tools, resulting in inefficiencies and missed opportunities in the sales process.', 'High variability in the Salesforce Engagement Rate may indicate inconsistent adoption and usage of the salesforce automation tools, leading to challenges in standardizing sales processes.'],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM platforms like Salesforce or HubSpot for comprehensive salesforce automation and management.', 'Sales enablement tools such as Highspot or Seismic to enhance the effectiveness of the sales team in using the automation tools.'],
    integration_points=["Integrate the Salesforce Engagement Rate with performance management systems to align individual sales team members' usage with their overall performance.", 'Link the Salesforce Engagement Rate with customer relationship management (CRM) systems to track the impact of tool usage on customer interactions and sales outcomes.'],
    
    # Impact
    change_impact="Improving the Salesforce Engagement Rate can lead to more accurate and comprehensive sales data, which can positively impact sales forecasting and strategic decision-making. Conversely, a declining Salesforce Engagement Rate may result in missed opportunities, decreased productivity, and potential negative impacts on sales performance.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Enablement Platform", "Lead", "Product Adoption", "Product Usage", "Prospect Engagement", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
