"""
Contract Renewal Rate KPI

Module: Business Development
"""

from analytics_models import KPI

CONTRACT_RENEWAL_RATE = KPI(
    name="Contract Renewal Rate",
    code="CONTRACT_RENEWAL_RATE",
    description="The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
    
    # Definition & Context
    kpi_definition="The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
    expected_business_insights="Indicates customer satisfaction and the long-term value of customer relationships.",
    measurement_approach="Measures the percentage of contracts that are renewed at the end of their term.",
    
    # Calculation
    formula="(Number of Contracts Renewed / Number of Contracts Up for Renewal) * 100",
    
    # Analysis
    trend_analysis="An increasing contract renewal rate may indicate improved customer satisfaction and loyalty. A decreasing rate could signal dissatisfaction with the product or service, leading to potential churn.",
    diagnostic_questions=['Are there common reasons why customers choose not to renew their contracts?', 'How does our contract renewal rate compare to industry benchmarks or our competitors?'],
    actionable_steps={
        "operational": ['Regularly survey customers to understand their satisfaction levels and address any issues proactively.'],
        "strategic": ['Offer incentives for contract renewals, such as discounts or additional services.', 'Provide exceptional customer service throughout the contract period to increase the likelihood of renewal.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of contract renewal rates over time.', 'Comparative bar charts to analyze renewal rates across different customer segments or product lines.']
    ],
    risk_warnings=['A declining contract renewal rate may lead to revenue loss and impact overall business performance.', 'Low renewal rates could indicate a need for product or service improvements to meet customer expectations.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track customer interactions and contract renewal dates.', 'Survey tools to gather feedback from customers about their experience and reasons for not renewing contracts.'],
    integration_points=['Integrate contract renewal data with sales and marketing systems to identify opportunities for targeted retention efforts.', 'Link contract renewal rates with customer support systems to address any issues that may impact renewals.'],
    
    # Impact
    change_impact="Improving contract renewal rates can lead to increased customer lifetime value and overall business growth. Conversely, a decline in renewal rates may require strategic shifts in product offerings or customer engagement strategies.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review", "Renewal Management"]
    }
)
