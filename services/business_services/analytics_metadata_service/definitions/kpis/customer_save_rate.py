"""
Customer Save Rate KPI

The percentage of customers who were at the brink of leaving but were retained by the company.
"""

CUSTOMER_SAVE_RATE = {
    "code": "CUSTOMER_SAVE_RATE",
    "name": "Customer Save Rate",
    "description": "The percentage of customers who were at the brink of leaving but were retained by the company.",
    "formula": "(Number of Customers Retained / Number of Customers Attempting to Leave) * 100",
    "calculation_formula": "(Number of Customers Retained / Number of Customers Attempting to Leave) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The percentage of customers who were at the brink of leaving but were retained by the company.",
    "expected_business_insights": "Measures the effectiveness of retention efforts and identifies potential improvements in customer service.",
    "measurement_approach": "Tracks the percentage of customers who were successfully retained after expressing an intention to leave.",
    "trend_analysis": """
    * An increasing customer save rate may indicate improved customer retention strategies or enhanced customer service efforts.
    * A decreasing rate could signal dissatisfaction with the company's products or services, or increased competition in the market.
    """,
    "diagnostic_questions": """
    * What are the common reasons customers consider leaving, and how can we address those specific issues?
    * Are there patterns or commonalities among the customers who were successfully retained, and how can we replicate those successes?
    """,
    "actionable_tips": """
    * Implement proactive customer outreach and engagement strategies to address potential churn before it happens.
    * Personalize the customer experience to better meet individual needs and preferences, increasing the likelihood of retention.
    * Invest in ongoing customer education and support to build long-term relationships and loyalty.
    """,
    "visualization_suggestions": """
    * Line charts showing the customer save rate over time to identify trends and seasonal variations.
    * Pie charts to compare the reasons for customer churn and the success rates of different retention strategies.
    """,
    "risk_warnings": """
    * A low customer save rate may indicate a lack of effective retention strategies, leading to potential revenue loss.
    * High customer save rates may mask underlying issues with product quality or customer satisfaction, leading to long-term negative impacts.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track customer interactions and identify at-risk customers.
    * Survey and feedback tools to gather insights from customers about their experiences and reasons for considering leaving.
    """,
    "integration_points": """
    * Integrate customer save rate data with sales and marketing systems to align retention efforts with overall business goals.
    * Link customer save rate with customer support systems to ensure a seamless experience for at-risk customers.
    """,
    "change_impact_analysis": """
    * Improving the customer save rate can lead to increased customer lifetime value and overall revenue growth.
    * Conversely, a declining customer save rate can indicate a need for significant changes in customer retention strategies and may impact overall business performance.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
