"""
Customer Satisfaction Index KPI

Module: Business Development
"""

from analytics_models import KPI

CUSTOMER_SATISFACTION_INDEX = KPI(
    name="Customer Satisfaction Index",
    code="CUSTOMER_SATISFACTION_INDEX",
    description="A measure of how satisfied customers are with a company's products or services, often determined through surveys and feedback mechanisms.",
    
    # Definition & Context
    kpi_definition="A measure of how satisfied customers are with a company's products or services, often determined through surveys and feedback mechanisms.",
    expected_business_insights="Provides a quantitative measure of customer satisfaction and can guide improvements in customer service.",
    measurement_approach="Calculates an index based on customer surveys regarding satisfaction with products or services.",
    
    # Calculation
    formula="(Sum of Customer Satisfaction Scores / Number of Respondents) * 100",
    
    # Analysis
    trend_analysis="An increasing CSI may indicate improved product quality or customer service. A decreasing CSI could signal declining customer satisfaction due to product issues or service shortcomings.",
    diagnostic_questions=['Are there specific products or services that consistently receive low satisfaction ratings?', "How does our CSI compare with industry benchmarks or competitors' ratings?"],
    actionable_steps={
        "operational": ['Implement regular customer feedback surveys to identify areas for improvement.'],
        "strategic": ['Train and empower customer-facing staff to address and resolve customer issues effectively.', 'Focus on continuous product and service enhancements based on customer feedback.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of CSI over time.', 'Pie charts to compare satisfaction levels across different product or service categories.']
    ],
    risk_warnings=['Low CSI can lead to customer churn and negative word-of-mouth, impacting future sales.', 'Consistently low satisfaction ratings may indicate systemic issues that require immediate attention.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and manage customer feedback and interactions.', 'Survey tools like SurveyMonkey or Qualtrics for collecting and analyzing customer satisfaction data.'],
    integration_points=['Integrate CSI data with sales and marketing systems to align efforts with customer satisfaction goals.', 'Link CSI with product development processes to prioritize enhancements based on customer feedback.'],
    
    # Impact
    change_impact="Improving CSI can lead to increased customer loyalty and repeat business. Conversely, declining CSI may result in reduced sales and brand reputation damage.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Quarterly Business Review"]
    }
)
