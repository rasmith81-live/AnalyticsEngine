"""
Customer Goal Achievement Rate KPI

The rate at which customers achieve their desired outcomes or goals with the company's products or services.
"""

from analytics_models import KPI

CUSTOMER_GOAL_ACHIEVEMENT_RATE = KPI(
    name="Customer Goal Achievement Rate",
    code="CUSTOMER_GOAL_ACHIEVEMENT_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customers achieve their desired outcomes or goals with the company\'s products or services.",
    kpi_definition="The rate at which customers achieve their desired outcomes or goals with the company\'s products or services.",
    expected_business_insights="Reveals the product\'s effectiveness and value from the customer\'s perspective, influencing customer retention.",
    measurement_approach="Measures the percentage of customers who achieve their desired outcomes or goals with the company\'s product or service.",
    
    # Formula
    formula="(Number of Customers Achieving Their Goals / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Achieving Their Goals / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer goal achievement rate may indicate improved product quality or better customer support.
    * A decreasing rate could signal issues with product performance, customer onboarding, or changing customer needs.
    """,
    diagnostic_questions="""
    * Are there common barriers that prevent customers from achieving their goals?
    * How does our customer goal achievement rate compare with industry benchmarks or competitor performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance customer onboarding processes to ensure clear goal setting and alignment with customer expectations.
    * Provide ongoing training and support to help customers maximize the value of our products or services.
    * Regularly gather customer feedback to identify areas for improvement and address any obstacles to goal achievement.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in customer goal achievement rate over time.
    * Stacked bar charts comparing goal achievement rates across different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low customer goal achievement rate can lead to customer churn and negative word-of-mouth, impacting future sales.
    * Consistently high achievement rates may indicate that customer goals are too easy to attain, potentially devaluing the product or service.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and progress towards goals.
    * Survey and feedback tools to gather insights into customer satisfaction and goal attainment.
    """,
    integration_points="""
    * Integrate customer goal achievement data with sales and marketing systems to better understand the impact on customer acquisition and retention.
    * Link with product development and innovation processes to align new features or improvements with customer goals.
    """,
    change_impact_analysis="""
    * Improving the customer goal achievement rate can lead to higher customer lifetime value and increased brand loyalty.
    * However, overly aggressive goal setting may lead to customer frustration and dissatisfaction, impacting overall customer experience.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Goal", "Product"]
    }
)
