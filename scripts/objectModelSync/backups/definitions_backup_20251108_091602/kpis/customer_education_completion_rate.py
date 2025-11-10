"""
Customer Education Completion Rate KPI

The rate at which customers complete educational programs or training offered by the company.
"""

from analytics_models import KPI

CUSTOMER_EDUCATION_COMPLETION_RATE = KPI(
    name="Customer Education Completion Rate",
    code="CUSTOMER_EDUCATION_COMPLETION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customers complete educational programs or training offered by the company.",
    kpi_definition="The rate at which customers complete educational programs or training offered by the company.",
    expected_business_insights="Provides insight into the effectiveness of customer education initiatives and their impact on product adoption.",
    measurement_approach="Measures the percentage of customers who complete educational courses or training offered by the company.",
    
    # Formula
    formula="(Number of Customers Who Complete Education Programs / Total Number of Customers Enrolled) * 100",
    calculation_formula="(Number of Customers Who Complete Education Programs / Total Number of Customers Enrolled) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer education completion rate may indicate a growing interest in the company\'s educational programs or an increased focus on customer success.
    * A decreasing rate could signal a lack of engagement with the educational materials or a need for improvement in the content or delivery of the programs.
    """,
    diagnostic_questions="""
    * Are there specific educational programs or training modules that have significantly lower completion rates?
    * How does the completion rate vary across different customer segments or product lines?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update and refresh educational content to keep it relevant and engaging for customers.
    * Offer incentives or rewards for customers who complete educational programs to increase participation and completion rates.
    * Provide multiple formats for educational materials (e.g., videos, webinars, written guides) to cater to different learning preferences.
    """,
    visualization_suggestions="""
    * Line charts showing the completion rate trend over time.
    * Pie charts to compare completion rates across different programs or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low completion rates may indicate a lack of customer understanding or proficiency with the company\'s products or services, leading to potential dissatisfaction or support issues.
    * High completion rates without corresponding improvements in customer satisfaction or retention may suggest that the educational programs are not effectively addressing customer needs.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and analyze customer progress through educational programs.
    * Customer relationship management (CRM) software to correlate completion rates with customer behavior and satisfaction metrics.
    """,
    integration_points="""
    * Integrate completion rate data with customer support systems to identify areas where additional education or resources may be needed.
    * Link completion rates with sales data to understand the impact of customer education on purchasing behavior and product adoption.
    """,
    change_impact_analysis="""
    * Improving the completion rate can lead to better-informed customers, potentially reducing support costs and increasing customer lifetime value.
    * However, a significant increase in completion rates without corresponding improvements in customer satisfaction or retention may indicate that the educational content needs to be re-evaluated.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Training", "Sales Training Program", "Training Program"]
    }
)
