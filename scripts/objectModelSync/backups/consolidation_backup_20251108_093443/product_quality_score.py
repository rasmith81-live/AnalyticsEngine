"""
Product Quality Score KPI

A measure of customer perceptions of product quality, often collected through customer surveys or feedback mechanisms.
"""

from analytics_models import KPI

PRODUCT_QUALITY_SCORE = KPI(
    name="Product Quality Score",
    code="PRODUCT_QUALITY_SCORE",
    category="Customer Success",
    
    # Core Definition
    description="A measure of customer perceptions of product quality, often collected through customer surveys or feedback mechanisms.",
    kpi_definition="A measure of customer perceptions of product quality, often collected through customer surveys or feedback mechanisms.",
    expected_business_insights="Provides insight into product reliability and user satisfaction, guiding improvements in product development.",
    measurement_approach="Considers factors like defect rates, user feedback, and compliance with specifications.",
    
    # Formula
    formula="Sum of weighted quality metrics (based on defect rates, user feedback, etc.) / Total number of quality metrics",
    calculation_formula="Sum of weighted quality metrics (based on defect rates, user feedback, etc.) / Total number of quality metrics",
    
    # Analysis
    trend_analysis="""
    * An increasing product quality score may indicate improvements in production processes or customer satisfaction.
    * A decreasing score could signal issues with product consistency, customer service, or market competition.
    """,
    diagnostic_questions="""
    * Are there specific products or features that consistently receive lower quality scores?
    * How do our product quality scores compare with industry benchmarks or customer expectations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular quality control checks throughout the production process.
    * Invest in customer feedback mechanisms to identify areas for product improvement.
    * Train and empower customer service teams to address product quality concerns effectively.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of product quality scores over time.
    * Pareto charts to identify the most common reasons for low product quality scores.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently low product quality scores can lead to customer churn and negative word-of-mouth.
    * High variability in product quality scores may indicate inconsistent production processes.
    """,
    tracking_tools="""
    * Quality management software like MasterControl or ETQ to track and analyze product quality data.
    * Customer feedback platforms such as SurveyMonkey or Medallia to gather and analyze customer perceptions of product quality.
    """,
    integration_points="""
    * Integrate product quality score tracking with production management systems to identify and address quality issues at the source.
    * Link quality score data with customer relationship management (CRM) systems to understand the impact on customer satisfaction and retention.
    """,
    change_impact_analysis="""
    * Improving product quality scores can lead to increased customer satisfaction and loyalty, ultimately impacting revenue and brand reputation positively.
    * Conversely, declining product quality scores may result in increased customer complaints, returns, and decreased sales.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Product", "Product Adoption", "Product Usage"]
    }
)
