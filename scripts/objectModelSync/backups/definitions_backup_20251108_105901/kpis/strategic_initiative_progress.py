"""
Strategic Initiative Progress KPI

Module: Business Development
"""

from analytics_models import KPI

STRATEGIC_INITIATIVE_PROGRESS = KPI(
    name="Strategic Initiative Progress",
    code="STRATEGIC_INITIATIVE_PROGRESS",
    description="A measure of the progress of key business initiatives against strategic goals.",
    
    # Definition & Context
    kpi_definition="A measure of the progress of key business initiatives against strategic goals.",
    expected_business_insights="Enables assessment of how strategic initiatives are advancing and contributing to long-term goals.",
    measurement_approach="Tracks milestones, deliverables, and percent completion against planned objectives and timelines.",
    
    # Calculation
    formula="(Sum of Completed Milestones or Objectives / Total Planned Milestones or Objectives) * 100",
    
    # Analysis
    trend_analysis="Monitoring the progress of key business initiatives against strategic goals over time. Identifying positive or negative performance shifts based on the trends of the KPI.",
    diagnostic_questions=['Are the key business initiatives aligned with the overall strategic goals of the organization?', 'What factors are contributing to the progress or lack of progress in key business initiatives?'],
    actionable_steps={
        "operational": ['Regularly review and adjust key business initiatives to ensure alignment with strategic goals.'],
        "strategic": ['Provide adequate resources and support for the successful implementation of key business initiatives.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the progress of key business initiatives over time.', 'Bar graphs comparing the progress of different key business initiatives against strategic goals.']
    ],
    risk_warnings=['Failure to make progress on key business initiatives may result in missed opportunities or competitive disadvantages.', 'Rapid progress on key business initiatives without proper evaluation may lead to unsustainable growth or resource strain.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Project management software to track and manage the progress of key business initiatives.', 'Data analytics tools to assess the impact and effectiveness of key business initiatives.'],
    integration_points=['Integrate the progress of key business initiatives with performance management systems to align individual and team goals.', 'Link the progress of key business initiatives with financial reporting systems to measure the impact on overall business performance.'],
    
    # Impact
    change_impact="Positive progress in key business initiatives can lead to improved overall business performance and competitive advantage. Negative progress in key business initiatives may result in decreased market share and financial performance.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Goal", "Key Account", "Key Account Manager", "Quarterly Business Review", "Strategic Initiative", "Strategic Review"]
    }
)
