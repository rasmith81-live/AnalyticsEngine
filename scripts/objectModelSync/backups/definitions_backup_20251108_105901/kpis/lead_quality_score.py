"""
Lead Quality Score KPI

Module: Business Development
"""

from analytics_models import KPI

LEAD_QUALITY_SCORE = KPI(
    name="Lead Quality Score",
    code="LEAD_QUALITY_SCORE",
    description="A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.",
    
    # Definition & Context
    kpi_definition="A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.",
    expected_business_insights="Helps prioritize sales efforts on leads more likely to convert and improve lead scoring models.",
    measurement_approach="Measures the perceived quality of leads based on predetermined scoring criteria.",
    
    # Calculation
    formula="(Various metrics depending on the lead scoring criteria used)",
    
    # Analysis
    trend_analysis="Higher lead quality scores over time may indicate improved targeting and lead generation strategies. A declining lead quality score trend could signal issues with lead sources or a need for better qualification criteria.",
    diagnostic_questions=['Are there specific industries or job titles that consistently yield higher quality leads?', 'How does our lead quality score compare with industry benchmarks or historical data?'],
    actionable_steps={
        "operational": ['Refine lead qualification criteria to focus on leads with higher potential for conversion.'],
        "strategic": ['Implement targeted marketing campaigns to attract leads from industries or job titles with historically higher quality scores.', 'Regularly review and update lead sources to prioritize those that consistently deliver high-quality leads.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing lead quality score trends over time.', 'Pie charts to compare lead quality scores by industry or job title.']
    ],
    risk_warnings=['Low lead quality scores may result in wasted resources on unproductive leads.', 'Overemphasis on lead quality without considering quantity may lead to missed opportunities for conversion.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) systems with lead scoring capabilities to track and analyze lead quality.', 'Marketing automation platforms to segment leads based on quality and tailor campaigns accordingly.'],
    integration_points=['Integrate lead quality scores with sales performance data to identify correlations between lead quality and conversion rates.', 'Link lead quality scores with marketing analytics to assess the effectiveness of lead generation efforts.'],
    
    # Impact
    change_impact="Improving lead quality scores can lead to higher conversion rates and increased sales efficiency. However, overly strict lead quality criteria may reduce the overall volume of leads, potentially impacting sales pipeline and revenue.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Lead", "Lead Qualification", "Prospect Engagement", "Quarterly Business Review", "Service Level Agreement"]
    }
)
