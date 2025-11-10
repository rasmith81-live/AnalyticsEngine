"""
Voice of the Customer (VoC) Score KPI

Module: Business Development
"""

from analytics_models import KPI

VOICE_OF_THE_CUSTOMER_VOC_SCORE = KPI(
    name="Voice of the Customer (VoC) Score",
    code="VOICE_OF_THE_CUSTOMER_VOC_SCORE",
    description="A measure of customer feedback about their experiences with and expectations for a company's products or services.",
    
    # Definition & Context
    kpi_definition="A measure of customer feedback about their experiences with and expectations for a company's products or services.",
    expected_business_insights="Provides a holistic view of customer perceptions and experiences, guiding customer-centric improvements.",
    measurement_approach="Aggregates customer feedback scores, satisfaction ratings, and sentiment analysis.",
    
    # Calculation
    formula="Sum of All Customer Feedback Scores / Number of Feedback Instances",
    
    # Analysis
    trend_analysis="Increasing VoC scores may indicate improved customer satisfaction and loyalty. Decreasing scores could signal declining customer experience or unmet expectations.",
    diagnostic_questions=['What specific aspects of our products or services are driving changes in VoC scores?', 'How do our VoC scores compare with industry benchmarks or competitors?'],
    actionable_steps={
        "operational": ['Implement regular customer feedback surveys to gather insights and identify areas for improvement.'],
        "strategic": ['Invest in training for sales and customer service teams to enhance customer interactions and satisfaction.', 'Use VoC data to drive product or service enhancements that align with customer expectations.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts to track VoC scores over time and identify trends.', 'Word clouds to visualize common themes or keywords in customer feedback.']
    ],
    risk_warnings=['Low VoC scores may lead to customer churn and negative word-of-mouth, impacting revenue and brand reputation.', 'Ignoring or misinterpreting customer feedback can result in missed opportunities for improvement and innovation.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer feedback management platforms like Medallia or Qualtrics to collect and analyze VoC data.', 'CRM systems with integrated VoC modules to track customer interactions and feedback.'],
    integration_points=['Integrate VoC data with product development processes to align offerings with customer needs and preferences.', 'Link VoC scores with sales performance metrics to understand the impact of customer satisfaction on revenue.'],
    
    # Impact
    change_impact="Improving VoC scores can lead to increased customer retention and lifetime value. Conversely, declining VoC scores may result in decreased sales and market share.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Product", "Quarterly Business Review"]
    }
)
