"""
Customer Referenceability Rate KPI

The percentage of customers who agree to act as a reference or case study for the company's marketing efforts.
"""

from analytics_models import KPI

CUSTOMER_REFERENCEABILITY_RATE = KPI(
    name="Customer Referenceability Rate",
    code="CUSTOMER_REFERENCEABILITY_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The percentage of customers who agree to act as a reference or case study for the company\'s marketing efforts.",
    kpi_definition="The percentage of customers who agree to act as a reference or case study for the company\'s marketing efforts.",
    expected_business_insights="Reveals the willingness of satisfied customers to promote the company, influencing new customer acquisition.",
    measurement_approach="Tracks the percentage of customers who are willing and able to serve as references or advocates for the company.",
    
    # Formula
    formula="(Number of Customers Willing to be References / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Willing to be References / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer referenceability rate may indicate higher satisfaction and loyalty among customers.
    * A decreasing rate could signal dissatisfaction with the company\'s products or services.
    """,
    diagnostic_questions="""
    * What are the common reasons customers agree or refuse to act as references or case studies?
    * Are there specific customer segments or product lines with higher or lower referenceability rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide exceptional customer service and support to increase the likelihood of customers agreeing to be references.
    * Regularly solicit feedback from customers to address any issues that may be affecting their willingness to act as references.
    * Offer incentives or rewards for customers who agree to participate in reference activities.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in customer referenceability rates over time.
    * Pie charts to compare referenceability rates across different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low customer referenceability rate may indicate a lack of advocacy and potential negative word-of-mouth in the market.
    * Over-reliance on a small number of customer references may lead to limited diversity in marketing materials.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and manage customer interactions and feedback.
    * Survey and feedback tools to gather insights into customer satisfaction and willingness to participate in reference activities.
    """,
    integration_points="""
    * Integrate customer referenceability data with sales and marketing systems to identify opportunities for leveraging references in the sales process.
    * Link referenceability rates with customer satisfaction metrics to understand the correlation between satisfaction and willingness to act as a reference.
    """,
    change_impact_analysis="""
    * Improving the customer referenceability rate can enhance the credibility and trustworthiness of the company\'s marketing efforts.
    * Conversely, a declining referenceability rate may impact the effectiveness of sales and marketing campaigns that rely on customer references.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"]
    }
)
