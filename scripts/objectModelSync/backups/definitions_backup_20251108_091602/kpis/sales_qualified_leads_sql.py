"""
Sales Qualified Leads (SQL) KPI

Module: Business Development
"""

from analytics_models import KPI

SALES_QUALIFIED_LEADS_SQL = KPI(
    name="Sales Qualified Leads (SQL)",
    code="SALES_QUALIFIED_LEADS_SQL",
    description="The number of leads that have been vetted by both marketing and sales teams and are deemed ready for the next step in the sales process.",
    
    # Definition & Context
    kpi_definition="The number of leads that have been vetted by both marketing and sales teams and are deemed ready for the next step in the sales process.",
    expected_business_insights="Assesses the effectiveness of lead qualification processes and the readiness of leads for sales engagement.",
    measurement_approach="Measures the number of leads deemed ready for direct sales follow-up after meeting specific qualifying criteria.",
    
    # Calculation
    formula="Number of Leads Meeting SQL Criteria",
    
    # Analysis
    trend_analysis="An increasing number of SQLs may indicate more effective lead generation and marketing efforts. A decreasing number of SQLs could signal issues with lead quality or alignment between marketing and sales teams.",
    diagnostic_questions=['Are there specific criteria used to qualify leads as SQLs, and are they consistently applied?', 'How are SQLs being nurtured and progressed through the sales funnel?'],
    actionable_steps={
        "operational": ['Regularly review and refine the criteria for SQL qualification to ensure alignment between marketing and sales teams.'],
        "strategic": ['Implement lead nurturing strategies to engage and educate SQLs, increasing their likelihood of conversion.', 'Utilize customer relationship management (CRM) software to track and manage SQLs effectively.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Funnel charts to visualize the progression of leads from initial contact to SQL status.', 'Line graphs to track the trend of SQLs over time, identifying peaks and troughs.']
    ],
    risk_warnings=['A high number of SQLs may lead to a bottleneck in the sales process if not managed effectively.', 'A low number of SQLs may indicate a disconnect between marketing efforts and the target audience.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Marketing automation platforms to streamline lead qualification and nurturing processes.', 'CRM systems with lead scoring capabilities to prioritize and manage SQLs efficiently.'],
    integration_points=['Integrate SQL data with sales performance metrics to analyze the impact of SQL quality on actual sales outcomes.', 'Link SQL information with customer relationship management systems to provide sales teams with comprehensive customer insights.'],
    
    # Impact
    change_impact="Improving the number of SQLs can lead to increased sales opportunities and revenue generation. Conversely, a decrease in SQLs may impact the overall sales pipeline and require adjustments in lead generation strategies.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Lead", "Meeting", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
