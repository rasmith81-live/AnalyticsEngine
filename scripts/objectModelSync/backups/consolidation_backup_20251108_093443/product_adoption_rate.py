"""
Product Adoption Rate KPI

The percentage of customers who are using the product or service in the way it was intended. This KPI measures the effectiveness of the Customer Success Team in educating customers about the product or service.
"""

from analytics_models import KPI

PRODUCT_ADOPTION_RATE = KPI(
    name="Product Adoption Rate",
    code="PRODUCT_ADOPTION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The percentage of customers who are using the product or service in the way it was intended. This KPI measures the effectiveness of the Customer Success Team in educating customers about the product or service.",
    kpi_definition="The percentage of customers who are using the product or service in the way it was intended. This KPI measures the effectiveness of the Customer Success Team in educating customers about the product or service.",
    expected_business_insights="Indicates how well a new product or feature meets customer needs and its market acceptance.",
    measurement_approach="Measures the percentage of customers that have started using a product or feature after its introduction.",
    
    # Formula
    formula="(Number of Customers Using the Product or Feature / Total Target Market Customers) * 100",
    calculation_formula="(Number of Customers Using the Product or Feature / Total Target Market Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing product adoption rate may indicate successful customer onboarding and education efforts.
    * A decreasing rate could signal issues with product usability, customer support, or changes in customer needs.
    """,
    diagnostic_questions="""
    * Are there specific features or functionalities that customers struggle to adopt?
    * How does our product adoption rate compare with industry benchmarks or with different customer segments?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide targeted training or resources to address common adoption barriers.
    * Collect and act on customer feedback to continuously improve product usability and customer support.
    * Segment customers based on their needs and provide personalized onboarding and education experiences.
    """,
    visualization_suggestions="""
    * Line charts showing the product adoption rate over time.
    * Pie charts to compare adoption rates across different customer segments or product features.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low product adoption rates may lead to customer churn and reduced lifetime value.
    * Failure to address adoption issues can result in negative reviews and damage to the brand\'s reputation.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and identify opportunities for education.
    * User behavior analytics tools to understand how customers engage with the product and identify adoption barriers.
    """,
    integration_points="""
    * Integrate product adoption data with customer support systems to identify and address common issues.
    * Link adoption rates with sales data to understand the impact on revenue and customer retention.
    """,
    change_impact_analysis="""
    * Improving product adoption can lead to increased customer satisfaction and loyalty.
    * However, changes in adoption rates may also impact revenue projections and customer retention metrics.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Market Segment", "Product", "Product Adoption", "Product Usage", "Sales Quota", "Sales Team", "Service Level Agreement"]
    }
)
