"""
Customer Effort Score (CES) KPI

A measure of how much effort a customer has to exert to get an issue resolved, a request fulfilled, or a product purchased.
"""

from analytics_models import KPI

CUSTOMER_EFFORT_SCORE_CES = KPI(
    name="Customer Effort Score (CES)",
    code="CUSTOMER_EFFORT_SCORE_CES",
    category="Customer Retention",
    
    # Core Definition
    description="A measure of how much effort a customer has to exert to get an issue resolved, a request fulfilled, or a product purchased.",
    kpi_definition="A measure of how much effort a customer has to exert to get an issue resolved, a request fulfilled, or a product purchased.",
    expected_business_insights="Helps identify pain points in customer experience, with a focus on making interactions more effortless.",
    measurement_approach="Measures the ease with which customers can interact with the company or use its products/services.",
    
    # Formula
    formula="Average of Customer Effort Ratings on a Scale (e.g., 1-7)",
    calculation_formula="Average of Customer Effort Ratings on a Scale (e.g., 1-7)",
    
    # Analysis
    trend_analysis="""
    * An increasing customer effort score may indicate growing customer dissatisfaction or operational inefficiencies.
    * A decreasing score could signal improved customer experience or more streamlined processes.
    """,
    diagnostic_questions="""
    * Are there common pain points or bottlenecks in the customer journey that contribute to a high effort score?
    * How does our customer effort score compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement self-service options to empower customers to resolve issues on their own.
    * Streamline processes and reduce unnecessary steps in the customer journey.
    * Invest in training and empowering customer service representatives to handle issues more efficiently.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer effort score over time.
    * Heat maps to identify specific touchpoints or interactions with high customer effort.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer effort scores can lead to customer churn and negative word-of-mouth.
    * Consistently high scores may indicate systemic issues in the customer experience that need immediate attention.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with built-in customer effort score tracking.
    * Customer feedback and survey platforms to gather and analyze data on customer effort.
    """,
    integration_points="""
    * Integrate customer effort score tracking with customer support ticketing systems to identify patterns and trends.
    * Link customer effort score data with customer segmentation and profiling for targeted improvement efforts.
    """,
    change_impact_analysis="""
    * Reducing customer effort score can lead to higher customer satisfaction and loyalty.
    * However, overly aggressive efforts to reduce customer effort may impact operational costs and resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Support Ticket"]
    }
)
