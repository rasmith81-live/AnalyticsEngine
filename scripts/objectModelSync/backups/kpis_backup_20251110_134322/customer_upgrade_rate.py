"""
Customer Upgrade Rate KPI

The percentage of customers that move to a higher-tier service or product offering.
"""

CUSTOMER_UPGRADE_RATE = {
    "code": "CUSTOMER_UPGRADE_RATE",
    "name": "Customer Upgrade Rate",
    "description": "The percentage of customers that move to a higher-tier service or product offering.",
    "formula": "(Number of Customers Upgraded / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Upgraded / Total Number of Customers) * 100",
    "category": "Customer Success",
    "is_active": True,
    "kpi_definition": "The percentage of customers that move to a higher-tier service or product offering.",
    "expected_business_insights": "Signals customer satisfaction and the perceived value of premium features or services.",
    "measurement_approach": "Tracks the percentage of customers who move to a higher-tier service or product within a given timeframe.",
    "trend_analysis": """
    * An increasing customer upgrade rate may indicate successful upselling strategies or a growing demand for higher-tier offerings.
    * A decreasing rate could signal customer dissatisfaction with higher-tier products or a lack of effective upselling techniques.
    """,
    "diagnostic_questions": """
    * Are there specific customer segments or industries that are more likely to upgrade?
    * What are the main reasons customers give for upgrading, and are there any common objections that prevent them from doing so?
    """,
    "actionable_tips": """
    * Train sales teams to effectively communicate the value of higher-tier offerings and identify upselling opportunities.
    * Personalize upselling strategies based on customer behavior and preferences to increase the likelihood of upgrades.
    * Offer incentives or promotions to encourage customers to move to higher-tier products or services.
    """,
    "visualization_suggestions": """
    * Line charts showing the customer upgrade rate over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of upgrades across different product or service categories.
    """,
    "risk_warnings": """
    * A low upgrade rate may indicate a lack of customer satisfaction with higher-tier offerings, leading to potential churn.
    * Overemphasis on upselling may lead to customer fatigue and resistance, impacting overall customer experience.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and identify upselling opportunities.
    * Analytics tools to segment customers and understand their behavior to tailor upselling strategies.
    """,
    "integration_points": """
    * Integrate customer upgrade rate data with customer feedback and satisfaction metrics to understand the impact of upgrades on overall customer experience.
    * Link with sales performance metrics to evaluate the effectiveness of upselling techniques and strategies.
    """,
    "change_impact_analysis": """
    * An increase in the customer upgrade rate can positively impact revenue and customer lifetime value.
    * However, aggressive upselling tactics may negatively impact customer trust and brand reputation, affecting long-term customer relationships.
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]},
    "modules": ["CUSTOMER_SUCCESS"],
    "module_code": "CUSTOMER_SUCCESS",
}
